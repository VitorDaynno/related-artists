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