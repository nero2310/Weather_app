from pytest import raises
import requests
from classes.weather_api import CurrentWeather
from classes.configuration_loader import Config
from classes.exceptions import UnsafeAdress

API_KEY = Config("config.json").get_api_key()


def test_connection():
    assert (CurrentWeather(API_KEY, "Warsaw")).make_request()


def test_invalid_api_key():
    with raises(requests.HTTPError):
        CurrentWeather("invalid_api_key", "Warsaw").make_request()


def test_http_use():
    with raises(UnsafeAdress):
        CurrentWeather(API_KEY, "Warsaw", allow_http=False,
                       api_link="http://api.openweathermap.org/data/2.5/weather?q={}&appid={}")
