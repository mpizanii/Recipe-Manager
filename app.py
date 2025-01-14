from flask import Flask
import google.generativeai as genai
from config import app_config, app_active
from routes.login import usuario_bp
from routes.home import home_bp
from models.models import db
from flask_migrate import Migrate

config = app_config[app_active]

def create_app():
    app = Flask(__name__)

    app.config.from_object(config) 
    app.secret_key = config.SECRET_KEY
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI

    app.register_blueprint(usuario_bp)
    app.register_blueprint(home_bp, url_prefix='/recipes')

    db.init_app(app)
    migrate = Migrate(app, db)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host = config.IP_HOST, port = config.PORT_HOST)
