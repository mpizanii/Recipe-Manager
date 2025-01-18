from flask import render_template, Blueprint

recipes_bp = Blueprint('recipes', __name__, template_folder= 'templates')

""" 
    /recipes (GET) - mostrar receitas
    /recipes/add (POST) - formulario para adicionar uma receita
    /recipes/edit (PUT) - formulario para editar uma receita
    /recipes/delete (DELETE) - excluir uma receita
    /recipes/ia - consulta ao gemini
"""

@recipes_bp.route('/', methods = ["GET"])
def receitas():
    return render_template('receitas.html')

@recipes_bp.route('/add')
def adicionar_receita():
    return render_template('adicionar_receita.html')

@recipes_bp.route('/edit')
def editar_receita():
    return render_template('editar_receita.html')

@recipes_bp.route('/delete')
def deletar_receita():
    return render_template('deletar_receita.html')

@recipes_bp.route('/ia')
def receita_ia():
    return render_template('receita_ia.html')
