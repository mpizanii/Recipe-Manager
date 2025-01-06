from flask import Blueprint

# Definindo o blueprint para o módulo 'usuario'
usuario_bp = Blueprint('usuario', __name__)

from . import routes  # Importando as rotas do módulo usuário
