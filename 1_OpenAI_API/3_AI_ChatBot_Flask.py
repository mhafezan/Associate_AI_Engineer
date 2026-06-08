"""Flask web application for an OpenAI-powered chatbot."""
from flask import Flask, Response, jsonify, render_template, request, session, redirect, url_for, stream_with_context
from openai import OpenAI
import json
import os

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "replace_this_with_a_secure_random_secret_key")

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set")

client = OpenAI(api_key=api_key)

SYSTEM_MESSAGE = {
    "role": "system",
    "content": (
        "You are a helpful math tutor that speaks concisely. "
        "Use clear step-by-step explanations when useful. "
        "If requested skills are not related to math learning, return the message: "
        "'Apologies, we are no longer supporting other skills.'"
    ),
}


def initialize_chat():
    session["messages"] = [SYSTEM_MESSAGE]


@app.route("/", methods=["GET"])
def index():
    if "messages" not in session:
        initialize_chat()

    visible_messages = session["messages"][1:]
    return render_template("index.html", messages=visible_messages)


@app.route("/chat", methods=["POST"])
def chat():
    if "messages" not in session:
        initialize_chat()

    user_input = request.json.get("user_input", "").strip() if request.is_json else ""
    if not user_input:
        return jsonify({"error": "Message cannot be empty."}), 400

    messages = list(session["messages"])
    messages.append({"role": "user", "content": user_input})
    session["messages"] = messages
    session.modified = True

    @stream_with_context
    def generate():
        try:
            stream = client.chat.completions.create(
                model="gpt-4o-mini",
                max_completion_tokens=300,
                messages=messages,
                stream=True,
            )

            for chunk in stream:
                token = chunk.choices[0].delta.content or ""
                if token:
                    yield f"data: {json.dumps({'token': token})}\n\n"

            yield "data: [DONE]\n\n"

        except Exception as exc:
            yield f"data: {json.dumps({'error': str(exc)})}\n\n"

    response = Response(generate(), mimetype="text/event-stream")
    response.headers["Cache-Control"] = "no-cache"
    response.headers["X-Accel-Buffering"] = "no"
    return response


@app.route("/clear", methods=["POST"])
def clear():
    initialize_chat()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, threaded=True)

# Run the Flask app and access it in your browser at http://127.0.0.1:5000
# python3 .\3_AI_ChatBot_Flask.py
