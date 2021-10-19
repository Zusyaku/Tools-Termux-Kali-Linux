# _*_ coding=UTF-8 _*_
#Codded By BL4CK DR460N
"""
Tolong Jangan Di Recode Yaa Gan
W Udh Cape" Buat Tool Ini
Agan Bilang Ini Tool Gk Ada Faedah Nya
Tapi Hargai Karya Seseorang
Jangan Bilang Ini Hasil Recode
Sumpah Ini Hasil W Sendiri

Salam
@BL4CK_DR460N"""
import os,sys,requests,json,time
try:
	r=requests.get("https://pastebin.com/raw/ERE9sdeQ")
except requests.exceptions.ConnectionError:
	print ("\033[37m[\033[31m×\033[37m] \033[33mConnection Error\033[0m")
	sys.exit()
apk = r.text
url = "https://wsapi.simsimi.com/190410/talk/"
banner = """\033[31m
 ____        _    ____ _          _____
| __ )  ___ | |_ / ___| |__   __ |_   _|
|  _ \ / _ \| __| |   | '_ \ / _` || |\033[37m
| |_) | (_) | |_| |___| | | | (_| || |
|____/ \___/ \__|\____|_| |_|\__,_||_| \033[34mV2\033[33m
 [ AUTHOR  ] BL4CK DR460N
 [ VERSION ] V2 (new update)
 [  TEAM   ] WOLL CYBER TEAM"""

def bantuan():
	print ("""
info:
  author : BL4CK DR460N
  version: 2 ( new update )
  my team: Woll Cyber Team
  github : https://github.com/Bl4ckDr460n
==========================================
perintah/command:
  bantu    => untuk meminta bantuan
  keluar   => keluar program
  example:
    input  => hai
    output => hai juga

support saya:
  Youtube : Yt DR460N

Terima Kasih Sudah Install Tool Saya ^_^""")
def help():
	print ("""
info:
  author : BL4CK DR460N
  version: 2 ( new update )
  my team: Woll Cyber Team
  github : https://github.com/Bl4ckDr460n
==========================================
perintah/command:
  help     => to show commands
  exit     => exit program
  example:
    input  => hello
    output => hello too

support me:
  Youtube : Yt DR460N

Thanks To Using This Tool ^_^""")
def run_indo():
	m = ["|","/","-","\\"]
	for b in range(2):
		for t in m:
			sys.stdout.write("\r\033[37m[!] \033[33mMenghubungkan ke server \033[34m"+t)
			sys.stdout.flush()
			time.sleep(1)
def run_en():
	m = ["|","/","-","\\"]
	for b in range(2):
                for t in m:
                        sys.stdout.write("\r\033[37m[!] \033[33mConnecting server \033[34m"+t)
                        sys.stdout.flush()
                        time.sleep(1)
class menu:
	def __init__(self):
		os.system('clear')
		print (banner)
		print ("")
		self.menu_bahasa()
	def menu_bahasa(self):
		print ("\033[37m[1].Indonesian ")
		print ("\033[37m[2].English")
		print ("\033[37m[3].Keluar/Exit ")
		print ("")
		self.pilih()
	def pilih(self):
		try:
			p = raw_input("\033[37m[?] Chooice : \033[32m")
		except:
			pass
		else:
			if p in ["1","01"]:
				kamu = raw_input("\033[37m[?] Nama Kamu : \033[32m")
#				chat = raw_input("\033[37m[?] Nama Bot : \033[32m")
				chat = "SimSimi"
				bahasa = "id"
#				try:
				run_indo()
#				requests.g
				os.system('clear')
				print (banner)
				print ("\033[33m"+40*"=")
				while True:
					try:
						text = raw_input("\033[37m["+kamu+"]: \033[32m")
						res = main().run(text,bahasa)
						if res == "":
							print ("\033[37m[\033[31mERROR\033[37m]: \033[33mTidak Ada Respon")
						elif text in ["bantu","help"]:
							bantuan()
						elif text in ["exit","keluar"]:
							print ("\033[31m[-] Terima Kasih Sudah Menggunakan Tool Saya ^_^\033[0m")
							sys.exit()
						elif text == "":
							print ("\033[37m[\033[31m×\033[37m] \033[33mTolong isi text kamu")
						else:
							print ("\033[37m["+chat+"]: \033[32m%s"%(res))
					except KeyboardInterrupt: print ("")
					except EOFError: print ("")
					except ValueError: print ("\033[31m[-] ERROR: silahkan ketik kalimat anda ")
			elif p in ["2","02"]:
				you = raw_input("\033[37m[?] You Name : \033[32m")
#				chat = raw_input("\033[37m[?] Bot Name : \033[32m")
				chat = "SimSimi"
				bahasa = "en"
				run_en()
				os.system('clear')
                	        print (banner)
				print ("\033[33m"+40*"=")
				while True:
					try:
						text = raw_input("\033[37m["+you+"]: \033[32m")
						res = main().run(text,bahasa)
						if res == "":
							print ("\33[37m[\033[31mERROR\033[37m]: \033[33mNo Responses")
						elif text in ["help"]:
							help()
						elif text in ["keluar","exit"]:
							print ("\033[31m[-] Thanks To Run ^_^ \033[0m")
							sys.exit()
						elif text == "":
							print ("\033[37m[\033[31m×\033[37m] \033[33mPlease input your text")
						else:
							print ("\033[37m["+chat+"]: \033[32m%s"%(res))
					except KeyboardInterrupt: print ("")
                                	except EOFError: print ("")
	                                except ValueError: print ("\033[31m[-] ERROR: plesse input your text")
			elif p in ["3","03","exit","keluar"]:
				print ("\033[37m[ID] Terima Kasih Sudah Menggunakan Tool Ini^_^")
				print ("\033[37m[EN] Thanks To Using This Tool ^_^\033[0m")
			else:
				print ("\033[31m[EN] Please Input 1/2/3")
				print ("\033[31m[ID] Tolong Masukan 1/2/3")
				self.pilih()
class main:
	def run(self,text,bahasa):
		try:
			data = "{\n\t\"utext\": \"%s\", \n\t\"lang\": \"%s\" \n}"%(text,bahasa)
			headers = {'Content-Type':"application/json",'x-api-key':apk}
			r = requests.post(url,data=data,headers=headers)
			j = json.loads(r.text)
			try:
				respon = j['atext']
				return respon
			except KeyError:
				print ("\033[37m[\033[31m×\033[37m] \033[31mERROR: \033[32mWait Last Update")
				sys.exit()
		except requests.exceptions.ConnectionError:
			print ("\033[31m[×] No Connection")
if __name__ == '__main__':
	menu()
