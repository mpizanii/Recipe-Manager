from flask import render_template, Blueprint, request, flash, url_for,redirect
from flask_login import login_required, current_user
from models.models import Alimentos, Receitas
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

home_bp = Blueprint('home', __name__, template_folder='templates')

"""
    /home (GET) - home
    /home/perfil (GET) - formulario para editar perfil
    /home/perfil (PUT) - editar perfil
"""
@home_bp.route('/', methods = ["GET"])
@login_required
def home():
    alimentos = Alimentos.query.filter_by(usuario_id=current_user.id).all()
    receitas = Receitas.query.filter_by(usuario_id=current_user.id).all()
    
    return render_template('home.html', alimentos=alimentos, receitas=receitas)

@home_bp.route('/perfil', methods = ["GET", "POST"])
def editar_perfil():
    if request.method == "POST":
        novo_nome = request.form.get('nome')
        novo_email = request.form.get('email')

        if novo_nome:
            current_user.nome = novo_nome
        if novo_email:
            current_user.email = novo_email

        senha = request.form.get('senha')
        nova_senha = request.form.get('nova_senha')
        confirmar_nova_senha = request.form.get('confirmar_senha')

        if senha and nova_senha and confirmar_nova_senha:
            
            senha_atual = current_user.senha

            if not check_password_hash(senha_atual, senha):
                flash("A senha não coincide com a atual!", 'danger')
                return redirect(url_for('home.editar_perfil'))
            
            elif nova_senha != confirmar_nova_senha:
                flash("Senhas não coincidem", "danger")
                return redirect(url_for('home.editar_perfil'))
            
            else:
                senha_hash = generate_password_hash(nova_senha)
                current_user.senha = senha_hash
                
        db.session.commit()
        return redirect(url_for('home.home'))
        
    return render_template('editar_perfil.html')    