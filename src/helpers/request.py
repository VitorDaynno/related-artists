import requests
import sys

from src.config.logger import logger
from src.config.config import Config


class RequestHelper:

    def __init__(self):
        self.__config = Config()
        logger.info("Initialize RequestHelper")

    def get(self, url):
        try:
            logger.info("Started get")
            token = self.__config.get_token()
            header = {
                "Authorization": "Bearer {0}".format(token)
            }

            response = requests.get(url, headers=header)

            if response.status_code != 200:
                raise Exception(response.content)

            return response.json()
        except:
            error = sys.exc_info()
            logger.error("An error occurred: {0}".format(error))