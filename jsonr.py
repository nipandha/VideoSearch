import urllib, json

def duration(videoid):
	key="AIzaSyBYsT2izlwODLxiN7rRcYUCcMeOa2I_ggY"
	url = "https://www.googleapis.com/youtube/v3/videos?part=contentDetails&id=%s&key=%s"%(videoid,key)
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	details=data['items'][0]['contentDetails']
	duration=details['duration']
	time=duration.split('PT')[1]
	min=0
	hr=0
	if('H' in time):
		hrstr=time.split('H')[0]
		hr=int(hrstr)
		time=time.split('H')[0]
	if('M' not in time):
		secstr=time.split('S')[0]
	else:
		minstr=time.split('M')[0]
		secstr=time.split('M')[1]
		secstr=secstr.split('S')[0]	
		min=int(minstr)
	sec=int(secstr)
	sec+=(min*60)
	if(hr):
		sec+=(hr*3600)
	return sec
	