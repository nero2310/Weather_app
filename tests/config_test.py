from pytest import raises
from classes.configuration_loader import Config


def test_config_file_not_found():
    false_path = "false_config.json"
    with raises(FileNotFoundError):
        Config(false_path).get_api_key()


def test_config_pass():
    true_path = "config.json"
    assert Config(true_path).get_api_key()

