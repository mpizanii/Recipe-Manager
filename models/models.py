from flask_sqlalchemy import SQLAlchemy
"""
    Para qualquer modificação no banco de dados rodar no terminal:
    flask db migrate
    flask db upgrade
"""
db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)