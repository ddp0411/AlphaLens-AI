from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import dashboard, insights, recommendation
import os

app = FastAPI(
    title="AgentFinance AI – Smart Investment Research Assistant",
    description="GenAI-powered financial analysis and recommendation tool",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(dashboard.router, prefix="/dashboard")
app.include_router(insights.router, prefix="/insights")
app.include_router(recommendation.router, prefix="/recommendation")

@app.get("/")
async def root():
    return {"message": "Welcome to AgentFinance AI"}
