import sqlite3
import pandas as pd

DATABASE_FILE = "data_pipeline/data/processed/books.db"

connection = sqlite3.connect(DATABASE_FILE)

books_df = pd.read_sql(
    "SELECT * FROM books",
    connection
)

categories_df = pd.read_sql(
    "SELECT * FROM categories",
    connection
)

sql_join = pd.read_sql(
    """
    SELECT
        b.title,
        b.rating,
        b.price_inr,
        c.category_name
    FROM books b
    JOIN categories c
        ON b.category_id = c.category_id
    ORDER BY b.rating DESC, b.title ASC
    LIMIT 10
    """,
    connection
)

pandas_join = (
    books_df
    .merge(
        categories_df,
        on="category_id",
        how="inner"
    )
    [
        [
            "title",
            "rating",
            "price_inr",
            "category_name"
        ]
    ]
    .sort_values(
        by=["rating", "title"],
        ascending=[False, True]
    )
    .head(10)
)

sql_join = sql_join.reset_index(drop=True)
pandas_join = pandas_join.reset_index(drop=True)

print("SQL JOIN RESULT:")
print(sql_join)

print("\nPANDAS MERGE RESULT:")
print(pandas_join)

print("\nResults equivalent:")
print(sql_join.equals(pandas_join))

connection.close()