from backend.services.llm_service import generate_response


def chart_advisor(
    question,
    column_name,
    column_dtype,
    unique_values
):

    prompt = f"""
    You are a Data Visualization Expert.

    User Request:
    {question}

    Column:
    {column_name}

    Data Type:
    {column_dtype}

    Unique Values:
    {unique_values}

    Determine:

    1. Is the requested chart appropriate?
    2. If not, explain why.
    3. Recommend a better chart.

    Keep response under 3 sentences.
    """

    return generate_response(prompt)