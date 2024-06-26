import json
from datetime import datetime
from pathlib import Path
from typing import Union

from data.rr import increment_rickroll
from flask import Flask, redirect, render_template, request
from werkzeug import Response

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
        return json.load(fp)[str(month)]  # type: ignore


@app.route("/")
def home() -> str:
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
    if month == 6:
        context["extra_stylesheets"] = ["/static/css/pride.css"]
        context["logo_overwrite"] = "/static/images/furry_hub_transparent.png"
    return render_template("home.html", **context)


@app.route("/redirects/rr")
def redirect_rr() -> Union[str, Response]:
    origin = request.args.get("origin", type=str)
    context = {
        "title": "Thank you!",
        "header_text": "GOTCHU!",
        "stfu": True,
        "no_music": True,
    }
    increment_rickroll(origin)
    if origin:
        return redirect("/redirects/rr")
    return render_template("rr.html", **context)


@app.route("/evaljs")
def evaljs() -> str:
    return render_template("evaljs.html")


@app.route("/about")
def about() -> str:
    context = {
        "title": "About",
        "header_text": "About",
    }
    return render_template("legal/about.html", **context)


@app.route("/tos")
def tos() -> str:
    context = {
        "title": "Terms of Service",
        "header_text": "Terms of Service",
    }
    return render_template("legal/tos.html", **context)


@app.route("/pp")
def pp() -> str:
    context = {
        "title": "Privacy Policy",
        "header_text": "Privacy Policy",
    }
    return render_template("legal/pp.html", **context)


@app.route("/contact")
def contact() -> str:
    context = {
        "title": "Contact",
        "header_text": "Contact us",
    }
    return render_template("legal/contact.html", **context)


@app.route("/pages/personal_stuff")
def personal_stuff() -> str:
    context = {
        "title": "Personal stuff",
        "header_text": "Personal stuff",
    }
    return render_template("pages/personal_stuff.html", **context)


@app.route("/premium")
def premium() -> str:
    context = {
        "title": "Buy PaulHub Premium",
        "header_text": "Buy Premium",
    }
    return render_template("premium/premium.html", **context)


@app.route("/pages/month_happiness_chart")
def month_happiness_chart() -> str:
    context = {
        "title": "Month happiness chart",
        "header_text": "Month happiness chart"
    }
    return render_template("pages/month_happiness_chart.html", **context)


@app.route("/pages/men_friendly_month_challenges")
def men_friendly_month_challenges() -> str:
    context = {
        "title": "Men friendly month challenges",
        "header_text": "Men friendly month challenges",
    }
    return render_template(
        "pages/men_friendly_month_challenges.html", **context
    )


@app.route("/pages/december_preparations")
def december_preparations() -> str:
    context = {
        "title": "December preparations",
        "header_text": "December preparations",
    }
    return render_template("pages/december_preparations.html", **context)


@app.route("/pages/mothsoc1")
def mothsoc1() -> str:
    context = {
        "title": "Manifest of the haunted spectre of communism (Jan. edition)",
        "header_text": "Manifest of the haunted spectre of communism (Jan. "
                       "edition)",
    }
    return render_template(
        "pages/mothsoc1.html", **context
    )


@app.route("/pages/mothsoc2")
def mothsoc2() -> str:
    context = {
        "title": "Manifest of the haunted spectre of communism (Feb. edition)",
        "header_text": "Manifest of the haunted spectre of communism (Feb. "
                       "edition)",
    }
    return render_template(
        "pages/mothsoc2.html", **context
    )


@app.route("/pages/mothsoc3")
def mothsoc3() -> str:
    context = {
        "title": "Manifest of the haunted spectre of communism (Mar. edition)",
        "header_text": "Manifest of the haunted spectre of communism (Mar. "
                       "edition)",
        "en": request.args.get("en", 0, int)
    }
    return render_template(
        "pages/mothsoc3.html", **context
    )


@app.route("/pages/mothsoc4")
def mothsoc4() -> str:
    context = {
        "title": "Manifest of the haunted spectre of communism (Apr. edition)",
        "header_text": "Manifest of the haunted spectre of communism (Apr. "
                       "edition)",
    }
    return render_template(
        "pages/mothsoc4.html", **context
    )


@app.route("/pages/mothsoc5")
def mothsoc5() -> str:
    context = {
        "title": "Manifest of the haunted spectre of communism (May. edition)",
        "header_text": "Manifest of the haunted spectre of communism (May. "
                       "edition)",
    }
    return render_template(
        "pages/mothsoc5.html", **context
    )


@app.route("/pages/how_to_furry")
def how_to_furry() -> str:
    context = {
        "title": "How to Furry [Updated] [Real]",
        "header_text": "How to Furry [Updated] [Real]",
    }
    return render_template(
        "pages/how_to_furry.html", **context
    )


@app.route("/pages/hardest_materials_on_earth")
def hardest_materials_on_earth() -> str:
    context = {
        "title": "The hardest materials on earth",
        "header_text": "The hardest materials on earth",
    }
    return render_template(
        "pages/hardest_materials_on_earth.html", **context
    )


@app.route("/pages/january_true_meaning")
def january_true_meaning() -> str:
    context = {
        "title": "January's true meaning",
        "header_text": "January's true meaning",
    }
    return render_template(
        "pages/true_meaning/january_true_meaning.html", **context
    )


@app.route("/pages/february_true_meaning")
def february_true_meaning() -> str:
    context = {
        "title": "February's true meaning",
        "header_text": "February's true meaning",
    }
    return render_template(
        "pages/true_meaning/february_true_meaning.html", **context
    )


@app.route("/pages/march_true_meaning")
def march_true_meaning() -> str:
    context = {
        "title": "March's true meaning",
        "header_text": "March's true meaning",
    }
    return render_template(
        "pages/true_meaning/march_true_meaning.html", **context
    )


@app.route("/pages/april_true_meaning")
def april_true_meaning() -> str:
    context = {
        "title": "April's true meaning",
        "header_text": "April's true meaning",
    }
    return render_template(
        "pages/true_meaning/april_true_meaning.html", **context
    )


@app.route("/pages/may_true_meaning")
def may_true_meaning() -> str:
    context = {
        "title": "May's true meaning",
        "header_text": "May's true meaning",
    }
    return render_template(
        "pages/true_meaning/may_true_meaning.html", **context
    )


@app.route("/pages/june_true_meaning")
def june_true_meaning() -> str:
    context = {
        "title": "June's true meaning",
        "header_text": "June's true meaning",
    }
    return render_template(
        "pages/true_meaning/june_true_meaning.html", **context
    )


@app.route("/pages/july_true_meaning")
def july_true_meaning() -> str:
    context = {
        "title": "July's true meaning",
        "header_text": "July's true meaning",
    }
    return render_template(
        "pages/true_meaning/july_true_meaning.html", **context
    )


@app.route("/pages/august_true_meaning")
def august_true_meaning() -> str:
    context = {
        "title": "August's true meaning",
        "header_text": "August's true meaning",
    }
    return render_template(
        "pages/true_meaning/august_true_meaning.html", **context
    )


@app.route("/pages/september_true_meaning")
def september_true_meaning() -> str:
    context = {
        "title": "September's true meaning",
        "header_text": "September's true meaning",
    }
    return render_template(
        "pages/true_meaning/september_true_meaning.html", **context
    )


@app.route("/pages/october_true_meaning")
def october_true_meaning() -> str:
    context = {
        "title": "October's true meaning",
        "header_text": "October's true meaning",
    }
    return render_template(
        "pages/true_meaning/october_true_meaning.html", **context
    )


@app.route("/pages/november_true_meaning")
def november_true_meaning() -> str:
    context = {
        "title": "November's true meaning",
        "header_text": "November's true meaning",
    }
    return render_template(
        "pages/true_meaning/november_true_meaning.html", **context
    )


@app.route("/pages/december_true_meaning")
def december_true_meaning() -> str:
    context = {
        "title": "December's true meaning",
        "header_text": "December's true meaning",
    }
    return render_template(
        "pages/true_meaning/december_true_meaning.html", **context
    )


@app.route("/pages/jam_of_jar_recipe")
def jam_of_jar_recipe() -> str:
    context = {
        "title": "Jam of Jar recipe",
        "header_text": "Jam of Jar recipe",
    }
    return render_template(
        "pages/month_philosophy/jam_of_jar_recipe.html", **context
    )


@app.route("/pages/the_conspiracy_of_free_food")
def the_conspiracy_of_free_food() -> str:
    context = {
        "title": "The conspiracy of free food",
        "header_text": "The conspiracy of free food",
    }
    return render_template(
        "pages/month_philosophy/the_conspiracy_of_free_food.html", **context
    )


@app.route("/pages/how_to_outplay_march")
def how_to_outplay_march() -> str:
    context = {
        "title": "How to outplay March",
        "header_text": "How to outplay March",
    }
    return render_template(
        "pages/month_philosophy/how_to_outplay_march.html", **context
    )


@app.route("/pages/a_doctors_statement_on_apple_april")
def a_doctors_statement_on_apple_april() -> str:
    context = {
        "title": "A doctor's statement on apple April",
        "header_text": "A doctor's statement on apple April",
    }
    return render_template(
        "pages/month_philosophy/a_doctors_statement_on_apple_april.html",
        **context
    )


@app.route("/pages/vegan_milk")
def vegan_milk() -> str:
    context = {
        "title": "Vegan milk",
        "header_text": "Vegan milk",
    }
    return render_template(
        "pages/month_philosophy/vegan_milk.html", **context
    )


@app.route("/pages/why_just_june")
def why_just_june() -> str:
    context = {
        "title": "Why just June?",
        "header_text": "Why just June?",
    }
    return render_template(
        "pages/month_philosophy/why_just_june.html", **context
    )


@app.route("/pages/how_to_not_get_banned_on_every_discord_server")
def how_to_not_get_banned_on_every_discord_server() -> str:
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
def gdtjett_please_sum() -> str:
    context = {
        "title": '"GDT Jett, please sum..."',
        "header_text": '"GDT Jett, please sum..."',
    }
    return render_template(
        "pages/month_philosophy/gdtjett_please_sum.html", **context
    )


@app.route("/pages/how_to_get_free_money")
def how_to_get_free_money() -> str:
    context = {
        "title": "How to get free money",
        "header_text": "How to get free money",
    }
    return render_template(
        "pages/month_philosophy/how_to_get_free_money.html", **context
    )


@app.route("/pages/why_onlyfans_is_so_popular")
def why_onlyfans_is_so_popular() -> str:
    context = {
        "title": "Why Onlyfans is so popular",
        "header_text": "Why Onlyfans is so popular",
    }
    return render_template(
        "pages/month_philosophy/why_onlyfans_is_so_popular.html", **context
    )


@app.route("/pages/its_christmas_time")
def its_christmas_time() -> str:
    context = {
        "title": "It's Christmas time",
        "header_text": "It's Christmas time",
    }
    return render_template(
        "pages/month_philosophy/its_christmas_time.html", **context
    )


@app.route("/redirects/anti_november_petition")
def anti_november_petition() -> Union[str, Response]:
    return redirect("https://www.change.org/antinovember")


@app.route("/pages/gay_test")
def gay_test() -> str:
    context = {
        "title": "Are you gay? Test yourself!",
        "header_text": "Are you gay? Test yourself!",
    }
    return render_template(
        "pages/gay_test.html", **context
    )


@app.route("/pages/schizo_test")
def schizo_test() -> str:
    context = {
        "title": "Are you schizophrenic? Test yourself!",
        "header_text": "Are you schizophrenic? Test yourself!",
    }
    return render_template(
        "pages/schizo_test.html", **context
    )


@app.route("/pages/book_review_jenna")
def book_review_jenna() -> str:
    context = {
        "title": "Book review: The adoration of Jenna Fox",
        "header_text": "Book review: The adoration of Jenna Fox",
    }
    return render_template(
        "pages/book_review_jenna.html", **context
    )


@app.route("/pages/google_user_parody")
def google_user_parody() -> str:
    context = {
        "title": "Things an average Google user once said",
        "header_text": "Things an average Google user once said",
    }
    return render_template(
        "pages/google_user_parody.html", **context
    )
