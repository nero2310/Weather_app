from flask import Flask, render_template, request, redirect, url_for

from Weather_app.exceptions import UnsafeAddress,CityNotFoundOrApiNotResponse
from Weather_app.json_parser import WeatherParser
from Weather_app.configuration_loader import Config
from Weather_app.weather_api import CurrentWeatherApi
from forms import GetWeatherForm, NavbarForm

conf = Config("config.json")
api_key = conf.get_api_key()
metric_system = conf.get_temperature_unit()

app = Flask(__name__)

app.config['SECRET_KEY'] = "9296e2354cf9eb6b4a52ca8be963c67a"  # toDo change it before run in production


@app.route("/")
def hello_word():
    navbar_form = NavbarForm()
    return render_template("main_site.html", navbar_form=navbar_form)


@app.route("/weather", methods=["POST", "GET"])
def get_weather():
    form = GetWeatherForm()
    navbar_form = NavbarForm()
    return render_template("weather_form.html", form=form, navbar_form=navbar_form)


@app.route("/weather_data", methods=["POST", "GET"])
def weather_summary():
    if request.method == "POST":
        city = request.form["city_name"]
        country = request.form.get("country")
        weather_dict = CurrentWeatherApi(api_key, city, state_code=None, country=country).make_request().json()
        parser = WeatherParser(weather_dict, accuracy=1)
        weather_dict = parser.weather_data()
        return render_template("weather.html", weather=weather_dict)
    else:
        return redirect(url_for("get_weather"))  # It will redirect user if he try to go to /weather_data manually


@app.errorhandler(UnsafeAddress)
def unsafe_address_exception(UnsafeAddress):
    return render_template("error_pages/not_safe_adress_exception.html")


@app.errorhandler(404)
def page_not_found():
    return render_template("error_pages/404_exception.html"), 404


@app.errorhandler(CityNotFoundOrApiNotResponse)
def city_not_found(CityNotFoundOrApiNotResponse):
    return render_template("error_pages/city_not_found_exception.html")

# @app.errorhandler(Exception)  # this will catch all not caught exceptions
# def unexpected_exception(Exception):
#     return render_template("unexpected_exception.html")


app.run(debug=True, host="0.0.0.0")  # run flask server
