from application import db
from application.models import Base

from sqlalchemy.sql import text


class Bid(Base):

    auction_id = db.Column(
            db.Integer,
            db.ForeignKey('auction.id'),
            nullable = False)

    account_id = db.Column(
            db.Integer,
            db.ForeignKey('account.id'),
            nullable = False)

    amount = db.Column(
            db.Integer,
            nullable = False)

    def __init__(self, auction_id, account_id, amount):
        self.auction_id = auction_id
        self.account_id = account_id
        self.amount = amount

    @staticmethod
    def find_bids(auction_id):

        stmt = text(
            "SELECT bid.amount, account.name, bid.date_created"
            " FROM bid"
            " JOIN account ON bid.account_id = account.id"
            " WHERE bid.auction_id = :auction_id"
            " ORDER BY bid.amount DESC;"
            ).params(auction_id = auction_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"amount":row[0], "bidder":row[1], "date":row[2]})

        return response


    @staticmethod
    def find_bidder(bid_id):

        stmt = text(
            "SELECT account.name FROM account"
            " JOIN bid ON bid.account_id = account.id"
            " WHERE bid.id = :bid_id;"
            ).params(bid_id = bid_id)
        res = db.engine.execute(stmt)
        for row in res:
            return row[0]


    @staticmethod
    def highest_bid(auction_id):

        stmt = text(
            "SELECT account.name, bid.amount, account.email, account.id"
            " FROM account JOIN bid ON bid.account_id = account.id"
            " WHERE (bid.auction_id = :auction_id) AND (bid.amount ="
            " (SELECT MAX(bid.amount) FROM bid"
            " WHERE bid.auction_id = :auction_id));"
            ).params(auction_id = auction_id)
        res = db.engine.execute(stmt)

        highest_bid = 0
        highest_bidder = ""
        email = ""
        id = 0
        for row in res:
            highest_bidder = row[0]
            highest_bid = row[1]
            email = row[2]
            id = row[3]

        return {"amount":highest_bid, "bidder":highest_bidder, "email":email, "id":id}


    @staticmethod
    def find_users_bids(account_id):

        stmt = text(
            "SELECT auction.id, auction.title, MAX(bid.amount)"
            " FROM auction JOIN bid ON bid.auction_id = auction.id"
            " WHERE bid.account_id = :account_id"
            " GROUP BY auction.id;"
            ).params(account_id = account_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            hb = 0
            if type(row[2]) == int:
                hb = row[2]

            response.append({
                    "id":row[0],
                    "title":row[1],
                    "my_bid":hb})

        return response


    @staticmethod
    def delete_bids(auction_id):

        stmt = text(
            "DELETE FROM bid WHERE bid.auction_id = :auction_id;"
            ).params(auction_id = auction_id)
        
        res = db.engine.execute(stmt)
        return True
