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
            url = "{0}{1}".format(url, artist_id)
            response = self.__request_helper.get(url)
            if response is None:
                raise Exception("Artist not found")
            artist = {
                "spotify_id": response["id"],
                "name": response["name"]
            }
            
            return artist
        except Exception as error:
            logger.error("An error occurred: {0}".format(error))
            raise error
    
    def get_related_artists(self, artist_id):
        try:
            logger.info("Getting relateds artist by id {0}".format(artist_id))
            url = self.__config.get_related_artists_url()
            url = url.format(artist_id)
            response = self.__request_helper.get(url)
            if response is None:
                raise Exception("Related artists not found")
            related_artists_ids = []
            for artist in response["artists"]:
                related_artists_ids.append(artist["id"]) 
            return related_artists_ids
        except Exception as error:
            logger.error("An error occurred: {0}".format(error))
            raise error