from application import db
from application.models import Base

from sqlalchemy.sql import text


class Message(Base):

    auction_id = db.Column(
            db.Integer,
            db.ForeignKey('auction.id'),
            nullable = False)

    account_id = db.Column(
            db.Integer,
            db.ForeignKey('account.id'),
            nullable = False)

    body = db.Column(
            db.String(200),
            nullable = False)

    def __init__(self, auction_id, account_id, body):
        self.auction_id = auction_id
        self.account_id = account_id
        self.body = body


    @staticmethod
    def get_messages(auction_id):

        stmt = text(
            "SELECT message.id, message.date_created, message.date_modified,"
            " account.id, account.name, message.body"
            " FROM message"
            " JOIN account ON message.account_id = account.id"
            " WHERE (message.auction_id = :auction_id)"
            " ORDER BY message.date_created DESC;"
            ).params(auction_id = auction_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({
                "id":row[0],
                "date_created":row[1],
                "date_modified":row[2],
                "author_id":row[3],
                "author":row[4],
                "body":row[5]})

        return response
