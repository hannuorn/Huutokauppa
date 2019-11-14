from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class AuctionForm(FlaskForm):
    title = StringField("Otsikko", [validators.Length(min=5)])
    description = StringField("Kuvaus", [validators.Length(min=5)])
    lahtohinta = IntegerField("Lähtöhinta")

    class Meta:
        csrf = False
