from langsmith import traceable

@traceable(name="evaluate_recommendation")
def evaluate_output(output: str):
    """Evaluate GenAI output using LangSmith for quality."""
    return output
