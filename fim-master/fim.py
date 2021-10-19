'''
Attention !!
------------

This is an open source script.
You can using it for learning purpose. and there is why i'm not encrypt it.
but,
if you try to adjust this code to your script,
please don't forget to write the source info.
thanks,



Crabs ID Admin,
Karjok Pangesty


Perhatian !!
------------

Ini adalah skrip sumber terbuka.
Anda bisa menggunakannya untuk tujuan belajar. dan itu adalah mengapa saya tidak mengenkripsinya.
Tetapi,
jika anda mencoba untuk menerapkannya ke skrip anda,
harap jangan lupa untuk menulis sumber informasinya
terimakasih


Admin Crabs ID,
Karjok Pangesty






Contact,
---------
Facebook : https://fb.me/om.karjok
Telegram : https://t.me/om_karjok
Email    : crabs2019@gmail.com

Join with us !
--------------
Cacker Noob Squads Indonesia
(https://t.me/CRABS_ID)

'''



from requests import *
from bs4 import BeautifulSoup as bs
from http.cookiejar import LWPCookieJar as cj
import re, os, sys


lx ='\033[0m'
lr = '\033[91m'
lg = '\033[92m'
la = '\033[90m'


s = Session()
s.cookies=cj('kuki.txt')
url = 'https://mbasic.facebook.com'


def login(id,pw):
	data ={'email':id,'pass':pw}
	r = s.post('https://mbasic.facebook.com/login',data=data)
	if 'm_ses' in r.url or 'save-device' in r.url:
		s.cookies.save()
		print('loged in !')
	elif 'checkpoint' in r.url:
		print('checkpoint session')
		exit()
	else:
		print('check the username/password !')
		exit()


def grab(id):
	print(f'{lg}Checking the user profiles..')
	global name,fold
	s.cookies.load()
	r = s.get('https://mbasic.facebook.com/' + id ).text
	b = bs(r,'html.parser')
	
	# profil name
	n = b.find('title').text
	name = n.replace(' ','+')[:15]
	if 'Halaman Tidak Ditemukan' in str(n) or 'Facebook' in str(n):
		print(f'{lg}Profile {lx}{id}{lg} not found')
		print('Program stoped !'+lx)
		exit()
	
	print(f'{lg}User profile name :{lx} {n}')
	fold = input(f'{lg}Folder name :{lx} ')
	np = input(f'{lg}Results amount : {lx}')
	try:
		os.mkdir(fold)
	except:
		pass
	imglink = []
	print(f'{lg}Finding user photo album(s)..')
	for a in b.find_all('a'):
		
		# search album, if exist, continue
		if 'profile.php?v=photos' in str(a) and 'Foto' in a.text or 'photos?lst=' in str(a) and 'Foto' in a.text:
			print('\nAlbum available !')
			print('Grabbing user photo(s)..')
			r = s.get(url+a.get('href')).text
			bb = bs(r,'html.parser')
			
			# get photo album named 'upload'
			div = bb.find('div',attrs={'title':'Unggah'})
			for ia in div.find_all('a'):
				
				# if album have pager link, continue
				if 'Lihat Semua' in ia.text:
					link = [ia.get('href')]
					no = 0
					while True:
						try:
							if len(imglink) == int(np):
								break
							r = s.get(url+link[no]).text
							b = bs(r,'html.parser')
							no += 1
							for a in b.find_all('a'):
								if len(imglink) == int(np):
									break
								if 'photo.php' in str(a):
									imglink.append(a.get('href')) # photos link for download
									print(f'\rget {len(imglink)} photo(s)',end=''),;sys.stdout.flush()
							
							# get pager link
							next = b.find('div',attrs={"id":"m_more_item"}).find('a').get('href')
							link.append(next)
							
						except:
							break
				else:
					# if album not have pager link, get photo that available.
					if len(imglink) == int(np):
						break
					if 'photo.php' in str(ia):
						imglink.append(ia.get('href'))
						print(f'\rget {len(imglink)} photo(s)',end=''),;sys.stdout.flush()

				
	if len(imglink) == 0:
		print('Album not found !')
	else:
		print('\nDownloading..\n')
		from multiprocessing.pool import ThreadPool as tp
		x = tp(100)
		p = x.map(dl,imglink)
		print(f'{lg}\nDone ! photo(s) saved in : {lx}FIm/{fold}')
def dl(link):
	r = s.get(url+link).text
	b = bs(r,'html.parser')
								
	# get photo links if not shielded photos
	if '/?c_src=share' in str(b):
		for img in b.find_all('a'):
			if 'photo/view_full_size' in str(img):
				pref = re.findall(r'\?fbid=(.*?)\&',str(img))[0]
				r = s.get(url+img.get('href'),allow_redirects=True)
				bb = bs(r.text,'html.parser')
				a = bb.find('a').get('href')
				r = get(a)
				
	# and this is how to get photos wich shielded.			
	else:
		for im in b.find_all('img'):
			if 'scontent' in str(im):
				pref = 'profiles_photo'
				r = get(im.get('src'))
				
	
	# download the image
	with open(f'{fold}/{name}_{pref}.jpg','wb') as f:
		f.write(r.content)
		print(f'  {lg}* {lx}{name}_{pref}.jpg')

def banner():
	os.system('clear')
	print(f'''

	{la}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
	{la}░░░░{lg}██████{la}░░░░░░░░░░░░░░░░░░░
	{la}░░░░{lg}██{la}░░░░░░░░░░░░░░░░░░░░░░░
	{la}░░░░{lg}████{la}░░{lg}██{la}░░{lg}████{la}░░{lg}████{la}░░░░░
	{la}░░░░{lg}██{la}░░░░{lg}██{la}░░{lg}██{la}░░{lg}██{la}░░{lg}██{la}░░░░░
	{la}░░{lg}Facebook Image Downloader{la}░░
	{la}░░░░░░░░░░░░░░░░░░░░░░░░░░░░░{lg}
	    {lx}Karjok Pangesty © 2019


''')

					
if __name__=='__main__':
	try:
		open('kuki.txt')
	except:
		login(input(f'{lg}Username: {lx}'),input(f'{lg}Password:{lx} '))

	banner()
	id = input(f'{lg}Username or ID :{lx} ')
	while len(id) == 0:
		print(f"{lr}can't be blank.{lx}")
		id = input(f'{lg}Username or ID :{lx} ')
		
	try:
		grab(id)
	except KeyboardInterrupt:
		print(lg+'Stoped !'+lx)
	except Exception as e:
		ex = sys.exc_info()
		print(f'{lg}error:{lx} {ex[0].__name__}\n{lg}text: {lx}{e}\n{lg}line: {lx}{ex[2].tb_lineno}')

	
		
# Mesuji, May 3th, 2019 2:14PM WIB
	
