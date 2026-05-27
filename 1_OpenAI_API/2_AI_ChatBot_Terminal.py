import os
from openai import OpenAI

# Load API key securely (environment variable) using setx OPENAI_API_KEY "sk-xxxxxxxxxxxxxxxx" in your environment variables
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set")
else:
    client = OpenAI(api_key=api_key)

messages = [{"role": "system", "content": "You are a helpful math tutor that speaks concisely.\
                                            Your answers should be freindly and objective.\
                                            If requested skill by user is non related to math learning, return the following message:\
                                            'Apologies, we are no longer supporting other skills.'"}]

print("\nChatbot is running. Type 'exit' to quit.\n")
print("Hi, how can I help you today?\n")

while True:
    # Capture user input from PowerShell terminal
    user_input = input("User: ")

    # Exit condition
    if user_input.lower() in ["exit", "quit"]:
        print("Chatbot terminated.")
        break

    # Append user message
    messages.append({"role": "user", "content": user_input})

    # API request
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        max_completion_tokens=100,
        messages=messages,
        stream=False # Enables streaming responses, i.e., the response appears token by token, like a real conversation
    )

    # Extract assistant response
    assistant_reply = response.choices[0].message.content

    # Append assistant message to history
    messages.append({"role": "assistant", "content": assistant_reply})

    # Show response in terminal
    print(f"Assistant: {assistant_reply}\n")