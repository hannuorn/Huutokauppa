from application import db
from application.models import Base

from sqlalchemy.sql import text


class Bid(Base):

    auction_id = db.Column(db.Integer, db.ForeignKey('auction.id'),
                           nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    amount = db.Column(db.Integer())

    def __init__(self, auction_id, account_id, amount):
        self.auction_id = auction_id
        self.account_id = account_id
        self.amount = amount

    @staticmethod
    def find_bids(auction_id):
        stmt = text("SELECT bid.amount, account.username, bid.date_created"
                    " FROM bid"
                    " JOIN account ON bid.account_id = account.id"
                    " WHERE (bid.auction_id = :auction_id)"
                    " ORDER BY bid.amount DESC;").params(
                           auction_id = auction_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"amount":row[0], "bidder":row[1], "date":row[2]})

        return response


    @staticmethod
    def highest_bid(auction_id):
        stmt = text("SELECT MAX(bid.amount) FROM bid"
                    " WHERE (bid.auction_id = :auction_id);").params(
                        auction_id = auction_id)
        res = db.engine.execute(stmt)
        response = 0
        for row in res:
            if type(row[0]) == int:
                response = row[0]

        return response
