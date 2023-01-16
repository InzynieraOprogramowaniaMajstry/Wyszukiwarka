import unittest

from models.database import User, Book


class TestDatabase(unittest.TestCase):
    def test_user(self):
        user = User(email="test", password="123")
        self.assertEqual(user.email, "test")
        self.assertEqual(user.password, "123")

    def test_book(self):
        book = Book(user_id=1, book_id='a')
        self.assertEqual(book.book_id, 'a')
        self.assertEqual(book.user_id, 1)

if __name__ == '__main__':
    unittest.main()
