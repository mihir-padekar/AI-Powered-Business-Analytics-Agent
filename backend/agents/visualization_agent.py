import plotly.express as px


def generate_charts(df):

    charts = {}

    numeric_cols = df.select_dtypes(
        include=["int64", "float64"]
    ).columns

    categorical_cols = df.select_dtypes(
        include=["object"]
    ).columns

    if len(numeric_cols) > 0:

        col = numeric_cols[0]

        charts["histogram"] = px.histogram(
            df,
            x=col,
            title=f"Distribution of {col}"
        )

    if len(categorical_cols) > 0:

        col = categorical_cols[0]

        charts["bar"] = px.bar(
            df[col].value_counts().head(10),
            title=f"Top Categories in {col}"
        )

    return charts