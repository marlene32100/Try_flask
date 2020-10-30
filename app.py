# this is the standard Python library
import os
#First we import the Flask class
from flask import Flask, render_template

# Then we create an instance of this and we store it inside a variable called app.
# The first argument is the name of the application´s module.
# We are using a single module, so we can use the built-in Python variable "__name__"
app = Flask(__name__)

# This is called app.route "decorator". The slash / indicates that we are browsing our root directory.
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        # We should NEVER leave debug=True in a production application, or when submitting a project
        # Change it to False before submitting
        debug=True
    )
    