import os
import sys
import logging
from logging.handlers import RotatingFileHandler

LOG_FILENAME = 'sudoku_solver.log'  # log filename


def create_logger(path, level=logging.INFO):

    fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    date_fmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter(fmt, datefmt=date_fmt)

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    if not os.path.exists(path):
        os.makedirs(path)

    # Max 10 files of 100MB
    fileHandler = RotatingFileHandler(
        os.path.join(
            path,
            LOG_FILENAME),
        maxBytes=104857600,
        backupCount=10)
    fileHandler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.addHandler(handler)
    logger.addHandler(fileHandler)
    logger.setLevel(level)
    return logger
