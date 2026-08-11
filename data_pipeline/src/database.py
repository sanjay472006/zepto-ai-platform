import sqlite3
import pandas as pd
import os

INPUT_FILE = "data_pipeline/data/processed/books_cleaned.csv"
DATABASE_FILE = "data_pipeline/data/processed/books.db"


def create_database():

    os.makedirs(
        os.path.dirname(DATABASE_FILE),
        exist_ok=True
    )

    df = pd.read_csv(INPUT_FILE)

    connection = sqlite3.connect(DATABASE_FILE)

    cursor = connection.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            category_id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_name TEXT UNIQUE NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            price_gbp REAL NOT NULL,
            price_inr REAL NOT NULL,
            rating INTEGER NOT NULL,
            in_stock INTEGER NOT NULL,
            category_id INTEGER NOT NULL,
            FOREIGN KEY (category_id)
                REFERENCES categories(category_id)
        )
    """)

    categories = df["category"].drop_duplicates()

    for category in categories:
        cursor.execute(
            """
            INSERT OR IGNORE INTO categories (category_name)
            VALUES (?)
            """,
            (category,)
        )

    for _, row in df.iterrows():

        cursor.execute(
            """
            SELECT category_id
            FROM categories
            WHERE category_name = ?
            """,
            (row["category"],)
        )

        category_id = cursor.fetchone()[0]

        cursor.execute(
            """
            INSERT INTO books (
                title,
                price_gbp,
                price_inr,
                rating,
                in_stock,
                category_id
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                row["title"],
                row["price_gbp"],
                row["price_inr"],
                row["rating"],
                int(row["in_stock"]),
                category_id
            )
        )

    connection.commit()

    category_count = cursor.execute(
        "SELECT COUNT(*) FROM categories"
    ).fetchone()[0]

    book_count = cursor.execute(
        "SELECT COUNT(*) FROM books"
    ).fetchone()[0]

    connection.close()

    print("Database created successfully!")
    print("Categories:", category_count)
    print("Books:", book_count)
    print("Database:", DATABASE_FILE)


if __name__ == "__main__":
    create_database()