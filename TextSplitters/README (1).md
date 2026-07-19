# LangChain Text Splitters

Hands-on exploration of **Text Splitters** in LangChain — breaking large documents into smaller chunks for embedding and retrieval, using length-based, structure-based, syntax-aware, and semantic strategies.

Part of my [LangChain Fundamentals](../) learning series.

## 📌 Overview

LLMs and embedding models have context limits, so large documents need to be split into smaller chunks before being embedded or passed to a model. This folder covers different chunking strategies, from simple to semantic.

## 🚀 What's Covered

| File | Description |
|---|---|
| `Length_based_split.py` | `CharacterTextSplitter` — splitting a PDF/text purely by character length |
| `text_structure_based.py` | `RecursiveCharacterTextSplitter` — splitting using a hierarchy of separators (paragraph → line → word → char) |
| `markdown_splitting.py` | Splitting Markdown documents while respecting headers/structure |
| `python_code_splitting.py` | Splitting source code while respecting syntax (functions/classes stay intact) |
| `semantic_meaning_based.py` | `SemanticChunker` — splitting based on semantic similarity using embeddings, not fixed length |

> Note: the PDF used to test `Length_based_split.py` is kept local only and excluded from this repo — see `.gitignore`.

## 🛠️ Tech Stack
- Python 3.x
- LangChain / langchain-text-splitters / langchain-community
- langchain-experimental (`SemanticChunker`)
- langchain-huggingface (`HuggingFaceEmbeddings`)
- sentence-transformers

## 📂 Folder Structure
```
TextSplitters/
├── Length_based_split.py
├── text_structure_based.py
├── markdown_splitting.py
├── python_code_splitting.py
├── semantic_meaning_based.py
├── requirements.txt
├── .env              # not pushed (see .gitignore)
├── .gitignore
└── README.md
```
*(local-only, not pushed: PDF file used for testing — kept out to avoid distributing copyrighted material)*

## ⚙️ Setup & Installation

```bash
git clone https://github.com/somil02/Langchain.git
cd Langchain/TextSplitters
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
python Length_based_split.py
python text_structure_based.py
python markdown_splitting.py
python python_code_splitting.py
python semantic_meaning_based.py
```

## 📖 What I Learned
- Difference between fixed-length, structure-aware, and semantic chunking
- How `RecursiveCharacterTextSplitter` falls back through separators to keep chunks meaningful
- Using `Language` enum to split code/markdown while preserving syntax boundaries
- How `SemanticChunker` uses embedding similarity to decide chunk boundaries instead of a fixed size

## 📜 License
MIT
