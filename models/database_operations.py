from flask_sqlalchemy import SQLAlchemy

from models.database import User, Book
import hashlib
from initialize_objects import db

class DatabaseOperations:
    @classmethod
    def add_user(cls, email, password):
        hashed_password = hashlib.sha512(str.encode(password)).hexdigest()
        user = User(email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()

    @classmethod
    def delete_user(cls, email):
        user = db.session.execute(db.select(User).filter_by(email=email))
        if user is not None:
            user = user.scalar_one()
            db.session.delete(user)
            db.session.commit()

    @classmethod
    def update_password(cls, user_id, password):
        hashed_password = hashlib.sha512(str.encode(password)).hexdigest()
        user: User = db.session.execute(db.select(User).filter_by(user_id=user_id)).scalar_one()
        user.password = hashed_password
        db.session.commit()

    @classmethod
    def add_book_to_library(cls, user_id, book_id):
        book = Book(user_id=user_id, book_id=book_id)
        db.session.add(book)
        db.session.commit()

    @classmethod
    def remove_book_from_library(cls, user_id, book_id):
        book: Book = db.session.execute(db.select(Book).filter_by(user_id=user_id, book_id=book_id)).scalar_one()
        db.session.delete(book)
        db.session.commit()

    @classmethod
    def check_if_email_exists(cls, email):
        user = db.session.execute(db.select(User).filter_by(email=email))
        return user is not None

    @classmethod
    def check_if_password_matches(cls, email, password):
        hashed_password = hashlib.sha512(str.encode(password)).hexdigest()
        user = db.session.execute(db.select(User).filter_by(email=email, password=hashed_password))
        return user is not None
