import unittest

from models.wolne_lektury_api import WolneLekturyAPI

from httmock import all_requests, HTTMock


@all_requests
def response_content(url, request):
    return {'status_code': 404}


class TestWolneLekturyAPINoInternet(unittest.TestCase):
    def test_books(self):
        with HTTMock(response_content):
            WolneLekturyAPI.get_books()
        self.assertEqual(0, len(WolneLekturyAPI.books_list))

    def test_authors(self):
        with HTTMock(response_content):
            WolneLekturyAPI.get_authors()
        self.assertEqual(0, len(WolneLekturyAPI.authors_list))

    def test_epochs(self):
        with HTTMock(response_content):
            WolneLekturyAPI.get_epochs()
        self.assertEqual(0, len(WolneLekturyAPI.epochs_list))

    def test_genres(self):
        with HTTMock(response_content):
            WolneLekturyAPI.get_genres()
        self.assertEqual(0, len(WolneLekturyAPI.genres_list))

    def test_kinds(self):
        with HTTMock(response_content):
            WolneLekturyAPI.get_kinds()
        self.assertEqual(0, len(WolneLekturyAPI.kinds_list))

    def test_fetch_api(self):
        with HTTMock(response_content):
            WolneLekturyAPI.fetch_api()
        self.assertEqual(0, len(WolneLekturyAPI.kinds_list))
