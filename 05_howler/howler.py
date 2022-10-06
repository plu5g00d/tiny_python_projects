#!/usr/bin/env python3
"""
Author : schoubal <schoubal@localhost>
Date   : 2022-10-04
Purpose: Rock the Casbah
"""

import argparse
import sys
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file name',
                        metavar='str',
                        type=str,
                        default='')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    fileName = args.outfile
    textOrFile = args.text

    #print(f'str_arg = "{str_arg}"')
    #print(f'positional = "{pos_arg}"')

    text = textOrFile
    if os.path.isfile(textOrFile):
        text = open(textOrFile).read().rstrip()

    fh = sys.stdout
    if fileName != '':
        fh = open(fileName, 'wt')
        #fh.write(text.upper())
        #fh.write("\n")
        #fh.close()
    #else:
        #print(text.upper())
    print(text.upper(), file=fh)

    if fileName != '':
        fh.close()
# --------------------------------------------------
if __name__ == '__main__':
    main()
