import os

class Config(object):
    CSRF_ENABLE = True
    SECRET_KEY = '6d234996b5456d0fd1c8d59269f24f4c'
    BASE_DIR = os.getcwd()
    APP = None

class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = f'http://{IP_HOST}:{PORT_HOST}'

app_config = {
    'development': DevelopmentConfig(),
    'testing': None,
    'production': None
}

app_active = os.getenv('FLASK_ENV')

if app_active not in app_config:
    app_active = 'development'