# Developer: Steve Baker
# Program: Module 4 Lab - Case Study: Python APIs
# Description: CRUD API for a Book

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)
# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
# Initialize the database
db = SQLAlchemy(app)

# Define the Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=False)

# Create the database and tables
db.create_all()

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)

# Route to create a new book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book = Book(book_name=data['book_name'], author=data['author'], publisher=data['publisher'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book), 201

# Route to get all books
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books]), 200

# Route to get a specific book by ID
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify(book.to_dict()), 200

# Route to update a book by ID
@app.route('/books/<int:id>', methods=['PATCH'])
def update_book(id):
    data = request.get_json()
    book = Book.query.get_or_404(id)
    if 'book_name' in data:
        book.book_name = data['book_name']
    if 'author' in data:
        book.author = data['author']
    if 'publisher' in data:
        book.publisher = data['publisher']
    db.session.commit()
    return jsonify(book.to_dict()), 200

# Route to delete a book by ID
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return '', 204

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
