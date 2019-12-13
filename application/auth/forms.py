from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators


class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False


class SignupForm(FlaskForm):
    name = StringField("Full name",
                [validators.Length(min = 4, max = 144)])

    email = StringField("Email address",
            [validators.Length(
                min = 5,
                max = 144)
            ])

    username = StringField("Username",
                [validators.Length(min = 4, max = 144)])

    password = PasswordField("Password",
                [validators.Length(min = 4, max = 144)])

    password_repeated = PasswordField("Repeat password",
                [validators.EqualTo('password', 
                    message = "Passwords must match.")])

    class Meta:
        csrf = False


class AccountEditForm(FlaskForm):
    name = StringField("Full name",
                [validators.Length(min = 4, max = 144)])

    email = StringField("Email address",
            [validators.Length(
                min = 5,
                max = 144)
            ])

    class Meta:
        csrf = False
