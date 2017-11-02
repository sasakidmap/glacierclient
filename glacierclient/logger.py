# -*- coding: utf-8 -*-

"""
logger
"""

from logging import getLogger
from termcolor import colored

def debug(msg):
    """
    debug
    """
    msg = colored('debug: ' + msg, 'blue')
    logger = getLogger(__name__)
    logger.debug(msg)

def info(msg):
    """
    infomation
    """
    msg = colored('info: ' + msg, 'green')
    logger = getLogger(__name__)
    logger.info(msg)

def warn(msg):
    """
    warring
    """
    msg = colored('warn: ' + msg, 'yellow')
    logger = getLogger(__name__)
    logger.warn(msg)

def error(msg):
    """
    error
    """
    msg = colored('error: ' + msg, 'red')
    logger = getLogger(__name__)
    logger.error(msg)
