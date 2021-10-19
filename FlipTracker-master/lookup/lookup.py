# coding=utf-8
# Coded By: Deray
# instagram: reyy05_

import requests,os,bs4,sys

#<-- ipinfo.io -->
def crack(ip,line):
	dt=[]
	r=requests.get("http://ipinfo.io/"+ip+"/json").json()
	for i in r:
		if i =="":
			continue
		dt.append(i)
	print(line)
	for i in dt:
		try:
			d=list(i)
			if len(d) !=20:
				for k in range(30):
					if len(d) ==10:
						print("[+] "+"".join(d)+" : "+r[i])
						break
					else:d.append(" ")
		except:pass
	print("\n"+"-"*len(line))


#<-- ipgeolocation.io
class ip_geolocation(object):
	def __init__(self,ip,line):
		self.line=line
		self.ip=ip
		self.data=[]
		self.dor=0
		self.realdata=[]
		self.res=[]
		self.fakenum=0
		self.crawl()
	
	# <-- LOAD BS4 RESPONSE -->
	def crawl(self):
		self.bs=bs4.BeautifulSoup(
			requests.get("https://ipgeolocation.io/ip-location/"+self.ip,
		headers={
			"User-Agent":"Mozilla/5.0 (Linux; Android 5.1)"}).text,"html.parser")
		print(self.line)
		self._loopdata()
	
	# <-- LOAD DATA -->
	def _loopdata(self):
		for i in self.bs.find_all("td"):
			self.data.append(i.text)
		self.loop_realdata()
	
	# <-- FILTERING DATA -->
	def loop_realdata(self):
		for i in self.data:
			self.dor+=1
			if self.dor>18:
				if i =="":
					continue
				self.realdata.append(i.replace("\n",""))
		self._result()
	
	# <-- GOT RESULT -->
	def _result(self):
		for i in self.realdata:
			self.fakenum+=1
			self.res.append(i)
			if len(self.res) ==2:
				self._map_result(self.res)
				self.res=[]
		print("-"*len(self.line))
				
	# <-- MAP RESULT -->
	def _map_result(self,_data):
		d=list(_data[0])
		for i in range(30):
			if len(d) ==30:
				print("[+] %s"%("".join(d)+": "+_data[1]))
				break
			else:d.append(" ")
