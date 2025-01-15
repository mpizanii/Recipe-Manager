from flask import render_template, Blueprint

larder_bp = Blueprint('larder', __name__, template_folder= 'templates')

""" 
    /larder (GET) - mostrar geladeira
    /larder/add (POST) - formulario para adicionar um alimento
    /larder/edit (PUT) - formulario para editar um alimento
    /larder/edit (DELETE) - excluir um alimento
"""

@larder_bp.route('/', methods = ["GET"])
def larder():
    return render_template('larder.html')

@larder_bp.route('/add')
def adicionar_alimento():
    return render_template('adicionar_alimento.html')

@larder_bp.route('/edit', methods = ["PUT"])
def editar_alimento():
    return render_template('editar_alimento.html')

@larder_bp.route('/edit', methods = ["DELETE"])
def deletar_alimento():
    return render_template('deletar_alimento.html')