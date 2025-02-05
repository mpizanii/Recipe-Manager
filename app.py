import os
from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')

    from routes.login import usuario_bp
    from routes.home import home_bp
    from routes.larder import larder_bp
    from routes.recipes import recipes_bp

    app.register_blueprint(usuario_bp)
    app.register_blueprint(home_bp, url_prefix = '/home')
    app.register_blueprint(larder_bp, url_prefix = '/larder')
    app.register_blueprint(recipes_bp, url_prefix = '/recipes')

    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager.init_app(app)
    login_manager.login_view = 'login'

    login_manager.login_view = 'usuario.login'
    login_manager.login_message = 'Por favor, realize o login para acessar a home!'
    login_manager.login_message_category = 'info'

    return app