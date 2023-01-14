class Conf():
    import os
    
    # ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(ROOT_DIR, 'database.db')
