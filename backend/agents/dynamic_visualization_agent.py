import plotly.express as px

from backend.agents.chart_spec_agent import (
    get_chart_spec
)


def generate_chart(df, question):

    spec = get_chart_spec(
        question,
        list(df.columns)
    )

    print(spec)

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

    else:

        return None

    return fig