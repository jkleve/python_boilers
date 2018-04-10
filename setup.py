from setuptools import setup

setup(
    name = 'alb',
    version = '0.1.0',
    description = '',
    author = '',
    entry_points = {
        'console_scripts': [
            'arg = boilers.argparse_logging_boiler:cli'
        ]
    },
)
