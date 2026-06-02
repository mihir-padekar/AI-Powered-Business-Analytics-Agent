from backend.services.llm_service import generate_response


def route_question_llm(question):

    prompt = f"""
    You are an AI Supervisor.

    Available Agents:

    analytics
    visualization
    insights

    User Question:
    {question}

    Return ONLY one word:

    analytics
    visualization
    insights
    """

    response = generate_response(prompt)

    return response.strip().lower()

print(
    route_question_llm(
        "Show me a graph of revenue"
    )
)