import random
import pandas as pd

random.seed(42)

products = {
    "milk": ("dairy", 60),
    "bread": ("bakery", 40),
    "eggs": ("dairy", 72),
    "chips": ("snacks", 30),
    "apple": ("fruits", 100),
    "banana": ("fruits", 60),
    "coffee": ("beverages", 150)
}

cities = [
    "hyderabad",
    "vijayawada",
    "chennai",
    "bangalore",
    "vizag"
]

payment_methods = [
    "upi",
    "cash",
    "card"
]

rows = []

for i in range(1, 501):

    customer_id = f"C{random.randint(1, 100):03d}"
    order_id = f"O{i:04d}"

    product = random.choice(list(products.keys()))
    category, price = products[product]

    quantity = random.randint(1, 15)
    city = random.choice(cities)
    payment_method = random.choice(payment_methods)

    rows.append([
        customer_id,
        order_id,
        product,
        category,
        quantity,
        price,
        city,
        payment_method
    ])

df = pd.DataFrame(
    rows,
    columns=[
        "customer_id",
        "order_id",
        "product",
        "category",
        "quantity",
        "price",
        "city",
        "payment_method"
    ]
)

df.to_csv(
    "analytics/data/orders_500.csv",
    index=False
)
print("500-order dataset created successfully!")
print(df.head())
print("Total rows:", len(df))