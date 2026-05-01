import requests
from bs4 import BeautifulSoup
import csv
import json
import os
import sqlite3
from datetime import datetime

headers = {
    "User-Agent": "Mozilla/5.0"
}


def create_database():

    conn = sqlite3.connect("data/books.db")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            price TEXT,
            rating TEXT,
            link TEXT
        )
    """)

    conn.commit()

    return conn, cursor


def get_soup(url):

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Failed to fetch page")
        return None

    return BeautifulSoup(response.text, "html.parser")


def scrape_page(soup, writer, all_books, cursor, conn):

    books = soup.find_all("article", class_="product_pod")

    for book in books:

        title = book.h3.a["title"]

        price = book.find("p", class_="price_color").text

        rating = book.p["class"][1]

        link = "https://books.toscrape.com/catalogue/" + book.h3.a["href"]

        writer.writerow([title, price, rating, link])

        book_data = {
            "title": title,
            "price": price,
            "rating": rating,
            "link": link
        }

        all_books.append(book_data)

        cursor.execute("""
            INSERT INTO books (title, price, rating, link)
            VALUES (?, ?, ?, ?)
        """, (title, price, rating, link))

        conn.commit()


def fetch_books(cursor):

    rating_map = {
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five"
    }

    user_rating = input("\nEnter rating (1-5): ")

    if user_rating not in rating_map:
        print("Invalid rating")
        return

    selected_rating = rating_map[user_rating]

    print(f"\nFetching {selected_rating}-star books...\n")

    cursor.execute("""
        SELECT title, price, rating
        FROM books
        WHERE rating = ?
        LIMIT 10
    """, (selected_rating,))

    rows = cursor.fetchall()

    for row in rows:

        print("Title:", row[0])
        print("Price:", row[1])
        print("Rating:", row[2])
        print("-" * 50)


os.makedirs("data", exist_ok=True)

conn, cursor = create_database()

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

csv_filename = f"data/books_{timestamp}.csv"

json_filename = f"data/books_{timestamp}.json"

all_books = []

with open(csv_filename, "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow(["Title", "Price", "Rating", "Link"])

    for page in range(1, 6):

        print(f"\nScraping Page {page}...")

        url = f"https://books.toscrape.com/catalogue/page-{page}.html"

        soup = get_soup(url)

        if soup:
            scrape_page(soup, writer, all_books, cursor, conn)

with open(json_filename, "w", encoding="utf-8") as json_file:

    json.dump(all_books, json_file, indent=4)

fetch_books(cursor)

conn.close()

print("\nData saved successfully in:")
print(csv_filename)
print(json_filename)
print("data/books.db")