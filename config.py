import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

class Config(object):
    CSRF_ENABLE = True
    SECRET_KEY = os.getenv('SECRET_KEY')
    BASE_DIR = os.getcwd()
    APP = None

class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = f'http://{IP_HOST}:{PORT_HOST}'
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    gemini_key = os.getenv('GEMINI_KEY')
    genai.configure(api_key=gemini_key)

app_config = {
    'development': DevelopmentConfig(),
    'testing': None,
    'production': None
}

app_active = os.getenv('FLASK_ENV')

if app_active not in app_config:
    app_active = 'development'
