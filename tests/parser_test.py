from Weather_app.json_parser import temp_converter
from Weather_app.json_parser import WeatherParser

weather_to_parse = {"main": {"temp": 200}, "name": "Warsaw", "sys": {"country": "Poland"}}


# Example how test dictionary should look like for WeatherParser
# self.property["temp"] = data["main"]["temp"]
# self.property["city_name"] = data["name"]
# self.property["country"] = data["country"]
# self.property["sunrise"] = data.get("sunrise")
# self.property["sunset"] = data.get("sunset")


def test_kelvins_to_cel():
    assert temp_converter(10, "celsius", "fahrenheit", accuracy=2) == 50
    assert temp_converter(10, "fahrenheit", "celsius", accuracy=2) == -12.22
    assert temp_converter(10, "celsius", "kelvin", accuracy=2) == 283.15
    assert temp_converter(10, "kelvin", "celsius", accuracy=2) == -263.15
    assert temp_converter(10, "kelvin", "fahrenheit", accuracy=2) == -441.67
    assert temp_converter(10, "fahrenheit", "kelvin", accuracy=2) == 260.93
    assert temp_converter("1,2", "celsius", "fahrenheit", accuracy=2) == 34.16


def test_temp_parser():
    dictonary = WeatherParser(weather_to_parse)
    assert dictonary.weather_data()["temp"] == -73.1


def test_country_names_conversion():  # toDO convert country shortcut to full country name
    assert False == True
