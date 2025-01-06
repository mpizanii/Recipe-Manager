from flask import render_template, request, redirect, url_for, flash
from . import usuario_bp
from .models import User, db

@usuario_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Adicione lógica de login aqui
        pass
    return render_template('login.html')

@usuario_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Adicione lógica de registro aqui
        pass
    return render_template('register.html')
