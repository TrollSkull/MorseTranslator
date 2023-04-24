#!/usr/bin/env python3

__author__ = 'TrollSkull'
__version__= 'v2.0'

try:
    from lib.main import Main, main
    from lib.core.exceptions import MyExceptions
except Exception as err:
    import sys

    print(err, file=sys.stderr)
    sys.exit(1)

if __name__ == "__main__":
    main()