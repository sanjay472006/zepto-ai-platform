import pandas as pd


def extract_data(file_path):
    df = pd.read_csv(file_path)

    print("Data extracted successfully!")
    print("Rows:", len(df))
    print("Columns:", len(df.columns))

    return df