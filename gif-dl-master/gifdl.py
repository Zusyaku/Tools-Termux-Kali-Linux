from requests import *
import json,random,re,os


def conversion(length):
	size = round((int(length) / 10**6),2)
	return size
def url_processor(link,name):
	print('Preparing..')
	if link.endswith('.gif'):
		url = link
	else:
		r = get('http://karjok-pangesty.herokuapp.com/api/gif',params={'url':link}).text
		resp = json.loads(r)
		if resp['oke'] == 'true':
			url = resp['url']
	print('Downloading..')
	r = get(url)
	size = conversion(r.headers['Content-Length'])
	with open(name+'.gif','wb') as gif:
		gif.write(r.content)
		gif.close()
	print(f'{size} Mb gif downloaded as \033[92m{name}.gif\033[0m')
	o = input('Open now ? (y/n): ')
	if o == 'y':
		os.system(f'termux-open {name}.gif')
	print('\n\033[90mGif Downloader by Karjok Pangesty\033[0m')
def banner():
	os.system('clear')
	print('''
	\033[92m░░░░░░░░░░░░░░░░░░░░░░
	░░\033[0m██████\033[92m░░\033[0m██\033[92m░░\033[0m██████\033[92m░░
	░░\033[0m██\033[92m░░░░░░░░░░\033[0m██\033[92m░░░░░░
	░░\033[0m██\033[92m░░\033[0m██\033[92m░░\033[0m██\033[92m░░\033[0m████\033[92m░░░░
	░░\033[0m██████\033[92m░░\033[0m██\033[92m░░\033[0m██\033[92m░░░░░░
	░░░░░░░░░░░░░░░░░░░░░░
	   \033[0mDownloader [1.0]
	''')
if __name__=='__main__':
	banner()
	link = input('Link: ')
	name= input('Output Name: ')
	url_processor(link,name)
	
