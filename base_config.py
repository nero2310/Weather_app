from Weather_app.configuration_loader import create_base_config
from os import path

path_to_config = "config2.json"


if not path.exists(path_to_config):  # create base config if config file doesn't exist
    create_base_config(path_to_config)
