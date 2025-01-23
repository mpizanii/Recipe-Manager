from flask import render_template, Blueprint, url_for, request, redirect
from flask_login import current_user
from models.models import Receitas, Alimentos
from app import db
import re, os
import google.generativeai as genai

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

    lista_ingredientes = [item.strip() for item in re.split(r'\d+[-.:]\s*', receita.ingredientes) if item.strip()]

    ingredientes_formatados = "\n".join([f'{i}: {ingrediente}.' for i, ingrediente in enumerate(lista_ingredientes, 1)])

    return ingredientes_formatados
    
def get_modo_preparo(id):

    receita = Receitas.query.get_or_404(id)

    lista_modo_preparo = [passo.strip() for passo in re.split(r'\d+[-.:]\s*', receita.modo_preparo) if passo.strip()]

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

@recipes_bp.route('/<int:id>/edit', methods = ["POST"])
def editar_receita(id):
    receita = Receitas.query.get_or_404(id)

    receita.nome = request.form.get('nome')
    receita.ingredientes = request.form.get('ingredientes')
    receita.modo_preparo = request.form.get('modo_preparo')

    db.session.commit()

    return redirect(url_for('recipes.receitas', id = id))

@recipes_bp.route('/<int:id>/delete', methods = ["POST"])
def deletar_receita(id):
    receita = Receitas.query.get_or_404(id)

    db.session.delete(receita)
    db.session.commit()

    return redirect(url_for('home.home'))

def get_nome_receita_ia(texto):
    nome = re.search(r"Nome da receita:\s*(.*)", texto)
    return nome.group(1) if nome else None

def get_ingredientes_receita_ia(texto):
    ingredientes = re.search(r"Ingredientes:\s*(.*?)(Modo de preparo:|$)", texto, re.DOTALL)
    return ingredientes.group(1).strip() if ingredientes else None

def get_modo_preparo_receita_ia(texto):
    preparo = re.search(r"Modo de preparo:\s*(.*)", texto, re.DOTALL)
    return preparo.group(1).strip() if preparo else None
    
@recipes_bp.route('/ia', methods = ["POST"])
def receita_ia():
    gemini_key = os.getenv('GEMINI_KEY')
    genai.configure(api_key=gemini_key)
    model = genai.GenerativeModel("gemini-pro")

    alimentos = request.form.getlist('alimentos')

    nomes_alimentos = [(alimento.nome, alimento.quantidade) for alimento in Alimentos.query.filter(Alimentos.id.in_(alimentos)).all()]

    pergunta = (
        "Responda apenas seguindo esse padrão (aonde tiver '\n' quebre uma linha):"
        "Nome da receita: (Nome da receita)\n"
        "Ingredientes: (1- (Ingrediente 1)\n 2- (Ingrediente 2)\n 3- ...)"
        "Modo de preparo: (1- (Passo 1)\n 2- (Passo 2)\n 3- ...\n\n"
        f"Faça uma receita, seguindo o padrão já mencionado, com APENAS os seguintes alimentos (não precisa utilizar todos): {nomes_alimentos}"
        )

    response = model.generate_content(pergunta)

    receita_texto = response.text

    nome = get_nome_receita_ia(receita_texto)
    ingredientes = get_ingredientes_receita_ia(receita_texto)
    modo_preparo = get_modo_preparo_receita_ia(receita_texto)

    return render_template('receita_ia.html', nome=nome, ingredientes=ingredientes, modo_preparo=modo_preparo)

@recipes_bp.route('/save', methods = ["POST"])
def salvar_receita():
    nome = request.form.get('nome')
    ingredientes = request.form.get('ingredientes')
    modo_preparo = request.form.get('modo_preparo')
    usuario_id = current_user.id

    receita = Receitas(nome=nome, ingredientes=ingredientes, modo_preparo=modo_preparo, usuario_id = usuario_id)

    db.session.add(receita)
    db.session.commit()

    return redirect(url_for('home.home'))