from src.config.logger import logger
from src.factories.factoryDAO import FactoryDAO
from src.controllers.artist import Artist
from src.controllers.spotify import Spotify
from src.helpers.request import RequestHelper
from src.config.config import Config


class Factory:

    def __init__(self):
        logger.info("Starting a Factory")
        self.__factory_dao = FactoryDAO()
        self.__request_helper = RequestHelper()
        self.__config = Config()

    def get_artist(self):
        logger.info("Getting a artist")
        dao = self.__factory_dao.get_artist()
        artist = Artist(dao)
        return artist

    def get_spotify(self):
        logger.info("Getting a spotify")
        request_helper = self.__request_helper
        config = self.__config

        spotify = Spotify(request_helper, config)
        return spotify
