from flask import Blueprint, jsonify
from models.weather import Location, location_list
from dao import weatherdao
from exceptions.errors import *


app = Blueprint('app', __name__, template_folder='templates')


@app.route("/")
def root():
    return "Hello, World!"


@app.route("/api/v1/weather/<string:city>/current")
def current_by_location(city: str):
    if not (city.upper() in location_list):
        return entity_not_found("city")

    city = Location[city.upper()].name
    result = weatherdao.get_latest_by_city(city)
    return jsonify(result)

