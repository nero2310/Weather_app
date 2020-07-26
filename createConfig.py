from Weather_app.configuration_loader import create_base_config

CONFIG_PATH = "config.json"

try:
    create_base_config(CONFIG_PATH)
except FileExistsError:
    print(f"File {CONFIG_PATH} already exist")



