from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from app.llm.embeddings import embeddings
from app.config import Config
import os

def ingest_filings():
    docs = []
    for file in os.listdir(Config.SEC_FILINGS_PATH):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(Config.SEC_FILINGS_PATH, file))
            docs.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = splitter.split_documents(docs)
    db = FAISS.from_documents(texts, embeddings)
    db.save_local(Config.VECTOR_DB_PATH)
