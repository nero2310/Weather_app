from flask import Flask,jsonify
from classes.configuration_loader import Config
from classes.weather_api import CurrentWeather


conf = Config("config.json")
api_key = conf.get_api_key()


app = Flask(__name__)


@app.route('/')
def hello_word():
    return 'Hello, World'


@app.route("/weather")
def get_weather():
    weather = CurrentWeather(api_key,"Kraków").make_request()
    return jsonify(weather.json())


app.run(debug=True)  # run flask server
