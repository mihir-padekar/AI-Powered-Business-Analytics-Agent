def detect_outliers(df):

    outlier_report = {}

    numeric_cols = df.select_dtypes(
        include=["int64", "float64"]
    ).columns

    for col in numeric_cols:

        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)

        iqr = q3 - q1

        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        outliers = df[
            (df[col] < lower) |
            (df[col] > upper)
        ]

        outlier_report[col] = len(outliers)

    return outlier_report

def profile_data(df):
    """
    Generate basic dataset profile
    """
    numerical_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()

    categorical_cols = df.select_dtypes(include=["object"]).columns.tolist()

    missing_percent = (df.isnull().sum() / len(df) * 100).round(2).to_dict()

    profile = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "column_names": list(df.columns),
        "data_types": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
        "duplicate_rows": int(df.duplicated().sum()),
        "numerical_columns": numerical_cols,
        "categorical_columns": categorical_cols,
        "missing_percent": missing_percent,
        "summary_statistics": df.describe().to_dict(),
        "outliers": detect_outliers(df)
    }

    return profile