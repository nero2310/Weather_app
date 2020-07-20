import pytest

from classes.json_parser import temp_converter


def test_kelvins_to_cel():
    assert temp_converter(10, "celsius", "fahrenheit") == 50
    assert temp_converter(10, "fahrenheit", "celsius") == -12.22
    assert temp_converter(10, "celsius", "kelvin") == 283.15
    assert temp_converter(10, "kelvin", "celsius") == -263.15
    assert temp_converter(10, "kelvin", "fahrenheit") == -441.67
    assert temp_converter(10, "fahrenheit", "kelvin") == 260.93
