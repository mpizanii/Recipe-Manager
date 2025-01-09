from config import app_config, app_active
from flask_sqlalchemy import SQLAlchemy

config = app_config[app_active]
db = SQLAlchemy(config.APP)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    birthdate = db.Column(db.Date, nullable = False)
    gender = db.Column(db.Enum('Masculino', 'Feminino', name='gender_enum'), nullable = False)


class Treinos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey(Usuario.id), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    date_criacao = db.Column(db.DateTime(6), default=db.func.current_timestamp(), nullable=False)
    