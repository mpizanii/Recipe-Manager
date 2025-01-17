from flask import render_template, Blueprint, url_for
from flask_login import current_user
from models.models import Alimentos

larder_bp = Blueprint('larder', __name__, template_folder= 'templates')

""" 
    /larder (GET) - mostrar geladeira
    /larder/add (POST) - formulario para adicionar um alimento
    /larder/edit (PUT) - formulario para editar um alimento
    /larder/edit (DELETE) - excluir um alimento
"""

@larder_bp.route('/', methods = ["GET"])
def dispensa():
    alimentos = Alimentos.query.filter_by(usuario_id=current_user.id).all()

    return render_template('dispensa.html', alimentos=alimentos)

@larder_bp.route('/add')
def adicionar_alimento():
    return render_template('adicionar_alimento.html')

@larder_bp.route('/edit')
def editar_alimento():
    return render_template('editar_alimento.html')

@larder_bp.route('/delete')
def deletar_alimento():
    return render_template('deletar_alimento.html')
