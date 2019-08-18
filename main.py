from flask import Flask
from controllers import weather
from configs import config
from db import mongo
from utils import logging
from dao import weatherdao


if __name__ == '__main__':

    config.init()
    logging.init()
    mongo.init()

    weatherdao.init()

    logging.logger.info("Successfully Started")
    logging.logger.info(f"target mongo host: {config.get_string('mongodb', 'uri')}")

    config.reset()

    app = Flask(__name__)
    app.register_blueprint(weather.app)
    app.run(port=8080, debug=True)


