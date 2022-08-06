import os


class Config:
    DEBUG = False
    DEVELOPMENT = False
    SECRET_KEY = os.getenv('SECRET_KEY', b'\xb0\t\xa5\\\x07\xd2\x0e<S\xd06\xc0\x16\xe9\x14\x9f.\x7f\x80\xdb\xbb\xe95\xb6')
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class ProductionConfig(Config):
    pass

class StagingConfig(Config):
    DEBUG = True

class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
