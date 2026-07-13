# LangChain Structured Output

Hands-on exploration of getting **structured, typed output** from LLMs using LangChain — covering TypedDict, Pydantic, and JSON Schema approaches.

Part of my [LangChain Fundamentals](../) learning series.

## 📌 Overview

By default, LLMs return free-form text. This folder demonstrates how to force models to return **structured, validated data** instead — useful for building reliable pipelines where output needs to be parsed programmatically (e.g. extracting sentiment, themes, and summary from a review).

## 🚀 What's Covered

| File | Description |
|---|---|
| `typeddict.py` | Basic Python `TypedDict` usage (no LangChain) |
| `pydantic_demo.py` | Basic Pydantic `BaseModel` usage with field validation (no LangChain) |
| `with_structured_output_typed_dict.py` | Using `.with_structured_output()` with a `TypedDict` schema |
| `with_structured_output_pydantic.py` | Using `.with_structured_output()` with a Pydantic schema |
| `with_structured_output_json.py` | Using `.with_structured_output()` with a raw JSON Schema |

## 🛠️ Tech Stack
- Python 3.x
- LangChain / langchain-openai
- Pydantic
- OpenAI (Chat Model)

## 📂 Folder Structure
```
Langchain_structured_output/
├── typeddict.py
├── pydantic_demo.py
├── with_structured_output_typed_dict.py
├── with_structured_output_pydantic.py
├── with_structured_output_json.py
├── requirements.txt
├── .env              # not pushed (see .gitignore)
├── .gitignore
└── README.md
```

## ⚙️ Setup & Installation

```bash
git clone https://github.com/somil02/Langchain.git
cd Langchain/Structured-Output
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in this folder:
```
OPENAI_API_KEY=your_key_here
```

## ▶️ Usage

```bash
python with_structured_output_pydantic.py
python with_structured_output_typed_dict.py
python with_structured_output_json.py
```

## 📖 What I Learned
- Difference between `TypedDict` and `Pydantic` for defining schemas
- How `.with_structured_output()` forces LLM responses into a validated schema
- Using `Literal`, `Optional`, and `Field` for constraints and descriptions that guide the LLM's output
- When to use JSON Schema directly vs. Python-native schema classes

## 📜 License
MIT
