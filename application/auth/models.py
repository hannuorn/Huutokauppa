from application import db
from application.models import Base

from sqlalchemy.sql import text


class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False, unique=True)
    password = db.Column(db.String(144), nullable=False)

    auctions = db.relationship("Auction", backref='account', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True



    @staticmethod
    def get_name(user_id):
        stmt = text("SELECT account.name FROM account"
                    " WHERE (account.id = :user_id);").params(
                        user_id = user_id)
        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

        return ""
