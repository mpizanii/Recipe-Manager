import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Config:
    SECRET_KEY = '6d234996b5456d0fd1c8d59269f24f4c'
    BASE_DIR = os.getcwd()
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_DIR, "instance", "gym_tracker.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
