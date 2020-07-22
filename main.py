from flask import Flask, jsonify,render_template

# from classes.configuration_loader import Config
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
    return render_template("weather.html",content=weather_data)

@app.route("/weather/<city>/<country>")
def weather_city_country(city,country):
    weather_data = CurrentWeather(api_key,city,country=country).make_request()
    return jsonify(weather_data.json())

app.run(debug=True)  # run flask server
