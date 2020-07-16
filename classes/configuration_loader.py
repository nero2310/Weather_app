import json
import os

#toDO i guess may be problem with paths Linux and Windows write paths in diffrent way / vs \

def get_config_path(path):
    return os.path.realpath(path)


class CreateBaseConfig:
    def __init__(self, path_to_config_file):
        pass


class Config:
    """
    :arg
    Take path to Config file as argument
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

    def get_api_key(self):
        with open(get_config_path(self.config_file), "r") as file:
            conig_json = json.load(file)
            api_key = conig_json["api_key"]
        return api_key


conf = Config("../config.json")
