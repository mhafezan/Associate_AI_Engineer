from transformers import pipeline

gpt2_pipeline = pipeline(
    task="text-generation",
    model="openai-community/gpt2")

results = gpt2_pipeline(
    "Hi, how are you doing today?",
    max_new_tokens=20,
    num_return_sequences=2,
    pad_token_id=gpt2_pipeline.tokenizer.eos_token_id)

for result in results:
    print(f"\n{result['generated_text']}\n")