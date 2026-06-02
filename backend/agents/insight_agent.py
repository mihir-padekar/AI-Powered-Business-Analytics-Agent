from backend.services.llm_service import generate_response


def generate_insights(analysis):

    prompt = f"""
    You are a Senior Business Analyst.

    Analyze the following dataset statistics
    and provide business insights.

    Data:

    {analysis}

    Give:

    1. Key findings
    2. Business observations
    3. Recommendations

    Keep response concise.
    """

    insights = generate_response(prompt)

    return insights

print("Insight agent loaded successfully")