from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

# Load the tokenizer and Model
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english", num_labels=2)
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

# Create the pipeline
pipeline = pipeline(task="text-classification", model=model, tokenizer=tokenizer)

text = input("Enter a text to classify: ")
# example: "I love this movie! It's fantastic and full of surprises."

# Predict the output, print the label, and confidence score
output = pipeline(text)
print(f"Label: {output[0]['label']}, Confidence Score: {output[0]['score']:.4f}")