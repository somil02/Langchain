# LangChain Models

Hands-on exploration of the **Models** component in LangChain — covering LLMs, Chat Models, and Embedding Models across both **open-source** and **closed-source** providers.

Part of my [LangChain Fundamentals](../) learning series.

## 📌 Overview

LangChain provides a unified interface to interact with different types of language and embedding models. This folder demonstrates:
- Calling **closed-source** models (e.g. OpenAI, Gemini) via API
- Running **open-source** models (e.g. via HuggingFace, Ollama)
- Using **Chat Models** for conversational interactions
- Generating **Embeddings** for semantic search / vector representations

## 🚀 What's Covered

| Concept | Description |
|---|---|
| LLMs | Basic text completion models |
| Chat Models | Conversational models with message-based input (Human/AI/System) |
| Open-Source Models | Running models locally or via free-tier APIs (e.g. HuggingFace, Ollama) |
| Embedding Models | Converting text into vector representations |

## 🛠️ Tech Stack
- Python 3.x
- LangChain / langchain-core
- OpenAI / Google Generative AI (closed-source)
- HuggingFace / Ollama (open-source)

## 📂 Folder Structure
```
LANGCHAIN_MODELS/
├── 1.LLM/
├── 2.ChatModels/
│   ├── 1.chatmodel_hf_api.py
│   └── 2.chatmodel_hf_local.py
├── 3.EmbeddedModels/
│   ├── 1.Embedding.local.py
│   ├── 2.document_similarity.py
│   └── 3.document_RAG.py
├── test.py
├── requirements.txt
├── .env              # not pushed (see .gitignore)
├── .gitignore
└── README.md
```

## ⚙️ Setup & Installation

```bash
git clone https://github.com/somil02/Langchain.git
cd Langchain/models
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in this folder:
```
OPENAI_API_KEY=your_key_here
GOOGLE_API_KEY=your_key_here
HUGGINGFACEHUB_API_TOKEN=your_key_here
```

## ▶️ Usage

```bash
python chat_model_demo.py
python embedding_demo.py
```

## 📖 What I Learned
- Difference between LLMs and Chat Models in LangChain
- How to swap between open-source and closed-source models with minimal code change
- How embeddings are generated and used for downstream tasks like similarity search

## 📜 License
MIT
