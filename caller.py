from search_options import search_options
from search import *
from jsonr import duration

query=raw_input("Enter a query ")
opt=search_options(query) 
search_result=youtube_search(opt)
videoid=search_result.split("(splitby)")[1]
urlname=search_result.split("(splitby)")[0]
l=duration(videoid)
print videoid
print urlname
print l
print (2*l)
#opt.display()