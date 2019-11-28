from flask import Flask, render_template, request
import random

app = Flask(__name__)


@app.route("/")
def home():
    """Return home webpage."""

    return render_template("home.html")


# @app.route("/form")
# def form():
#     """Return form submission webpage."""

#     return render_template("form.html", form=form)

# @app.route("/form", methods=["POST"])
# def my_form_post():
#     text = request.form["text"]
#     processed_text = text.upper()
#     return processed_text

rammoush_list = [
    "Just being a dork",
    "Who are you and why are you sitting at Grainne’s desk?",
    "My fearless leader",
    "Grainnnoush oush oush begoush",
    "Well done lady!",
    "My official name is Lady Dr. Frau Elizabeth Ramsey Lupita Martinez Baranca Kukuktshka Bass Wise",
    "I’m a doctor, bitch",
    "Whoooop whoop",
    "Sneaky Snakey",
    "I got you boo!",
    "Fuzzy Wuzzy",
    "Declean and rebase",
    "Are we meeting now?",
    "#ourfireisbiggerthanyours",
    "I don’t have permissions",
    "Feel better babe!",
    "Merci buckets",
    "You  can run, but you can’t escape Macau",
    "Data ladies, fuck yeah",
    "Let’s pp together",
    "DWH had a little meltdown",
    "Virtual hug",
    "Paw paw paw paw at my <3",
    "Fifty shades of Gondor",
    "My Irish Southern Belle",
    "The Macau-AML-Plumbum Love Child",
    "You killed it, G",
    "Panda eats, shoots and leaves",
    "Dungeon Demon",
    "Get stuff FUN day",
    "Hey squirrel friend",
    "We’re gonna catch us some frauds!",
    "Bokey bokeh",
    "OMG I love this pussy!",
    "Prrrrrrrrrfect ",
    "Yaaaaaasss queen",
]


@app.route("/kitty")
def kitty():
    """Return random kitty webpage."""

    insert = random.choice(rammoush_list)

    return render_template("kitty.html")


@app.route("/haha")
def haha():
    """Return prank webpage."""

    return render_template("haha.html")


if __name__ == "__main__":
    app.run(debug=True)
