"""First Flask App."""

import sys
import random
import requests
from io import BytesIO, TextIOWrapper
# from flask_restplus import reqparse, Api, Resource, abort
# from flask_restful import request
# from flask_cors import CORS
from google_images_download import google_images_download
from flask import Flask, render_template, request, Response


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


@app.route("/haha")
def haha():
    """Return prank webpage."""

    return render_template("haha.html")


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
    insert = random.choice(rammoush_list)

    url = "http://www.randomkittengenerator.com/cats/rotator.php"

    return render_template("kitty.html", response=url, insert=insert)


@app.route("/badass")
def badass():
    """Return google search initiative webpage."""

    keys = [
        "Cat AND just being a dork",
        "Cat AND territorial?",
        "Cat AND  fearless leader",
        "kitten AND super cute",
        "Cat AND praise",
        "Cat AND doctor AND sass",
        "Cat AND Whoooop whoop",
        "Cat AND Sneaky",
        "Cat AND I got you boo",
        "Cat AND Fuzzy Wuzzy",
        "Cat AND Declean and rebase",
        "Cat AND confused",
        "Cat AND mischievious",
        "Cat AND locked out",
        "Cat AND Feel better babe!",
        "Cat AND buckets",
        "Cat AND thank you",
        "YCat AND you can run, but you cant escape Macau",
        "Cat AND Data ladies",
        "Cat AND toilet",
        "Cat AND DWH had a little meltdown",
        "Cat AND Virtual hug",
        "Cat AND Paw paw paw paw at my <3",
        "Cat AND Fifty shades of Gondor",
        "Cat AND My Irish Southern Belle",
        "Cat AND Love Child",
        "Cat AND femme fatale",
        "Cat AND pandas",
        "Cat AND Dungeon Demon",
        "Cat AND FUN day",
        "Cat AND Hey squirrel friend",
        "Cat AND We are gonna catch us some frauds",
        "Cat AND coding",
        "cutest cat photo ever",
        "Cat AND super chilled AND cute",
        "Cat AND adorable",
        "Cat AND  queen",
    ]
    values = [
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
    d = dict(zip(keys, values))
    res = key, val = random.choice(list(d.items()))
    

    # old_stdout = sys.stdout
    # sys.stdout = TextIOWrapper(BytesIO(), sys.stdout.encoding)

    # response = google_images_download.googleimagesdownload()

    # arguments = {
    #     "keywords": res[0], 
    #     "limit": 1, 
    #     "print_urls": True,
    # }
    # paths = response.download(arguments)
    # print(paths)

    # sys.stdout.seek(0)
    # output = sys.stdout.read()

    # sys.stdout.close()
    # sys.stdout = old_stdout
    
    # for line in output.split("\n"):
    #     if line.startswith("Image URL:"):
    #         image_url = line.replace("Image URL: ", "") 

    return render_template("badass.html", response=results, insert=val)


if __name__ == "__main__":
    app.run(debug=True)
   