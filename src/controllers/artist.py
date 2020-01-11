import sys

from src.config.logger import logger


class Artist:

    def __init__(self, dao):
        logger.info("Started a Artist")
        self.dao = dao

    def get_artists(self):
        logger.info("Started get artists")
        try:
            artists = self.dao.get_artists({})
            return artists
        except:
            error = sys.exc_info()
            logger.error("An error occurred: {0}".format(error))
