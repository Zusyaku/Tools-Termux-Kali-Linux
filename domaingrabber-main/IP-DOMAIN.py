#!/usr/bin/python
import requests, sys
import time

def grab(i):
		try:
			ch = requests.get('http://api.hackertarget.com/reverseiplookup/?q='+i)
			if '.' in ch.content:
				print ch.content
				open('sites.txt', 'a').write(ch.content)
				time.sleep(5)
	
			else:
				print "[!] => "+i+'  Problem '
		except:
			pass		
nam=raw_input('file name :')
with open(nam) as f:
    for i in f:
        grab(i)
