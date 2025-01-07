from flask import Blueprint

usuario_bp = Blueprint('usuario', __name__)

from . import routes  
