import gspread
import json
import time
from oauth2client.client import SignedJwtAssertionCredentials

json_key = json.load(open('NitishaProject-82d3623f7c3e.json'))
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)

gc = gspread.authorize(credentials)

sheet = gc.open_by_key('1Imau9PnuvXQCrUW6S_xZK3-76PdsQCUofKCp5fmNR8s')
worksheet = sheet.get_worksheet(0)
worksheet.resize(rows=, cols=20)


