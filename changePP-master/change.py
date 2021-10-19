# change profile photo
# start : jumat 28 juni 2019 2:38am
# finish : jumat 28 juni 2019 3:08am
# karjok pangesty


# PLEASE DON'T FORGET TO INSERT MY NAME IF YOU ADD THIS FEATURE TO YOUR PROGRAM !!

from requests import *
from bs4 import BeautifulSoup as bs
from http.cookiejar import LWPCookieJar as cj

s = Session()
s.cookies = cj('kuki.txt')
def login(e,p):
	r = s.post('https://mbasic.facebook.com/login',data={'email':e,'pass':p})
	if 'save-device' in r.url or 'm_sess' in r.url:
		s.cookies.save()
		print('login sukses')
	elif 'checkpoint' in r.url:
		print('checkpoint')
	else:
		print('login failed')

def change():
	s.cookies.load()
	pict = input('Input pict name: ')
	try:
		open(pict,'rb')
	except:
		print('not exist')
		exit()
	# file to upload
	file = {'file1':('pict.jpg',open(pict,'rb'),'multipart/form-data')}
	data = {}
	# get form data
	print('get form data')
	r = s.get('https://mbasic.facebook.com/photos/upload/?profile_pic&upload_source=profile_pic_upload&profile_pic_source=tagged_photos_page').text
	b = bs(r,'html.parser')
	form = b.find('form')
	to = form.get('action')
	for i in form.find_all('input',{'type':'hidden'}):
		try:
			# update data to upload
			data[i['name']]=i['value']
		except:
			pass
	# upload photo
	print('uploading profile picture')
	r = s.post(to,files=file,data=data)
	print('status: ',r.status_code)

if __name__=='__main__':
	try:
		open('kuki.txt','r')
	except:
		e = input('username: ')
		p = input('password: ')
		login(e,p)
	change()