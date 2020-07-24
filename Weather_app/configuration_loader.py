import json
import os.path
from pathlib import Path


# toDO i guess may be problem with paths Linux and Windows write paths in different way / vs \


def get_config_path(path_to_config):
    return os.path.realpath(path_to_config)


def create_base_config(path_to_config, content={"api_key": "sample_key"}):
    path_to_config = Path(path_to_config)
    content = json.dumps(content, indent=4)
    if path_to_config.exists():
        raise FileExistsError
    else:
        with open(path_to_config, "w") as file:
            file.write(content)


class Config:
    """
    :arg
    Take path to config file as argument
    """

    def __init__(self, path_to_config_file):
        try:
            self.config_file = path_to_config_file
        except FileNotFoundError:
            print("Error there is not Config file")
            raise FileNotFoundError
        except KeyError:
            print("There was not api_key in Config file")
            raise KeyError
        with open(get_config_path(self.config_file), "r") as file:
            config_json = json.load(file)
            self.api_key = config_json[
                "api_key"
            ]  # I don't catch exception, because program have to have api_key to work
            self.temp_unit = config_json["temp_unit"]

    def get_api_key(self):
        return self.api_key

    def get_temperature_unit(self):
        return self.temp_unit

