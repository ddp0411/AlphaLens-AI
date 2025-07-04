from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.tools import tool

llm = ChatOpenAI(temperature=0.3)

@tool
def analyze_risk(stock_info: dict) -> str:
    """Analyze financial risk from stock data."""
    prompt = ChatPromptTemplate.from_template("""
    Given the following stock data, identify potential financial risks:
    
    {stock_info}
    
    Provide a short risk summary.
    """)
    chain = prompt | llm
    return chain.invoke({"stock_info": stock_info})
