import os,sys
import time
import json
import requests

######AUTH By ZeDD######
"""
IG : @rezadkim
WA : 0895611252563
"""
try:
	import requests
except ImportError:
	os.system('reset')
	rqs = raw_input('\033[1;91m[+] \033[1;92mPerlu install requests (y/t): ')
	if rqs =="":
		print "\033[1;91m[!] Jangan kosong"
		os.sys.exit()
	elif rqs =="y":
		os.system('pip2 install requests')
	elif rqs =="Y":
		os.system('pip2 install requests')
	elif rqs =="t":
		os.sys.exit()
	elif rqs =="T":
		os.sys.exit()
	else:
		print "\033[1;91m[!]\033[1;92m Pilih\033[1;93m (y/n)"
		time.sleep(1)
		os.sys.exit()

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0000.1)
		
logo ="""      \033[1;91m[\033[1;97mCreated by \033[1;96mZeDD\033[1;91m]
 \033[1;97m- _ \033[1;91m+-+-+-+-+-+-+-+-+-+
  \033[1;97m__-\033[1;93m|F|a|k|e|-|M|a|i|l|
 \033[1;97m--_ \033[1;92m+-+-+-+-+-+-+-+-+-+ \033[1;97m\033[4mTempGenerate\033[0m
"""
zedd = "@network-source.com"
zedd1 ="@myfavorite.info"
zedd2 ="@mailfavorite.com"
zedd3 ="@networkapps.info"
zedd4 ="@gift-link.com"
zedd5 ="@postemail.net"

def main():
	global zed
	os.system('reset')
	print logo
	print "\033[1;97mUse email valid \033[1;91m:"
	print "\033[1;97mUse - \033[1;92m jancok@network-source.com"
	print "\033[1;97mUse - \033[1;92m jancok@myfavorite.info"
	print "\033[1;97mUse - \033[1;92m jancok@mailfavorite.com"
	print "\033[1;97mUse - \033[1;92m jancok@networkapps.info"
	print "\033[1;97mUse - \033[1;92m jancok@gift-link.com"
	print "\033[1;97mUse - \033[1;92m jancok@postemail.net"
	print "\033[1;97m-Git\033[1;91m : \033[1;97mhttps://github.com/rezadkim"
	print
	mails = raw_input("\033[1;91m[+] \033[1;92mGenerate \033[1;91m: \033[1;97m")
	if zedd in mails:
		jalan('\033[1;91m[+]\033[1;92m Create Email \033[1;97m...')
		print('\033[1;91m[+]\033[1;92m Email\033[1;91m :\033[1;97m '+mails)
		zed = "https://temp-mail.org/en/?email="+mails+"&app=1"
	elif zedd1 in mails:
		jalan('\033[1;91m[+]\033[1;92m Create Email \033[1;97m...')
		print('\033[1;91m[+]\033[1;92m Email\033[1;91m :\033[1;97m '+mails)
		zed = "https://temp-mail.org/en/?email="+mails+"&app=1"
	elif zedd2 in mails:
		jalan('\033[1;91m[+]\033[1;92m Create Email \033[1;97m...')
		jalan('\033[1;91m[+]\033[1;92m Email\033[1;91m :\033[1;97m '+mails)
		zed = "https://temp-mail.org/en/?email="+mails+"&app=1"
	elif zedd3 in mails:
		jalan('\033[1;91m[+]\033[1;92m Create Email \033[1;97m...')
		print('\033[1;91m[+]\033[1;92m Email\033[1;91m :\033[1;97m '+mails)
		zed = "https://temp-mail.org/en/?email="+mails+"&app=1"
	elif zedd4 in mails:
		jalan('\033[1;91m[+]\033[1;92m Create Email \033[1;97m...')
		print('\033[1;91m[+]\033[1;92m Email\033[1;91m :\033[1;97m '+mails)
		zed = "https://temp-mail.org/en/?email="+mails+"&app=1"
	elif zedd5 in mails:
		jalan('\033[1;91m[+]\033[1;92m Create Email \033[1;97m...')
		print('\033[1;91m[+]\033[1;92m Email\033[1;91m :\033[1;97m '+mails)
		zed = "https://temp-mail.org/en/?email="+mails+"&app=1"
	elif mails =="":
		print"\033[1;91m[!] don't be empty"
		time.sleep(0.1)
		raw_input("\033[1;91m[ \033[1;97mEnter \033[1;91m]")
		main()
	else:
		print"\033[1;91m[!] invalid email"
		time.sleep(0.1)
		raw_input("\033[1;91m[ \033[1;97mEnter \033[1;91m]")
		main()
	print("\033[1;91m[+] \033[1;92mOpen inbox from url \033[1;91m:\033[1;97m https://temp-mail.org/en/?email="+mails+"&app=1")
	memek()

def memek():
	tanya = raw_input("\n\033[1;91m[+] \033[1;97mWant to make another email? \033[1;93m(y/n): ")
	if tanya =="":
		print"\033[1;91m[!] don't be empty"
		time.sleep(1)
		memek()
	elif tanya =="y":
		main()
	elif tanya =="Y":
		main()
	elif tanya =="n":
		exit()
	elif tanya =="N":
		exit()
	else:
		print "   Y/N"
		time.sleep(1)
		memek()
		
if __name__=="__main__":
	main()