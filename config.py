class Conf:
    """
    Conf contains all the important configuration options, that is used by the flask and sqlalchemy
    """
    import os

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(ROOT_DIR, 'database.db')
