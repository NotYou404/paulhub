from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    context = {
        "title": "Home",
        "header_text": "Happy October!"
    }
    return render_template("base.html", **context)

@app.route("/about")
def about():
    context = {
        "title": "About",
    }
    return render_template("base.html", **context)
