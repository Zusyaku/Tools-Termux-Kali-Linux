#Author:karim shoair (D4Vinci)
#Downloading youtube videos as mp4 and as mp3
import os,sys

try:
	Type = sys.argv[1]
	url  = sys.argv[2]
except:
	print("Error missing arguments!")
	print("yt.py (mp3/mp4) <url>")
	sys.exit(0)

if Type.lower()=="mp3":
	os.system("youtube-dl --exec 'ffmpeg -i {} -vn -ab 128k -ar 44100 -y {}.mp3' --extract-audio "+url)
elif Type.lower()=="mp4":
	os.system("youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' "+url)
else:
	print("Error unsupported format!")
