from flask import render_template, Blueprint

home_bp = Blueprint('home', __name__, template_folder='templates')

"""
    /home (GET) - home
"""
@home_bp.route('/', methods = ["GET"])
def home():
    return render_template('home.html')

    