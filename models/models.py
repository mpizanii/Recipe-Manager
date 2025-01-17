from flask_login import UserMixin
from app import db, login_manager

"""
    Para qualquer modificação no banco de dados rodar no terminal:
    flask db migrate
    flask db upgrade
"""
@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)

    alimentos = db.relationship('Alimentos', back_populates='usuario', cascade="all, delete-orphan")
    receitas = db.relationship('Receitas', back_populates='usuario', cascade="all, delete-orphan")

class Alimentos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    quantidade = db.Column(db.String(100), nullable=False)

    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable = False, index=True)

    usuario = db.relationship('Usuario', back_populates='alimentos')

class Receitas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    ingredientes = db.Column(db.Text, nullable=False)
    modo_preparo = db.Column(db.Text, nullable=False)

    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable = False, index=True)

    usuario = db.relationship('Usuario', back_populates='receitas')