from flask import render_template, Blueprint
from database.usuario import USUARIO

home_bp = Blueprint('home', __name__, template_folder='templates')

"""
    /gym/tracker/<id> (GET) - home
    /gym/tracker/<id>/edit (PUT) - formulario para editar perfil
"""
@home_bp.route('/')
def home():
    return render_template('home.html', usuario=USUARIO)

@home_bp.route('/edit')
def editar_usuario():
    return render_template('editar_usuario.html', usuario=USUARIO)
    