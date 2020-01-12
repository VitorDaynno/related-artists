from src.factories.factory import Factory
from src.helpers.file import FileHelper
from src.config.logger import logger


def init():
    file_helper = FileHelper()

    file_helper.open("to_process", "r")
    to_process = file_helper.get_lines()
    file_helper.close()

    process(to_process)

def process(to_process):
    logger.info('Started process')
    factory = Factory()
    spotify = factory.get_spotify()
    artist_controller = factory.get_artist()
    artist_id = ""
    while len(to_process) > 0:
        try:
            id = to_process.pop(0)
            artist_id = format(id)
            processeds = artist_controller.get_spotify_ids()
            if artist_id not in processeds:
                artist = spotify.get_artist(artist_id)
                related_artists = spotify.get_related_artists(artist_id)
                artist["related_artists"] = related_artists
                artists = find_non_existent_items(to_process, related_artists)
                to_process.extend(artists)
                artist_controller.save(artist)
        except Exception as error:
            logger.error("An error occurred: {0}".format(error))
            to_process.append(artist_id)
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

def find_non_existent_items(list, items):
    non_existent_items = []
    for item in items:
        if item not in list:
            non_existent_items.append(item)
    return non_existent_items

init()
