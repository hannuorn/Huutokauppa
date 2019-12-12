from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from flask_login import current_user

import datetime

from application.auctions.models import Auction
from application.auctions.forms import AuctionForm
from application.auctions.forms import BiddingForm
from application.auctions.forms import AuctionEditForm
from application.bids.models import Bid
from application.auth.models import User


@app.route("/")
def rootpage():
    return redirect(url_for("auctions_index"))

@app.route("/auctions", methods=["GET"])
def auctions_index():
    return render_template("auctions/list.html",
            auctions = Auction.find_active_auctions())

@app.route("/auctions_ended", methods=["GET"])
def auctions_ended_index():
    return render_template("auctions/list.html",
            auctions = Auction.find_ended_auctions())

@app.route("/auctions/", methods=["GET"])
def auctions_index_slash():
    return redirect(url_for("auctions_index"))


@app.route("/auctions/<auction_id>/", methods=["GET", "POST"])
@login_required(role = "ANY")
def auctions_view(auction_id):

    html_file = "auctions/view.html"

    a = Auction.query.get(auction_id)
    seller = User.get_name(a.account_id)
    bids = Bid.find_bids(auction_id)
    highest_bid = Bid.highest_bid(auction_id)
    ended = 0
    if a.date_ends < datetime.datetime.now():
        ended = 1

    time_to_go = a.date_ends - datetime.datetime.now()

    if request.method == "GET":
        return render_template(html_file, 
            form = BiddingForm(),
            seller = seller,
            bids = bids,
            highest_bid = highest_bid,
            ended = ended,
            days_to_go = time_to_go.days,
            auction = a)

    form = BiddingForm(request.form)
    invalid = False
    biderror = ""

    if not form.validate():
        invalid = True
    elif current_user.id == a.account_id:
        invalid = True
        biderror = "You can not bid in your own auction."
    elif a.minimum_bid > form.amount.data:
        invalid = True
        biderror = "You must bid at least the minimum bid."
    elif highest_bid.get("amount") >= form.amount.data:
        invalid = True
        biderror = "You must bid more than the current highest bid."

    if invalid:
        return render_template(html_file, 
                form = form,
                seller = seller,
                bids = bids,
                highest_bid = highest_bid,
                ended = ended,
                days_to_go = time_to_go.days,
                auction = a,
                biderror = biderror)

    b = Bid(auction_id, current_user.id, form.amount.data)

    db.session().add(b)
    db.session().commit()

    bids = Bid.find_bids(auction_id)
    highest_bid = Bid.highest_bid(auction_id)

    return redirect(url_for("auctions_view", auction_id = auction_id))


@app.route("/auctions/new/")
@login_required(role = "ANY")
def auctions_form():
    form = AuctionForm()
    return render_template(
        "auctions/new.html",
        form = form)


@app.route("/auctions/", methods=["POST"])
@login_required(role = "ANY")
def auctions_create():
    form = AuctionForm(request.form)

    if not form.validate():
        return render_template(
            "auctions/new.html",
            form = form)

    a = Auction(form.title.data)
    a.account_id = current_user.id
    a.description = form.description.data
    a.minimum_bid = form.minimum_bid.data
    ends = form.date_ends.data
    a.date_ends = datetime.datetime(
        ends.year, ends.month, ends.day, 23, 59, 00, 00)

    if a.date_ends < datetime.datetime.now():
        form.date_ends.errors = ["End date must be in the future."]
        return render_template(
            "auctions/new.html",
            form = form)

    db.session().add(a)
    db.session().commit()

    return redirect(url_for("auctions_index"))


@app.route("/auctions/edit/<auction_id>/", methods=["GET", "POST"])
@login_required(role = "ANY")
def auctions_edit(auction_id):

    a = Auction.query.get(auction_id)
    if request.method == "GET":
        form = AuctionEditForm()
        form.title.data = a.title
        form.description.data = a.description
        form.minimum_bid.data = a.minimum_bid
        return render_template(
            "auctions/edit.html",
            form = form,
            auction = a)

    form = AuctionEditForm(request.form)

    invalid = False
    if not form.validate():
        invalid = True

    if form.minimum_bid.data > a.minimum_bid:
        invalid = True
        form.minimum_bid.errors = ["Raising minimum bid is not allowed."]
        form.minimum_bid.data = a.minimum_bid

    if invalid:
        return render_template(
            "auctions/edit.html",
            form = form,
            auction = a)

    a.title = form.title.data
    a.description = form.description.data
    a.minimum_bid = form.minimum_bid.data

    db.session().commit()

    return redirect(url_for("auth_account"))


@app.route("/auctions/delete/<auction_id>/", methods=["POST"])
@login_required(role = "ANY")
def auctions_delete(auction_id):

    Bid.delete_bids(auction_id)

    a = Auction.query.get(auction_id)
    db.session().delete(a)
    db.session().commit()

    return redirect(url_for("auth_account"))
