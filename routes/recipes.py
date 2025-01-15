from flask import render_template, Blueprint

recipes_bp = Blueprint('recipes', __name__, template_folder= 'templates')

""" 
    /recipes (GET) - mostrar receitas
    /recipes/add (POST) - formulario para adicionar uma receita
    /recipes/edit (PUT) - formulario para editar uma receita
    /recipes/edit (DELETE) - excluir uma receita
"""

@recipes_bp.route('/', methods = ["GET"])
def recipes():
    return render_template('recipes.html')

@recipes_bp.route('/add')
def adicionar_receita():
    return render_template('adicionar_receita.html')

@recipes_bp.route('/edit', methods = ["PUT"])
def editar_receita():
    return render_template('editar_receita.html')

@recipes_bp.route('/edit', methods = ["DELETE"])
def deletar_receita():
    return render_template('deletar_receita.html')