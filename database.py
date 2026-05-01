import sqlite3


def get_books(search_query=None, rating=None):

    conn = sqlite3.connect("data/books.db")

    cursor = conn.cursor()

    query = """
        SELECT title, price, rating
        FROM books
        WHERE 1=1
    """

    params = []

    if search_query:

        query += " AND title LIKE ?"

        params.append(f"%{search_query}%")

    if rating:

        query += " AND rating = ?"

        params.append(rating)

    query += " LIMIT 50"

    cursor.execute(query, params)

    books = cursor.fetchall()

    conn.close()

    return books