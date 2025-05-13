import json

from flask import Flask, jsonify


app = Flask(__name__)


def load_data():
    with open('client_data.json', 'r') as file:
        data = json.load(file)
    return data


