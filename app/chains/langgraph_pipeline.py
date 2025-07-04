from langgraph.graph import StateGraph
from app.agents.data_collector import fetch_stock_data
from app.agents.risk_analyzer import analyze_risk
from app.agents.recommendation_generator import generate_recommendation

def build_graph():
    builder = StateGraph()

    builder.add_node("Fetch", fetch_stock_data)
    builder.add_node("Risk", analyze_risk)
    builder.add_node("Recommend", generate_recommendation)

    builder.set_entry_point("Fetch")
    builder.add_edge("Fetch", "Risk")
    builder.add_edge("Risk", "Recommend")

    graph = builder.compile()
    return graph
