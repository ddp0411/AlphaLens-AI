import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    VECTOR_DB_PATH = "./data/vectorstore"
    SEC_FILINGS_PATH = "./data/sec_filings"
    LANGSMITH_PROJECT = "AgentFinance-Eval"
