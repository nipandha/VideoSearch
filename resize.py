import gspread
import json
import time
from oauth2client.client import SignedJwtAssertionCredentials

json_key = json.load(open('NitishaProject-82d3623f7c3e.json'))
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)

gc = gspread.authorize(credentials)

sheet = gc.open_by_key('1JlAE1J8zmG6-C_pasKg1C8KjhJ3wWwXO9a2CqM254B0')
worksheet = sheet.get_worksheet(0)
worksheet.resize(rows=1, cols=20)


