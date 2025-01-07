from flask import Flask
from usuario.routes import usuario_bp
from treinos.routes import treinos_bp
from extensions import db 
import os

def create_app():
    app = Flask(__name__)   
    app.config['SECRET_KEY'] = '6d234996b5456d0fd1c8d59269f24f4c'  
    db_path = os.path.join(os.getcwd(), 'instance', 'gym_tracker.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

    db.init_app(app)

    app.register_blueprint(usuario_bp, url_prefix='/usuario')
    app.register_blueprint(treinos_bp, url_prefix='/treinos')

    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()  
    app.run(debug=True)



