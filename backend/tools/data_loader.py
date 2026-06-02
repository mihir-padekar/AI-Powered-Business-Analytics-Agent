import pandas as pd


def load_data(file):
    """
    Load CSV file into a Pandas DataFrame
    """

    df = pd.read_csv(file)

    return df