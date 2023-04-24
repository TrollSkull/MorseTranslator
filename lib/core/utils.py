import sys, os

class Colors:
    OK = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    WORKING = '\033[34m'
    GRAY = '\033[1;30m'
    CYAN = '\033[1;36m'

def MorseEncrypt(text):
    encrypt = {'A':'.-', 'B':'-...', 'C':'-.-.',
               'D':'-..', 'E':'.', 'F':'..-.',
               'G':'--.', 'H':'....', 'I':'..',
               'J':'.---', 'K':'-.-', 'L':'.-..',
               'M':'--', 'N':'-.', 'O':'---',
               'P':'.--.', 'Q':'--.-', 'R':'.-.',
               'S':'...', 'T':'-', 'U':'..-',
               'V':'...-', 'W':'.--', 'X':'-..-',
               'Y':'-.--', 'Z':'--..', ' ':'|'}
            
    decrypt = {var: key for key, var in encrypt.items()}

    if '-' in text:
        return ''.join(decrypt[i] for i in text.split())
    else:
        return ''.join(encrypt[i] for i in text.upper() if i.isalpha())

def CheckOSClear():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

def Banner():
    print(Colors.CYAN + """
  	    MORSE     TRANSLATOR
  	     
          .--.                   .---.
      .---|__|           .-.     |~~~|
   .--|===|--|_          |_|     |~~~|--.
   |  |===|  |'\     .---!~|  .--|   |--|
   |%%|   |  |.'\    |===| |--|%%|   |  |
   |%%|   |  |\.'\   |   | |__|  |   |  |
   |  |   |  | \  \  |===| |==|  |   |  |
   |  |   |__|  \.'\ |   |_|__|  |~~~|__|
   |  |===|--|   \.'\|===|~|--|%%|~~~|--|
   ^--^---'--^    `-'`---^-^--^--^---'--'
   """ + Colors.RESET)
    
    print("____________________________________________ \n")
    print("           Created by " + Colors.OK + "@TrollSkull \n" + Colors.RESET)
    print(Colors.GRAY + '[INFO] Type "show options" to show command. \n' + Colors.RESET)