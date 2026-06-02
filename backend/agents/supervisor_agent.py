def route_question(question):

    question = question.lower()

    if any(word in question for word in [
        "chart",
        "graph",
        "plot",
        "visualize"
    ]):
        return "visualization"

    elif any(word in question for word in [
        "mean",
        "average",
        "max",
        "min",
        "highest",
        "lowest"
    ]):
        return "analytics"

    else:
        return "insights"