# -*- coding: utf-8 -*-
"""
main function
"""

from glacierclient.glacier import Glacier
from glacierclient import logger

def main():
    """
    main function
    """
    logger.debug('--- main start ---')
    glacier = Glacier()
    glacier.create_vault()
    logger.debug('--- main  end  ---')

if __name__ == "__main__":
    main()
