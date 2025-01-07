from flask import Flask
from usuario.routes import usuario_bp
from usuario.models import User  
from treinos.models import Workout 
from treinos.routes import treinos_bp
from config import *

def create_app():
    app = Flask(__name__)   
    app.config.from_object(Config) 

    db.init_app(app)

    app.register_blueprint(usuario_bp)
    app.register_blueprint(treinos_bp, url_prefix='/treinos')

    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()  
    app.run(debug=True)





