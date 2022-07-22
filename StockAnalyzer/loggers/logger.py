import logging
from datetime import datetime as dt
import os


def logfile():
    if not os.path.exists('./logs/{}_log.log'.format(dt.strftime(dt.now(),'%Y-%m-%d'))):
        open('./logs/{}_log.log'.format(dt.strftime(dt.now(),'%Y-%m-%d')),'w')

def log(statement,level):
    logfile()
    logging.basicConfig(filename='./logs/{}_log.log'.format(dt.strftime(dt.now(),'%Y-%m-%d')))
    if level == 'DEBUG':
        logging.debug(statement)
    elif level == 'WARN':
        logging.warning(statement)
    elif level == 'INFO':
        logging.info(statement)
    elif level == 'ERROR':
        logging.error(statement)
    else:
        logging.log(0,statement)