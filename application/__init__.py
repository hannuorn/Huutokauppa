from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///auctions.db"
    app.config["SQLALCHEMY_ECHO"] = True

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = "False"

db = SQLAlchemy(app)


from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."



from functools import wraps
from application.auth import models

def login_required(role = "ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user:
                return login_manager.unauthorized()
          
            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            
            unauthorized = False

            if role != "ANY":
                unauthorized = True
                
                for user_role in current_user.roles():
                    if user_role == role:
                        unauthorized = False
                        break

            if unauthorized:
                return login_manager.unauthorized()
            
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper


from application import views

from application.auctions import models
from application.auctions import views

from application.auth import models
from application.auth import views

from application.bids import models

from application.messages import models


# login

from application.auth.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


try:
    db.create_all()
except:
    pass
