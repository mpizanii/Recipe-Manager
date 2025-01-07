from flask import Blueprint

treinos_bp = Blueprint('treinos', __name__)

from . import routes  
