from src.factories.factory import Factory
from src.helpers.file import FileHelper
from src.config.logger import logger

def init():
    factory = Factory()
    file_helper = FileHelper()

    artist = factory.get_artist()
    file_helper.open("to_processed", "r")

    processeds = artist.get_artists()
    to_processed = file_helper.get_lines()

    process(to_processed, processeds)

    file_helper.close()

def process(to_processed, processeds):
    logger.info('Started process')
    factory = Factory()
    spotify = factory.get_spotify()
    while len(to_processed) > 0:
        try:
            id = to_processed.pop()
            artist_id = format(id)
            if artist_id not in processeds:
                artist = spotify.get_artist(artist_id)
                print(artist)
        except Exception as error:
            logger.error("An error occurred: {0}".format(error))
            break

def format(artist_id):
    return artist_id.replace("\n", "")


init()
