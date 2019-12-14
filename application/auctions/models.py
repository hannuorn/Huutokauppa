from application import db
from application.models import Base

from sqlalchemy.sql import text


class Auction(Base):

    date_ends = db.Column(
            db.DateTime,
            nullable = False)

    title = db.Column(
            db.String(40),
            nullable = False)

    description = db.Column(
            db.String(200),
            nullable = False)

    minimum_bid = db.Column(
            db.Integer(),
            nullable = False)

    account_id = db.Column(
            db.Integer,
            db.ForeignKey('account.id'),
            nullable = False)


    def __init__(self, title):
        self.title = title


    @staticmethod
    def parse_auctions(res):
        response = []
        for row in res:
            highest_bid = 0
            highest_bidder = ""
            if type(row[2]) == int:
                highest_bid = row[2]
                highest_bidder = row[3]

            response.append(
                {"id":row[0],
                "title":row[1],
                "highest_bid":highest_bid,
                "highest_bidder":highest_bidder,
                "date_ends":row[4]})

        return response


    @staticmethod
    def find_active_auctions():
        stmt = text("SELECT auction.id, auction.title, bid.amount, account.name, auction.date_ends"
                    " FROM auction LEFT JOIN bid ON bid.auction_id = auction.id"
                    " LEFT JOIN account ON account.id = bid.account_id"
                    " WHERE (auction.date_ends > CURRENT_TIMESTAMP) AND"
                    " (bid.amount IS NULL or (bid.amount ="
                    "    (SELECT MAX(bid.amount) FROM bid"
                    "     WHERE bid.auction_id = auction.id)))"
                    " ORDER BY auction.date_ends;")
        res = db.engine.execute(stmt)
        return Auction.parse_auctions(res)


    @staticmethod
    def find_ended_auctions():
        stmt = text("SELECT auction.id, auction.title, bid.amount, account.name, auction.date_ends"
                    " FROM auction LEFT JOIN bid ON bid.auction_id = auction.id"
                    " LEFT JOIN account ON account.id = bid.account_id"
                    " WHERE (auction.date_ends < CURRENT_TIMESTAMP) AND"
                    " (bid.amount IS NULL or (bid.amount ="
                    "    (SELECT MAX(bid.amount) FROM bid"
                    "     WHERE bid.auction_id = auction.id)))"
                    " ORDER BY auction.date_ends DESC;")
        res = db.engine.execute(stmt)
        return Auction.parse_auctions(res)


    @staticmethod
    def find_users_auctions(account_id):
        stmt = text(
                "SELECT auction.id, auction.title, MAX(bid.amount)"
                " FROM auction LEFT JOIN bid ON bid.auction_id = auction.id"
                " WHERE auction.account_id = :account_id"
                " GROUP BY auction.id;").params(
                        account_id = account_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            hb = 0
            if type(row[2]) == int:
                hb = row[2]

            response.append({
                    "id":row[0],
                    "title":row[1],
                    "highest_bid":hb})

        return response
        
