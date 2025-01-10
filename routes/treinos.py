from flask import Blueprint, render_template

treinos_bp = Blueprint('treinos', __name__, template_folder='templates')

"""
    /workouts/<id>/view (GET) - visualizar treino
    /workouts/<id>/create (POST) - formulario p/ criar treino
    /workouts/<id>/edit (PUT) - formulario p/ editar treino
    /workouts/<id>/delete (DELETE) - excluir treino
    /workouts/<id>/edit (PUT) - formulario para editar perfil
"""

@treinos_bp.route('/<int:usuario_id>/view')
def visualizar_treino():
    return render_template('visualizar_treino.html')

@treinos_bp.route('/<int:usuario_id>/create')
def criar_treino():
    return render_template('criar_treino.html')

@treinos_bp.route('/<int:usuario_id>/edit')
def editar_treino():
    return render_template('editar_treino.html')

@treinos_bp.route('/<int:usuario_id>/delete')
def deletar_treino():
    pass