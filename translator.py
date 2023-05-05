#!/usr/bin/env python3

__author__ = 'TrollSkull'
__version__= 'v2.0'

try:
    import requests
except ImportError as error:
    import time, os

    print(error + '\nSome requirements are not installed.')
    requirements = ['requests']

    for requirement in requirements:

        print(f'Installing "{requirement}"...')
        os.system(f'pip3 install {requirement}')
        time.sleep(1)

    print('\nRequirements have been installed.')

try:
    from lib.main import Main, main
    from lib.core.exceptions import MyExceptions
except Exception as err:
    import sys

    print(err, file=sys.stderr)
    sys.exit(1)

if __name__ == "__main__":
    main()