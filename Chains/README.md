# LangChain Chains

Hands-on exploration of **Chains** in LangChain — combining prompts, models, and parsers into pipelines using LangChain Expression Language (LCEL), including sequential, parallel, and conditional flows.

Part of my [LangChain Fundamentals](../) learning series.

## 📌 Overview

Chains let you connect multiple steps (prompt → model → parser → next prompt...) into a single pipeline using the `|` (pipe) operator. This folder covers the four main chain patterns.

## 🚀 What's Covered

| File | Description |
|---|---|
| `one.py` | Basic setup — connecting to a Hugging Face model |
| `simple_chain.py` | A single prompt → model → parser chain |
| `sequential_chain.py` | Multiple chained steps where output of one feeds into the next |
| `parallel_chain.py` | Running multiple chains simultaneously using `RunnableParallel` |
| `conditional_chains.py` | Branching logic with `RunnableBranch` based on classified input (e.g. sentiment) |

## 🛠️ Tech Stack
- Python 3.x
- LangChain / langchain-core
- langchain-huggingface (`ChatHuggingFace`, `HuggingFaceEndpoint`)
- Pydantic (for structured classification in conditional chains)

## 📂 Folder Structure
```
Chains/
├── one.py
├── simple_chain.py
├── sequential_chain.py
├── parallel_chain.py
├── conditional_chains.py
├── requirements.txt
├── .env              # not pushed (see .gitignore)
├── .gitignore
└── README.md
```

## ⚙️ Setup & Installation

```bash
git clone https://github.com/somil02/Langchain.git
cd Langchain/Chains
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
python simple_chain.py
python sequential_chain.py
python parallel_chain.py
python conditional_chains.py
```

## 📖 What I Learned
- How LCEL's `|` operator composes prompts, models, and parsers into a single pipeline
- Difference between sequential and parallel chain execution
- Using `RunnableBranch` with a Pydantic-classified input to route logic conditionally
- Using `RunnableLambda` to wrap custom functions inside a chain

## 📜 License
MIT
