import re
from setuptools import setup

with open('boilers/argparse_logging_boiler.py') as f:
    program_text = f.read()

program_name = re.search("^PROGRAM_NAME\s*=\s'(.*)'", program_text, re.M).group(1)
version = re.search("__version__\s*=\s'(.*)'", program_text, re.M).group(1)
author = re.search("__author__\s*=\s'(.*)'", program_text, re.M).group(1)
license = re.search("__license__\s*=\s'(.*)'", program_text, re.M).group(1)

setup(
    name = program_name,
    version = version,
    description = '',
    author = author,
    entry_points = {
        'console_scripts': [
            'arg = boilers.argparse_logging_boiler:cli'
        ]
    },
)
