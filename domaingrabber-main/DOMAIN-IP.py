import socket, sys


x="python Script.py list.txt"
print x

def getIP(site):
	
		site = i.strip()
		try:
			if 'http://' not in site:
				IP1 = socket.gethostbyname(site)
				print "IP: "+IP1
				open('ips.txt', 'a').write(IP1+'\n')
			elif 'http://' in site:
				url = site.replace('http://', '').replace('https://', '').replace('/', '')
				IP2 = socket.gethostbyname(url)
				print "IP: "+IP2
				open('ips.txt', 'a').write(IP2+'\n')
	
		except:
			pass
			
nam=raw_input('file name :')
with open(nam) as f:
    for i in f:
        getIP(i)

		
