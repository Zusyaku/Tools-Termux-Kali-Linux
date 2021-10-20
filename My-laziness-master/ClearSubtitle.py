#Author : D4Vinci
#Clear subtitles files from coloring codes to play on non color-supported devices like TVs in my case
#Usage : ClearSubtitle.py <Subtitle_file> Or just run it in the subtitles folder

import sys,re,os

def clear(srt):
	  font_regex = re.compile(r"<.*?>")  #<font face=""> </font> <i> </i> <b> </b>...
	  shit_regex = re.compile(r"{.*?}") #{\fs50\fad(1000,1500)\c&#008008&\..\...\..\....}
	  f=open(srt,"r")
	  subtitles=f.read()
	  f.close()
	  extracted =font_regex.findall(subtitles)
	  extracted+=shit_regex.findall(subtitles)
	  for i in extracted :
		  subtitles=subtitles.replace(i,"")
	  open(srt,"w").write(subtitles)

try:
	srt = sys.argv[1]
	print("[+] Clearing "+srt+" ...")
	clear(srt)
except:
	srts =[ i for i in os.listdir() if i.endswith(".srt") ]
	for srt in srts:
		print("[+] Clearing "+srt+" ...")
		clear(srt)
