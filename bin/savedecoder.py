"""
This is my attempt at converting the ClickerLister Source Code
from JavaScript to Python.  All credit for the function of the
code itself goes to Alex B. https://github.com/alexbonjour
"""

from base64 import b64decode, b64encode
from hashlib import md5
import json

ANTI_CHEAT_CODE = 'Fe12NAfA3R6z4k0z'
SALT = 'af0ik392jrmt0nsfdghy0'

def decryptSave(string):
    if string.find(ANTI_CHEAT_CODE) != -1:
        string = fromAntiCheatFormat(string)
        if string != 'hash is bad!':
            decodedString = b64decode(string)
            return json.loads(decodedString)
        else:
            return 'Invalid Save File - bad hash'
    else:
        return 'Invalid Save File'
    
def fromAntiCheatFormat(string):
    elements = string.split(ANTI_CHEAT_CODE)
    data = elements[0][::2]
    hash = elements[1]
    dataHash = getHash(data)
    if dataHash == hash:
        return data
    else:
        return 'hash is bad!'
    
def getHash(string):
    characters = string.split()
    characters.sort()
    sortedcharacters = "".join(characters)
    return md5(sortedcharacters + SALT).hexdigest()