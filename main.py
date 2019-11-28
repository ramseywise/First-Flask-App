from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config["SECRET_KEY"] = "7d441f27d441f27567d441f2b6176a"


@app.route("/")
def home():
    """Return home webpage."""

    return render_template("home.html")


class ReusableForm(Form):
    name = TextField("Entry:", validators=[validators.required()])

    @app.route("/grainnoush", methods=["GET", "POST"])
    def grainnoush():
        """Return hello Grainnoush."""

        form = ReusableForm(request.form)

        print form.errors
        if request.method == "POST":
            entry = request.form["entry"]
            print name

        if form.validate():
            # Save the comment here.
            flash("Try out my Rammoush bot!" + entry)
        else:
            flash("All the form fields are required. ")

        return render_template("grainnoush.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
