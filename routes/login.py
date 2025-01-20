from flask import Blueprint, render_template, request, flash, redirect, url_for
from app import db
from models.models import Usuario
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

usuario_bp = Blueprint('usuario', __name__, template_folder='templates')
"""
    / (GET) - formulario de login
    /register (GET)- formulario de cadastro
    /register (POST) - formulario de cadastro
"""

@usuario_bp.route('/', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        usuario = Usuario.query.filter_by(email = email).first()

        if usuario and check_password_hash(usuario.senha, senha):
            login_user(usuario)

            return redirect(url_for('home.home'))
        
        else:
            flash("Usuário ou senha incorretos. Tente novamente.", "danger")

            return redirect(url_for('usuario.login'))

    return render_template('login.html')

@usuario_bp.route('/register', methods = ["GET"])
def form_cadastro():
    return render_template('register.html')

@usuario_bp.route('/register', methods = ["POST"])
def cadastro():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    confirmar_senha = request.form['confirmar_senha']

    usuario_existente = Usuario.query.filter_by(email=email).first()

    if usuario_existente:
        flash("Este e-mail já está cadastrado", "danger")

        return redirect(url_for('usuario.login'))
    
    elif senha != confirmar_senha:
        flash("Senhas não coincidem", "danger")

        return redirect(url_for('usuario.cadastro'))
    
    hash_senha = generate_password_hash(senha)
    novo_usuario = Usuario(nome = nome, email = email, senha = hash_senha)

    db.session.add(novo_usuario)
    db.session.commit()
    
    return redirect(url_for('usuario.login'))

from flask_login import logout_user

@usuario_bp.route('/logout')
def logout():
    logout_user()
    flash('Logout realizado com sucesso.', 'success')
    return redirect(url_for('usuario.login'))