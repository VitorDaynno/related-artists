from src.config.logger import logger


class Spotify():

    def __init__(self, request_helper, config):
        logger.info("Starting a spotify")
        self.__request_helper = request_helper
        self.__config = config

    def get_artist(self, artist_id):
        try:
            logger.info("Getting artist by id {0}".format(artist_id))
            url = self.__config.get_artist_url()
            artist = self.__request_helper.get(url)
            if artist is None:
                raise Exception("Artist not found")
            return artist
        except Exception as error:
            logger.error("An error occurred: {0}".format(error))
            raise error