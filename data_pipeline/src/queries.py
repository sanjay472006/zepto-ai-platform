import sqlite3
import pandas as pd

DATABASE_FILE = "data_pipeline/data/processed/books.db"

connection = sqlite3.connect(DATABASE_FILE)

queries = {
    "Query 1 - SELECT and WHERE": """
        SELECT title, price_gbp, rating
        FROM books
        WHERE rating >= 4
    """,

    "Query 2 - ORDER BY and LIMIT": """
        SELECT title, price_inr
        FROM books
        ORDER BY price_inr DESC
        LIMIT 10
    """,

    "Query 3 - DISTINCT": """
        SELECT DISTINCT rating
        FROM books
        ORDER BY rating
    """,

    "Query 4 - BETWEEN": """
        SELECT title, price_gbp
        FROM books
        WHERE price_gbp BETWEEN 20 AND 40
    """,

    "Query 5 - JOIN": """
        SELECT
            b.title,
            b.rating,
            b.price_inr,
            c.category_name
        FROM books b
        JOIN categories c
            ON b.category_id = c.category_id
        ORDER BY b.rating DESC
        LIMIT 10
    """
}

output_file = "data_pipeline/outputs/query_results.txt"

import os
os.makedirs("data_pipeline/outputs", exist_ok=True)

with open(output_file, "w", encoding="utf-8") as file:

    for name, query in queries.items():

        print("\n" + "=" * 60)
        print(name)
        print("=" * 60)

        print(query.strip())

        result = pd.read_sql(
            query,
            connection
        )

        print(result)

        file.write("\n" + "=" * 60 + "\n")
        file.write(name + "\n")
        file.write("=" * 60 + "\n")
        file.write(query.strip() + "\n\n")
        file.write(result.to_string(index=False))
        file.write("\n")

connection.close()

print("\nAll SQL queries executed successfully!")
print("Results saved to:", output_file)