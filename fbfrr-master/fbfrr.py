# karjok pangesty
# guna tool: automatisasi untuk menolak permintaan ertemanan facebook
# metode: scrapping
# dibuat: 12:12am 13 juni 2019
# selesai: 4:04am 13 juni 2019

# tujuan akhir : sebagai media belajar untuk scrapping web (facebook)

from bs4 import BeautifulSoup as bs
from requests import *
from http.cookiejar import LWPCookieJar as cj
import os,sys,re


basic = 'https://mbasic.facebook.com'
s = Session()
s.cookies = cj('kuki.txt')
def login():
	
	print('[\033[96minfo\033[0m] Believe me bro, the login is safe for you :)')
	u = input('[\033[96minput\033[0m] email: ')
	p = input('[\033[96minput\033[0m] passw: ')
	data = {'email':u,'pass':p}
	print('[\033[96minfo\033[0m] Login for you..')
	r = s.post(basic+'/login',data=data)
	if 'm_sess' in r.url or 'save-device' in r.url:
		s.cookies.save()
		print('[\033[96msuccess\033[0m] Login Success')
	elif 'checkpoint' in r.url:
		print('[\033[93mcheckpoint\033[0m] Login checkpoint')
		exit()
	else:
		print('[\033[91merror\033[0m] Login Error.')
		exit()
		

def cekreq():
	global strg
	try:
		open('kuki.txt','r')
	except:
		login()
	s.cookies.load()
	profile = s.get(basic+'/me/friends').text
	b = bs(profile,'html.parser')
	user = re.findall(r'>Keluar (.*?)<',profile)[0].replace('(','').replace(')','')
	ftot = re.findall(r'>Teman (.*?)<',profile)[0].replace('(','').replace(')','')
	freq = re.findall(r'>Teman(.*?)<',profile)[0].replace('(','').replace(')','')
	if len(freq) == 0:
		freq = "don't have"
		banner(user,ftot,freq)
		print("[\033[93mwarning\033[0m] You don't have friend requests to confirm or delete.\nthis tool only running if you have one or more friend requests.")
		exit()

	banner(user,ftot,freq)
	print('''[\033[93mwarning\033[0m] this tool runs
by retrieving all friend request data in your account.
if any, all will be rejected or approved.
but if not, this tool will be finished without results.
''')
	dcac = input('[\033[96minput\033[0m] Decline or Approve ? (d/a) : ')
	if dcac == 'a':
		strg = ['Konfirmasi','Approved','confirm']
		
	else:
		strg = ['Hapus Permintaan','Deleted','delete']
	val = input(f'[\033[96minput\033[0m] Set value (max:{freq}) : ')
	while len(val) == 0 or val not in [f'{x+1}' for x in range(int(freq))]:
		val = input(f'[\033[96minput\033[0m] Set value (max:{freq}) : ')
	print('[\033[96minfo\033[0m] Collecting..')
	link =[basic+'/friends/center/requests/?ref=dbl#friends_center_main']
	no = 0
	dcl = []
	while True:
		if len(dcl) == int(val):
			break
		try:	
			r = s.get(link[no]).text
			no += 1
			b = bs(r,'html.parser')
			for a in b.find_all('a',string=strg[0]):
				if len(dcl) == int(val):
					break
				dcl.append(basic+a.get('href'))
				
			nx = b.find('a',string='Lihat selengkapnya').get('href')
			link.append(basic+nx)
			
			print(f'\r[\033[96minfo\033[0m] {len(dcl)} collected.',end=''),;sys.stdout.flush()
		except:
			break
	if len(dcl) != 0:
		print(f'\n[\033[96minfo\033[0m] Success get {len(dcl)} friend requests')
		print(f'[\033[96minfo\033[0m] Starting..')
		from multiprocessing.pool import ThreadPool as tp
		p = tp(100)
		a = p.map(responder,dcl)
	else:
		print(f"[\033[96minfo\033[0m] It looks like you don't have a friend request to respond")

	print(f'\033[0m[\033[96minfo\033[0m] Done. Program finished')
def responder(href):
	id = re.findall(r'\?'+strg[2]+'=(.*?)\&redir=',str(href))
	r = s.get(href).status_code
	if r == 200:
		print('\033[96m       '+id[0],'\033[0m > ',strg[1],' : \033[92m',r)
	else:
		print('\033[96m       '+id[0],'\033[0m > Failed : \033[91m',r)


def banner(u,ft,fr):
	os.system('clear')
	print(f'''
\033[96m ____________________
\033[96m|\033[0m                    \033[96m|\033[0m
\033[96m|\033[0m   ██          ██   \033[96m|\033[0m        
\033[96m|\033[0m   ████      ████   \033[96m|\033[0m        
\033[96m|\033[0m   ██  ██████  ██   \033[96m|\033[0m        
\033[96m|\033[0m   ██          ██   \033[96m|\033[0m     
\033[96m|\033[0m  ██  ██    ██  ██  \033[96m|\033[0m     
\033[96m|\033[0m ██      ██      ██ \033[96m|\033[0m \033[96mFACEBOOK FRIEND REQUESTS RESPONDER © 2019\033[0m
\033[96m|\033[0m  ██   ██████   ██  \033[96m|\033[0m Wellcome {u} !
\033[96m|\033[0m    ██        ██    \033[96m|\033[0m You have {ft} friends
\033[96m|\033[0m     ██████████     \033[96m|\033[0m and {fr} friend requests
\033[96m|____________________|\033[0m Add me at https://fb.me/om.karjok


''')
if __name__=='__main__':
	try:
		print('[\033[96minfo\033[0m] Updating..')
		os.system('git pull')


		cekreq()
	except Exception as e:
		ex = sys.exc_info()
		banner(os.uname()[1],None,None)
		print(f'''[\033[91merror\033[0m] {ex[0].__name__}: {e} at line {ex[2].tb_lineno}
If you don't know why this happened,
please contact me,
\033[93m  https://fb.me/om.karjok
  https://t.me/om_karjok\033[0m''')

#	
