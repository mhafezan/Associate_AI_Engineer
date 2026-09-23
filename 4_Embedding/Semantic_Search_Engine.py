"""Search Shopify products with persistent local ChromaDB storage.

Install: python -m pip install chromadb openai
Set OPENAI_API_KEY for -init and -query. Run with -help for commands.
Dataset: https://huggingface.co/datasets/Shopify/product-catalogue (Apache-2.0)
"""

import argparse
import json
import os
from pathlib import Path
import shlex
import sys
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.request import urlopen

import chromadb
from chromadb.errors import ChromaError
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from openai import OpenAIError

MODEL = "text-embedding-3-small"
COLLECTION_NAME = "shopify_products"
DB_PATH = Path(__file__).resolve().parent / "chroma_db"


def load_products(limit=2048):
    """Download up to limit source rows without creating a file cache."""
    products = []
    offset = 0
    while offset < limit:
        params = urlencode({
            "dataset": "Shopify/product-catalogue", "config": "default",
            "split": "train", "offset": offset, "length": min(100, limit - offset),
        })
        with urlopen(f"https://datasets-server.huggingface.co/rows?{params}", timeout=60) as response:
            page = json.load(response)
        rows = page["rows"]
        if not rows:
            break
        for item in rows:
            row = item["row"]
            title = (row.get("product_title") or "").strip()
            if not title:
                continue
            brand = (row.get("ground_truth_brand") or "").strip()
            products.append({
                "id": f"shopify_train_{item['row_idx']}",
                "title": title,
                "short_description": (row.get("product_description") or "").strip()[:2000],
                "category": row.get("ground_truth_category") or "Uncategorized",
                "features": [f"Brand: {brand}"] if brand else [],
            })
        offset += len(rows)
        print(f"Downloaded {offset:,} rows ({len(products):,} usable products)...", flush=True)
        if offset >= page["num_rows_total"]:
            break
    if not products:
        raise ValueError("The dataset returned no usable products.")
    return products


def create_product_text(product):
    """Combine the product fields into one searchable string."""
    return (
        f"Title: {product['title']}\n"
        f"Description: {product['short_description']}\n"
        f"Category: {product['category']}\n"
        f"Features: {'; '.join(product['features'])}"
    )


def initialize_collection(collection, limit):
    products = load_products(limit)
    # Stable source-row IDs make repeated initialization safe from duplicates.
    for start in range(0, len(products), 32):
        batch = products[start:start + 32]
        product_texts = [create_product_text(product) for product in batch]
        collection.upsert(
            ids=[product["id"] for product in batch],
            documents=product_texts,
            metadatas=[{
                "title": product["title"],
                "short_description": product["short_description"],
                "category": product["category"],
                "features": "; ".join(product["features"]),
            } for product in batch],
        )
        print(f"Stored {start + len(batch):,}/{len(products):,} products...", flush=True)
    print(f"{collection.name}: {collection.count():,} documents stored in {DB_PATH}")


def find_n_closest(query_text, collection, n=5):
    """Let Chroma embed the query and retrieve the nearest stored documents."""
    count = collection.count()
    if count == 0:
        raise ValueError("The collection is empty. Run -init first.")
    return collection.query(
        query_texts=[query_text], n_results=min(n, count),
        include=["documents", "metadatas", "distances"],
    )


def run_command(argv):
    parser = argparse.ArgumentParser(description=__doc__, add_help=False, allow_abbrev=False)
    parser.add_argument("-help", "--help", "-h", action="help", help="Show this help and exit")
    actions = parser.add_mutually_exclusive_group(required=True)
    actions.add_argument("-init", "--init", action="store_true", help="Download and upsert Shopify products")
    actions.add_argument("-list", "--list", action="store_true", help="List local collections")
    actions.add_argument("-count", "--count", metavar="COLLECTION", help="Count documents in a collection")
    actions.add_argument("-peek", "--peek", metavar="COLLECTION", help="Show up to 10 items in a collection")
    actions.add_argument("-query", "--query", action="store_true", help="Search shopify_products using TEXT")
    parser.add_argument("-limit", "--limit", type=int, help="Source rows for -init (default: 2048)")
    parser.add_argument("-n_results", "--n_results", type=int, help="Matches for -query (default: 5)")
    parser.add_argument("text", nargs="?", metavar="TEXT", help="Quoted search text for -query")
    args = parser.parse_args(argv)
    if args.limit is not None and (not args.init or args.limit < 1):
        parser.error("-limit must be positive and used with -init")
    if args.n_results is not None and (not args.query or args.n_results < 1):
        parser.error("-n_results must be positive and used with -query")
    if args.query and (not args.text or not args.text.strip()):
        parser.error('-query requires nonempty quoted text, e.g. -query -n_results 5 "summer hat"')
    if args.text is not None and not args.query:
        parser.error("TEXT can only be used with -query")
    if (args.init or args.query) and not os.environ.get("OPENAI_API_KEY", "").strip():
        parser.error("Set OPENAI_API_KEY before using -init or -query")

    client = chromadb.PersistentClient(path=str(DB_PATH))
    if args.list:
        collections = client.list_collections()
        print("\n".join(collection.name for collection in collections) or "No collections. Run -init first.")
        return
    if args.count or args.peek:
        collection = client.get_collection(args.count or args.peek, embedding_function=None)
        if args.count:
            print(f"{collection.name}: {collection.count()} documents")
        else:
            # Omit embedding arrays from terminal output.
            hits = collection.get(limit=10, include=["documents", "metadatas"])
            print(json.dumps(hits, ensure_ascii=False, indent=2))
        return

    embedding_function = OpenAIEmbeddingFunction(model_name=MODEL)
    if args.init:
        collection = client.get_or_create_collection(
            name=COLLECTION_NAME, embedding_function=embedding_function,
            configuration={"hnsw": {"space": "cosine"}},
        )
        initialize_collection(collection, args.limit if args.limit is not None else 2048)
    else:
        collection = client.get_collection(COLLECTION_NAME, embedding_function=embedding_function)
        query_text = args.text.strip()
        hits = find_n_closest(query_text, collection, args.n_results or 5)
        print(f'Search results for "{query_text}"')
        for rank, (document, distance) in enumerate(
            zip(hits["documents"][0], hits["distances"][0]), start=1
        ):
            print(f"\n{rank}. Cosine distance: {distance:.4f}\n{document}")


def main():
    if len(sys.argv) > 1:
        run_command(sys.argv[1:])
        return

    print('Enter commands such as -help or -query -n_results 5 "summer hat".')
    print('Type exit to quit.')
    while True:
        try:
            command = input("\nsearch> ").strip()
            if command.casefold() == "exit":
                break
            if not command:
                continue
            # Parse quoted query text without executing shell commands.
            run_command(shlex.split(command))
        except SystemExit:
            # Argparse help and invalid arguments must not end the session.
            continue
        except (ChromaError, OpenAIError, URLError, OSError, ValueError, KeyError) as error:
            print(f"Semantic search failed: {error}", file=sys.stderr)
        except (EOFError, KeyboardInterrupt):
            break
    print("\nGoodbye!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye!")
    except (ChromaError, OpenAIError, URLError, OSError, ValueError, KeyError) as error:
        print(f"Semantic search failed: {error}", file=sys.stderr)
        sys.exit(1)
