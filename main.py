from fastapi import FastAPI

app = FastAPI()


books = [
    {"id": 1, "title": "Book One", "author": "Author A", "year": 2020, "rating": 4.5},
    {"id": 2, "title": "Book Two", "author": "Author B", "year": 2021, "rating": 3.7},
]


@app.get("/books")
def get_books():
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    return {"error": "Book not found!"}

@app.post("/books")
def create_book(book: dict):
    book["id"] = len(books) + 1
    books.append(book)
    return book


@app.patch("/books/{book_id}")
def update_book_rating(book_id: int, rating: float):
    for book in books:
        if book["id"] == book_id:
            book["rating"] = rating
            return book
    return {"error": "Book not found!"}
