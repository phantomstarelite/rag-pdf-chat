from langchain_community.embeddings import HuggingFaceEmbeddings

_embeddings = None  # module-level cache

def get_embeddings():
    global _embeddings
    if _embeddings is None:
        _embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
    return _embeddings
