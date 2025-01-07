from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import User, db  

usuario_bp = Blueprint('usuario', __name__, template_folder='templates')

@usuario_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        flash("Lógica de login ainda não implementada", "info")
    return render_template('login.html')

@usuario_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        flash("Lógica de registro ainda não implementada", "info")
    return render_template('register.html')
