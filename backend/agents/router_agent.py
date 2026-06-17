def route_question(question):
    print(">>> ROUTER AGENT CALLED")
    q = question.lower()

    viz_keywords = [
        "chart",
        "graph",
        "plot",
        "histogram",
        "scatter",
        "bar",
        "line",
        "pie",
        "visualize"
    ]

    insight_keywords = [
        "insight",
        "finding",
        "recommendation",
        "risk",
        "summary"
    ]

    if any(word in q for word in viz_keywords):
        return "visualization"

    if any(word in q for word in insight_keywords):
        return "insights"

    return "analytics"