#!/usr/bin/env python3
"""
Author : schoubal <schoubal@localhost>
Date   : 2022-08-06
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='Item(s) to bring',
                        nargs='+')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    sort_flag= args.sorted
    items = args.str

#    print(f'flag_arg = "{sort_flag}"')
#    print(f'positional = "{items}"')

    if sort_flag:
        items = sorted(items)

    if len(items) ==1:
        basket = items[0]
    elif len(items) ==2:
        basket = items[0] + " and " + items[1]
    else:
        basket = ', '.join(items[0:-1]) + ", and " + items[-1]

    print(f'You are bringing {basket}.') 

# --------------------------------------------------
if __name__ == '__main__':
    main()
