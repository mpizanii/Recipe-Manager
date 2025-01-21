from flask import render_template, Blueprint, url_for, request, flash,redirect
from flask_login import current_user
from models.models import Receitas
from app import db
import re

recipes_bp = Blueprint('recipes', __name__, template_folder= 'templates')

""" 
    /recipes (GET) - mostrar receitas
    /recipes/add (POST) - formulario para adicionar uma receita
    /recipes/edit (PUT) - formulario para editar uma receita
    /recipes/delete (DELETE) - excluir uma receita
    /recipes/ia - consulta ao gemini
"""

def get_ingredientes(id):

    receita = Receitas.query.get_or_404(id)

    lista_ingredientes = [item.strip() for item in re.split(r'[;,.]', receita.ingredientes) if item.strip()]

    ingredientes_formatados = "\n".join([f'{i}: {ingrediente}.' for i, ingrediente in enumerate(lista_ingredientes, 1)])

    return ingredientes_formatados
    
def get_modo_preparo(id):

    receita = Receitas.query.get_or_404(id)

    lista_modo_preparo = [passo.strip() for passo in re.split(r'\d+[-.]\s*', receita.modo_preparo) if passo.strip()]

    passos_formatados = "\n".join([f'Passo {i}: {passo}' for i, passo in enumerate(lista_modo_preparo, 1)])

    return passos_formatados

@recipes_bp.route('/<int:id>', methods = ["GET"])
def receitas(id):
    receita = Receitas.query.get_or_404(id)

    return render_template('receitas.html', receita = receita, lista_ingredientes = get_ingredientes(id), lista_modo_preparo = get_modo_preparo(id))

@recipes_bp.route('/add', methods = ["POST"])
def adicionar_receita():
    nome = request.form.get('nome')
    ingredientes = request.form.get('ingredientes')
    modo_preparo = request.form.get('modo_preparo')
    usuario_id = current_user.id

    nova_receita = Receitas(nome = nome, ingredientes = ingredientes, modo_preparo = modo_preparo, usuario_id = usuario_id)

    db.session.add(nova_receita)
    db.session.commit()

    return redirect(url_for('home.home'))

@recipes_bp.route('/edit')
def editar_receita():
    return render_template('editar_receita.html')

@recipes_bp.route('/delete')
def deletar_receita():
    return render_template('deletar_receita.html')

@recipes_bp.route('/ia')
def receita_ia():
    return render_template('receita_ia.html')
