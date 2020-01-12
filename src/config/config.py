import os
import sys
from dotenv import load_dotenv

from src.config.logger import logger


class Config:

    def __init__(self):
        logger.info("Starting Config")
        load_dotenv()

    def get_db_server(self):
        logger.info("Getting db's server for enviroment")
        DB_SERVER = os.getenv("DB_SERVER")
        if DB_SERVER is None:
            logger.error("DB_SERVER not found")
            sys.exit()
        else:
            logger.info("Get db's server with success")
            return DB_SERVER
    
    def get_db_port(self):
        logger.info("Getting db's port for enviroment")
        DB_PORT = os.getenv("DB_PORT")
        if DB_PORT is None:
            logger.error("DB_PORT not found")
            sys.exit()
        else:
            logger.info("Get db's port with success")
            return int(DB_PORT)

    def get_db_name(self):
        logger.info("Getting db's name for enviroment")
        DB_NAME = os.getenv("DB_NAME")
        if DB_NAME is None:
            logger.error("DB_NAME not found")
            sys.exit()
        else:
            logger.info("Get db's name with success")
            return DB_NAME
    
    def get_artist_url(self):
        logger.info("Getting artist's url for enviroment")
        ARTIST_URL = os.getenv("ARTIST_URL")
        if ARTIST_URL is None:
            logger.error("ARTIST_URL not found")
            sys.exit()
        else:
            logger.info("Get artist's url with success")
            return ARTIST_URL

    def get_related_artists_url(self):
        logger.info("Getting related artists's url for enviroment")
        RELATED_ARTISTS_URL = os.getenv("RELATED_ARTISTS_URL")
        if RELATED_ARTISTS_URL is None:
            logger.error("RELATED_ARTISTS_URL not found")
            sys.exit()
        else:
            logger.info("Get related artists's url with success")
            return RELATED_ARTISTS_URL

    def get_token(self):
        logger.info("Getting spotify's token for enviroment")
        SPOTIFY_TOKEN = os.getenv("SPOTIFY_TOKEN")
        if SPOTIFY_TOKEN is None:
            logger.error("SPOTIFY_TOKEN not found")
            sys.exit()
        else:
            logger.info("Get spotify's token with success")
            return SPOTIFY_TOKEN