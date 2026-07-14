# LangChain Output Parsers

Hands-on exploration of **Output Parsers** in LangChain — converting raw LLM text output into structured, usable formats (strings, JSON, Pydantic objects) using Hugging Face models.

Part of my [LangChain Fundamentals](../) learning series.

## 📌 Overview

LLM responses come back as plain text by default. Output parsers instruct the model on the expected format and then parse the raw response into that format. This folder covers the main parser types available in LangChain.

## 🚀 What's Covered

| File | Description |
|---|---|
| `str_output_Parser.py` | Chaining multiple prompts without an explicit parser |
| `str_output_Parser1.py` | Using `StrOutputParser` to cleanly extract string output |
| `json_output_parser.py` | Using `JsonOutputParser` to get JSON-formatted output |
| `pydantic_output_parser.py` | Using `PydanticOutputParser` for schema-validated output |
| `structured_output_parser.py` | Using `StructuredOutputParser` with `ResponseSchema` (⚠️ deprecated in LangChain v1.0+, kept for reference) |

## 🛠️ Tech Stack
- Python 3.x
- LangChain / langchain-core
- langchain-huggingface (`ChatHuggingFace`, `HuggingFaceEndpoint`)
- Pydantic

## 📂 Folder Structure
```
Output_parser/
├── str_output_Parser.py
├── str_output_Parser1.py
├── json_output_parser.py
├── pydantic_output_parser.py
├── structured_output_parser.py
├── requirements.txt
├── .env              # not pushed (see .gitignore)
├── .gitignore
└── README.md
```

## ⚙️ Setup & Installation

```bash
git clone https://github.com/somil02/Langchain.git
cd Langchain/Output_parser
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in this folder:
```
HUGGINGFACEHUB_API_TOKEN=your_key_here
```

## ▶️ Usage

```bash
python str_output_Parser1.py
python json_output_parser.py
python pydantic_output_parser.py
```

## 📖 What I Learned
- How `StrOutputParser`, `JsonOutputParser`, and `PydanticOutputParser` differ in what they enforce
- Chaining prompts and parsers together using LangChain's pipe (`|`) syntax
- That `StructuredOutputParser` is deprecated in LangChain v1.0+ in favor of Pydantic-based structured output

## 📜 License
MIT
