from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableLambda

def create_rag_chain(vectorstore, model_name="phi3.5"):
    llm = OllamaLLM(model=model_name, temperature=0, timeout=60)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

    prompt = ChatPromptTemplate.from_template(
        """
        You are a helpful assistant.
        Use the conversation history and the context to answer.

        Conversation history:
        {history}

        Context:
        {context}

        Question:
        {question}
        """
    )

    rag_chain = (
        {
            "history": lambda x: x["history"],
            "question": lambda x: x["question"],
            "context": RunnableLambda(lambda x: x["question"]) | retriever,
        }
        | prompt
        | llm
    )

    return rag_chain, retriever
