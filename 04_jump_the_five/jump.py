#!/usr/bin/env python3
"""
Author : schoubal <schoubal@localhost>
Date   : 2022-09-01
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    codedTxt = args.text

    jumper ={'1':'9','2':'8','3':'7','4':'6','5':'0','6':'4','7':'3','8':'2','9':'1','0':'5'}
#    for ch in codedTxt:
#        print(jumper.get(ch,ch), end='')
#    print('\r')

    ## list comprehension
#    print(''.join([jumper.get(ch,ch) for ch in codedTxt])) 

    ## string translate method
    print(codedTxt.translate(str.maketrans(jumper)))
# --------------------------------------------------
if __name__ == '__main__':
    main()
