#!/usr/bin/env python3
"""
Author : schoubal <schoubal@localhost>
Date   : 2022-10-04
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import io

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

    text = textOrFile 
    if os.path.isfile(text):
        #text = open(textOrFile).read().rstrip()
        text = open(text)
    else:
        ## https://stackoverflow.com/questions/65005261/passing-a-string-with-spaces-and-newlines-as-command-line-argument-python
        ## newline \n  not recognized in text stream by StringIO as Python escapes \n in command line args as \\n
        text = text.replace('\\n', '\n')
        text = io.StringIO(text)

    fh = sys.stdout
    if fileName != '':
        fh = open(fileName, 'wt')
    #print(text.upper(), file=fh)

    # str.rstrip([chars])
    # Return a copy of the string with trailing characters removed. 
    # str.strip([chars])
    # Return a copy of the string with the leading and trailing characters removed. 
    # The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace.
    for line in text:
        print(line.strip("\n").upper(), file=fh)

    if fileName != '':
        fh.close()
# --------------------------------------------------
if __name__ == '__main__':
    main()
