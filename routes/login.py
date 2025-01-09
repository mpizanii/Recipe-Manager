from flask import Blueprint, render_template, request, flash, redirect, url_for
from database.usuario import USUARIO

login_bp = Blueprint('login', __name__, template_folder='templates')

"""
    / (GET) - formulario de login
    /register - formulario de cadastro
"""
@login_bp.route('/', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['password']

        for usuario in USUARIO:
            if usuario["Email"] == email and usuario["Senha"] == senha:
                return redirect(url_for('home.home'))
        else:
            flash("Email ou senha inválidos", "danger")
            return redirect(url_for('login.login'))
    return render_template('login.html')

@login_bp.route('/register')
def register():
    return render_template('register.html')