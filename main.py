from flask import Flask, jsonify, render_template
from classes.exceptions import UnsafeAdress

from classes.configuration_loader import Config
from classes.weather_api import CurrentWeather

conf = Config("config.json")
api_key = conf.get_api_key()

app = Flask(__name__)


@app.route("/")
def hello_word():
    return "Hello, World"


@app.route("/weather")
def get_weather():
    weather_data = CurrentWeather(api_key, "Sydney", country="CA").make_request()
    return jsonify(weather_data.json())


@app.route("/weather/<city>")
def weather_city(city):
    weather_data = CurrentWeather(api_key, city).make_request().json()
    weather_data["cod"]
    return render_template("weather.html", content=weather_data)


@app.route("/weather/<city>/<country>")
def weather_city_country(city, country):
    weather_data = CurrentWeather(api_key, city, country=country).make_request()
    return jsonify(weather_data.json())


@app.errorhandler(UnsafeAdress)
def unsafe_adress_exception(UnsafeAdress):
    return render_template("not_safe_adress_exception.html")


@app.errorhandler(Exception)  # this will catch all not caught exceptions
def unexpected_exception(Exception):
    return render_template("unexpected_exception.html")


app.run(debug=True)  # run flask server
