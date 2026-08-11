import requests
import pandas as pd

from bs4 import BeautifulSoup
from urllib.parse import urljoin


BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

books = []

# Scrape first 5 pages
for page in range(1, 6):

    url = BASE_URL.format(page)

    print(f"Scraping page {page}...")

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Get every book on the page
    for book in soup.select("article.product_pod"):

        # Book title
        title = book.h3.a["title"]

        # Price
        price = book.select_one(".price_color").get_text(strip=True)

        # Star rating
        star_rating = book.select_one(".star-rating")["class"][1]

        # Availability
        availability = book.select_one(
            ".availability"
        ).get_text(" ", strip=True)

        # Get book page URL correctly
        relative_url = book.h3.a["href"]

        book_url = urljoin(url, relative_url)

        # Open individual book page
        book_response = requests.get(
            book_url,
            timeout=10
        )

        book_response.raise_for_status()

        book_soup = BeautifulSoup(
            book_response.text,
            "html.parser"
        )

        # Get category from breadcrumb
        breadcrumb = book_soup.select(
            "ul.breadcrumb li"
        )

        if len(breadcrumb) >= 3:
            category = breadcrumb[2].get_text(
                strip=True
            )
        else:
            category = "Unknown"

        books.append({
            "title": title,
            "price": price,
            "star_rating": star_rating,
            "availability": availability,
            "category": category
        })


# Convert to DataFrame
df = pd.DataFrame(books)


# Display results
print("\n==============================")
print("SCRAPING COMPLETED")
print("==============================")

print("Total books:", len(df))

print(
    "Total categories:",
    df["category"].nunique()
)

print("\nFirst 5 books:")
print(df.head())


print("\nCategories found:")
print(df["category"].unique())


# Save raw data
df.to_csv(
    "data_pipeline/data/raw/books_raw.csv",
    index=False
)

print("\nRaw data saved successfully!")
print(
    "File: data_pipeline/data/raw/books_raw.csv"
)
