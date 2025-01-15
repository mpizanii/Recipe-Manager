from flask import render_template, Blueprint, request

home_bp = Blueprint('home', __name__, template_folder='templates')

"""
    /home (GET) - home
    /home/perfil (GET) - formulario para editar perfil
    /home/perfil (PUT) - editar perfil
"""
@home_bp.route('/', methods = ["GET"])
def home():
    return render_template('home.html')

@home_bp.route('/perfil', methods = ["GET", "PUT"])
def editar_senha():
    if request.method == "PUT":
        ...
    return render_template('editar_senha.html')    