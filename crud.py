# Import necessary libraries
import fastapi
from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

# Mock database - List of books
books = [
    {
        "id": 1,
        "title": "Falleso adventures",
        "author": "Homeless man",
        "publish_data": "04-11-2008",
    },
    {
        "id": 2,
        "title": "Third impact",
        "author": "Weird dude with a mech",
        "publish_data": "25-04-2015",
    },
    {
        "id": 3,
        "title": "Ai will replace your job",
        "author": "Some dude on twitter with a nft pfp",
        "publish_data": "11-11-2025",
    },
    {
        "id": 4,
        "title": "Look at this new javascript framework!",
        "author": "twitter_random_user",
        "publish_data": "30-09-2023",
    }
]

# Initialize FastAPI application
app = FastAPI()

# GET endpoint - Retrieve all books
@app.get("/book")
def get_book():
    """Returns a list of all books"""
    return books

# GET endpoint - Retrieve a specific book by ID
@app.get("/book/{id}")
def get_book_by_id(id: int):
    """
    Get a book by its ID
    
    Parameters:
    - id: The book ID to search for
    
    Returns: Book object if found, otherwise raises 404 error
    """
    for book in books:
        if book["id"] == id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


# Data model for a complete Book
class Book(BaseModel):
    """Book data model with id, title, author, and publisher"""
    id: int
    title: str
    author: str
    publisher: str

# Data model for creating a new Book (without ID)
class BookCreate(BaseModel):
    """Book creation model - doesn't include ID as it's auto-generated"""
    title: str
    author: str
    publisher: str

# POST endpoint - Create a new book
@app.post("/book")
def create_book(book: BookCreate):
    """
    Create a new book with auto-generated ID
    
    Parameters:
    - book: BookCreate object with title, author, and publisher
    
    Returns: The created book with generated ID
    """
    # Auto-generate the next ID based on the highest existing ID
    new_id = max([b["id"] for b in books]) + 1 if books else 1
    new_book = {
        "id": new_id,
        "title": book.title,
        "author": book.author,
        "publisher": book.publisher
    }
    books.append(new_book)
    return new_book

# Data model for updating a Book
class BookUpdate(BaseModel):
    """Book update model - contains only updatable fields"""
    title: str
    author: str
    publisher: str

# PUT endpoint - Update an existing book
@app.put("/book/{book_id}")
def update_book(book_id: int, book_update: BookUpdate):
    """
    Update an existing book by ID
    
    Parameters:
    - book_id: The ID of the book to update
    - book_update: BookUpdate object with new title, author, and publisher
    
    Returns: The updated book object if found, otherwise raises 404 error
    """
    for book in books:
        if book["id"] == book_id:
            # Update the book fields
            book["title"] = book_update.title
            book["author"] = book_update.author
            book['publisher'] = book_update.publisher
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@app.delete("/book/{book_id}")
# Literally delete
def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "Book successfully deleted"}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")