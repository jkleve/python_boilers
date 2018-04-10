from argparse import ArgumentParser
import logging
import logging.config
import sys

# __author__ = None
# __license__ = None
__version__ = '0.1.0'
PROGRAM_NAME = 'argparse logging boiler'

LOGGING_FORMAT = '%(asctime)s %(levelname)-7s %(name)s: %(message)s'
LOGGING_DATEFMT = '%H:%M:%S'


def program_description():
    """Returns a string with a description of the program
    """
    return None


def configure_logging(verbosity):
    logging_config = {
        'version': 1,
        'formatters': {
            'brief': {
                'format': LOGGING_FORMAT,
                'datefmt': LOGGING_DATEFMT,
            }
        },
        'handlers': {
            'brief': {
                'class': 'logging.StreamHandler',
                'formatter': 'brief',
            }
        },
        'loggers': {
            '': {  # root logger
                'level': logging.WARNING,
                'stream': sys.stdout,
                'handlers': ['brief',],
            },
        }
    }

    if verbosity == 1:
        logging_config['loggers']['']['level'] = logging.INFO
    elif verbosity >= 2:
        logging_config['loggers']['']['level'] = logging.DEBUG

    logging.config.dictConfig(logging_config)


def main(args):
    pass


if __name__ == '__main__':
    parser = ArgumentParser(prog=PROGRAM_NAME, description=program_description())
    parser.add_argument('-v', '--verbose', default=0, action='count', help='verbosity level. counting (e.g. -v, -vv)')
    parser.add_argument('--version', action='version', version='%(prog)s {__version__}'.format(**globals()))

    # parser.add_argument('-n', '--number', type=int)

    args = parser.parse_args()

    configure_logging(args.verbose)

    main(args)

