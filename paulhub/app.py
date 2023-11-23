import json
from datetime import datetime
from pathlib import Path

from flask import Flask, redirect, render_template, request

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
    today_month = datetime.today().month
    month = request.args.get("month", today_month, int)
    if not (1 <= month <= 12):
        month = today_month
    month_data = get_month_data(month)
    context = {
        "title": "Home",
        "header_text": month_data["header_text"],
        "month_data": month_data,
    }
    return render_template("home.html", **context)


@app.route("/evaljs")
def evaljs():
    return render_template("evaljs.html")


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


@app.route("/pages/december_preparations")
def december_preparations():
    context = {
        "title": "December preparations",
        "header_text": "December preparations",
    }
    return render_template("pages/december_preparations.html", **context)


@app.route("/pages/opinion_why_communism_is_better_for_us")
def why_communism_is_better_for_us():
    context = {
        "title": "Opinion: Why communism is better for us",
        "header_text": "Opinion: Why communism is better for us",
    }
    return render_template(
        "pages/opinion_why_communism_is_better_for_us.html", **context
    )


@app.route("/pages/january_true_meaning")
def january_true_meaning():
    context = {
        "title": "January's true meaning",
        "header_text": "January's true meaning",
    }
    return render_template(
        "pages/true_meaning/january_true_meaning.html", **context
    )


@app.route("/pages/february_true_meaning")
def february_true_meaning():
    context = {
        "title": "February's true meaning",
        "header_text": "February's true meaning",
    }
    return render_template(
        "pages/true_meaning/february_true_meaning.html", **context
    )


@app.route("/pages/march_true_meaning")
def march_true_meaning():
    context = {
        "title": "March's true meaning",
        "header_text": "March's true meaning",
    }
    return render_template(
        "pages/true_meaning/march_true_meaning.html", **context
    )


@app.route("/pages/april_true_meaning")
def april_true_meaning():
    context = {
        "title": "April's true meaning",
        "header_text": "April's true meaning",
    }
    return render_template(
        "pages/true_meaning/april_true_meaning.html", **context
    )


@app.route("/pages/may_true_meaning")
def may_true_meaning():
    context = {
        "title": "May's true meaning",
        "header_text": "May's true meaning",
    }
    return render_template(
        "pages/true_meaning/may_true_meaning.html", **context
    )


@app.route("/pages/june_true_meaning")
def june_true_meaning():
    context = {
        "title": "June's true meaning",
        "header_text": "June's true meaning",
    }
    return render_template(
        "pages/true_meaning/june_true_meaning.html", **context
    )


@app.route("/pages/july_true_meaning")
def july_true_meaning():
    context = {
        "title": "July's true meaning",
        "header_text": "July's true meaning",
    }
    return render_template(
        "pages/true_meaning/july_true_meaning.html", **context
    )


@app.route("/pages/august_true_meaning")
def august_true_meaning():
    context = {
        "title": "August's true meaning",
        "header_text": "August's true meaning",
    }
    return render_template(
        "pages/true_meaning/august_true_meaning.html", **context
    )


@app.route("/pages/september_true_meaning")
def september_true_meaning():
    context = {
        "title": "September's true meaning",
        "header_text": "September's true meaning",
    }
    return render_template(
        "pages/true_meaning/september_true_meaning.html", **context
    )


@app.route("/pages/october_true_meaning")
def october_true_meaning():
    context = {
        "title": "October's true meaning",
        "header_text": "October's true meaning",
    }
    return render_template(
        "pages/true_meaning/october_true_meaning.html", **context
    )


@app.route("/pages/november_true_meaning")
def november_true_meaning():
    context = {
        "title": "November's true meaning",
        "header_text": "November's true meaning",
    }
    return render_template(
        "pages/true_meaning/november_true_meaning.html", **context
    )


@app.route("/pages/december_true_meaning")
def december_true_meaning():
    context = {
        "title": "December's true meaning",
        "header_text": "December's true meaning",
    }
    return render_template(
        "pages/true_meaning/december_true_meaning.html", **context
    )


@app.route("/pages/jam_of_jar_recipe")
def jam_of_jar_recipe():
    context = {
        "title": "Jam of Jar recipe",
        "header_text": "Jam of Jar recipe",
    }
    return render_template(
        "pages/month_philosophy/jam_of_jar_recipe.html", **context
    )


@app.route("/pages/the_conspiracy_of_free_food")
def the_conspiracy_of_free_food():
    context = {
        "title": "The conspiracy of free food",
        "header_text": "The conspiracy of free food",
    }
    return render_template(
        "pages/month_philosophy/the_conspiracy_of_free_food.html", **context
    )


@app.route("/pages/how_to_outplay_march")
def how_to_outplay_march():
    context = {
        "title": "How to outplay March",
        "header_text": "How to outplay March",
    }
    return render_template(
        "pages/month_philosophy/how_to_outplay_march.html", **context
    )


@app.route("/pages/a_doctors_statement_on_apple_april")
def a_doctors_statement_on_apple_april():
    context = {
        "title": "A doctor's statement on apple April",
        "header_text": "A doctor's statement on apple April",
    }
    return render_template(
        "pages/month_philosophy/a_doctors_statement_on_apple_april.html",
        **context
    )


@app.route("/pages/vegan_milk")
def vegan_milk():
    context = {
        "title": "Vegan milk",
        "header_text": "Vegan milk",
    }
    return render_template(
        "pages/month_philosophy/vegan_milk.html", **context
    )


@app.route("/pages/why_just_june")
def why_just_june():
    context = {
        "title": "Why just June?",
        "header_text": "Why just June?",
    }
    return render_template(
        "pages/month_philosophy/why_just_june.html", **context
    )


@app.route("/pages/how_to_not_get_banned_on_every_discord_server")
def how_to_not_get_banned_on_every_discord_server():
    context = {
        "title": "How to not get banned on every Discord server",
        "header_text": "How to not get banned on every Discord server",
    }
    return render_template(
        "pages/month_philosophy/how_to_not_get_banned_on_every_discord_server"
        ".html",
        **context
    )


@app.route("/pages/gdtjett_please_sum")
def gdtjett_please_sum():
    context = {
        "title": '"GDT Jett, please sum..."',
        "header_text": '"GDT Jett, please sum..."',
    }
    return render_template(
        "pages/month_philosophy/gdtjett_please_sum.html", **context
    )


@app.route("/pages/how_to_get_free_money")
def how_to_get_free_money():
    context = {
        "title": "How to get free money",
        "header_text": "How to get free money",
    }
    return render_template(
        "pages/month_philosophy/how_to_get_free_money.html", **context
    )


@app.route("/pages/why_onlyfans_is_so_popular")
def why_onlyfans_is_so_popular():
    context = {
        "title": "Why Onlyfans is so popular",
        "header_text": "Why Onlyfans is so popular",
    }
    return render_template(
        "pages/month_philosophy/why_onlyfans_is_so_popular.html", **context
    )


@app.route("/pages/its_christmas_time")
def its_christmas_time():
    context = {
        "title": "It's Christmas time",
        "header_text": "It's Christmas time",
    }
    return render_template(
        "pages/month_philosophy/its_christmas_time.html", **context
    )


@app.route("/redirects/anti_november_petition")
def anti_november_petition():
    return redirect("https://www.change.org/antinovember")
