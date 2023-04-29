try:
    import time, sys, os
    import argparse

    from lib.core.utils import (
        CheckOSClear, Colors,
        Banner, MorseEncrypt
    )
    
    from lib.core.updater import CheckVersion
    from lib.core.wifi import CheckWifi
    
except ImportError as error:
    pass

parser = argparse.ArgumentParser(description='Morse translator v1.0 by TrollSkull',
                                 usage="translator.py -t [your text here] or just python translator.py")

parser.add_argument('--text', '-t', type=str, required=False,
                    help='you can put morse code here or normal letters.')

args = parser.parse_args()

class Main:
    if args.text:
        print(Colors.CYAN + "MorseTranslator v1.1" + Colors.RESET)
        print(MorseEncrypt(args.text))
        sys.exit(0)
    
    CheckOSClear()
    Banner()
    try:
        while True:
            option = str(input("\nTranslator " + Colors.CYAN + "~# " + Colors.RESET))

            if option == "/update":
                CheckVersion()

            elif option == "/exit":
                sys.exit(0)
            
            else:
                print(MorseEncrypt(option))

    except KeyboardInterrupt:
            print(Colors.WARNING + "\n[Translator] " + Colors.RESET + "Keyboard interrupt detected, exiting.")
            sys.exit(1)   

def main():
    try:
        translator = Main()
        translator
    except Exception as err:
        import sys

        print(err, file=sys.stderr)
        sys.exit(1)
