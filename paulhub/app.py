from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    context = {
        "title": "Home",
        "header_text": "Happy October!",
        "trending": (
            (
                {
                    "name": "menu.png",
                    "alt": "Petition against the November",
                },
                {
                    "func": "about",
                    "text": "Petition against the November",
                },
            ),
            (
                {
                    "name": "menu.png",
                    "alt": "Personal stuff",
                },
                {
                    "func": "about",
                    "text": "Personal stuff",
                }
            ),
            (
                {
                    "name": "menu.png",
                    "alt": "December preparations",
                },
                {
                    "func": "about",
                    "text": "December preparations",
                }
            ),
        ),
    }
    return render_template("home.html", **context)


@app.route("/about")
def about():
    context = {
        "title": "About",
    }
    return render_template("base.html", **context)
