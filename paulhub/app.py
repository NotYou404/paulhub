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
        "header_text": "About"
    }
    return render_template("base.html", **context)


@app.route("/redirects/anti_november_petition")
def anti_november_petition():
    return redirect("https://chng.it/DTnJPHWht6")
