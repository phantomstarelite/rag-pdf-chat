import os
from langchain_community.vectorstores import FAISS

INDEX_PATH = "faiss_index"

def create_or_load_vectorstore(chunks, embeddings):
    if os.path.exists(INDEX_PATH):
        print("📂 Loading existing FAISS index...")
        return FAISS.load_local(
            INDEX_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )

    print("📦 Creating new FAISS index...")
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(INDEX_PATH)
    return vectorstore
