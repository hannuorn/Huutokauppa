from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators


class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False


class SignupForm(FlaskForm):
    fullname = StringField("Full name",
                [validators.Length(min = 4)])

    username = StringField("Username",
                [validators.Length(min = 4)])

    password = PasswordField("Password",
                [validators.Length(min = 4)])

    password_repeated = PasswordField("Repeat password",
                [validators.EqualTo('password', 
                    message = "Passwords must match.")])

    class Meta:
        csrf = False
