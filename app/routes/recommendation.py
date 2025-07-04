from fastapi import APIRouter
from app.chains.langgraph_pipeline import build_graph

router = APIRouter()

@router.get("/run")
def get_recommendation(symbol: str):
    pipeline = build_graph()
    result = pipeline.invoke({"symbol": symbol})
    return {"recommendation": result}
