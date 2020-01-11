from src.factories.factory import Factory
from src.helpers.file import FileHelper

factory = Factory()
file_helper = FileHelper()

artist = factory.get_artist()
spotify = factory.get_spotify()
file_helper.open('to_processed', 'a+')

PROCESSEDS = artist.get_artists()
TO_PROCESSED = file_helper.get_lines()

file_helper.close()
