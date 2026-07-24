# RAG Mini — YouTube Transcript Q&A

A small end-to-end **RAG (Retrieval-Augmented Generation)** pipeline — fetching a YouTube video transcript, chunking it, embedding it, storing it in a vector store, and querying it with an LLM.

Part of my [LangChain Fundamentals](../) learning series.

## 📌 Overview

This notebook ties together everything from earlier folders (document loading, text splitting, embeddings, vector stores, retrievers) into one complete RAG pipeline: fetch a YouTube transcript → split into chunks → embed and store → retrieve relevant chunks for a question → generate an answer grounded in the transcript.

## 🚀 What's Covered
- Fetching a video transcript using `youtube-transcript-api`
- Splitting the transcript into chunks
- Embedding chunks and storing them in a vector store
- Retrieving relevant chunks for a user question
- Generating a grounded answer using an LLM

## 🛠️ Tech Stack
- Python 3.x
- LangChain / langchain-community
- youtube-transcript-api
- langchain-huggingface (embeddings + chat model)
- ChromaDB (vector store)
- Jupyter Notebook

## 📂 Folder Structure
```
RAG_MINI/
├── YT_Transcript.ipynb
├── requirements.txt
├── .env              # not pushed (see .gitignore)
├── .gitignore
└── README.md
```

## ⚙️ Setup & Installation

```bash
git clone https://github.com/somil02/Langchain.git
cd Langchain/RAG_MINI
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
jupyter notebook YT_Transcript.ipynb
```

## 📖 What I Learned
- How to wire together loading, splitting, embedding, storing, and retrieving into one working RAG pipeline
- Fetching and cleaning transcript data from an external API
- Why grounding LLM answers in retrieved context reduces hallucination compared to relying on the model's raw knowledge

## 📜 License
MIT
