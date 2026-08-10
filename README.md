# Associate AI Engineer Career Track - DataCamp Projects

A comprehensive collection of hands-on projects demonstrating practical applications of modern AI APIs and transformer models. This repository covers two major areas: **OpenAI API integration** and **HuggingFace Transformers**, providing educational resources for developers learning to build production-ready AI applications.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Module 1: OpenAI Chat Completions API](#module-1-openai-chat-completions-api)
- [Module 2: HuggingFace Transformers](#module-2-huggingface-transformers)
- [Module 3: OpenAI Responses API](#module-3-openai-responses-api)
- [Requirements](#requirements)
- [Installation](#installation)
- [Environment Setup](#environment-setup)
- [Usage Examples](#usage-examples)
- [Learning Objectives](#learning-objectives)
- [Best Practices](#best-practices)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## 🎯 Project Overview

This project is designed for aspiring AI Engineers participating in DataCamp's Associate AI Engineer Career Track. It provides practical, runnable implementations covering:

- **API Integration Patterns**: Learn how to authenticate and interact with state-of-the-art language models
- **Application Architecture**: From CLI tools to full-stack web applications
- **NLP Task Diversity**: Text generation, classification, zero-shot learning, and question-answering
- **Production Patterns**: Secure API key management, session handling, error management
- **Modern ML Stack**: OpenAI's latest models and HuggingFace's pre-trained transformers

## 📁 Repository Structure

```
Associate_AI_Engineer_Career_Track/
├── 1_OpenAI_Chat_Completion_API/
│   ├── 1_Fundamentals.py
│   ├── 2_AI_ChatBot_Terminal.py
│   ├── 3_AI_ChatBot_Flask.py
│   └── templates/
│       └── index.html
├── 2_HuggingFace_API/
│   ├── 1_Task_Text_Generation_Model_GPT2.py
│   ├── 2_Task_Text_Classification_Model_Bart.py
│   ├── 3_Task_Text_Classification_AutoModel_AutoTokenizer.py
│   └── 4_Task_DocumentQA_Model_Bert.py
├── 3_OpenAI_Responses_API/
│   └── agentic_chatbot_terminal.py
├── README.md
└── LICENSE
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- An OpenAI API key (for OpenAI module)
- Basic understanding of Python and command-line interfaces

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/mhafezan/Associate_AI_Engineer_Career_Track.git
   cd Associate_AI_Engineer_Career_Track
   ```

2. **Install dependencies** (see [Installation](#installation) section)

3. **Configure environment** (see [Environment Setup](#environment-setup) section)

4. **Run your first example**
   ```bash
   python 2_HuggingFace_API/1_Task_Text_Generation_Model_GPT2.py
   ```

---

## 🔌 Module 1: OpenAI Chat Completions API

This module demonstrates practical patterns for integrating with OpenAI's Chat Completions API, progressing from simple CLI tools to full-featured web applications.

### 1.1 Fundamentals (`1_Fundamentals.py`)

**Purpose**: Master the basics of OpenAI API interactions with prompt engineering and cost estimation.

**Key Features**:
- Command-line argument parsing for flexible configuration
- System prompts for behavior control and guardrails
- Few-shot prompting for output shaping
- Token-based cost estimation
- Temperature and completion token controls

**Use Cases**:
- Learning API request structure
- Prompt engineering experimentation
- Cost analysis for API calls
- Language learning study plan generation

**Example Usage**:
```bash
python 1_OpenAI_Chat_Completion_API/1_Fundamentals.py \
  --model gpt-4o-mini \
  --user_content "I want to learn to speak Dutch. Create a study plan for me." \
  --max_completion_tokens 400 \
  --temperature 0.7 \
  --cost
```

**Key Concepts**:
- System role: Controls assistant behavior
- Few-shot examples: Demonstrates desired output format
- Temperature: Balances creativity (higher) vs. consistency (lower)
- Token counting: Tracks API usage and costs

---

### 1.2 Terminal Chatbot (`2_AI_ChatBot_Terminal.py`)

**Purpose**: Build a conversational AI that maintains context across multiple turns.

**Key Features**:
- Multi-turn conversation with message history
- Real-time user interaction from terminal
- Stateful conversation management
- Context preservation across turns
- Interactive exit mechanism

**Use Cases**:
- Building lightweight chatbots for development
- Learning conversation state management
- Local experimentation before web deployment
- Testing conversational prompts and behaviors

**Example Usage**:
```bash
python 1_OpenAI_Chat_Completion_API/2_AI_ChatBot_Terminal.py
```

**Interaction Example**:
```
Chatbot is running. Type 'exit' to quit.

Hi, how can I help you today?

User: What is calculus?
Assistant: Calculus is a branch of mathematics...

User: Can you give me a simple example?
Assistant: Sure! Let me break it down...
```

**Key Concepts**:
- Message list accumulation: Full conversation history sent with each request
- Role-based messaging: System, user, and assistant roles
- Context management: Maintaining conversational coherence
- Stateful interactions: Preserving context between API calls

---

### 1.3 Flask Web Chatbot (`3_AI_ChatBot_Flask.py`)

**Purpose**: Deploy a chatbot as a web application with browser-based UI and session management.

**Key Features**:
- Flask-based web framework integration
- Session-based conversation storage
- RESTful API endpoints
- HTML template rendering
- Chat history management and clearing

**Use Cases**:
- Building production-ready chat interfaces
- Learning web framework integration with AI APIs
- Creating shareable interfaces for AI applications
- Demonstrating multi-user session handling

**Example Usage**:
```bash
python 1_OpenAI_Chat_Completion_API/3_AI_ChatBot_Flask.py
```

Then visit `http://127.0.0.1:5000` in your browser.

**Key Concepts**:
- Flask routing: GET/POST request handling
- Session management: Per-user conversation state
- Template rendering: Dynamic HTML with Jinja2
- State persistence: Conversation history across page reloads

**HTML Interface** (`templates/index.html`):
- Responsive chat display with user/assistant differentiation
- Real-time message rendering
- Clean, modern UI with styled messages
- Clear chat functionality

---

## 🤗 Module 2: HuggingFace Transformers

This module demonstrates diverse NLP tasks using pre-trained transformer models from HuggingFace's extensive model hub.

### 2.1 Text Generation with GPT-2 (`1_Task_Text_Generation_Model_GPT2.py`)

**Purpose**: Generate creative text using a pre-trained language model.

**Key Features**:
- Pipeline abstraction for easy model usage
- Configurable token generation limits
- Multiple sequence generation
- Automatic tokenization

**Use Cases**:
- Text generation and creative writing
- Understanding model output formats
- Learning pipeline patterns

**Example Usage**:
```bash
python 2_HuggingFace_API/1_Task_Text_Generation_Model_GPT2.py
```

**Key Concepts**:
- Pipeline abstraction: Simplified model interfaces
- Token generation: Controlling output length
- Multiple outputs: Generating diverse completions
- Padding tokens: Handling sequence termination

---

### 2.2 Zero-Shot Classification with BART (`2_Task_Text_Classification_Model_Bart.py`)

**Purpose**: Classify text into arbitrary categories without fine-tuning.

**Key Features**:
- Zero-shot learning capability
- Flexible category definition
- Confidence score output
- User-defined classification schemes

**Use Cases**:
- Dynamic text categorization
- No-training-required classification
- Learning zero-shot paradigm

**Example Usage**:
```bash
python 2_HuggingFace_API/2_Task_Text_Classification_Model_Bart.py
```

Input example:
```
Enter a text to classify: "AI-powered robots assist in complex brain surgeries with precision and efficiency"
Output:
science: 0.9847
politics: 0.0089
sports: 0.0064
```

**Key Concepts**:
- Zero-shot learning: No model fine-tuning required
- Category flexibility: Arbitrary classification schemes
- Confidence scores: Model certainty measures
- Entailment-based classification

---

### 2.3 Sentiment Analysis with DistilBERT (`3_Task_Text_Classification_AutoModel_AutoTokenizer.py`)

**Purpose**: Perform sentiment analysis using fine-tuned BERT models.

**Key Features**:
- Auto-loading of tokenizer and model
- Sentiment classification (positive/negative)
- Confidence scoring
- Fine-tuned model utilization

**Use Cases**:
- Sentiment analysis for content
- Learning AutoModel patterns
- Production-ready classification

**Example Usage**:
```bash
python 2_HuggingFace_API/3_Task_Text_Classification_AutoModel_AutoTokenizer.py
```

Input example:
```
Enter a text to classify: "I love this movie! It's fantastic and full of surprises."
Output:
Label: POSITIVE, Confidence Score: 0.9989
```

**Key Concepts**:
- AutoModel/AutoTokenizer: Automatic architecture loading
- Fine-tuned models: Pre-trained on specific tasks
- Tokenization: Converting text to model inputs
- Pipeline pattern: Simplifying complex workflows

---

### 2.4 Document Question-Answering with BERT (`4_Task_DocumentQA_Model_Bert.py`)

**Purpose**: Extract answers from documents using question-answering models.

**Key Features**:
- PDF document processing
- Context-based question answering
- Extractive QA (finds spans in text)
- No fine-tuning required

**Use Cases**:
- Automated document analysis
- Knowledge extraction from PDFs
- Building FAQ systems
- Document-based Q&A interfaces

**Example Usage**:
```bash
python 2_HuggingFace_API/4_Task_DocumentQA_Model_Bert.py
```

**Workflow**:
1. Loads PDF file (`employee_policy.pdf`)
2. Extracts text from all pages
3. User provides a question
4. Model finds and returns relevant answer span

**Example**:
```
Enter your question: "What is the vacation policy?"
Answer: "Employees receive 20 days of paid vacation annually."
```

**Key Concepts**:
- Document processing: PDF text extraction
- Extractive QA: Span-based answer finding
- Context awareness: Document-aware reasoning
- Information retrieval: Finding relevant text sections

---

## 🧠 Module 3: OpenAI Responses API

This module demonstrates a stateful, streaming terminal chatbot built with the OpenAI Responses API.

### 3.1 Global Tour Guide Chatbot (`agentic_chatbot_terminal.py`)

**Purpose**: Build a global tour guide that can answer travel questions with current online information while preserving multi-turn context without repeatedly sending the complete message history.

**Key Features**:
- OpenAI Responses API
- `gpt-5.4-mini` with low reasoning effort
- Maximum output limit of 400 tokens
- Real-time streaming in the terminal
- Multi-turn context using `previous_response_id`
- Built-in web search using `tools=[{"type": "web_search"}]`
- Travel guidance for attractions, culture, food, transportation, accommodations, itineraries, budgets, weather, accessibility, entry requirements, and safety
- Current, location-specific answers for opening hours, prices, events, schedules, entry rules, and travel advisories
- Instructions to distinguish verified current facts from general travel guidance
- Concise, practical output formatted for a plain-text terminal
- Secure API-key loading from `OPENAI_API_KEY`

**Example Usage**:
```powershell
python .\3_OpenAI_Responses_API\agentic_chatbot_terminal.py
```

**Interaction Example**:
```text
Chatbot is running. Type 'exit' to quit.

Hi! Where would you like to explore today?

User: What are the best attractions to visit in Toronto this weekend?
Assistant: Here are several current options for Toronto this weekend...
```

**Key Concepts**:
- Responses API: Generates stateful model responses
- Reasoning effort: Uses `low` reasoning for concise travel assistance
- Response chaining: Passes `previous_response_id` into the next request
- Streaming events: Prints `response.output_text.delta` events as they arrive
- Web search tool: Produces a `web_search_call` when current online information is needed
- Travel guardrails: Encourages confirmation of important requirements with official authorities before booking or departure
- Model compatibility: Uses the model's default sampling because `temperature` is not supported

---

## 📦 Requirements

### Core Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `openai` | Latest | OpenAI API SDK |
| `flask` | Latest | Web framework for chatbot UI |
| `transformers` | Latest | HuggingFace transformer models |
| `torch` | Latest | Deep learning framework |
| `pypdf` | Latest | PDF processing |

### Optional Dependencies

- `python-dotenv`: For .env file support
- `gunicorn`: For production Flask deployment

---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/mhafezan/Associate_AI_Engineer_Career_Track.git
cd Associate_AI_Engineer_Career_Track
```

### 2. Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
# Install all requirements
pip install openai flask transformers torch pypdf

# Or install individual modules as needed
# For OpenAI module
pip install openai flask

# For HuggingFace module
pip install transformers torch pypdf
```

### 4. Verify Installation

```bash
python -c "import openai; import flask; import transformers; print('All dependencies installed!')"
```

---

## 🔐 Environment Setup

### OpenAI API Key Configuration

The OpenAI examples require an API key. Set it as an environment variable before running any OpenAI scripts.

#### Windows (PowerShell)

```powershell
$env:OPENAI_API_KEY = "sk-your-api-key-here"
```

To make it permanent:
```powershell
setx OPENAI_API_KEY "sk-your-api-key-here"
```

#### Windows (Command Prompt)

```cmd
setx OPENAI_API_KEY "sk-your-api-key-here"
```

#### macOS/Linux

```bash
export OPENAI_API_KEY="sk-your-api-key-here"
```

To make it permanent, add to `~/.bash_profile` or `~/.zshrc`:
```bash
echo 'export OPENAI_API_KEY="sk-your-api-key-here"' >> ~/.bash_profile
source ~/.bash_profile
```

#### Verification

```bash
python -c "import os; print('API Key set:', bool(os.getenv('OPENAI_API_KEY')))"
```

---

## 💻 Usage Examples

### OpenAI Module Examples

#### Example 1: Generate a Language Learning Plan

```bash
python 1_OpenAI_Chat_Completion_API/1_Fundamentals.py \
  --model gpt-4o-mini \
  --user_content "I want to learn to speak French. Create a 30-day study plan." \
  --max_completion_tokens 500 \
  --temperature 0.7 \
  --cost
```

#### Example 2: Interactive Math Tutor

```bash
python 1_OpenAI_Chat_Completion_API/2_AI_ChatBot_Terminal.py
```

Then interact:
```
User: What is the derivative of x^2?
Assistant: The derivative of x^2 is 2x. This comes from...

User: Can you explain the power rule?
Assistant: The power rule states that for a function f(x) = x^n...
```

#### Example 3: Web-Based Chatbot

```bash
python 1_OpenAI_Chat_Completion_API/3_AI_ChatBot_Flask.py
```

Open browser to `http://127.0.0.1:5000`

#### Example 4: Streaming Responses API Global Tour Guide

```powershell
python .\3_OpenAI_Responses_API\agentic_chatbot_terminal.py
```

The chatbot can search the web for current travel information, streams its answers, and retains conversation context by chaining each request with `previous_response_id`.

### HuggingFace Module Examples

#### Example 1: Generate Text

```bash
python 2_HuggingFace_API/1_Task_Text_Generation_Model_GPT2.py
```

Output:
```
Hi, how are you doing today? I'm doing great, thanks for asking!

Hi, how are you doing today? Not much, just relaxing at home.
```

#### Example 2: Zero-Shot Classification

```bash
python 2_HuggingFace_API/2_Task_Text_Classification_Model_Bart.py
```

Input: `"NASA launches new Mars rover for deep space exploration"`

Output:
```
science: 0.9876
politics: 0.0089
sports: 0.0035
```

#### Example 3: Sentiment Analysis

```bash
python 2_HuggingFace_API/3_Task_Text_Classification_AutoModel_AutoTokenizer.py
```

Input: `"This product is amazing! Highly recommend!"`

Output:
```
Label: POSITIVE, Confidence Score: 0.9995
```

#### Example 4: Document Question-Answering

```bash
python 2_HuggingFace_API/4_Task_DocumentQA_Model_Bert.py
```

Workflow:
1. Place `employee_policy.pdf` in the script directory
2. Run the script
3. Input: `"How many vacation days do employees get?"`
4. Output: `"20 days of paid vacation per year"`

---

## 🎓 Learning Objectives

By completing this project, you will understand:

### API Integration
- ✅ Authenticating with modern AI APIs
- ✅ Crafting effective API requests
- ✅ Using both Chat Completions and Responses APIs
- ✅ Streaming Responses API output events
- ✅ Using hosted web search in Responses API applications
- ✅ Error handling and validation
- ✅ Cost estimation and monitoring

### Prompt Engineering
- ✅ System prompts for behavior control
- ✅ Few-shot prompting for output guidance
- ✅ Temperature and token controls
- ✅ Guardrails and safety considerations

### Application Architecture
- ✅ CLI tools for simple interactions
- ✅ Terminal-based interactive applications
- ✅ Web frameworks (Flask) integration
- ✅ Session management and state persistence
- ✅ Multi-turn response chaining with `previous_response_id`

### NLP Tasks
- ✅ Text generation and completion
- ✅ Text classification (supervised and zero-shot)
- ✅ Sentiment analysis
- ✅ Question-answering systems
- ✅ Document processing

### ML Engineering
- ✅ Model selection and loading
- ✅ Tokenization and preprocessing
- ✅ Pipeline abstraction patterns
- ✅ Confidence scoring and uncertainty

---

## 🏆 Best Practices

### Security
- ✅ Never hardcode API keys
- ✅ Always use environment variables
- ✅ Implement API rate limiting in production
- ✅ Validate and sanitize user inputs
- ✅ Use HTTPS for all API communication

### Code Quality
- ✅ Add error handling for API failures
- ✅ Implement logging for debugging
- ✅ Use type hints for clarity
- ✅ Follow PEP 8 style guidelines
- ✅ Add docstrings to functions

### Performance
- ✅ Cache model loading to avoid redundant downloads
- ✅ Batch API requests when possible
- ✅ Implement connection pooling
- ✅ Monitor token usage and costs
- ✅ Use streaming for long-form content

### Development
- ✅ Start with simpler models before complex ones
- ✅ Test with small datasets first
- ✅ Use version control for tracking changes
- ✅ Document API changes and updates
- ✅ Keep dependencies up to date

---

## 🚀 Future Enhancements

Suggested improvements to extend these projects:

### OpenAI Module
- [x] Add streaming response support for real-time output
- [ ] Implement conversation persistence to database
- [x] Add multi-turn conversation management
- [ ] Create conversation history export (PDF/JSON)
- [ ] Implement rate limiting and usage analytics
- [ ] Add user authentication and multi-user support
- [ ] Deploy with production WSGI server (Gunicorn)
- [ ] Add conversation analytics and insights

### HuggingFace Module
- [ ] Add model fine-tuning on custom datasets
- [ ] Implement batch processing for multiple documents
- [ ] Create evaluation metrics and benchmarks
- [ ] Add model caching and optimization
- [ ] Build API endpoints for model serving
- [ ] Implement A/B testing for model comparison
- [ ] Add monitoring and performance tracking
- [ ] Create dataset creation and annotation tools

### Cross-Module
- [ ] Create unified CLI with subcommands
- [ ] Build dashboard for model monitoring
- [ ] Add A/B testing framework
- [ ] Implement cost comparison tools
- [ ] Create automated testing suite
- [ ] Build CI/CD pipeline
- [ ] Add Docker containerization
- [ ] Create deployment templates

---

## 📚 Additional Resources

### OpenAI Documentation
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [Chat Completions Guide](https://platform.openai.com/docs/guides/gpt)
- [Responses API Guide](https://developers.openai.com/api/docs/guides/responses)
- [Prompt Engineering Best Practices](https://platform.openai.com/docs/guides/prompt-engineering)

### HuggingFace Documentation
- [HuggingFace Transformers](https://huggingface.co/docs/transformers/)
- [Model Hub](https://huggingface.co/models)
- [Pipeline Documentation](https://huggingface.co/docs/transformers/main_classes/pipelines)

### Learning Resources
- [DataCamp Associate AI Engineer Track](https://www.datacamp.com/)
- [OpenAI Cookbook](https://github.com/openai/openai-cookbook)
- [HuggingFace Course](https://huggingface.co/course)

---

## 👤 Author

**Mohammad Hafezan**
AI/ML Systems | Embedded AI | Computer Architecture | AI Security

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to:
- Report bugs and issues
- Suggest improvements and enhancements
- Submit pull requests with new features
- Share your own project implementations

---

## 📞 Support

For questions, issues, or feedback:
- Open an issue on GitHub
- Check existing documentation
- Review code comments and docstrings
- Consult official API documentation

---

**Last Updated**: August 2026
**Python Version**: 3.8+  
**Status**: Active Development
