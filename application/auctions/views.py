from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application.auctions.models import Auction
from application.auctions.forms import AuctionForm
from application.auctions.forms import BiddingForm
from application.bids.models import Bid


@app.route("/")
def rootpage():
    return redirect(url_for("auctions_index"))

@app.route("/auctions", methods=["GET"])
def auctions_index():
    return render_template("auctions/list.html", auctions = Auction.query.all())


@app.route("/auctions/", methods=["GET"])
def auctions_index_slash():
    return redirect(url_for("auctions_index"))


@app.route("/auctions/<auction_id>/", methods=["GET"])
@login_required
def auctions_view(auction_id):

    return render_template("auctions/view.html", 
            form = BiddingForm(),
            bids = Bid.find_bids(auction_id),
            highest_bid = Bid.highest_bid(auction_id),
            auction = Auction.query.get(auction_id), error = "")


@app.route("/auctions/<auction_id>/", methods=["POST"])
@login_required
def auctions_bid(auction_id):

    form = BiddingForm(request.form)
    highest_bid = Bid.highest_bid(auction_id)

    if highest_bid >= form.amount.data:
        error = "You must bid more."
        return render_template("auctions/view.html", 
                form = BiddingForm(),
                bids = Bid.find_bids(auction_id),
                highest_bid = Bid.highest_bid(auction_id),
                auction = Auction.query.get(auction_id),
                error = error)

    b = Bid(auction_id, current_user.id, form.amount.data)

    db.session().add(b)
    db.session().commit()

    return render_template("auctions/view.html", 
            form = BiddingForm(),
            bids = Bid.find_bids(auction_id),
            highest_bid = Bid.highest_bid(auction_id),
            auction = Auction.query.get(auction_id))


@app.route("/auctions/new/")
@login_required
def auctions_form():
    return render_template("auctions/new.html", form = AuctionForm())


@app.route("/auctions/", methods=["POST"])
@login_required
def auctions_create():
    form = AuctionForm(request.form)

    if not form.validate():
        return render_template("auctions/new.html", form = form)

    a = Auction(form.title.data)
    a.description = form.description.data
    a.lahtohinta = form.lahtohinta.data
    a.account_id = current_user.id

    db.session().add(a)
    db.session().commit()

    return redirect(url_for("auctions_index"))
