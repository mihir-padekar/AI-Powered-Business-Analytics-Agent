from backend.services.llm_service import generate_response


def answer_question(question, analysis, chat_history=""):
    relevant_analysis = {
        "numeric_summary": analysis["numeric_summary"],
        "categorical_summary": analysis["categorical_summary"]
    }

    prompt = f"""
    You are a Senior Business Analyst.

    Conversation History:
    {chat_history}

    Dataset Analysis:
    {relevant_analysis}

    Current User Question:
    {question}

    Instructions:

    - This is an ongoing conversation.
    - The user may refer to previous insights, findings, charts, recommendations, or answers.
    - Resolve references such as:
        - "expand on that"
        - "expand on the second insight"
        - "tell me more"
        - "why?"
        - "what risk does that create?"
        - "explain further"

    using the conversation history.

    - Never say there is no previous discussion if conversation history is available.
    - If the user refers to a numbered finding or insight, identify it from the previous assistant response and elaborate on it.
    - Answer in a business-focused manner.

    Response:
    """

    return generate_response(prompt)