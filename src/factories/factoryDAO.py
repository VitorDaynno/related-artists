from src.config.logger import logger
from src.daos.artistDAO import ArtistDAO
from src.helpers.db import DBHelper


class FactoryDAO():

    def __init__(self):
        logger.info('Starting a FactoryDAO')
        self.__db_helper = DBHelper()
    
    def get_artist(self):
        logger.info('Getting a artistDAO')
        db_helper = self.__db_helper
        return ArtistDAO(db_helper)