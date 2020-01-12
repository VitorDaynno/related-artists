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
        except Exception as error:
            logger.error("An error occurred: {0}".format(error))
            raise error
        finally:
            self.__db.close()
    
    def save(self, artist):
        logger.info("Starting save artist")
        try:
            self.__db.open()
            artists = self.__db.save("artists", artist)
            return artists
        except Exception as error:
            logger.error("An error occurred: {0}".format(error))
            raise error
        finally:
            self.__db.close()

    def get_spotify_ids(self):
        logger.info("Starting get spotify's ids")
        try:
            self.__db.open()
            ids = self.__db.distinct("artists", "spotify_id")
            return list(ids)
        except Exception as error:
            logger.error("An error occurred: {0}".format(error))
            raise error
        finally:
            self.__db.close()