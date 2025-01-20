from flask import render_template, Blueprint, url_for, request, flash,redirect
from flask_login import current_user
from models.models import Alimentos
from app import db

larder_bp = Blueprint('larder', __name__, template_folder= 'templates')

""" 
    /larder (GET) - mostrar geladeira
    /larder/add (POST) - formulario para adicionar um alimento
    /larder/edit (DELETE) - excluir um alimento
"""

@larder_bp.route('/', methods = ["GET"])
def dispensa():
    alimentos = Alimentos.query.filter_by(usuario_id=current_user.id).all()

    return render_template('dispensa.html', alimentos=alimentos)

@larder_bp.route('/add', methods = ["POST"])
def adicionar_alimento():
    nome = request.form.get('nome')
    quantidade = request.form.get('quantidade')
    usuario_id = current_user.id

    novo_alimento = Alimentos(nome = nome, quantidade = quantidade, usuario_id = usuario_id)

    db.session.add(novo_alimento)
    db.session.commit()

    return redirect(url_for('home.home'))
    

@larder_bp.route('/delete', methods = ["POST"])
def deletar_alimento():
    alimentos_ids = request.form.getlist('alimentos')

    for alimento_id in alimentos_ids:
        Alimentos.query.filter_by(id = alimento_id).delete()

    db.session.commit()

    return redirect(url_for('home.home'))
