import gspread
import json
import datetime
import time
from oauth2client.client import SignedJwtAssertionCredentials
import sys

def insert_ruralvideo(URL,Description,Name,Tags,IsYoutube):
	reload(sys)  
	sys.setdefaultencoding('Cp1252')
	json_key = json.load(open('NitishaProject-82d3623f7c3e.json'))
	scope = ['https://spreadsheets.google.com/feeds']

	credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)

	gc = gspread.authorize(credentials)
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%m/%d/%Y %H:%M:%S')
	sheet = gc.open_by_key('1Imau9PnuvXQCrUW6S_xZK3-76PdsQCUofKCp5fmNR8s')
	worksheet = sheet.get_worksheet(0)
	#worksheet.resize(rows=1, cols=5)
	rowtoadd=[st,URL,Description,Name,Tags,IsYoutube]
	worksheet.append_row(rowtoadd)