from backend.services.llm_service import generate_response


def answer_question(question, analysis):

    relevant_analysis = {
        "numeric_summary": analysis["numeric_summary"],
        "categorical_summary": analysis["categorical_summary"]
    }

    prompt = f"""
    You are a Senior Business Analyst.

    Dataset Analysis:
    {relevant_analysis}

    User Question:
    {question}

    Answer using only the available dataset information.

    If information is unavailable, say so.

    Keep the response concise and business-focused.
    """

    return generate_response(prompt)