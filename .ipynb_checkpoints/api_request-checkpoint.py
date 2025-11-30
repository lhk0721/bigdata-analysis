
import os
import requests
import urllib
import src.mylib

keyPath = os.path.join(os.getcwd(),'src','key.properties')
key = src.mylib.getKey(keyPath)

KEY = str(key['gokr'])
TYPE = ''
SERVICE = ''
START_INDEX = ''
END_INDEX = ''
params = '/'.join([KEY,TYPE,SERVICE,START_INDEX,END_INDEX])

_url = ''
url = '/'.join([_url, params])

