import logging


logger = logging.getLogger("Related-artists")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(("%(asctime)s - %(name)s - %(levelname)s -"
                               "[%(filename)s] %(message)s"))
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)