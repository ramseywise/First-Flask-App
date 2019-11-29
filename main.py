from flask import Flask, render_template, request, url_for, send_from_directory
import random
import requests
from google_images_download import google_images_download
import sys
from io import BytesIO, TextIOWrapper

# app = Flask(__name__)

app = Flask(
    __name__,
    static_url_path="",
    static_folder="web/static",
    template_folder="web/templates",
)


@app.route("/")
def home():
    """Return home webpage."""

    return render_template("home.html")


@app.route("/kitty")
def kitty():
    """Return random kitty webpage."""

    rammoush_list = [
        "Just being a dork",
        "Who are you and why are you sitting at Grainnoushes desk?",
        "My fearless leader",
        "Grainnnoush oush oush begoush",
        "Well done lady!",
        "Im a doctor bitch",
        "Whoooop whoop",
        "Sneaky Snakey",
        "I got you boo",
        "Fuzzy Wuzzy",
        "Declean and rebase",
        "Are we meeting now?",
        "ourfireisbiggerthanyours",
        "I dont have permissions",
        "Feel better babe!",
        "Merci buckets",
        "Spanks",
        "You can run, but you cant escape Macau",
        "Data ladies, fuck yeah",
        "Lets pp together",
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
        "We are gonna catch us some frauds",
        "Bokey bokeh",
        "OMG I love this pussy!",
        "Prrrrrrrrrfect ",
        "Tots adorbs",
        "Yaaaaaasss queen",
    ]

    keywords = [
        "Cat AND Yaaaaaasss queen",
        "Cat AND Tots adorbs",
    ]
    insert = random.choice(rammoush_list)

    old_stdout = sys.stdout
    sys.stdout = TextIOWrapper(BytesIO(), sys.stdout.encoding)
    # url = "http://www.randomkittengenerator.com/cats/rotator.php"
    # url = "https://www.google.com/search?tbm=isch&q=" + insert

    response = google_images_download.googleimagesdownload()
    arguments = {"keywords": insert, "limit": 1, "print_urls": True}
    paths = response.download(arguments)
    print(paths)
    sys.stdout.seek(0)
    output = sys.stdout.read()

    sys.stdout.close()
    sys.stdout = old_stdout

    for line in output.split("\n"):
        if line.startswith("Image URL:"):
            image_url = line.replace("Image URL: ", "")

    return render_template("kitty.html", response=url, insert=insert)


@app.route("/haha")
def haha():
    """Return prank webpage."""

    return render_template("haha.html")


if __name__ == "__main__":
    app.run(debug=True)

# @app.route("/form")
# def form():
#     """Return form submission webpage."""

#     return render_template("form.html", form=form)

# @app.route("/form", methods=["POST"])
# def my_form_post():
#     text = request.form["text"]
#     processed_text = text.upper()
#     return processed_text
