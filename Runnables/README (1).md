# LangChain Runnables

Hands-on exploration of the **Runnable** interface in LangChain — the core abstraction behind LCEL (`|` syntax) that lets prompts, models, parsers, and custom functions all be composed together the same way.

Part of my [LangChain Fundamentals](../) learning series.

## 📌 Overview

Every component in LangChain (prompts, models, parsers, retrievers) implements the `Runnable` interface, which is what makes chaining them with `|` possible. This folder breaks down each `Runnable` primitive individually.

## 🚀 What's Covered

| File | Description |
|---|---|
| `Runnable_seq.py` | `RunnableSequence` — chaining steps one after another |
| `Runnable.parallel.py` | `RunnableParallel` — running multiple branches simultaneously |
| `Runnable_passthrough.py` | `RunnablePassthrough` — forwarding input unchanged alongside other branches |
| `Runnable_branch.py` | `RunnableBranch` — conditional routing between chains |
| `Runnable_lambda.py` | `RunnableLambda` — wrapping custom Python functions as a Runnable step |
| `langchain_mentos_zindagi.ipynb` | Notebook walkthrough example |
| `langchain_aam_zindagi.ipynb` | Notebook walkthrough example |

## 🛠️ Tech Stack
- Python 3.x
- LangChain / langchain-core
- langchain-huggingface (`ChatHuggingFace`, `HuggingFaceEndpoint`)
- Jupyter Notebook

## 📂 Folder Structure
```
Runnables/
├── Runnable_seq.py
├── Runnable.parallel.py
├── Runnable_passthrough.py
├── Runnable_branch.py
├── Runnable_lambda.py
├── langchain_mentos_zindagi.ipynb
├── langchain_aam_zindagi.ipynb
├── requirements.txt
├── .env              # not pushed (see .gitignore)
├── .gitignore
└── README.md
```

## ⚙️ Setup & Installation

```bash
git clone https://github.com/somil02/Langchain.git
cd Langchain/Runnables
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
python Runnable_seq.py
python Runnable.parallel.py
python Runnable_branch.py
```
Or open the notebooks:
```bash
jupyter notebook
```

## 📖 What I Learned
- How all LangChain components share the same `Runnable` interface, enabling the `|` pipe syntax
- Difference between sequential, parallel, and conditional (branch) execution
- Using `RunnablePassthrough` to pass original input through unmodified alongside transformed branches
- Wrapping arbitrary Python logic into a chain using `RunnableLambda`

## 📜 License
MIT
