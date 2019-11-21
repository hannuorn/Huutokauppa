from application import db
from application.models import Base


class Auction(Base):

    date_ends = db.Column(db.DateTime, default=db.func.current_timestamp())
    title = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    lahtohinta = db.Column(db.Integer())

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, title):
        self.title = title
