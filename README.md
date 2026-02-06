
# 📄 RAG PDF Chat (Local)

A **local Retrieval-Augmented Generation (RAG) system** that allows users to **ask natural language questions from PDF documents** using a **terminal-based chat interface**.

The system runs **fully offline** using **Ollama**, **FAISS**, and **LangChain**, and supports **conversation memory**, **source citation**, and a **Streamlit-like terminal UI** built with **Textual**.

---

## 🚀 Features

* 📚 **PDF Question Answering** using RAG
* 🧠 **Semantic Search** with FAISS vector store
* 🤖 **Local LLMs via Ollama** (phi3.5 / llama3.1)
* 💬 **Chat-based Interface** (Terminal UI)
* 🧾 **Source Citation Toggle** (view retrieved chunks)
* 🧠 **Conversation Memory** (context-aware follow-ups)
* 🔒 **Fully Offline & Private**
* ⚡ **FAISS persistence** (no re-embedding every run)

---

## 🛠️ Tech Stack

* **Python 3.11**
* **LangChain**
* **FAISS**
* **Ollama**
* **HuggingFace Sentence Transformers**
* **Textual (Terminal UI)**

---

## 📂 Project Structure

```text
rag-pdf-chat/
│
├── app.py                  # Entry point
├── README.md
├── .gitignore
│
├── data/
│   └── sample.pdf          # Input PDF(s)
│
├── src/
│   ├── loader.py           # PDF loading
│   ├── chunking.py         # Text chunking
│   ├── embeddings.py       # Embedding model
│   ├── vectorstore.py      # FAISS store (load/save)
│   ├── rag_chain.py        # RAG pipeline
│   ├── tui_app.py          # Terminal UI (Textual)
│   └── __init__.py
│
├── faiss_index/             # Saved vector index (ignored in git)
└── venv/                    # Virtual environment (ignored)
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/rag-pdf-chat.git
cd rag-pdf-chat
```

---

### 2️⃣ Create & activate virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

*(Or install manually if you prefer)*

---

### 4️⃣ Install & run Ollama

Install Ollama from:
👉 [https://ollama.com](https://ollama.com)

Pull a model (example):

```bash
ollama pull phi3.5
```

---

## ▶️ Run the Application

```bash
python app.py
```

You will see a **full-screen terminal UI**.

---

## 💬 How to Use

* Type your question and press **Enter**
* Ask follow-up questions (memory enabled)
* Press **`s`** → toggle source citations
* Type **`:clear`** → clear conversation memory
* Type **`exit`** → quit the app

---

## 🧠 Example

```text
You: what is collection in java?
Assistant: A Collection in Java is part of the Java Collections Framework...

You: explain more
Assistant: Collections provide standardized data structures such as List, Set, and Map...
```

---

## 🔍 How It Works (Architecture)

1. PDF is loaded and split into chunks
2. Chunks are embedded using a sentence transformer
3. FAISS stores vectors for semantic search
4. User query retrieves relevant chunks
5. Retrieved context + chat history are passed to the LLM
6. LLM generates a grounded response

---

## 🎯 Why This Project Matters

* Demonstrates **real-world RAG implementation**
* Uses **modern LangChain Runnable architecture**
* Shows **offline-first AI design**
* Includes **custom terminal UI**
* Suitable for **portfolio, interviews, and demos**

---

## 📌 Future Improvements

* Multiple PDF selection
* Live LLM model switching
* Streaming token output
* Export chat history
* Web UI version

---

## 👤 Author

**Pratik**  
Computer Science Student | Web Development | AI | Cybersecurity

---

## ⭐ Acknowledgements

* LangChain
* HuggingFace
* Ollama
* FAISS
* Textual

---
