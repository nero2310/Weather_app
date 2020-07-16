import json
import os


def get_config_path(path):
    return os.path.realpath(path)


class CreateBaseConfig:
    pass


class Config:
    """
    :arg
    Take path to Config file as argument
    """

    def __init__(self, path_to_config_file):
        self.config_file = path_to_config_file

    def get_api_key(self):
        try:
            with open(get_config_path(self.config_file), "r") as file:
                conig_json = json.load(file)
                api_key = conig_json["api_key"]
            return api_key
        except FileNotFoundError:
            print("Error there is not Config file")
        except KeyError:
            print("There was not api_key in Config file")
