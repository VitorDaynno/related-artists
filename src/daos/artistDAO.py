import sys

from src.config.logger import logger


class ArtistDAO():

    def __init__(self, db_helper):
        logger.info("Starting a ArtistDAO")
        self.__db = db_helper

    def get_artists(self, filters):
        logger.info("Starting get artists")
        try:
            self.__db.open()
            artists = self.__db.find("artists", filters)
            return list(artists)
        except:
            error = sys.exc_info()
            logger.error('An error occurred: {error}'.format(error))
        finally:
            self.__db.close()