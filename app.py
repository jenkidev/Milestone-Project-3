import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/display_articles")
def display_articles():
    articles = list(mongo.db.articles.find())
    return render_template("articles.html", articles=articles)


@app.route("/display_players")
def display_players():
    players = list(mongo.db.players.find())
    return render_template("players.html", players=players)


@app.route("/add_player", methods=["GET", "POST"])
def add_player():
    if request.method == "POST":
        player = {
            "position_name": request.form.get("position_name"),
            "player_name": request.form.get("player_name"),
            "player_height": request.form.get("player_height"),
            "player_weight": request.form.get("player_weight"),
            "player_points": request.form.get("player_points"),
            "player_rebounds": request.form.get("player_rebounds"),
            "player_assists": request.form.get("player_assists"),
            "player_profile": request.form.get("player_profile"),
        }
        mongo.db.players.insert_one(player)
        flash("Player Successfully Added")
        return redirect(url_for("display_players"))

    positions = mongo.db.positions.find()
    return render_template("add_player.html", positions=positions)
    return render_template("players.html")


@app.route("/edit_player/<player_id>", methods=["GET", "POST"])
def edit_player(player_id):
    player = mongo.db.players.find_one({"_id": ObjectId(player_id)})
    positions = mongo.db.positions.find()
    return render_template("edit_player.html", player=player, positions=positions)


@app.route("/register", methods=["GET", "POST"])
def register_user():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register_user"))

        if request.form.get("password") != request.form.get("password_check"):
            flash("Passwords do not match, please re-try")
            return redirect(url_for("register_user"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")

    return render_template("register.html")


@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        # check if username exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure password in database matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for("display_articles"))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("signin"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("signin"))

    return render_template("signin.html")


@app.route("/signout")
def signout():
    # remove user from session cookie
    flash("You have been signed out")
    session.pop("user")
    return redirect(url_for("signin"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)