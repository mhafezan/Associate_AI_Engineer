# Working with the OpenAI API

This repository contains three Python applications that demonstrate practical integration patterns with the OpenAI API, ranging from a command-line prompt-driven tool to interactive chatbot interfaces in both terminal and web environments.

## Repository Overview

The codebase is organized into three standalone scripts, each designed to illustrate a different application pattern:

- **`1_Fundamentals.py`** — a command-line OpenAI client for controlled prompt execution and optional cost estimation.
- **`2_AI_ChatBot_Terminal.py`** — a terminal-based conversational chatbot that maintains message history across turns.
- **`3_AI_ChatBot_Flask.py`** — a Flask-powered web chatbot with session-based conversation state and browser UI support.

Together, these files provide a useful progression from API fundamentals to interactive application development.

---

## File-by-File Description

### 1. `1_Fundamentals.py`

This script demonstrates the fundamentals of interacting with the OpenAI Chat Completions API from a Python command-line interface.

#### Core capabilities
- Parses runtime arguments using `argparse`
- Accepts a model name, prompt content, token limit, and temperature
- Applies a system prompt to constrain the assistant’s behavior
- Uses a few-shot example to guide output style
- Optionally estimates request cost using token counts

#### Main use case
This file is appropriate for:
- learning basic request structure
- testing prompt engineering
- experimenting with response controls
- building a simple reusable CLI tool

#### Example command

```bash
python 1_Fundamentals.py --model gpt-4o-mini --user_content "I want to learn to speak Dutch. Create a study plan for me." --max_completion_tokens 400 --temperature 0.7 --cost
```

#### Notes
- The script expects the OpenAI API key in an environment variable.
- Cost estimation is approximate and depends on the selected model pricing.

---

### 2. `2_AI_ChatBot_Terminal.py`

This script implements a conversational chatbot that runs in the terminal.

#### Core capabilities
- Loads the OpenAI API key securely from the environment
- Accepts user input interactively from the terminal
- Preserves conversation context in a `messages` list
- Sends the full chat history to the model on each turn
- Supports quitting with `exit` or `quit`

#### Main use case
This file is appropriate for:
- learning multi-turn conversation handling
- building a lightweight local chatbot
- testing conversational prompts in a development environment

#### Example run

```bash
python 2_AI_ChatBot_Terminal.py
```

#### Interaction example

```text
User: Explain what pi is.
Assistant: Pi is the ratio of a circle's circumference to its diameter.

User: Summarize that in one sentence.
Assistant: Pi is the constant ratio between a circle’s circumference and diameter.
```

#### Notes
- This script is designed as a minimal chatbot prototype.
- It is ideal for local experimentation before adding logging, streaming, or UI layers.

---

### 3. `3_AI_ChatBot_Flask.py`

This script extends the chatbot concept into a web application using Flask.

#### Core capabilities
- Creates a browser-accessible chatbot using Flask
- Stores chat history in the user session
- Uses an OpenAI model to answer user prompts
- Renders messages through an HTML template
- Supports clearing conversation history with a dedicated route

#### Main use case
This file is appropriate for:
- learning how to integrate the OpenAI API into web applications
- building a simple chat interface for demonstrations
- prototyping AI-enabled backend services

#### Example run

```bash
python 3_AI_ChatBot_Flask.py
```

Then open:

```text
http://127.0.0.1:5000
```

#### Notes
- The Flask script requires a corresponding HTML template such as `templates/index.html`.
- For production use, the Flask `secret_key` should be moved to a secure environment variable.

---

## Requirements

Install the required packages before running the scripts:

```bash
pip install openai flask
```

> `flask` is only required for the web-based chatbot. The first two scripts only require the OpenAI Python SDK.

---

## Environment Setup

Set your OpenAI API key as an environment variable.

### Windows PowerShell

```powershell
setx OPENAI_API_KEY "your-api-key-here"
```

After setting the variable, restart your terminal or VS Code session.

---

## Project Highlights

This repository demonstrates several important concepts relevant to practical AI application development:

- **Prompt engineering** using system and user roles
- **Few-shot prompting** for response shaping
- **Conversational memory** using message history
- **Session-based state management** in Flask
- **CLI and web-based AI application patterns**
- **Basic token-cost estimation**

---

## Suggested Next Improvements

This project is a strong foundation for extending into more production-oriented AI applications. The following enhancements would be natural next steps:

- streaming responses for real-time output
- dynamic pricing per model
- structured logging and analytics
- error handling and retry logic
- model selection from the interface
- persistent chat storage
- deployment using Flask with a production WSGI server

---

## Author

**Mohammad Hafezan**  
AI/ML Systems | Embedded AI | Computer Architecture
