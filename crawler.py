from src.factories.factory import Factory
from src.helpers.file import FileHelper
from src.config.logger import logger

def init():
    factory = Factory()
    file_helper = FileHelper()

    artist = factory.get_artist()
    file_helper.open("to_process", "r")

    processeds = artist.get_spotify_ids()
    to_process = file_helper.get_lines()
    file_helper.close()

    process(to_process, processeds)

def process(to_process, processeds):
    logger.info('Started process')
    factory = Factory()
    spotify = factory.get_spotify()
    artist_controller = factory.get_artist()
    while len(to_process) > 0:
        try:
            id = to_process.pop()
            artist_id = format(id)
            if artist_id not in processeds:
                artist = spotify.get_artist(artist_id)
                related_artists = spotify.get_related_artists(artist_id)
                artist["related_artists"] = related_artists
                to_process.extend(related_artists)
                artist_controller.save(artist)
        except Exception as error:
            logger.error("An error occurred: {0}".format(error))
            break
    save_to_process(to_process)

def format(artist_id):
    return artist_id.replace("\n", "")

def save_to_process(to_process):
    file_helper = FileHelper()
    file_helper.open("to_process", "w")
    
    for item in to_process:
        file_helper.write(item)

    file_helper.close()

init()
