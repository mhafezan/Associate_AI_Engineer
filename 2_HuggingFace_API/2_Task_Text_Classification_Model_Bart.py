from transformers import pipeline

text = input("Enter a text to classify: ")

# example: "AI-powered robots assist in complex brain surgeries with precision and efficiency"

# Create the pipeline
classifier = pipeline(task="zero-shot-classification", model="facebook/bart-large-mnli")

# Create the categories list
categories = ["politics", "science", "sports"]

# Predict the output
output = classifier(text, categories)

# Print the labels and confidence scores
for label, score in zip(output["labels"], output["scores"]):
    print(f"{label}: {score:.4f}")