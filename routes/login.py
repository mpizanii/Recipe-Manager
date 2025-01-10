from flask import Blueprint, render_template, request, flash, redirect, session, url_for
from models.models import Usuario, db
from werkzeug.security import generate_password_hash, check_password_hash

usuario_bp = Blueprint('usuario', __name__, template_folder='templates')
"""
    / (GET) - formulario de login
    /register - formulario de cadastro
"""
@usuario_bp.route('/', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        
        usuario = Usuario.query.filter_by(email = email).first()

        if not usuario:
            flash("Usuário não cadastrado!", "error")
            return redirect("/")
        
        if not check_password_hash(usuario.senha, senha):
            flash("Informações incorretas!", "error")
            return redirect("/")
        
        session['usuario_id'] = usuario.id
        session['usuario_nome'] = usuario.nome

        return redirect(url_for('home.home'))

    return render_template('login.html')

@usuario_bp.route('/register', methods = ["GET"])
def form_cadastro():
    return render_template('register.html')

@usuario_bp.route('/register', methods = ["POST"])
def cadastro():
    nome = request.form['nome']
    email = request.form['email']
    genero = request.form['genero']
    data_nascimento = request.form['data_nascimento']
    senha = request.form['senha']
    confirmar_senha = request.form['confirmar_senha']

    usuario_existente = Usuario.query.filter_by(email=email).first()

    if usuario_existente:
        flash("Este e-mail já está cadastrado", "error")
        return redirect("/")
    elif senha != confirmar_senha:
        flash("Senhas não coincidem", "error")
        return redirect("/register")
    
    hash_senha = generate_password_hash(senha)
    novo_usuario = Usuario(nome = nome, email = email, genero = genero, data_nascimento = data_nascimento, senha = hash_senha)

    db.session.add(novo_usuario)
    db.session.commit()
    
    flash("Cadastro realizado com sucesso!", "sucess")
    return redirect("/")