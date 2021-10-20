#!usr/bin/python
#Author: KANG-NEWBIE

import requests, json, os

os.system('clear')
print("""
		+-+-+-+ +-+-+ +-+-+-+-+-+-+
		|C|E|K| |I|P| |P|U|B|L|I|K|
		+-+-+-+ +-+-+ +-+-+-+-+-+-+
""")
while True:
	try:
		r1=requests.get('https://ipapi.co/json/')
		print("Ini IP Kamu:",r1.json()['ip'])
		ip=input("Masukan IP: ")
		r=requests.get('https://ipapi.co/'+ip+'/json')
		j=json.loads(r.text)
		print("""
Ip 	       : {}
Kota 	       : {}
Wilayah        : {}
Kode Wilayah   : {}
Negara	       : {}
Nama Negara    : {}
Kode Benua     : {}
Latitude       : {}
Longitude      : {}
Zona Waktu     : {}
Code Telepon   : {}
Mata Uang      : {}
Bahasa	       : {}
Organisasi     : {}
""".format(j['ip'],j['city'],j['region'],j['region_code'],j['country'],j['country_name'],j['continent_code'],j['latitude'],j['longitude'],j['timezone'],j['country_calling_code'],j['currency'],j['languages'],j['org']))
	except KeyError:
		print("\nAlamat IP:",ip,"INVALID\n")
