# use python3
try:
	import requests as r, os, re, random, threading, time
	from bs4 import BeautifulSoup as par
except ModuleNotFoundError:
	exit("[!] Module not installed\n")

url = "https://www.freewebhostingarea.com/"
ses = r.Session()
ua  = {"user-agent":"Mozilla/5.0 (Linux; Android 11; vivo 1904 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36"}

def animate(teks):
	lis = list("-\|/")
	for x in lis:
		print("\r["+x+"] "+teks+"... ", end="")
		time.sleep(0.15)

class Random:
	def __init__(self):
		self.lis = list("abcdefghijklmnopqrstuvwxyz1234567890")
		self.email_fake = ["@gmail.com","@yahoo.com"]

	def RandomDigit(self, digit):
		acak = [random.choice(self.lis) for _ in range(digit)]
		return "".join(acak)

	def RandomEmail(self):
		dig = self.RandomDigit(15)
		return dig+random.choice(self.email_fake)

def collect_domain():
	action = par(ses.get(url, headers=ua).text, "html.parser")
	formA = action.find("form")
	opt = re.findall("\<option value=\"(.*?\..*?)\">", str(formA))
	return formA["action"], opt

def create(subdo, email, pasw, action):
	dataData = {
		"action":"validate",
		"domainName":subdo,
		"email":email,
		"password":pasw,
		"confirmPassword":pasw,
		"agree":"1"
	}
	ses.post(action, data=dataData, headers=ua).text

def main():
	os.system("clear")
	print("""
 __      __.__
/  \    /  \  |__ _____
\   \/\/   /  |  \\\__  \\
 \        /|   Y  \/ __ \_
  \__/\  / |___|  (____  /
       \/       \/     \/ v0.2

        * Author: RizkyDev
        * Github: https://github.com/hekelpro
        * Thanks: All Member XiuzCode
""")
	name = input("[!] Name domain: ").replace(".","-").replace(" ","")
	action, option = collect_domain()
	print("") #-> Blok hehehe
	for opt in range(len(option)):
		print(" "*3,"["+str(opt+1)+"] "+option[opt])
	print("")
	chos = input("[?] Choose domain: ")
	while not chos.isdigit() or int(chos) > len(option):
		chos = input("[?] Choose domain: ")
	res = str(option[int(chos)-1])
	data1 = {
		"thirdLevelDomain":name,
		"domain":res,
		"action":"check_domain"
	}
	run1 = par(ses.post(action, data=data1, headers=ua).text, "html.parser")
	if "already created" in str(run1):
		exit("[!] This domain name already exists, please recreate it with a different domain name")

	action2 = run1.find("form")["action"]
	#-> Input email user
	email = input("\n[!] Manual/Default Email? (D/M): ").lower()
	while email == "":
		email = input("[!] Manual/Default Email? (D/M): ").lower()
	if email == "m":
		mail = input("[!] Input Your Email: ")
		while mail == "" or "@" not in mail:
			mail = input("[!] Input Your Email: ")
	else:
		mail = Random().RandomEmail()
		print("[!] Your Email: "+str(mail))

	#-> Input Password user
	pas = input("\n[!] Manual/Default Password? (D/M): ").lower()
	while pas == "":
		pas = input("\n[!] Manual/Default Password? (D/M): ").lower()
	if pas == "m":
		pasw = input("[!] Input Your Password: ")
		while pasw == "" or len(pasw) < 9:
			pasw = input("[!] Input Your Password: ")
	else:
		pasw = Random().RandomDigit(10)
		print("[!] Your Password: "+pasw)

	subdo = name+"."+res
	td = threading.Thread(name="created", target=create, args=(subdo,mail,pasw,action2,))
	td.start()
	while td.is_alive():
		animate("Processing")
	print("\n\n[CPANEL]: http://"+subdo+"/cpanel")
	print("        * username: "+subdo)
	print("        * password: "+pasw)
	print("\n[FTP]: http://"+subdo+"/ftp")
	print("     * host/server: "+subdo)
	print("     * username   : "+subdo)
	print("     * password   : "+pasw)
	print("\n[✓] success created account\n")

if __name__=="__main__":
	try:
		main()
	except Exception as ex:
		exit("\n[!] ERROR: "+str(ex)+"\n")
