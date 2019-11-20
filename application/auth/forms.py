from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField


class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False


class SignupForm(FlaskForm):
    fullname = StringField("Full name")
    username = StringField("Username")
    password = PasswordField("Password")
    password_repeated = PasswordField("Repeat password")

    class Meta:
        csrf = False

