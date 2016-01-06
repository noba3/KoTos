
import locale
import re
import sys
import urlparse
import HTMLParser

import xbmc

from plugin import Plugin
from keyboard import Keyboard

def getFormatDateShort(year, month, day):
    date_format = xbmc.getRegion('dateshort')
    date_format = date_format.replace('%d', day)
    date_format = date_format.replace('%m', month)
    date_format = date_format.replace('%Y', year)
    return date_format

def executebuiltin(function):
    xbmc.executebuiltin(function)

def stripHtmlFromText(text):
    return re.sub('<[^<]+?>', '', text)

def decodeHtmlText(text):
    hp = HTMLParser.HTMLParser()
    return hp.unescape(text)

def getParam(name, default=None):
    args = urlparse.parse_qs(sys.argv[2][1:])
    value = args.get(name, None)
    if value and len(value)>=1:
        return value[0]
    
    return default

def getLanguageId(default='en-US'):
    result = default
    
    try:
        language = locale.getdefaultlocale()
        if language and len(language)>=1 and language[0]:
            result = language[0].replace('_', '-')
    except:
        pass
    
    return result