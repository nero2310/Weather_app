from pytest import raises
import requests
from classes.weather_api import CurrentWeather
from classes.configuration_loader import Config
from classes.exceptions import UnsafeAdress

API_KEY = Config("config.json").get_api_key() # You need to have you own api key to run tests


def test_connection():
    assert (CurrentWeather(API_KEY, "Warsaw")).make_request()


def test_invalid_api_key():
    with raises(requests.HTTPError):
        CurrentWeather("invalid_api_key", "Warsaw").make_request()


def test_http_use():
    with raises(UnsafeAdress):
        CurrentWeather(API_KEY, "Warsaw", allow_http=False,
                       api_link="http://api.openweathermap.org/data/2.5/weather?q={}&appid={}")


def test_http_use_with_user_permission():
    assert (CurrentWeather(API_KEY, "Warsaw", allow_http=True,
                           api_link="http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"))


def test_api_http():
    assert (CurrentWeather(API_KEY,"Warsaw",allow_http=False,
            api_link="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"))


def test_country():
    assert (CurrentWeather(API_KEY,city_name="Warsaw", country="pl").api_link
            == "https://api.openweathermap.org/data/2.5/weather?q=Warsaw,None,pl&appid={}".format(API_KEY))
