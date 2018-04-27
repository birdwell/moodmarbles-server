# Construct the base Flask app
from flask import Flask

_BASE_APP = Flask(__name__)

def get_app():
    return _BASE_APP
