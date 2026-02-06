from src.loader import load_pdf
from src.chunking import chunk_documents
from src.embeddings import get_embeddings
from src.vectorstore import create_or_load_vectorstore
from src.rag_chain import create_rag_chain
from src.tui_app import RAGTerminalApp


def main():
    print("📄 Loading PDF...")
    documents = load_pdf("data/sample.pdf")

    print("✂️ Chunking documents...")
    chunks = chunk_documents(documents)

    print("🧠 Loading embeddings...")
    embeddings = get_embeddings()

    print("📂 Loading / Creating vector store...")
    vectorstore = create_or_load_vectorstore(chunks, embeddings)

    print("🤖 Initializing RAG system...")
    qa_chain, retriever = create_rag_chain(vectorstore)

    app = RAGTerminalApp(qa_chain, retriever)
    app.run()



if __name__ == "__main__":
    main()
