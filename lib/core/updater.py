import requests, urllib.request, os
from lib.core.utils import Colors
from lib.core.wifi import CheckWifi

URL = "https://raw.githubusercontent.com/TrollSkull/MorseTranslator/master/"

def Update():
    FILES = ['translator.py', 'lib/core/wifi.py', 'lib/core/updater.py', 'lib/core/version',
             'lib/core/utils.py', 'lib/main.py', 'lib/core/exceptions.py',]
    
    for FL in FILES:
        DATA = urllib.request.urlopen(URL + FL).read()
        
        with open(FL, "wb") as F:
            F.write(DATA)
    
    print("\n[Translator] Updated successfull, exiting script.")

def CheckVersion():
    try:
        toolVersion = open("./lib/core/version", "r").read()
    except:
        toolVersion = "1.0"
    
    try:
        CheckWifi()
        gitVersion = requests.get("https://raw.githubusercontent.com/TrollSkull/MorseTranslator/main/lib/core/version").text
    except Exception as err:
        import sys

        print(err, file=sys.stderr)
        sys.exit(1)
    
    print("\n[Translator] Verifying Git version...")
    if (toolVersion == gitVersion):
        print("\n[Translator] Version match with GitHub repository.")
        
    else:
        print("\n[Translator] Update available, downloading...")
        Update()