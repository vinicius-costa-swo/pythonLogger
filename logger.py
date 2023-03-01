#Importing Libraries
import logging
import socket
import json

#Fetching Hostname
logger = logging.getLogger(socket.gethostname())

class logger_config:
    def debug(debug):
        debug = json.loads(debug)
        logger = logging.getLogger(socket.gethostname())
        formatter = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s')
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        if not logger.handlers:
            logger.addHandler(handler)
        if debug:
            logger.setLevel(logging.DEBUG)
        if not debug:
            logger.setLevel(logging.INFO)
        logger.propagate = False
                          
    

class log:
    def INFO(x):
        logger.info(x)
    def DEBUG(x):
        logger.debug(x)
    def WARNING(x):
        logger.warning(x)
    def CRITICAL(x):
        logger.critical(x)     

       

