from argparse import ArgumentParser
import logging
import logging.config
import sys

# __author__ = None
# __license__ = None
__version__ = '0.1.0'
PROGRAM_NAME = 'argparse boiler'

def program_description():
    """Returns a string with a description of the program
    """
    return None


def main(args):
    pass


if __name__ == '__main__':
    parser = ArgumentParser(prog=PROGRAM_NAME, description=program_description())
    parser.add_argument('-v', '--verbose', default=0, action='count', help='verbosity level. counting (e.g. -v, -vv)')
    parser.add_argument('--version', action='version', version='%(prog)s {__version__}'.format(**globals()))

    # parser.add_argument('-n', '--number', type=int)

    args = parser.parse_args()

    main(args)

