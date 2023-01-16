import requests


class WolneLekturyAPI:
    """
    WolneLekturyAPI holds all the relevant data from the WolneLektury public api.
    Usage: Whenever you want to grab data from list, just use WolneLekturyAPI.some_list

    Attributes
    ----------
        books_list : list
            List of books from "api/books" with fields: title, author, epoch, genre, kind, url and id
        authors_list : list
            List of authors from "api/authors" with fields: name and id
        epochs_list : list
            List of epochs from "api/epochs" with fields: name and id
        genres_list : list
            List of genres from "api/genres" with fields: name and id
        kinds_list : list
            List of kinds from "api/kinds" with fields: name and id
    """
    books_list = []
    authors_list = []
    epochs_list = []
    genres_list = []
    kinds_list = []

    @classmethod
    def fetch_api(cls):
        """This method is run on initialization to fetch all the data to respective lists"""
        cls.get_books()
        cls.get_authors()
        cls.get_epochs()
        cls.get_genres()
        cls.get_kinds()

    @classmethod
    def get_kinds(cls):
        """Fetch data from "api/kinds" and puts them into kinds_list"""
        response = requests.get("https://wolnelektury.pl/api/kinds/")
        if not response:
            return
        json_response = response.json()
        for record in json_response:
            d = {'name': record['name'], 'id': record['slug']}
            cls.kinds_list.append(d)

    @classmethod
    def get_genres(cls):
        """Fetch data from "api/genres" and puts them into genres_list"""
        response = requests.get("https://wolnelektury.pl/api/genres/")
        if not response:
            return
        json_response = response.json()
        for record in json_response:
            d = {'name': record['name'], 'id': record['slug']}
            cls.genres_list.append(d)

    @classmethod
    def get_epochs(cls):
        """Fetch data from "api/epochs" and puts them into epochs_list"""
        response = requests.get("https://wolnelektury.pl/api/epochs/")
        if not response:
            return
        json_response = response.json()
        for record in json_response:
            d = {'name': record['name'], 'id': record['slug']}
            cls.epochs_list.append(d)

    @classmethod
    def get_authors(cls):
        """Fetch data from "api/authors" and puts them into authors_list"""
        response = requests.get("https://wolnelektury.pl/api/authors/")
        if not response:
            return
        json_response = response.json()
        for record in json_response:
            d = {'name': record['name'], 'id': record['slug']}
            cls.authors_list.append(d)

    @classmethod
    def get_books(cls):
        """Fetch data from "api/books" and puts them into books_list"""
        response = requests.get("https://wolnelektury.pl/api/books")
        if not response:
            return
        json_response = response.json()
        for record in json_response:
            d = {'title': record['title'], 'author': record['author'], 'epoch': record['epoch'],
                 'genre': record['genre'], 'kind': record['kind'], 'simple_thumb': record['simple_thumb'],
                 'url': record['url'], 'id': record['slug']}
            cls.books_list.append(d)
