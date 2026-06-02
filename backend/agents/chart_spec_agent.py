import json

from backend.services.llm_service import generate_response


def get_chart_spec(question, columns):

    prompt = f"""
    Dataset Columns:
    {columns}

    User Question:
    {question}

    Return ONLY JSON.

    Example:

    {{
        "chart_type":"line",
        "x":"month",
        "y":"revenue"
    }}
    """

    response = generate_response(prompt)

    

    response = (
        response
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    try:

        spec = json.loads(response)

        return spec

    except Exception as e:

        print("JSON ERROR:", e)

        return {
            "chart_type": None,
            "x": None,
            "y": None
        }