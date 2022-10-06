#!/usr/bin/env python3
"""
Author : schoubal <schoubal@localhost>
Date   : 2022-07-31
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Crows Nest-- choose the correct article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word', metavar='word', help='Word')

    # extra
    parser.add_argument('-s',
                        '--starboard',
                        help='starboard flag',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word

    article = 'an' if word[0].lower() in 'aeiou' else 'a'
    flag = args.starboard
    location = 'starboard' if flag else 'larboard'
    print(f'Ahoy, Captain, {article} {word} off the {location} bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
