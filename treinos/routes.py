from flask import render_template, Blueprint
from . import treinos_bp

treinos_bp = Blueprint('treinos',__name__, template_folder='templates')

@treinos_bp.route('/workouts')
def list_workouts():
    return render_template('base.html', message="Lista de Treinos")
    