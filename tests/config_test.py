import json
from pytest import raises
from Weather_app.configuration_loader import Config, create_base_config

CONTENT_OF_FALSE_CONF = json.dumps({"False_api_key": "random_word"})


def test_config_file_not_found():
    false_path = "false_config.json"
    with raises(FileNotFoundError):
        Config(false_path).get_api_key()


def test_config_pass():
    true_path = "config.json"
    assert Config(true_path).get_api_key()


def test_dont_containt_api_key(tmp_path):
    path = tmp_path / "test_dir"
    path.mkdir()
    conf_file = tmp_path / "config.json"
    conf_file.write_text(CONTENT_OF_FALSE_CONF)
    with raises(KeyError):
        Config(conf_file).get_api_key()


def test_create_base_conf(tmp_path):
    path = tmp_path / "test_dir"
    path.mkdir()
    path = tmp_path / "config.json"
    assert create_base_config(path) is None


def test_data_visability():  # toDO create config whose will decide data is printed to website or not
    assert True == False
