from datetime import datetime


# Kelvins-273.15 = Celsius
# Celsius = (Fahrenheit-32)/1.8


def temp_converter(value, input_unit, output_unit, accuracy=1):
    """
    Convert temperature unit from one metric system to another
    Supported systems celsius,kelvin,fahrenheit
    :param value: value
    :param input_unit: input metric system
    :param output_unit: output metric system
    :param accuracy: rounded to the decimal places
    :return: value after conversion to another metric system
    """
    try:
        value = float(value)
    except ValueError:
        value = value.replace(",", ".", 1)
        value = float(value)
    if input_unit == "kelvin" and output_unit == "celsius":
        return round(value - 273.15, accuracy)
    if input_unit == "celsius" and output_unit == "kelvin":
        return round(value + 273.15, accuracy)
    if input_unit == "fahrenheit" and output_unit == "celsius":
        return round((value - 32) / 1.8, accuracy)
    if input_unit == "celsius" and output_unit == "fahrenheit":
        return round((value * 1.8) + 32, accuracy)
    if input_unit == "kelvin" and output_unit == "fahrenheit":
        return round(value * 1.8 - 459.67, accuracy)
    if input_unit == "fahrenheit" and output_unit == "kelvin":
        return round((value + 459.67) * 5 / 9, accuracy)


def timestamp_to_date(timestamp, timezone=0, time_format="%H:%M:%S"):
    """
    Convert timestamp (number of seconds from 1.1.1970) to user friendly date format
    :param timestamp: number of seconds from 1.1.1970
    :param timezone: number of seconds whose should be add/delted to obtain local time
    :param time_format: define how output time should look like more info in https://strftime.org/
    """
    timestamp = int(timestamp) + timezone
    return datetime.utcfromtimestamp(timestamp).strftime(time_format)


class WeatherParser:

    def __init__(self, data):
        self.property = {}
        self.property["city_name"] = data["name"]
        self.property["country"] = data["sys"]["country"]
        self.property["temp"] = data["main"]["temp"]
        sunrise = data.get("sys", {}).get("sunrise")
        sunset = data.get("sys", {}).get("sunset")
        self.property["timezone"] = data.get("timezone")
        if sunrise is not None:
            self.property["sunrise"] = timestamp_to_date(sunrise, self.property["timezone"])
        else:
            self.property["sunrise"] = None
        if sunset is not None:
            self.property["sunset"] = timestamp_to_date(sunset, self.property["timezone"])
        else:
            self.property["sunset"] = None

    def temp_converter(self, input_unit="kelvin", output_unit="celsius", accuracy=1):
        """
           Convert temperature unit from one metric system to another
           Supported systems celsius,kelvin,fahrenheit
           :param input_unit: input metric system
           :param output_unit: output metric system
           :param accuracy: rounded to the decimal places
           """
        try:
            temperature = float(self.property["temp"])
        except ValueError:
            temperature = temperature.replace(",", ".", 1)
            temperature = float(temperature)
        if input_unit == "kelvin" and output_unit == "celsius":
            temperature = round(temperature - 273.15, accuracy)
        if input_unit == "celsius" and output_unit == "kelvin":
            temperature = round(temperature + 273.15, accuracy)
        if input_unit == "fahrenheit" and output_unit == "celsius":
            temperature = round((temperature - 32) / 1.8, accuracy)
        if input_unit == "celsius" and output_unit == "fahrenheit":
            temperature = round((temperature * 1.8) + 32, accuracy)
        if input_unit == "kelvin" and output_unit == "fahrenheit":
            temperature = round(temperature * 1.8 - 459.67, accuracy)
        if input_unit == "fahrenheit" and output_unit == "kelvin":
            temperature = round((temperature + 459.67) * 5 / 9, accuracy)

        self.property["temp"] = temperature

    def weather_data(self):
        return self.property
