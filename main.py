from flask import Flask, jsonify, render_template, request, redirect, url_for
from classes.exceptions import UnsafeAdress

from classes.json_parser import temp_converter
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
        print(city)
        return redirect(url_for("weather_city", city=city))
    return render_template("weather_form.html", form=form)


@app.route("/weather_data/<city>", methods=["POST","GET"])
def weather_city(city):
    weather_data = CurrentWeather(api_key, city).make_request().json()
    weather_data["main"]["temp"] = temp_converter(weather_data["main"]["temp"], "kelvin", "celsius")
    weather_data["main"]["temp_max"] = temp_converter(weather_data["main"]["temp_max"], "kelvin", "celsius")
    weather_data["main"]["temp_min"] = temp_converter(weather_data["main"]["temp_min"], "kelvin", "celsius")
    return render_template("weather.html", content=weather_data)


@app.route("/weather/<city>/<country>")
def weather_city_country(city, country):
    weather_data = CurrentWeather(api_key, city, country=country).make_request()
    return jsonify(weather_data.json())


@app.errorhandler(UnsafeAdress)
def unsafe_adress_exception(UnsafeAdress):
    return render_template("not_safe_adress_exception.html")


# @app.errorhandler(Exception)  # this will catch all not caught exceptions
# def unexpected_exception(Exception):
#     return render_template("unexpected_exception.html")


app.run(debug=True)  # run flask server
