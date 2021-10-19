
# guard cheker
# 4 mei 2019, 6:42PM WIB
# karjok pangesty










from requests import *
from bs4 import BeautifulSoup as bs
from http.cookiejar import LWPCookieJar as cj

lx ='\033[0m'
lg ='\033[92m'
lr ='\033[91m'
ly ='\033[94m'
def login(mail,pw):
	s.cookies = cj('kuki.txt')
	data ={'email':mail,'pass':pw}
	r = s.post('https://mbasic.facebook.com/login',data=data)
	if 'm_sess' in r.url or 'save-device' in r.url:
		s.cookies.save()
	elif 'checkpoint' in r.url:
		print('Checkpoint session')
		exit()
	else:
		print('Check the username/password')
		exit()

def ceksing(id):
	print(f'{lg}get {id} info..')
	s.cookies = cj('kuki.txt')
	s.cookies.load()
	r = s.get('https://mbasic.facebook.com/'+id).text
	b = bs(r,'html.parser')
	name = b.find('title').text
#	if 'Facebook' or 'tidak ' in str(name):
#		print('Invalid user')
#		exit()
	if True:
		print(f'{lg}User profile name : {lx}{name}')
		print(f'{lg}Checking the {name} guard status..')
		for a in b.find_all('a'):
			if 'profile/picture/view/?' in str(a) or 'photo.php?' in str(a) and 'u_0' in str(a.get('id')):
				r = s.get('https://mbasic.facebook.com'+a.get('href')).text
				if 'https://static.xx.fbcdn.net/rsrc.php/v3/yN/r/' in str(r):
					status= 'Active'	
				else:
					status = 'Inactive'
		print('Done !')
		print(f'{lg}Id : {lx}{id}\n{lg}Name :{lx} {name}\n{lg}Guard status : {lx} {status}{lx}')
		
def checkmas(id):

	s.cookies = cj('kuki.txt')
	s.cookies.load()
	r = s.get('https://mbasic.facebook.com/'+id).text
	b = bs(r,'html.parser')
	name = b.find('title').text

	for a in b.find_all('a'):
		if 'profile/picture/view/?' in str(a) or 'photo.php?' in str(a) and 'u_0' in str(a.get('id')):
			r = s.get('https://mbasic.facebook.com'+a.get('href')).text
			if 'https://static.xx.fbcdn.net/rsrc.php/v3/yN/r/' in str(r):
				print(f'{lx}[{lg}{id}{lx}] {name} : {lg}Active{lx}')
			else:
				print(f'{lx}[{lg}{id}{lx}] {name} : {lr}Inactive{lx}')

if __name__=='__main__':
	import os
	os.system('clear')
	st= ['FACEBOOK PROFILE GUARD CHECKER','by Karjok Pangesty']
	for banner in st:
		print(banner.center(40))
	s = Session()
	try:
		open('kuki.txt')
	except:
		login(input(f'\nUsername :{lx} '),input(f'{lg}Password :{lx} '))
	ask = input(f'\nMass/Single (m/s):{lx} ')
	if ask == 'm':
		try:
			f = open(input(f'{lg}id list: {lx}'),'r').readlines()
		except:
			print(lr+'file not found')
			exit()
		print('Running..')
		print('*'*30)
		idn = []
		for i in f:
			checkmas(i.strip())
	elif ask == 's':
		id = input(f'{lg}username/id : {lx}')
		ceksing(id)
				
