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


class WeatherParser:

    def __init__(self, data):
        self.property = {}
        self.property["temp"] = data["main"]["temp"]
        self.property["city_name"] = data["name"]
        self.property["country"] = data["country"]
        self.property["sunrise"] = data.get("sunrise")
        self.property["sunset"] = data.get("sunset")

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

    def timestamp_to_date(self, timestamp, time_format="%H:%M:%S", timezone=0):
        """
        Convert timestamp (number of seconds from 1.1.1970) to user friendly date format
        :param timestamp:
        :param timezone:
        :param time_format:
        :return:
        """
        timestamp = int(timestamp)+timezone
        return datetime.utcfromtimestamp(timestamp).strftime(time_format)

    def data(self):
        return self.property
