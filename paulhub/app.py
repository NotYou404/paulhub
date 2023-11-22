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


@app.route("/pages/month_happiness_chart")
def month_happiness_chart():
    context = {
        "title": "Month happiness chart",
        "header_text": "Month happiness chart"
    }
    return render_template("pages/month_happiness_chart.html", **context)


@app.route("/pages/men_friendly_month_challenges")
def men_friendly_month_challenges():
    context = {
        "title": "Men friendly month challenges",
        "header_text": "Men friendly month challenges",
    }
    return render_template(
        "pages/men_friendly_month_challenges.html", **context
    )


@app.route("/pages/january_true_meaning")
def january_true_meaning():
    context = {
        "title": "January's true meaning",
        "header_text": "January's true meaning",
    }
    return render_template("pages/january_true_meaning.html", **context)


@app.route("/pages/february_true_meaning")
def february_true_meaning():
    context = {
        "title": "February's true meaning",
        "header_text": "February's true meaning",
    }
    return render_template("pages/february_true_meaning.html", **context)


@app.route("/pages/march_true_meaning")
def march_true_meaning():
    context = {
        "title": "March's true meaning",
        "header_text": "March's true meaning",
    }
    return render_template("pages/march_true_meaning.html", **context)


@app.route("/pages/april_true_meaning")
def april_true_meaning():
    context = {
        "title": "April's true meaning",
        "header_text": "April's true meaning",
    }
    return render_template("pages/april_true_meaning.html", **context)


@app.route("/pages/may_true_meaning")
def may_true_meaning():
    context = {
        "title": "May's true meaning",
        "header_text": "May's true meaning",
    }
    return render_template("pages/may_true_meaning.html", **context)


@app.route("/pages/june_true_meaning")
def june_true_meaning():
    context = {
        "title": "June's true meaning",
        "header_text": "June's true meaning",
    }
    return render_template("pages/june_true_meaning.html", **context)


@app.route("/pages/july_true_meaning")
def july_true_meaning():
    context = {
        "title": "July's true meaning",
        "header_text": "July's true meaning",
    }
    return render_template("pages/july_true_meaning.html", **context)


@app.route("/pages/august_true_meaning")
def august_true_meaning():
    context = {
        "title": "August's true meaning",
        "header_text": "August's true meaning",
    }
    return render_template("pages/august_true_meaning.html", **context)


@app.route("/pages/september_true_meaning")
def september_true_meaning():
    context = {
        "title": "September's true meaning",
        "header_text": "September's true meaning",
    }
    return render_template("pages/september_true_meaning.html", **context)


@app.route("/pages/october_true_meaning")
def october_true_meaning():
    context = {
        "title": "October's true meaning",
        "header_text": "October's true meaning",
    }
    return render_template("pages/october_true_meaning.html", **context)


@app.route("/pages/november_true_meaning")
def november_true_meaning():
    context = {
        "title": "November's true meaning",
        "header_text": "November's true meaning",
    }
    return render_template("pages/november_true_meaning.html", **context)


@app.route("/pages/december_true_meaning")
def december_true_meaning():
    context = {
        "title": "December's true meaning",
        "header_text": "December's true meaning",
    }
    return render_template("pages/december_true_meaning.html", **context)


@app.route("/redirects/anti_november_petition")
def anti_november_petition():
    return redirect("https://www.change.org/antinovember")
