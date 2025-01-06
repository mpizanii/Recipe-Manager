from flask import Blueprint

# Definindo o blueprint para o módulo 'treinos'
treinos_bp = Blueprint('treinos', __name__)

from . import routes  # Importando as rotas do módulo treinos
