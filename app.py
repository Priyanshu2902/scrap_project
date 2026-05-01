from flask import Flask, render_template, request
from database import get_books

app = Flask(__name__)


@app.route("/")
def home():

    search = request.args.get("search")

    rating = request.args.get("rating")

    books = get_books(search, rating)

    return render_template(
        "index.html",
        books=books,
        search=search,
        rating=rating
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)