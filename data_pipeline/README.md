# Data Pipeline

## Overview

This module implements an end-to-end data pipeline using Books to Scrape.

The pipeline performs:

1. Web scraping
2. Data cleaning
3. GBP to INR conversion
4. SQLite database loading
5. SQL analysis
6. Pandas analysis

## Data Source

Books to Scrape:

https://books.toscrape.com/

The pipeline scrapes the first 5 catalogue pages and collects 100 books across 29 categories.

## Technologies

- Python
- Requests
- BeautifulSoup
- Pandas
- SQLite

## Scraped Fields

- title
- price
- star_rating
- availability
- category

## Cleaned Fields

- title
- price_gbp
- price_inr
- rating
- in_stock
- category

## Currency Conversion

The project uses the required fixed conversion rate:

1 GBP = 105.50 INR

price_inr is calculated as:

price_inr = price_gbp * 105.50

No external currency API is used.

## Data Cleaning Decisions

Price values are converted from text to float.

Star ratings are converted from text to integers:

One = 1
Two = 2
Three = 3
Four = 4
Five = 5

Availability is converted to a boolean value.

Invalid numeric price values are converted to missing values and filled using the median price.

Rows with missing rating, title, or category are removed because these fields are required for analysis and database loading.

## Database Design

The SQLite database contains two normalized tables.

### categories

- category_id - Primary Key
- category_name - Unique

### books

- book_id - Primary Key
- title
- price_gbp
- price_inr
- rating
- in_stock
- category_id - Foreign Key

The relationship is:

categories.category_id → books.category_id

## SQL Queries

The project includes queries demonstrating:

- SELECT
- WHERE
- ORDER BY
- LIMIT
- DISTINCT
- BETWEEN
- JOIN

Query outputs are stored in:

data_pipeline/outputs/query_results.txt

## Pandas

The project uses:

- pd.read_sql() to read SQL query results
- pd.merge() to reproduce the SQL JOIN

The SQL JOIN and Pandas merge results were compared and produced equivalent results.

## Dataset Summary

The pipeline successfully scrapes 100 books across 29 categories and stores the cleaned data in a normalized SQLite database.

## How to Run

Activate the virtual environment:

```powershell
venv\Scripts\activate