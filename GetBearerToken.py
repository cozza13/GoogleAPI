#THIS WILL SPIT BACK OUT A BEARER TOKEN THAT YOU CAN USE TO CALL THE GOOGLE RESAPI AND USE IN PROGRAMS LIKE POSTMAN
#SPENT A WHILE TRYING TO FIND A SOLUTION AND THIS IS A COMBINATION OF SEVERAL PIECES OF CODE. 
#AUTHER: CHRIS COLLINS JAN 7TH 2019

import pprint
import sys
import json
import httplib2
import logging
logging.basicConfig(filename='debug.log',level=logging.DEBUG)

from apiclient.discovery import build_from_document
from apiclient.http import build_http
from oauth2client.service_account import ServiceAccountCredentials


SCOPE = 'SCOPE_URL'
CREDENTIAL_FILE = 'CREDENTIALS.json'


credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIAL_FILE, SCOPE)
http = credentials.authorize(httplib2.Http())
credentials.get_access_token()
token1 = credentials.access_token
print(token1)
