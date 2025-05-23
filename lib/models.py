from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker, relationship
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    DateTime,
    Sequence,
    Float,
    create_engine
)
from zope.sqlalchemy import register
import datetime
import transaction

Base = declarative_base()
DBSession = scoped_session(sessionmaker())
register(DBSession)

class Book(Base):  
    __tablename__ = "books"   
    id = Column(Integer, Sequence('book_seq'), primary_key=True) 
    name = Column(String(50))                                   
    author_id = Column(Integer, ForeignKey('authors.id'))              
    price = Column(Float)
    date_added = Column(DateTime, default=datetime.datetime.now)       
    promote = Column(Boolean, default=False)

    def __init__(self, name, author_id, price, date_added=None, promote=False):
        self.name = name
        self.author_id = author_id
        self.price = price
        self.date_added = date_added or datetime.datetime.now()
        self.promote = promote

class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, Sequence('author_seq'), primary_key=True)
    name = Column(String(50))
    books = relationship("Book", backref="author")

    def __init__(self, name):
        self.name = name

    def add_book(self, book):
        self.books.append(book)
        book.author = self

if __name__ == "__main__":
    engine = create_engine('sqlite:///lib/db/Library.db', echo=True)
    Base.metadata.create_all(engine)
    DBSession.configure(bind=engine)
    session = DBSession()

    authors_books = {
        "J.K. Rowling": [("Harry Potter and the Sorcerer's Stone", 29.99), ("Harry Potter and the Chamber of Secrets", 31.99)],
        "George R.R. Martin": [("A Game of Thrones", 39.99), ("A Clash of Kings", 42.50)],
        "J.R.R. Tolkien": [("The Hobbit", 25.00), ("The Lord of the Rings", 49.99)],
        "Dan Brown": [("The Da Vinci Code", 22.95), ("Angels and Demons", 20.00)],
        "Stephen King": [("The Shining", 24.99), ("It", 27.50)],
        "Agatha Christie": [("Murder on the Orient Express", 19.99), ("And Then There Were None", 21.50)],
        "Chinua Achebe": [("Things Fall Apart", 18.99)],
        "Ngugi wa Thiong’o": [("Petals of Blood", 17.49)],
        "Yuval Noah Harari": [("Sapiens", 34.99), ("Homo Deus", 36.00)],
        "Malcolm Gladwell": [("Outliers", 23.00), ("The Tipping Point", 20.00)],
    }

    with transaction.manager:
        for author_name, books in authors_books.items():
            author = Author(name=author_name)
            session.add(author)
            session.flush()  # populate author.id
            for book_title, price in books:
                book = Book(name=book_title, author_id=author.id, price=price)
                session.add(book)

    print("Bulk authors and books inserted successfully.")


with transaction.manager:
    book_to_delete = session.query(Book).filter(Book.id == 3).first()
    if book_to_delete:
        session.delete(book_to_delete)
        print(f"Deleted book: {book_to_delete.name}")
    else:
        print("Book not found.")
