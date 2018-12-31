import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """
    Basic environment configurations
    """
    DEBUG = False
    TESTING = False
    # Flask-Security
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authorization'
    WTF_CSRF_ENABLED = False
    SECURITY_TOKEN_MAX_AGE = 3600
    SECURITY_UNAUTHORIZED_VIEW = None
    SECRET_KEY = os.urandom(25)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root123@mysql:3306/ticket_management'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root123@127.0.0.1:6033/ticket_management'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    """
    Production environment configurations
    """
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    """
    Development environment configuration
    """
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    """
    Testing environment configurations
    """
    TESTING = True


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'stagging': StagingConfig,
}