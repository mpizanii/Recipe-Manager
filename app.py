from flask import Flask
from config import app_config, app_active
from routes.usuario import usuario_bp
from routes.treinos import treinos_bp

config = app_config[app_active]

def create_app():
    app = Flask(__name__)

    app.config.from_object(config) 
    app.secret_key = config.SECRET_KEY

    app.register_blueprint(usuario_bp)
    app.register_blueprint(treinos_bp, url_prefix='/treinos')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host = config.IP_HOST, port = config.PORT_HOST)