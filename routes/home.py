from flask import render_template, Blueprint, request, flash, url_for,redirect
from flask_login import login_required, current_user
from models.models import Alimentos, Usuario
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
    return render_template('home.html', alimentos=alimentos)

@home_bp.route('/perfil', methods = ["GET", "PUT"])
def editar_senha():
    if request.method == "PUT":
        senha = request.form['senha']
        nova_senha = request.form['nova_senha']
        confirmar_nova_senha = request.form['confirmar_senha']

        senha_atual = current_user.senha

        if not check_password_hash(senha_atual, senha):
            flash("A senha não coincide com a atual!", 'danger')
            return redirect(url_for('home.editar_senha'))
        
        elif nova_senha != confirmar_nova_senha:
            flash("Senhas não coincidem", "danger")
            return redirect(url_for('usuario.cadastro'))
        
        else:
            senha_hash = generate_password_hash(nova_senha)

            current_user.senha = senha_hash
            db.session.commit()

            flash("Senha alterada com sucesso!", "sucess")
            return redirect(url_for('home.home'))
        
    return render_template('editar_senha.html')    