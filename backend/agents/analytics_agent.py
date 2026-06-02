def analyze_data(df):

    analysis = {}

    numeric_cols = df.select_dtypes(
        include=["int64", "float64"]
    ).columns

    categorical_cols = df.select_dtypes(
        include=["object"]
    ).columns

    numeric_summary = {}

    for col in numeric_cols:

        numeric_summary[col] = {
            "mean": round(df[col].mean(), 2),
            "median": round(df[col].median(), 2),
            "min": round(df[col].min(), 2),
            "max": round(df[col].max(), 2)
        }

    analysis["numeric_summary"] = numeric_summary

    categorical_summary = {}

    for col in categorical_cols:

        categorical_summary[col] = (
            df[col]
            .value_counts()
            .head(5)
            .to_dict()
        )

    analysis["categorical_summary"] = categorical_summary

    return analysis