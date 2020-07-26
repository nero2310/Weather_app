from pytest import raises

from Weather_app.weather_api import CurrentWeatherApi
from Weather_app.configuration_loader import Config
from Weather_app.exceptions import UnsafeAddress, CityNotFoundOrApiNotResponse

API_KEY = Config(
    "config.json"
).get_api_key()  # You need to have you own api key to run tests


def test_connection():
    assert (CurrentWeatherApi(API_KEY, "Warsaw")).make_request()


def test_invalid_api_key():
    with raises(CityNotFoundOrApiNotResponse):
        CurrentWeatherApi("invalid_api_key", "Warsaw").make_request()


def test_http_use():
    with raises(UnsafeAddress):
        CurrentWeatherApi(
            API_KEY,
            "Warsaw",
            allow_http=False,
            api_link="http://api.openweathermap.org/data/2.5/weather?q={0}&appid={3}",
        )


def test_http_use_with_user_permission():
    assert (
            CurrentWeatherApi(
                API_KEY,
                "Warsaw",
                allow_http=True,
                api_link="http://api.openweathermap.org/data/2.5/weather?q={0}&appid={3}",
            ).api_link
            == f"http://api.openweathermap.org/data/2.5/weather?q=Warsaw&appid={API_KEY}"
    )


def test_api_http():
    assert CurrentWeatherApi(
        API_KEY,
        "Warsaw",
        allow_http=False,
        api_link="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}",
    )


def test_country():  # https://realpython.com/python-f-strings/
    assert (
            CurrentWeatherApi(API_KEY, city_name="Warsaw", country="pl").api_link
            == f"https://api.openweathermap.org/data/2.5/weather?q=Warsaw,None,pl&appid={API_KEY}"
    )
    assert (
            CurrentWeatherApi(API_KEY, city_name="Moscow", country="ru").api_link
            == f"https://api.openweathermap.org/data/2.5/weather?q=Moscow,None,ru&appid={API_KEY}"
    )


def test_two_part_city_name():
    assert CurrentWeatherApi(API_KEY, city_name="New York").make_request()
