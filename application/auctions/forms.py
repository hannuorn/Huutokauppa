from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateTimeField, validators


class AuctionForm(FlaskForm):

    title = StringField("Title", 
            [validators.Length(
                    min = 5,
                    max = 50),
             validators.DataRequired()
            ])

    description = StringField("Description",
            [validators.Length(
                    min = 5,
                    max = 200),
             validators.DataRequired()
            ])

    minimum_bid = IntegerField("Minimum bid",
            [validators.NumberRange(
                    min = 1,
                    max = 1000),
             validators.DataRequired()
            ])

    date_ends = DateTimeField("Ends",
            [validators.InputRequired()])

    class Meta:
        csrf = False


class BiddingForm(FlaskForm):
    amount = IntegerField("Bid amount",
            [validators.NumberRange(
                    min = 1,
                    max = 1000000)
            ])

    class Meta:
        csrf = False
