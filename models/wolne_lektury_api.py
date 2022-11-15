import requests


# Usage: Whenever you want to grab data from list, just use WolneLekturyAPI.some_list
class WolneLekturyAPI:
    books_list = []
    authors_list = []
    epochs_list = []
    genres_list = []
    kinds_list = []

    @classmethod
    def fetch_api(cls):
        cls.get_books()
        cls.get_authors()
        cls.get_epochs()
        cls.get_genres()
        cls.get_kinds()

    @classmethod
    def get_kinds(cls):
        response = requests.get("https://wolnelektury.pl/api/kinds/")
        json_response = response.json()
        for record in json_response:
            d = {'name': record['name'], 'slug': record['slug']}
            cls.kinds_list.append(d)

    @classmethod
    def get_genres(cls):
        response = requests.get("https://wolnelektury.pl/api/genres/")
        json_response = response.json()
        for record in json_response:
            d = {'name': record['name'], 'slug': record['slug']}
            cls.genres_list.append(d)

    @classmethod
    def get_epochs(cls):
        response = requests.get("https://wolnelektury.pl/api/epochs/")
        json_response = response.json()
        for record in json_response:
            d = {'name': record['name'], 'slug': record['slug']}
            cls.epochs_list.append(d)

    @classmethod
    def get_authors(cls):
        response = requests.get("https://wolnelektury.pl/api/authors/")
        json_response = response.json()
        for record in json_response:
            d = {'name': record['name'], 'slug': record['slug']}
            cls.authors_list.append(d)

    @classmethod
    def get_books(cls):
        response = requests.get("https://wolnelektury.pl/api/books")
        json_response = response.json()
        for record in json_response:
            d = {'title': record['title'], 'author': record['author'], 'epoch': record['epoch'],
                 'genre': record['genre'], 'kind': record['kind']}
            cls.books_list.append(d)
