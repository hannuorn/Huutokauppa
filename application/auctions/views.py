from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application.auctions.models import Auction
from application.auctions.forms import AuctionForm
from application.auctions.forms import BiddingForm
from application.bids.models import Bid
from application.auth.models import User


@app.route("/")
def rootpage():
    return redirect(url_for("auctions_index"))

@app.route("/auctions", methods=["GET"])
def auctions_index():
    return render_template("auctions/list.html",
            auctions = Auction.find_auctions_with_highest_bid())


@app.route("/auctions/", methods=["GET"])
def auctions_index_slash():
    return redirect(url_for("auctions_index"))


@app.route("/auctions/<auction_id>/", methods=["GET", "POST"])
@login_required
def auctions_view(auction_id):

    html_file = "auctions/view.html"

    a = Auction.query.get(auction_id)
    seller = User.get_name(a.account_id)
    bids = Bid.find_bids(auction_id)
    highest_bid = Bid.highest_bid(auction_id)

    if request.method == "GET":
        return render_template(html_file, 
            form = BiddingForm(),
            seller = seller,
            bids = bids,
            highest_bid = highest_bid,
            auction = a)

    form = BiddingForm(request.form)
    if not form.validate():
        return render_template(html_file, 
            form = form,
            seller = seller,
            bids = bids,
            highest_bid = highest_bid,
            auction = a)

    if current_user.id == a.account_id:
        biderror = "You can not bid in your own auction."
        return render_template(html_file, 
                form = form,
                seller = seller,
                bids = bids,
                highest_bid = highest_bid,
                auction = a,
                biderror = biderror)

    if a.minimum_bid > form.amount.data:
        biderror = "You must bid at least the minimum bid."
        return render_template(html_file, 
                form = form,
                seller = seller,
                bids = bids,
                highest_bid = highest_bid,
                auction = a,
                biderror = biderror)


    if highest_bid.get("amount") >= form.amount.data:
        biderror = "You must bid more than the current highest bid."
        return render_template(html_file, 
                form = form,
                seller = seller,
                bids = bids,
                highest_bid = highest_bid,
                auction = a,
                biderror = biderror)

    b = Bid(auction_id, current_user.id, form.amount.data)

    db.session().add(b)
    db.session().commit()

    bids = Bid.find_bids(auction_id)
    highest_bid = Bid.highest_bid(auction_id)

    return render_template(html_file, 
            form = form,
            seller = seller,
            bids = bids,
            highest_bid = highest_bid,
            auction = a)


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
    a.minimum_bid = form.minimum_bid.data
    a.account_id = current_user.id

    db.session().add(a)
    db.session().commit()

    return redirect(url_for("auctions_index"))
