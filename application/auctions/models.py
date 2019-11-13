from application import db

class Auction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
#    date_ends = db.Column(db.DateTime())
    title = db.Column(db.String(40), nullable=False)
#    description = db.Column(db.String(200), nullable=False)

    def __init__(self, title):
        self.title = title

