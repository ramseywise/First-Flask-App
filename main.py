from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """Return home webpage."""

    return render_template("home.html")


@app.route("/grainnoush")
def grainnoush():
    """Return hello Grainnoush."""
    return "Hello, Grainnoush!"


if __name__ == "__main__":
    app.run(debug=True)
