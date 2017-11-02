# -*- coding: utf-8 -*-
"""
main function
"""
import sys
import argparse
from glacierclient.glacier import Glacier

VERSION = '0.0.1'

def option():
    """
    Command line options
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version', version='%s' % VERSION)
    parser.add_argument('command', metavar='command', type=str)

    args = parser.parse_args()
    return args

def main():
    """
    main function
    """
    glacier = Glacier()

    args = option()
    command = args.command
    if command == 'create-vault':
        glacier.create_vault()
    else:
        sys.exit('%s is undefind!' % command)

if __name__ == "__main__":
    main()
