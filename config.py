import os

class Config(object):
    ''' Main configurations '''

    CSRF_ENABLED = True
    SECURITY_PASSWORD_SALT = os.environ['SECURITY_PASSWORD_SALT']
    SECRET_KEY = os.environ['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_RECYCLE = 60
    
    # mail settings
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ['APP_MAIL_USERNAME']
    MAIL_PASSWORD = os.environ['APP_MAIL_PASSWORD']
    MAIL_DEFAULT_SENDER = 'noreply@calbang.com'
    
    # recaptcha
    RECAPTCHA_PUBLIC_KEY = os.environ['RECAPTCHA_PUBLIC_KEY']
    RECAPTCHA_PRIVATE_KEY = os.environ['RECAPTCHA_PRIVATE_KEY']
    
    JSON_AS_ASCII = False
    
class DevConfig(Config):
    ''' Development configurations '''

    DEBUG = True
    TESTING = True
    SQLALCHEMY_ECHO = True
            
class ProdConfig(Config):
    ''' Production configurations '''
    
    SQLALCHEMY_ECHO = False