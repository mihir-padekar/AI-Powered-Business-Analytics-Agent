from backend.services.llm_service import generate_response


def detect_chart_column(
    question,
    columns
):

    prompt = f"""
    Dataset Columns:

    {columns}

    User Question:

    {question}

    Return ONLY the column name
    most relevant to the chart.

    No explanation.
    """

    response = generate_response(prompt)

    return response.strip()

columns = [
    "gender",
    "age",
    "salary"
]

print(
    detect_chart_column(
        "Create pie chart for gender",
        columns
    )
)