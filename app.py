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


@app.route("/add_article", methods=["GET", "POST"])
def add_article():
    if request.method == "POST":
        article = {
            "heading": request.form.get("article_heading"),
            "date": request.form.get("article_date"),
            "content": request.form.get("article_content"),
            "author": request.form.get("article_author"),
        }
        mongo.db.articles.insert_one(article)
        flash("Article Successfully Posted")
        return redirect(url_for("display_articles"))

    return render_template("add_article.html")


@app.route("/edit_article/<article_id>", methods=["GET", "POST"])
def edit_article(article_id):
    if request.method == "POST":
        submit = {
            "heading": request.form.get("article_heading"),
            "date": request.form.get("article_date"),
            "content": request.form.get("article_content"),
            "author": request.form.get("article_author"),
        }
        mongo.db.articles.update_one(
            {"_id": ObjectId(article_id)}, {"$set": submit})
        flash("Player Successfully Updated")
        return redirect(url_for("display_articles"))

    article = mongo.db.articles.find_one({"_id": ObjectId(article_id)})
    return render_template("edit_article.html", article=article)


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


@app.route("/edit_player/<player_id>", methods=["GET", "POST"])
def edit_player(player_id):
    if request.method == "POST":
        submit = {
            "position_name": request.form.get("position_name"),
            "player_name": request.form.get("player_name"),
            "player_height": request.form.get("player_height"),
            "player_weight": request.form.get("player_weight"),
            "player_points": request.form.get("player_points"),
            "player_rebounds": request.form.get("player_rebounds"),
            "player_assists": request.form.get("player_assists"),
            "player_profile": request.form.get("player_profile"),
        }
        mongo.db.players.update_one(
            {"_id": ObjectId(player_id)}, {"$set": submit})
        flash("Player Successfully Updated")
        return redirect(url_for("display_players"))

    player = mongo.db.players.find_one({"_id": ObjectId(player_id)})
    positions = mongo.db.positions.find()
    return render_template("edit_player.html", player=player,
                           positions=positions)


@app.route("/delete_player/<player_id>")
def delete_player(player_id):
    mongo.db.players.delete_one({"_id": ObjectId(player_id)})
    flash("Player successfully deleted")
    return redirect(url_for("display_players"))


@app.route("/display_fixtures")
def display_fixtures():
    fixtures = list(mongo.db.fixtures.find())
    return render_template("fixtures.html", fixtures=fixtures)


@app.route("/add_fixture", methods=["GET", "POST"])
def add_fixture():
    if request.method == "POST":
        fixture = {
            "game": request.form.get("game_number"),
            "opponent": request.form.get("opponent"),
            "home_away": request.form.get("home_away"),
            "location": request.form.get("location"),
            "time": request.form.get("time"),
            "eagles_score": request.form.get("eagles_score"),
            "opponent_score": request.form.get("opponent_score"),
            "date": request.form.get("date"),
        }
        mongo.db.fixtures.insert_one(fixture)
        flash("Fixture Successfully Added")
        return redirect(url_for("display_fixtures"))

    return render_template("add_fixture.html")


@app.route("/edit_fixture/<fixture_id>", methods=["GET", "POST"])
def edit_fixture(fixture_id):
    if request.method == "POST":
        submit = {
                "game": request.form.get("game_number"),
                "opponent": request.form.get("opponent"),
                "home_away": request.form.get("home_away"),
                "location": request.form.get("location"),
                "time": request.form.get("time"),
                "eagles_score": request.form.get("eagles_score"),
                "opponent_score": request.form.get("opponent_score"),
                "date": request.form.get("date"),
            }

        mongo.db.fixtures.update_one(
                {"_id": ObjectId(fixture_id)}, {"$set": submit})
        flash("Fixture Successfully Updated")
        return redirect(url_for("display_fixtures"))

    fixture = mongo.db.fixtures.find_one({"_id": ObjectId(fixture_id)})
    return render_template("edit_fixture.html", fixture=fixture)


@app.route("/delete_fixture/<fixture_id>")
def delete_fixture(fixture_id):
    mongo.db.fixtures.delete_one({"_id": ObjectId(fixture_id)})
    flash("Fixture successfully deleted")
    return redirect(url_for("display_fixtures"))


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
