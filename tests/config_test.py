import json
from pytest import raises
from Weather_app.configuration_loader import Config, create_base_config

CONTENT_OF_FALSE_CONF = json.dumps({"False_api_key": "random_word"})


def test_config_file_not_found():
    false_path = "false_config.json"
    with raises(FileNotFoundError):  # check if error was raised if config not exists
        Config(false_path).get_api_key()


def test_config_pass():  # checks the correctness of the configuration
    true_path = "config.json"
    assert Config(true_path).get_api_key()
    assert Config(true_path).get_temperature_unit()
    assert Config(true_path).get_secret_key()


def test_dont_containt_api_key(tmp_path):
    path = tmp_path / "test_dir"
    path.mkdir()
    conf_file = tmp_path / "config.json"
    conf_file.write_text(CONTENT_OF_FALSE_CONF)
    with raises(KeyError):
        Config(conf_file).get_api_key()


def test_base_config_creator(tmp_path):
    path = tmp_path / "base_conf"
    path.mkdir()
    path = tmp_path / "config.json"
    create_base_config(path)
    with open(path, "r") as file:
        json_dict = json.load(file)
    assert json_dict["api_key"]
    assert json_dict["secret_key"]
    assert json_dict["temp_unit"]
