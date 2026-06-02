import plotly.express as px

from backend.agents.chart_spec_agent import (
    get_chart_spec
)
SUPPORTED_CHARTS = [
    "bar",
    "pie",
    "line",
    "scatter",
    "histogram",
    "box"
]

def generate_chart(df, question):

    spec = get_chart_spec(
        question,
        list(df.columns)
    )

    print("SPEC:", spec)

    chart_type = spec["chart_type"]

    if chart_type == "pie":

        column = spec["column"]

        fig = px.pie(
            df,
            names=column,
            title=f"{column} Distribution"
        )

    elif chart_type == "bar":

        x = spec["x"]
        y = spec["y"]

        if y.lower() == "count":

            counts = (
                df[x]
                .value_counts()
                .reset_index()
            )

            counts.columns = [x, "count"]

            fig = px.bar(
                counts,
                x=x,
                y="count",
                title=f"Count of {x}"
            )

        else:

            grouped = (
                df.groupby(x)[y]
                .sum()
                .reset_index()
            )

            fig = px.bar(
                grouped,
                x=x,
                y=y
            )

    elif chart_type == "line":

        x = spec["x"]
        y = spec["y"]

        grouped = (
            df.groupby(x)[y]
            .sum()
            .reset_index()
        )

        fig = px.line(
            grouped,
            x=x,
            y=y
        )

    elif chart_type == "scatter":

        x = spec["x"]
        y = spec["y"]

        fig = px.scatter(
            df,
            x=x,
            y=y
        )

    elif chart_type == "histogram":

        x = spec["x"]

        fig = px.histogram(
            df,
            x=x,
            title=f"Distribution of {x}"
        )

    elif chart_type == "box":

        x = spec["x"]

        fig = px.box(
            df,
            y=x,
            title=f"Box Plot of {x}"
        )
    else:

        return None
    print("Returning figure")
    return fig