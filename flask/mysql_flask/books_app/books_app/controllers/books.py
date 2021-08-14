from books_app import app
from flask import render_template, redirect, request, session, flash
from books_app.models.book import Book
from books_app.models.author import Author

# Display routes
@app.route('/books')
def books():
    all_books = Book.get_all()
    return render_template("books.html", all_books = all_books)

@app.route('/books/<int:book_id>')
def book_info(book_id):
    data = {
        "id": book_id
    }
    all_authors = Author.get_all()
    book_favorites = Book.get_books_favorite_authors(data)
    return render_template("book_info.html", book_favorites = book_favorites, all_authors = all_authors)



# Action routes
@app.route('/books/create', methods=["POST"])
def book_create():
    data = {
        "title": request.form["title"],
        "pnum": request.form["page_num"]
    }
    create_book = Book.save(data)
    book_id = Book.get_by_id(data)
    return redirect(f'/books/{book_id}')


@app.route('/books/favorite', methods=["POST"])
def book_favorite():
    data = {
        "bid": request.form["book_id"],
        "aid": request.form["author_id"]
    }
    Book.add_author(data)
    return redirect(f"/books/{data['bid']}")