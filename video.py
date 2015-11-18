import os
from search_options import search_options
from search import *
from media import *
from jsonr import duration
from insert1 import insert_collection
from insert2 import insert_ruralvideo
 
class video():
	filename="video name"
	urlname="video name"
	location="video location"
	url="video url"
	tags="video tags"
	isyoutube=False
	isnamematch=False
	videoid="video id"
	fileduration=0
	urlduration=0
	category="video category"
	path="video path"
	description="video description"
	def __init__(self,path):
		self.path=path
		filename=os.path.basename(path);
		self.filename=os.path.splitext(filename)[0]
		self.location=os.path.split(path)[0]
		self.create_tags()
		self.searchvideo()
		self.insert()
	def create_tags(self):
		hierarchy=self.location.replace("\\","/")
		parts=hierarchy.split("/")
		removetags=['C:','D:','Video','c:','d:','G:','g:','Videos','Collection','Agri Books, Articles & Video','f:','F:','h:','H:','Data from Sandeep Goradia']  #To be updated with nonsense file names
		tags=""
		for part in parts:
			if(part in removetags):
				continue
			else:
				if(tags):
					tags="%s,%s"%(tags,part)
				else:
					tags=part
					self.category=part
		self.tags=tags
	def searchvideo(self):
		opt=search_options(self.filename) 
		search_result=youtube_search(opt)
		print "search_result is: %s"%(search_result)
		if(search_result):
			results=search_result.split("(splitby)")
			self.videoid=results[2]
			self.urlname=results[0]
			self.description=results[1]
			self.isyoutube=self.time_check()
			self.isnamematch=self.name_check()
		self.url="https://www.youtube.com/watch?v=%s"%(self.videoid)	
		
	def time_check(self):	
		self.fileduration=getLength(self.path)
		self.urlduration=duration(self.videoid)
		if(abs(self.fileduration-self.urlduration)<5):
			return True
		return False	
	def name_check(self):
		return ((self.filename.lower())==(self.urlname.lower()))
	def insert(self):
		insert_collection(self.category,self.location,self.filename,self.urlname,self.url,self.isyoutube,self.isnamematch)
		if(self.isyoutube or self.isnamematch):
			insert_ruralvideo(self.url,self.description,self.urlname,self.tags,self.isyoutube)