import json
import os.path
from typing import Dict, List
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

    def get_api_key(self):
        with open(get_config_path(self.config_file), "r") as file:
            conig_json = json.load(file)
            api_key = conig_json["api_key"]
        return api_key


