from flask import render_template
from . import treinos_bp

@treinos_bp.route('/workouts')
def list_workouts():
    # Lógica para listar treinos
    return render_template('base.html', message="Lista de Treinos")
    