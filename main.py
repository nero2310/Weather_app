from flask import Flask, jsonify

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
def weather(city):
    weather_data = CurrentWeather(api_key, city).make_request()
    return jsonify(weather_data.json())


app.run(debug=True)  # run flask server
