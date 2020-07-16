from flask import Flask
from classes.configuration_loader import Config

app = Flask(__name__)


@app.route('/')
def main_page():
    return 'Hello, World'


# app.run(debug=True) # run flask server

conf = Config("config.json")
api_key = conf.get_api_key()
print(api_key)
