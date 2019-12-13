from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db, login_required
from application.auth.models import User
from application.auth.forms import LoginForm, SignupForm, AccountEditForm
from application.auctions.models import Auction
from application.bids.models import Bid


@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():

    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(
            username = form.username.data,
            password = form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")

    login_user(user)
    return redirect(url_for("auctions_index"))


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("auctions_index"))


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

    u = User(
        form.name.data, form.email.data,
        form.username.data, form.password.data)

    db.session().add(u)
    db.session().commit()

    user = User.query.filter_by(username=form.username.data).first()
    login_user(user)

    return redirect(url_for("auctions_index"))


@app.route("/auth/account", methods = ["GET"])
@login_required(role = "ANY")
def auth_account():
    if request.method == "GET":
        return render_template(
            "auth/view.html",
            edit_mode = 0,
            user = current_user,
            auctions = Auction.find_users_auctions(current_user.id),
            bids = Bid.find_users_bids(current_user.id))



@app.route("/auth/account/edit_name", methods = ["GET", "POST"])
@login_required(role = "ANY")
def auth_edit():
    if request.method == "GET":
        form = AccountEditForm()
        form.name.data = current_user.name
        form.email.data = current_user.email
        return render_template(
            "auth/view.html",
            form = form,
            edit_mode = 1,
            user = current_user,
            auctions = Auction.find_users_auctions(current_user.id),
            bids = Bid.find_users_bids(current_user.id))

    form = AccountEditForm(request.form)

    invalid = False
    if not form.validate():
        invalid = True

    if invalid:
        return render_template(
            "auth/view.html",
            form = form,
            edit_mode = 1,
            user = current_user,
            auctions = Auction.find_users_auctions(current_user.id),
            bids = Bid.find_users_bids(current_user.id))

    u = User.query.get(current_user.id)
    u.name = form.name.data
    u.email = form.email.data
    db.session().commit()

    return redirect(url_for("auth_account"))
