import subprocess
import os
#def getLength(filename):
#  result = subprocess.Popen(["ffprobe", "filename"],stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
#  return [x for x in result.stdout.readlines() if "Duration" in x]

#fileToWorkWith = 'G:\Songs\Videos\Tarkanland.mp4'

#getLength(fileToWorkWith)
#_______________

def getLength(input_video):
	env = os.environ
	command="\"C:\\Program Files\\ffmpeg\\bin\\ffprobe.exe\" -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 \"%s\""%(input_video)
	result = subprocess.Popen(command, stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell=True)
	#result=subprocess.call(command,env={'PATH': os.environ()['PATH']})
	output = result.communicate()
	l= output[0]
	
	l=l.strip()
	l=l.split('.')[0]  
	len=int(l)
	return len
input_video='G:\Songs\Videos\Tarkanland.mp4'    
l= getLength(input_video)  
print (2*l)