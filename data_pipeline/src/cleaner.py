import pandas as pd
import os

INPUT_FILE = "data_pipeline/data/raw/books_raw.csv"
OUTPUT_FILE = "data_pipeline/data/processed/books_cleaned.csv"

GBP_TO_INR = 105.50

RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

def clean_data():

    print("Starting data cleaning...")

    if not os.path.exists(INPUT_FILE):
        raise FileNotFoundError(
            f"Input file not found: {INPUT_FILE}"
        )

    df = pd.read_csv(INPUT_FILE)

    print("Raw rows:", len(df))

    df["price_gbp"] = (
        df["price"]
        .astype(str)
        .str.replace("Â", "", regex=False)
        .str.replace("£", "", regex=False)
        .str.strip()
    )

    df["price_gbp"] = pd.to_numeric(
        df["price_gbp"],
        errors="coerce"
    )

    price_median = df["price_gbp"].median()

    df["price_gbp"] = df["price_gbp"].fillna(
        price_median
    )

    df["rating"] = df["star_rating"].map(
        RATING_MAP
    )

    df["in_stock"] = (
        df["availability"]
        .astype(str)
        .str.contains(
            "In stock",
            case=False,
            na=False
        )
    )

    df["price_inr"] = (
        df["price_gbp"] * GBP_TO_INR
    )

    df = df.dropna(
        subset=[
            "rating",
            "category",
            "title"
        ]
    )

    df["rating"] = df["rating"].astype(int)
    df["in_stock"] = df["in_stock"].astype(bool)

    df = df[
        [
            "title",
            "price_gbp",
            "price_inr",
            "rating",
            "in_stock",
            "category"
        ]
    ]

    os.makedirs(
        os.path.dirname(OUTPUT_FILE),
        exist_ok=True
    )

    df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print()
    print("DATA CLEANING COMPLETED")
    print("Rows:", len(df))
    print("Columns:", len(df.columns))
    print("Columns:", df.columns.tolist())
    print()
    print("Data types:")
    print(df.dtypes)
    print()
    print("Missing values:")
    print(df.isnull().sum())
    print()
    print("First 5 cleaned rows:")
    print(df.head())
    print()
    print("GBP to INR rate:", GBP_TO_INR)
    print()
    print("Cleaned data saved to:", OUTPUT_FILE)


if __name__ == "__main__":
    clean_data()