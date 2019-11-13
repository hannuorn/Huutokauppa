from application import app, db
from flask import redirect, render_template, request, url_for
from application.auctions.models import Auction


@app.route("/auctions", methods=["GET"])
def auctions_index():
    return render_template("auctions/list.html", auctions = Auction.query.all())


@app.route("/auctions/<auction_id>/", methods=["GET"])
def auctions_view(auction_id):
    return render_template("auctions/view.html", auction = Auction.query.get(auction_id))


@app.route("/auctions/new/")
def auctions_form():
    return render_template("auctions/new.html")


@app.route("/auctions/", methods=["POST"])
def auctions_create():
    title = request.form.get("name")
    if len(title) > 5:
        print(title)
        a = Auction(title)

        db.session().add(a)
        db.session().commit()
    else:
        print("Liian lyhyt otsikko!")
  
    return redirect(url_for("auctions_index"))
