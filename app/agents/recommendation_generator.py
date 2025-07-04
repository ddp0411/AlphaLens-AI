from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.tools import tool

llm = ChatOpenAI(temperature=0.4)

@tool
def generate_recommendation(risk_summary: str, stock_info: dict) -> str:
    """Generate buy/hold/sell recommendation."""
    prompt = ChatPromptTemplate.from_template("""
    Based on the risk summary and stock info below, generate a concise investment recommendation:
    
    Risk Summary: {risk_summary}
    
    Stock Info: {stock_info}
    
    Give final verdict in format: [Buy/Hold/Sell] - Reason.
    """)
    chain = prompt | llm
    return chain.invoke({"risk_summary": risk_summary, "stock_info": stock_info})
