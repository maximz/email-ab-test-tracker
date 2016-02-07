import os
import string, random


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    PORT = 5000
    BASIC_AUTH_USERNAME = 'test'
    BASIC_AUTH_PASSWORD = 'test'


class ProductionConfig(Config):
    DEBUG = False
    PORT = 80
    BASIC_AUTH_USERNAME = 'maxim'
    BASIC_AUTH_PASSWORD = os.getenv('ADMIN_PASSWORD', ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(25)))


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
