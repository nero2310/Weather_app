from flask import Flask,render_template, request, redirect, url_for
from json import loads,dumps
from classes.exceptions import UnsafeAdress

from classes.json_parser import temp_converter,WeatherParser
from classes.configuration_loader import Config
from classes.weather_api import CurrentWeather
from forms import GetWeatherForm

conf = Config("config.json")
api_key = conf.get_api_key()

app = Flask(__name__)

app.config['SECRET_KEY'] = "9296e2354cf9eb6b4a52ca8be963c67a"


@app.route("/")
def hello_word():
    return "Hello, World"


@app.route("/weather", methods=["POST", "GET"])
def get_weather():
    form = GetWeatherForm()
    if request.method == "POST":
        city = request.form["city_name"]
        country = request.form.get("country", "None")
        return redirect(url_for("weather_summary"), code=307)  # code 307 force using POST instead of GET
    return render_template("weather_form.html", form=form)


@app.route("/weather_data", methods=["POST","GET"])
def weather_summary(city=None, country=None):
    if request.method == "POST":
        city = request.form["city_name"]
        country = request.form.get("country")
        weather_data = CurrentWeather(api_key, city, state_code=None, country=country).make_request().json()
        parser = WeatherParser(weather_data)
        parser.temp_converter()
        weather_data = parser.data()
        return render_template("weather.html", weather=weather_data)
    else:
        return redirect(url_for("get_weather")) # It will redirect user if he try to go to /weather_data manually


@app.errorhandler(UnsafeAdress)
def unsafe_adress_exception(UnsafeAdress):
    return render_template("not_safe_adress_exception.html")


# @app.errorhandler(Exception)  # this will catch all not caught exceptions
# def unexpected_exception(Exception):
#     return render_template("unexpected_exception.html")


app.run(debug=True,host="0.0.0.0")  # run flask server
