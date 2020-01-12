from pymongo import MongoClient

from src.config.logger import logger
from src.config.config import Config


class DBHelper():

    def __init__(self):
        logger.info('Starting DBHelper')
        self.__config = Config()

    def open(self):
        SERVER = self.__config.get_db_server()
        PORT = self.__config.get_db_port()
        NAME = self.__config.get_db_name()
        self.__client = MongoClient(SERVER, PORT)
        self.__db = self.__client[NAME]

    def find(self, collection_name, filters):
        collection = self.__db[collection_name]
        registries = collection.find(filters)
        return registries

    def save(self, collection_name, artist):
        collection = self.__db[collection_name]
        result = collection.save(artist)
        return result

    def distinct(self, collection_name, field):
        collection = self.__db[collection_name]
        registries = collection.distinct(field)
        return registries

    def close(self):
         self.__client.close()