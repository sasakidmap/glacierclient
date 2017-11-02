# -*- coding: utf-8 -*-
"""
main function
"""

from glacierclient.glacier import Glacier

def main():
    """
    main function
    """
    glacier = Glacier()
    glacier.create_vault()

if __name__ == "__main__":
    main()
