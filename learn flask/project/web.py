from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta
from blueprint import bp


app = Flask(__name__)
app.secret_key = "SECRET_KEY"
app.permanent_session_lifetime = timedelta(minutes=5)
app.register_blueprint(bp, url_prefix="")

@app.route("/")
def index():
    return render_template('index.html',content=['Ritik', 'Reizo', 'Tim'])

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        session.permanent = False
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("You are already logged in.")
            return redirect(url_for("user"))

        return render_template('login.html')

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        flash("You are logged in.")
        return render_template('user.html', user=user)   
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("You have been logged out", "info")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)