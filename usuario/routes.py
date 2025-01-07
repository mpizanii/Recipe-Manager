from flask import Blueprint, render_template

usuario_bp = Blueprint('usuario', __name__, template_folder='templates')

@usuario_bp.route('/')
def login():
    return render_template('login.html')

@usuario_bp.route('/register')
def register():
    return render_template('register.html')
