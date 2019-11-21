from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class AuctionForm(FlaskForm):
    title = StringField("Title", [validators.Length(min=5)])
    description = StringField("Description", [validators.Length(min=5)])
    lahtohinta = IntegerField("Minimum bid")

    class Meta:
        csrf = False


class BiddingForm(FlaskForm):
    amount = IntegerField("Bid amount")

    class Meta:
        csrf = False
