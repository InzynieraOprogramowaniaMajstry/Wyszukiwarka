from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

from models.database import User, Book
import hashlib
from initialize_objects import db


class DatabaseOperations:
    """
    DatabaseOperations is used to perform any allowed operations on the database.
    Usage: Whenever you want to use function on database, just use DatabaseOperations.some_function()
    """
    @classmethod
    def add_user(cls, email, password):
        """Add new user to the database, hashing his password before it"""
        hashed_password = hashlib.sha512(str.encode(password)).hexdigest()
        user = User(email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return user.user_id

    @classmethod
    def delete_user(cls, user_id):
        """Remove given user from the database"""
        user = db.session.execute(db.select(User).filter_by(user_id=user_id))
        if user is not None:
            user = user.scalar_one()
            db.session.delete(user)
            db.session.commit()

    @classmethod
    def update_password(cls, user_id, password):
        """Update the password for the given user, hashish password beforehand"""
        hashed_password = hashlib.sha512(str.encode(password)).hexdigest()
        user: User = db.session.execute(db.select(User).filter_by(user_id=user_id)).scalar_one()
        user.password = hashed_password
        db.session.commit()

    @classmethod
    def add_book_to_library(cls, user_id, book_id):
        """Add book to the given user library"""
        book = Book(user_id=user_id, book_id=book_id)
        db.session.add(book)
        db.session.commit()

    @classmethod
    def remove_book_from_library(cls, user_id, book_id):
        """Remove given book from the user library"""
        book: Book = db.session.execute(db.select(Book).filter_by(user_id=user_id, book_id=book_id)).scalar_one()
        db.session.delete(book)
        db.session.commit()

    @classmethod
    def check_if_email_exists(cls, email):
        """Check if given email already exists in the database"""
        try:
            db.session.execute(db.select(User).filter_by(email=email)).scalar_one()
            return True
        except SQLAlchemyError:
            return False

    @classmethod
    def get_user_id(cls, email):
        """Return user_id associated with given email"""
        user: User = db.session.execute(db.select(User).filter_by(email=email)).scalar_one()
        return user.user_id

    @classmethod
    def check_if_password_matches(cls, email, password):
        """Check if email and password matches the one in the database. Password is hashed before comparing."""
        hashed_password = hashlib.sha512(str.encode(password)).hexdigest()
        try:
            db.session.execute(db.select(User).filter_by(email=email, password=hashed_password)).scalar_one()
            return True
        except SQLAlchemyError:
            return False
