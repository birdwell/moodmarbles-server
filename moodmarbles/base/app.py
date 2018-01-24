from flask import Flask

_BASE_APP = Flask(__name__)

def get_app():
    return _BASE_APP
