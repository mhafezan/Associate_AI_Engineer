from pypdf import PdfReader
from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering

# Load the PDF document and extract text
reader = PdfReader("employee_policy.pdf")
document_text = ""
for page in reader.pages:
    document_text += page.extract_text()

# Load the tokenizer and model for question answering
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-cased-distilled-squad")
model = AutoModelForQuestionAnswering.from_pretrained("distilbert-base-cased-distilled-squad")

# Create the question-answering pipeline
QA_pipeline = pipeline(task="question-answering", model=model, tokenizer=tokenizer, framework="pt")

# Get a question from the user and predict the answer based on the document text
question = input("Enter your question: ")
result = QA_pipeline(question=question, context=document_text)
print(f"Answer: {result['answer']}")