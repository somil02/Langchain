# LangChain Document Loaders

Hands-on exploration of **Document Loaders** in LangChain — ingesting data from different sources (text, CSV, PDF, folders, web pages) into a unified `Document` format for downstream use in RAG pipelines.

Part of my [LangChain Fundamentals](../) learning series.

## 📌 Overview

Before you can chunk, embed, or retrieve data, you first need to **load** it into LangChain's `Document` object. This folder covers the main loader types for different data sources.

## 🚀 What's Covered

| File | Description |
|---|---|
| `text_loader.py` | `TextLoader` — loading a plain `.txt` file, then summarizing it with an LLM |
| `CSVLoader.py` | `CSVLoader` — loading rows from a `.csv` file as documents |
| `PyPdfLoader.py` | `PyPDFLoader` — loading text from a PDF, page by page |
| `DirectoryLoader.py` | `DirectoryLoader` — loading multiple files from a folder (with glob patterns) |
| `webBaseLoader.py` | `WebBaseLoader` — scraping and loading content directly from a web page URL |

> Note: sample data used to test these loaders (`books/`, PDFs) is kept local only and excluded from this repo — see `.gitignore`.

## 🛠️ Tech Stack
- Python 3.x
- LangChain / langchain-community / langchain-core
- langchain-huggingface (`ChatHuggingFace`, `HuggingFaceEndpoint`)
- pypdf, BeautifulSoup4 (used internally by loaders)

## 📂 Folder Structure
```
DocumentLoader/
├── text_loader.py
├── CSVLoader.py
├── PyPdfLoader.py
├── DirectoryLoader.py
├── webBaseLoader.py
├── cricket.txt
├── Social_Network_Ads.csv
├── requirements.txt
├── .env              # not pushed (see .gitignore)
├── .gitignore
└── README.md
```
*(local-only, not pushed: `books/` folder and any full PDF documents used for testing — kept out to avoid distributing copyrighted material)*

## ⚙️ Setup & Installation

```bash
git clone https://github.com/somil02/Langchain.git
cd Langchain/DocumentLoader
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
python text_loader.py
python CSVLoader.py
python PyPdfLoader.py
python DirectoryLoader.py
python webBaseLoader.py
```

## 📖 What I Learned
- How different loaders standardize different data sources into the same `Document` schema
- Using glob patterns with `DirectoryLoader` to selectively load files from nested folders
- Trade-offs between `PyPDFLoader` and other PDF loaders (tables, scanned docs, layout-heavy PDFs)
- Loading and summarizing live web content directly with `WebBaseLoader`

## 📜 License
MIT
