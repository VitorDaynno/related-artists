import sys

from src.config.logger import logger


class Artist:

    def __init__(self, dao):
        logger.info("Started a Artist")
        self.__dao = dao

    def get_artists(self):
        logger.info("Started get artists")
        try:
            artists = self.__dao.get_artists({})
            return artists
        except:
            error = sys.exc_info()
            logger.error("An error occurred: {0}".format(error))

    def save(self, artist):
        logger.info("Started save artist")
        try:
            self.__dao.save(artist)
        except Exception as error:
            logger.error("An error occurred: {0}".format(error))
            raise error
    
    def get_spotify_ids(self):
        logger.info("Started get spotify's ids")
        try:
            ids = self.__dao.get_spotify_ids()
            return ids
        except:
            error = sys.exc_info()
            logger.error("An error occurred: {0}".format(error))