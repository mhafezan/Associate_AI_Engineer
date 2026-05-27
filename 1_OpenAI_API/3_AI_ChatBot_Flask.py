"""Flask is a web framework for Python.
   Flask allows developers to create RESTful APIs and server-side web applications.
"""
from flask import Flask, render_template, request, session, redirect, url_for
from openai import OpenAI
import os

app = Flask(__name__)
app.secret_key = "replace_this_with_a_secure_random_secret_key"

# Load API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set")

client = OpenAI(api_key=api_key)

SYSTEM_MESSAGE = {"role": "system", "content": "You are a helpful math tutor that speaks concisely."
                                    "If requested skills are non related to math learning, return the message:"
                                    "'Apologies, we are no longer supporting other skills.'"}

def initialize_chat():
    session["messages"] = [SYSTEM_MESSAGE]


@app.route("/", methods=["GET", "POST"])
def index():
    if "messages" not in session:
        initialize_chat()

    if request.method == "POST":
        user_input = request.form.get("user_input", "").strip()

        if user_input:
            messages = session["messages"]

            # Append user message
            messages.append({"role": "user", "content": user_input})

            # Create API request
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                max_completion_tokens=100,
                messages=messages
            )

            # Extract assistant reply
            assistant_reply = response.choices[0].message.content

            # Append assistant message
            messages.append({"role": "assistant", "content": assistant_reply})

            # Save updated chat
            session["messages"] = messages

        return redirect(url_for("index"))

    # Exclude system message from display
    visible_messages = session["messages"][1:]
    return render_template("index.html", messages=visible_messages)

@app.route("/clear", methods=["POST"])
def clear():
    initialize_chat()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)

# Run the Flask app and access it in your browser at http://127.0.0.1:5000
# python3 .\3_AI_ChatBot_Flask.py