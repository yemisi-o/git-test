import os
from flask import Flask
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# BASE_DIR = os.path.dirname(os.path.abspath(__name__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SECRET_KEY = '\xa7\x99\xed4\xfc\xa1\xf8\x07a\x11\xbaE"L\xa7D\t\x07\xebE\xe1\xf0\xa5\x08'

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////{}'.format(os.path.join(BASE_DIR, 'database.db'))
    # 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')


class TestingConfig(Config):
    TESTING = True

app = Flask(__name__, template_folder='templates')


# app.config.from_object('TestingConfig')

# app.config.from_object('DevelopmentConfig')

# app.config.from_object('ProductionConfig')
