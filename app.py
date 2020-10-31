# this is the standard Python library
import os
#we are using data from json so we need to import it
import json
#First we import the Flask class
from flask import Flask, render_template, request, flash

if os.path.exists("env.py"):
    import env

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
    #first we open an empty list called data
    data = []
    #then we tell Python to take data from our json file. This is called "with block"
    with open("data/company.json", "r") as json.data:
        data = json.load(json.data)
    return render_template("about.html", page_title="About", company=data)


@app.route('/about/<member_name>')
def about_member(member_name):
    member = {}
    
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        print(request.form)
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        # We should NEVER leave debug=True in a production application, or when submitting a project
        # Change it to False before submitting
        debug=True
    )
    