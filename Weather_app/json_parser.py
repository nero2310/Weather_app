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
    :param timezone: number of seconds whose should be add/deleted to obtain local time
    :param time_format: define how output time should look like more info in https://strftime.org/
    """
    if timestamp is not None:
        timestamp = int(timestamp) + timezone
        return datetime.utcfromtimestamp(timestamp).strftime(time_format)
    else:
        return None


class WeatherParser:
    """
    This class adjust data to send to client
    :arg data weather data in json/dict
    """

    def __init__(self, data, temp_input_system="kelvin", temp_output_system="celsius", accuracy=1):
        self.property = {}
        self.property["city_name"] = data["name"]
        self.property["country"] = data["sys"]["country"]
        self.property["temp"] = self.temp_converter(data["main"]["temp"], temp_input_system, temp_output_system,
                                                    accuracy)
        sunrise = data.get("sys", {}).get("sunrise")
        sunset = data.get("sys", {}).get("sunset")
        self.property["timezone"] = data.get("timezone")
        self.property["sunrise"] = timestamp_to_date(sunrise, self.property["timezone"])
        self.property["sunset"] = timestamp_to_date(sunset, self.property["timezone"])

    def temp_converter(self, value, input_unit="kelvin", output_unit="celsius", accuracy=1):
        """
           Convert temperature unit from one metric system to another
           Supported systems celsius,kelvin,fahrenheit
           :param value: temperature value
           :param input_unit: input metric system
           :param output_unit: output metric system
           :param accuracy: rounded to the decimal places
           """
        try:
            temperature = float(value)
        except ValueError:
            temperature = str(value).replace(",", ".", 1)  # float will not convert numbers with , separators to float
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

        return temperature

    def weather_data(self):
        return self.property
