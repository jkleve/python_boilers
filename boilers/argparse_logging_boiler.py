from argparse import ArgumentParser
import logging
import logging.config
import sys

# __author__ = ''
# __license__ = ''
__version__ = '0.1.0'
PROGRAM_NAME = 'argparse logging boiler'

LOGGING_FORMAT = '%(asctime)s %(levelname)-8s %(name)s: %(message)s'
LOGGING_DATEFMT = '%H:%M:%S'


def program_description():
    """Returns a string with a description of the program
    """
    return None


def main(args):
    pass


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


def cli():
    parser = ArgumentParser(prog=PROGRAM_NAME, description=program_description())
    parser.add_argument('-v', '--verbose', action='count', help='verbosity level. counting (e.g. -v, -vv)')
    parser.add_argument('--version', action='version', version='%(prog)s {__version__}'.format(**globals()))

    # parser.add_argument('-n', '--number', type=int)

    args = parser.parse_args()

    configure_logging(args.verbose)

    return main(args)


if __name__ == '__main__':
    sys.exit(cli())

