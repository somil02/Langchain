# LangChain Retrievers

Hands-on exploration of **Retrievers** in LangChain — fetching relevant documents from a vector store (or other source) given a query, as the retrieval half of a RAG pipeline.

Part of my [LangChain Fundamentals](../) learning series.

## 📌 Overview

A retriever wraps a vector store (or other document source) with a standard `.invoke(query)` interface, returning the most relevant documents. This notebook walks through setting up and using retrievers.

## 🛠️ Tech Stack
- Python 3.x
- LangChain / langchain-community
- langchain-huggingface (embeddings)
- Chroma / FAISS (vector store)
- Jupyter Notebook

## 📂 Folder Structure
```
Langchain_retrievers/
├── Retrievers.ipynb
├── requirements.txt
├── .env              # not pushed (see .gitignore)
├── .gitignore
└── README.md
```

## ⚙️ Setup & Installation

```bash
git clone https://github.com/somil02/Langchain.git
cd Langchain/Langchain_retrievers
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in this folder:
```
HF_TOKEN=your_key_here
```
The notebook loads this via `python-dotenv` — never hardcode tokens directly in notebook cells.

## ▶️ Usage

```bash
jupyter notebook Retrievers.ipynb
```

## 📖 What I Learned
- How retrievers standardize document lookup across different vector store backends
- Difference between similarity search and other retrieval strategies
- Why API keys should always be loaded via `.env` + `python-dotenv`, never hardcoded in notebook cells — hardcoded tokens get committed permanently into notebook history since notebooks are plain JSON files

## 📜 License
MIT
