from flask import Flask, redirect, render_template
from pathlib import Path
import json
from datetime import datetime

app = Flask(__name__)


MonthDataType = dict[str, list[list[dict[str, str]]]]


def get_month_data(month: int) -> MonthDataType:
    """
    Retrieve trending, latest and recommendations information about a
    specific month.

    :param month: The month as int from 1 to 12 (Jan-Dec)
    :type month: int
    :return: The datatype to be passed to the template as `month_data`
    :rtype: MonthDataType
    """
    data_path = Path(__file__).parent / "data" / "home.json"
    with open(data_path, "r", encoding="utf-8") as fp:
        return json.load(fp)[str(month)]


@app.route("/")
def home():
    month = datetime.today().month
    context = {
        "title": "Home",
        "header_text": "Happy October!",
        "month_data": get_month_data(month),
    }
    return render_template("home.html", **context)


@app.route("/about")
def about():
    context = {
        "title": "About",
        "header_text": "About",
    }
    return render_template("legal/about.html", **context)


@app.route("/tos")
def tos():
    context = {
        "title": "Terms of Service",
        "header_text": "Terms of Service",
    }
    return render_template("legal/tos.html", **context)


@app.route("/pp")
def pp():
    context = {
        "title": "Privacy Policy",
        "header_text": "Privacy Policy",
    }
    return render_template("legal/pp.html", **context)


@app.route("/contact")
def contact():
    context = {
        "title": "Contact",
        "header_text": "Contact us",
    }
    return render_template("legal/contact.html", **context)


@app.route("/pages/personal_stuff")
def personal_stuff():
    context = {
        "title": "Personal stuff",
        "header_text": "Personal stuff",
    }
    return render_template("pages/personal_stuff.html", **context)


@app.route("/premium")
def premium():
    context = {
        "title": "Buy PaulHub Premium",
        "header_text": "Buy Premium",
    }
    return render_template("premium/premium.html", **context)


@app.route("/redirects/anti_november_petition")
def anti_november_petition():
    return redirect("https://www.change.org/antinovember")
