import unittest

from models.wolne_lektury_api import WolneLekturyAPI


class TestWolneLekturyAPI(unittest.TestCase):
    def test_books(self):
        self.assertEqual(0, len(WolneLekturyAPI.books_list))
        WolneLekturyAPI.get_books()
        self.assertNotEqual(0, len(WolneLekturyAPI.books_list))

    def test_authors(self):
        self.assertEqual(0, len(WolneLekturyAPI.authors_list))
        WolneLekturyAPI.get_authors()
        self.assertNotEqual(0, len(WolneLekturyAPI.authors_list))

    def test_epochs(self):
        self.assertEqual(0, len(WolneLekturyAPI.epochs_list))
        WolneLekturyAPI.get_epochs()
        self.assertNotEqual(0, len(WolneLekturyAPI.epochs_list))

    def test_genres(self):
        self.assertEqual(0, len(WolneLekturyAPI.genres_list))
        WolneLekturyAPI.get_genres()
        self.assertNotEqual(0, len(WolneLekturyAPI.genres_list))

    def test_kinds(self):
        self.assertEqual(0, len(WolneLekturyAPI.kinds_list))
        WolneLekturyAPI.get_kinds()
        self.assertNotEqual(0, len(WolneLekturyAPI.kinds_list))

    def test_fetch_api(self):
        WolneLekturyAPI.fetch_api()
        self.assertNotEqual(0, len(WolneLekturyAPI.kinds_list))


if __name__ == '__main__':
    unittest.main()
