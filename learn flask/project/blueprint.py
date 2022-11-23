from flask import Blueprint, render_template

bp = Blueprint("blueprint", __name__, template_folder="templates")

@bp.route("/")
def index():
    return render_template("login.html")

@bp.route("/index")
def home():
    return render_template("index.html")