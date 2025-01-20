from flask import render_template, Blueprint, url_for, request, flash,redirect
from flask_login import current_user
from models.models import Receitas
from app import db

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
