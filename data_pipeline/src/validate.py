def validate_data(df):

    required_columns = [
        "customer_id",
        "order_id",
        "product",
        "category",
        "quantity",
        "price",
        "city",
        "payment_method"
    ]

    # Check required columns
    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"Missing column: {column}")

    # Check missing important values
    if df["customer_id"].isnull().any():
        raise ValueError("Customer ID contains missing values")

    if df["order_id"].isnull().any():
        raise ValueError("Order ID contains missing values")

    # Check price
    if (df["price"] < 0).any():
        raise ValueError("Price cannot be negative")

    # Check quantity
    if (df["quantity"] <= 0).any():
        raise ValueError("Quantity must be greater than 0")

    print("Data validation successful!")

    return True