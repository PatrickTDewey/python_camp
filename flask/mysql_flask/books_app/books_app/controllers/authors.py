from books_app import app
from flask import render_template, redirect, request, session, flash
from books_app.models.author import Author
from books_app.models.book import Book

# Display Routes
@app.route('/authors')
def authors():
    authors = Author.get_all()
    return render_template("author.html", authors = authors)

@app.route('/authors/<int:author_id>')
def author_info(author_id):
    data = {
        "id": author_id
    }
    all_books = Book.get_all()
    author_favorites = Author.get_authors_favorite_books(data)
    return render_template("author_info.html", author_favorites = author_favorites, all_books = all_books)


# Action Routes
@app.route('/authors/create', methods=["POST"])
def author_create():
    data = {
        "fname": request.form["first_name"],
        "lname": request.form["last_name"]
    }
    create_author = Author.save(data)
    get_author = Author.get_by_id(data)
    return redirect(f'/authors/{get_author.id}')

@app.route('/authors/favorite', methods=["POST"])
def author_favorite():
    data = {
        "bid": request.form["book_id"],
        "aid": request.form["author_id"]
    }
    Author.add_to_favorites(data)
    return redirect(f"/authors/{data['aid']}")