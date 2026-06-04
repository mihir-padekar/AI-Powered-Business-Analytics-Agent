import json

from backend.services.llm_service import generate_response


def get_chart_spec(question, columns):

    prompt = f"""
    Dataset Columns:
    {columns}

    User Question:
    {question}

    Return ONLY valid JSON.

    Examples:

    For Pie Chart:

    {{
        "chart_type":"pie",
        "column":"gender"
    }}

    For Histogram:

    {{
        "chart_type":"histogram",
        "x":"age"
    }}

    For Box Plot:

    {{
        "chart_type":"box",
        "x":"salary"
    }}

    For Scatter Plot:

    {{
        "chart_type":"scatter",
        "x":"age",
        "y":"income"
    }}

    For Bar Chart:

    {{
        "chart_type":"bar",
        "x":"gender",
        "y":"count"
    }}

    For Line Chart:

    {{
        "chart_type":"line",
        "x":"month",
        "y":"sales"
    }}

    Return ONLY JSON.
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