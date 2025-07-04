from fastapi import APIRouter
from app.agents.qa_analyst import answer_query

router = APIRouter()

@router.get("/ask")
def query_qa(query: str):
    return {"answer": answer_query(query)}
