# LangChain Tools

Hands-on exploration of **Tools** in LangChain — defining, binding, and invoking tools so LLMs can take actions beyond text generation.

Part of my [LangChain Fundamentals](../) learning series.

## 📌 Overview

Tools let an LLM call external functions (APIs, calculators, search, custom Python functions) as part of its reasoning. This notebook walks through creating custom tools, using built-in tools, binding tools to a model, and handling tool calls in a response.

## 🛠️ Tech Stack
- Python 3.x
- LangChain / langchain-community
- langchain-openai (or your preferred chat model provider)
- Jupyter Notebook

## 📂 Folder Structure
```
langchain_tools/
├── langchain_tools.ipynb
├── requirements.txt
├── .env              # not pushed (see .gitignore)
├── .gitignore
└── README.md
```

## ⚙️ Setup & Installation

```bash
git clone https://github.com/somil02/Langchain.git
cd Langchain/langchain_tools
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in this folder:
```
OPENAI_API_KEY=your_key_here
```
The notebook loads these via `python-dotenv` — never hardcode tokens directly in notebook cells.

## ▶️ Usage

```bash
jupyter notebook langchain_tools.ipynb
```

## 📖 What I Learned
- How to define custom tools using the `@tool` decorator
- Difference between built-in tools and custom tools
- How to bind tools to a chat model and inspect tool calls in the model's response
- How to route tool calls back into the model to produce a final answer

## 📜 License
MIT
