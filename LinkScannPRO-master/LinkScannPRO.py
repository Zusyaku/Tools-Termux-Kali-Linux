#!/usr/bin/env python3
#https://github.com/AngelSecurityTeam
import sys,os,time,requests
from bs4 import BeautifulSoup

print ("""
\033[33m 
  _     _       _     ____                        ____  ____   ___  
 | |   (_)_ __ | | __/ ___|  ___ __ _ _ __  _ __ |  _ \|  _ \ / _ \ 
 | |   | | '_ \| |/ /\___ \ / __/ _` | '_ \| '_ \| |_) | |_) | | | |
 | |___| | | | |   <  ___) | (_| (_| | | | | | | |  __/|  _ <| |_| |
 |_____|_|_| |_|_|\_\|____/ \___\__,_|_| |_|_| |_|_|   |_| \_\\\___/ 
\033[91m                                                 |AngelSecurityTeam|                            

""")

try:

	link = input("\033[33m  Website: ")

	start1 = link.startswith('http')
	start2 = link.startswith('https')
	if(start1 == False or start2 == False):
		link2 = ("https://" + link)
		if(len(link) == 0):
			print(" \n \033[33m Url Undefined")

		else:
			response = requests.get(link2)
			content = response.content
			soup = BeautifulSoup(content, "lxml")
			links = soup.find_all('a')
			for link in links:
				href = link.get('href')
				print( "\n\033[91m  Link Found: " + str(href))
				time.sleep(1)

except KeyboardInterrupt as exitt:
		sys.exit()
