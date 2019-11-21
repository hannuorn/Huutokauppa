from application import db
from application.models import Base

from sqlalchemy.sql import text;


class Auction(Base):

    date_ends = db.Column(db.DateTime, default=db.func.current_timestamp())
    title = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    minimum_bid = db.Column(db.Integer())

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, title):
        self.title = title


    @staticmethod
    def find_auctions_with_highest_bid():
        stmt = text("SELECT auction.id, auction.title, MAX(bid.amount)"
                    " FROM auction LEFT JOIN bid ON bid.auction_id = auction.id"
                    " GROUP BY auction.id;")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            hb = 0
            if type(row[2]) == int:
                hb = row[2]

            response.append({"id":row[0], "title":row[1], "highest_bid":hb})

        return response
