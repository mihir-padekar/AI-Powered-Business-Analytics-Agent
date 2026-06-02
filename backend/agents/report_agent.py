from backend.services.llm_service import generate_response


def generate_report(analysis):

    prompt = f"""
    You are a Senior Business Consultant.

    Dataset Analysis:
    {analysis}

    Create an Executive Business Report.

    Include:

    1. Executive Summary
    2. Key Findings
    3. Risks
    4. Recommendations

    Keep it professional.
    """

    return generate_response(prompt)