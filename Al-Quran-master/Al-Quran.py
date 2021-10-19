import requests as r, os
from bs4 import BeautifulSoup as par
clear = lambda : os.system('clear')

def main():
	clear()
	print('''\x1b[1;97m=============================================
\x1b[1;91m   * \x1b[1;97mAuthor : \x1b[1;92mRizky
\x1b[1;91m   * \x1b[1;97mSupport: \x1b[1;92mAprilia
\x1b[1;91m   * \x1b[1;97mTeam   : \x1b[1;92mXIUZCODE
\x1b[1;91m   * \x1b[1;97mGithub : \x1b[1;92mhttps://github.com/hekelpro
\x1b[1;97m=============================================''')
	try:
		a = r.get('https://litequran.net').text
	except r.exceptions.ConnectionError:
		exit('\x1b[1;91m! \x1b[1;97mTidak Ada Koneksi')
	a = par(a,'html.parser')
	print('\n\x1b[1;92m1\x1b[1;91m. Keluar Program')
	# <!-- Variabel --!>
	no, ayat, bacaan, arti, link = 0, 0, 0, 0, []
	for x in a.find_all('a'):
		no += 1
		titel = x.get('title')
		if titel == None:
			pass
		else:
			print(f'\x1b[1;92m{str(no)}\x1b[1;91m. \x1b[1;97m{titel}')
	for z in a.find_all('a'):
		run = z.get('href')
		link.append(run)
	try:
		pil = input('\n\x1b[1;91m# \x1b[1;97mPilih:\x1b[1;96m ')
		if pil =='1':
			exit('\x1b[1;91m! \x1b[1;97mProgram Berakhir')
		else:
			pil = int(pil) - 1
			lanjut = r.get(str(link[pil])).text
			scrap = par(lanjut,'html.parser')
			find1 = scrap.find('h1', class_="page-title").text
			print("\x1b[1;97m="*45)
			print("\x1b[1;92m            "+find1)
			print("\x1b[1;97m="*45)
			print("\x1b[1;97mTulisan Arab: \n")
			for al in scrap.find_all('span', class_="ayat"):
				ayat += 1
				al = (al.text)
				print(f'\x1b[1;92m{str(ayat)}\x1b[1;91m.\x1b[1;97m {al.strip()}')
			print("\x1b[1;97m="*45)
			print("Cara Bacanya: \n")
			for bc in scrap.find_all('span', class_="bacaan"):
				bacaan += 1
				bc = (bc.text)
				print(f'\x1b[1;92m{str(bacaan)}\x1b[1;91m. \x1b[1;97m{bc.strip()}')
			print("\x1b[1;97m="*45)
			print("Artinya: \n")
			for ar in scrap.find_all('span', class_="arti"):
				arti += 1
				ar = (ar.text)
				print(f'\x1b[1;92m{str(arti)}\x1b[1;91m. \x1b[1;97m{ar.strip()}')
			print("="*45)
	except ValueError:
	        exit('\x1b[1;91m! \x1b[1;97mJangan Kosong')
	except IndexError:
	        exit('\x1b[1;91m! \x1b[1;97mIsi Yang Betul')

if __name__=='__main__':
	main()

# <!-- XIUZCODE | OPEN SOURCE TEAM
# <!-- THANKS TO ALL MEMBER XIUZCODE
