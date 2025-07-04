from langchain.chains import RetrievalQA
from app.llm.vectorstore import vectorstore
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0.3)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(search_type="similarity", k=3)
)

def answer_query(query: str) -> str:
    """Answer natural language financial queries using vectorized SEC filings."""
    return qa_chain.run(query)
