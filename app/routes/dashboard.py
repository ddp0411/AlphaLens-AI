from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_dashboard():
    return {"message": "Welcome to AgentFinance AI Dashboard!"}
