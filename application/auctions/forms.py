from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateTimeField, validators
from wtforms.fields.html5 import DateField


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

    date_ends = DateField("Ends", format = "%Y-%m-%d")


    class Meta:
        csrf = False


class BiddingForm(FlaskForm):
    amount = IntegerField("Bid amount",
            [validators.NumberRange(
                    min = 1,
                    max = 1000000)
            ])

    message = StringField("Message",
            [validators.Length(
                    min = 5,
                    max = 200)
            ])
            
    message_edit = StringField("Message",
            [validators.Length(
                    min = 5,
                    max = 200)
            ])
            
    class Meta:
        csrf = False


class AuctionEditForm(FlaskForm):
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

    class Meta:
        csrf = False
