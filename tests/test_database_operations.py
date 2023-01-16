import hashlib
import unittest

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_testing import TestCase
from sqlalchemy import exc

import initialize_objects
from models.database import User, Book
from models.database_operations import DatabaseOperations


class TestDataseOperations(TestCase):
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):
        from initialize_objects import app, db
        self.db: SQLAlchemy = db
        return app

    def test_add_user(self):
        email = "a@a.com"
        password = "123"
        DatabaseOperations.add_user(email, password)

        user_added: User = self.db.session.execute(self.db.select(User).filter_by(email=email)).scalar()
        self.assertEqual(email, user_added.email)
        self.db.session.delete(user_added)
        self.db.session.commit()

    def test_delete_user(self):
        email = "a@a.com"
        password = "123"
        user: User = User(email=email, password=password)
        self.db.session.add(user)
        self.db.session.commit()
        DatabaseOperations.delete_user(user.user_id)
        user = self.db.session.execute(self.db.select(User).filter_by(email=email)).scalar()
        self.assertEqual(None, user)

    def test_update_password(self):
        email = "a@a.com"
        password = hashlib.sha512(str.encode("123")).hexdigest()
        user: User = User(email=email, password=password)
        self.db.session.add(user)
        self.db.session.commit()
        DatabaseOperations.update_password(user.user_id, '456')
        user_in_db = self.db.session.execute(self.db.select(User).filter_by(user_id=user.user_id)).scalar()
        self.assertNotEqual(password, user_in_db.password)
        self.db.session.delete(user)
        self.db.session.commit()

    def test_add_book_to_library(self):
        DatabaseOperations.add_book_to_library(999, 'test')
        book = self.db.session.execute(self.db.select(Book).filter_by(user_id=999)).scalar()
        self.assertNotEqual(None, book)
        self.db.session.delete(book)
        self.db.session.commit()

    def test_remove_book_to_library(self):
        book = Book(user_id=999, book_id='test')
        self.db.session.add(book)
        self.db.session.commit()
        DatabaseOperations.remove_book_from_library(999, 'test')
        book = self.db.session.execute(self.db.select(Book).filter_by(user_id=999)).scalar()
        self.assertEqual(None, book)

    def test_get_books_from_library(self):
        book = Book(user_id=999, book_id='test')
        self.db.session.add(book)
        self.db.session.commit()
        books = DatabaseOperations.get_books_from_library(999)
        self.assertNotEqual([], books)
        self.db.session.delete(book)
        self.db.session.commit()

    def test_check_if_email_exists(self):
        email = "a@a.com"
        password = hashlib.sha512(str.encode("123")).hexdigest()
        user: User = User(email=email, password=password)
        self.db.session.add(user)
        self.db.session.commit()
        self.assertTrue(DatabaseOperations.check_if_email_exists(email))
        self.db.session.delete(user)
        self.db.session.commit()

    def test_check_if_password_matches(self):
        email = "b@b.com"
        password = hashlib.sha512(str.encode("456")).hexdigest()
        user: User = User(email=email, password=password)
        self.db.session.add(user)
        self.db.session.commit()
        self.assertTrue(DatabaseOperations.check_if_password_matches(email, "456"))
        self.db.session.delete(user)
        self.db.session.commit()

    def test_get_user_id(self):
        email = "b@b.com"
        password = hashlib.sha512(str.encode("456")).hexdigest()
        user: User = User(email=email, password=password)
        self.db.session.add(user)
        self.db.session.commit()
        id = DatabaseOperations.get_user_id(email)
        self.assertEqual(user.user_id, id)
        self.db.session.delete(user)
        self.db.session.commit()

if __name__ == '__main__':
    unittest.main()
