from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, SignupForm


@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():

    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")

    login_user(user)
    return redirect(url_for("index"))


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/auth/signup", methods = ["GET", "POST"])
def auth_signup():

    if request.method == "GET":
        return render_template("auth/signupform.html", form = SignupForm())

    form = SignupForm(request.form)

    if not form.validate():
        return render_template("auth/signupform.html", form = form)

    user = User.query.filter_by(username=form.username.data).first()

    if user:
        return render_template("auth/signupform.html", form = form,
                               error = "Username already exists")

    if form.password.data != form.password_repeated.data:
        return render_template("auth/signupform.html", form = form,
                               error = "Passwords do not match")

    u = User(form.fullname.data, form.username.data, form.password.data)
    u.password = form.password.data

    db.session().add(u)
    db.session().commit()

    user = User.query.filter_by(username=form.username.data).first()
    login_user(user)

    return redirect(url_for("index"))


@app.route("/auth/account", methods = ["GET"])
def auth_account():
    return render_template(
            "auth/view.html",
            user = current_user)
