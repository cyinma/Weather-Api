from pymongo.collection import Collection
import pymongo
from db import mongo
from utils import logging
from models.weather import WeatherRecord

collection: Collection


def init():
    global collection
    collection = mongo.db["weather"]
    logging.logger.info(f"located collection weather")


def get_latest_by_city(city: str):
    result = collection.find_one({
        "location": city
    }, sort=[("timestamp", pymongo.DESCENDING)])

    return WeatherRecord.from_dict(result)
