from flask import render_template, Blueprint

home_bp = Blueprint('home', __name__, template_folder='templates')

"""
    /recipes<id> (GET) - home
"""
@home_bp.route('/')
def home():
    return render_template('home.html')

@home_bp.route('/edit')
def editar_usuario():
    return render_template('editar_usuario.html')
    