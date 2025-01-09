from flask import render_template, Blueprint

treinos_bp = Blueprint('treinos', __name__, template_folder='templates')

@treinos_bp.route('/')
def list_workouts():
    return render_template('base.html')
    