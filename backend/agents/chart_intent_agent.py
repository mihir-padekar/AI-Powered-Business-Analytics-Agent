from backend.services.llm_service import generate_response


def detect_chart_request(question):

    prompt = f"""
    Identify chart type.

    User Question:
    {question}

    Return ONLY one:

    pie
    bar
    line
    scatter
    """

    response = generate_response(prompt)

    return response.strip().lower()

