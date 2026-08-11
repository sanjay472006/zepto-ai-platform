def transform_data(df):

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove rows with missing important values
    df = df.dropna(subset=[
        "customer_id",
        "order_id",
        "product"
    ])

    # Standardize text
    df["product"] = df["product"].str.lower()
    df["category"] = df["category"].str.lower()
    df["city"] = df["city"].str.lower()

    # Convert numeric columns
    df["price"] = df["price"].astype(float)
    df["quantity"] = df["quantity"].astype(int)

    # Create a new useful feature
    df["total_amount"] = df["price"] * df["quantity"]

    return df