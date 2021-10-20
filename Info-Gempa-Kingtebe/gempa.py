# Wkwkwkwkwk ngentod mau apa ?
# Kagak usah rikod anjing :v

# Start : 19-04-2021 14:08 WIB
# Done  : 19-04-2021 15-01 WIB
# Only py3

import sys as cosmic, os, platform
from bs4 import BeautifulSoup as bs
from time import sleep as date
try:
	import requests
except ImportError:
	exit("\n \033[91m-- \033[97mPlease install module \033[93mrequests\n\033[97m")

if platform.python_version().split('.')[0] != '3':
	exit("\n \033[91m-- \033[97mNeed support for python2 \033[93m:(\n\033[97m")

exec(open("img/.colors").read())

_baner = lambda: print("\n\033[97m _____  \033[91m{ \033[90mScript Gempa \033[91m}\n\033[97m|   __|___ _____ ___ ___\n\033[97m|  |  | -_|     | . | .'| \033[93m• \033[97mAuthor \033[91m: \033[97mKingtebe\n\033[97m|_____|___|_|_|_|  _|__,| \033[93m• \033[97mGithub \033[91m: \033[97mgithub.com/Kingtebe\n\033[97m                |_|\n")

class Gempa:

	def __init__(self):
		self.https = requests.Session()
		self._Main()

	def _Main(self):

		_url = self.https.get("https://www.bmkg.go.id/")
		_scrap = bs(_url.text, "html.parser")
		_all = _scrap.find('div', class_="col-md-4 md-margin-bottom-10")
		_get = _all.findAll("li")
		_map = _all.find('a')['href']
		try:
			__import__('os').system('clear');_baner()
			print(f' {yellow}-- {white}Information Gempa Terkini Dari BMKG {yellow}-- ');date(1.3)
			print('\n Map : {}'.format(_map))
			print(' Waktu : {}'.format(_get[0].text))
			print('\n Magnitude : {}'.format(_get[1].text))
			print(' Kedalaman : {}'.format(_get[2].text))
			print(' Koordinat : {}'.format(_get[3].text))
			print('\n Lokasi : {}'.format(_get[4].text))
			print(' Potensi : {}'.format(_get[5].text+'\n'));date(1.3);print(f' {red}[ {grey}Silahkan copy link nya untuk melihat peta map nya {red}]\n')

		except (KeyboardInterrupt,EOFError):
			pass

if __name__=='__main__':
	Gempa()
