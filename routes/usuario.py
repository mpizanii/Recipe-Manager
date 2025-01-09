from flask import Blueprint, render_template,request

usuario_bp = Blueprint('usuario', __name__, template_folder='templates')

@usuario_bp.route('/', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        print('Lógica ainda não implementada')
    return render_template('login.html')

@usuario_bp.route('/register')
def register():
    return render_template('register.html')
