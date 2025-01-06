from flask import Flask
from usuario import usuario_bp
from treinos import treinos_bp
from flask_sqlalchemy import SQLAlchemy
import os

# Inicialização do banco de dados
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configurações do Flask
    app.config['SECRET_KEY'] = '6d234996b5456d0fd1c8d59269f24f4c'  # Definir a chave secreta
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/gym_tracker.db'  # Caminho do banco
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desabilitar o rastreamento de modificações no banco
    db_path = os.path.join(os.getcwd(), 'instance', 'gym_tracker.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

    # Inicializa o banco de dados no app
    db.init_app(app)

    # Registrar blueprints
    app.register_blueprint(usuario_bp, url_prefix='/usuario')
    app.register_blueprint(treinos_bp, url_prefix='/treinos')

    return app

# Ponto de entrada para rodar a aplicação
if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()  # Criar as tabelas no banco, se necessário
    app.run(debug=True)


