# encoding: utf-8
"""
	   * author : RizkyDev
	   * github : https://github.com/hekelpro
	   * support: all member XiuzCode
"""

# <!-- library -->
import os, re, time, platform, sys, shutil

try:import requests as r
except:os.system("python3 -m pip install requests")

try:import progressbar
except:os.system("pip install progressbar2")

try:from bs4 import BeautifulSoup as par
except:os.system("python3 -m pip install bs4")

try: shutil.rmtree("__pycache__")
except: pass

# variable
url = "https://animasu.net/"
head = {"user-agent":"chrome"}

# check python version
if platform.python_version().split(".")[0] != "3":
	exit("Use: python "+sys.argv[0])

# run code
def progress():
    return progressbar.ProgressBar(
        redirect_stdout=True,
        redirect_stderr=True,
        widgets=[
            progressbar.Percentage(),
            progressbar.Bar(),
            ' (',
            progressbar.AdaptiveTransferSpeed(),
            ' ',
            progressbar.ETA(),
            ') ',
        ])

def download(run, title):
	print("[•] Download "+title)
	save = title.split(" ")
	try:
		os.mkdir(save[0])
	except OSError:
		pass

	getv = r.get(run, headers=head, stream=True)
	with open(save[0]+"/"+title+'.mp4', 'wb') as f:
		total_length = int(getv.headers.get('content-length'))
		bar = progress()
		bar.start(total_length)
		readsofar = 0
		for chunk in getv.iter_content(chunk_size=1024):
			if chunk:
				readsofar += len(chunk)
				bar.update(readsofar)
				f.write(chunk)
				f.flush()
		bar.finish()
	
	return "\n[+] Save: "+save[0]+"/"+title+".mp4"

def getvideo(links, judul):
	reso, jml = [], 0

	if "uservideo.xyz" not in links:
		exit("[=] Maaf video tidak didukung untuk script ini\n")

	meh = par(r.get(links.replace("?embed=true",""), headers=head).text, "html.parser")
	if "form-gruop" in str(meh):
		for section in meh.find_all("section",{"class":"content"}):
			xe = par("".join(["".join(re.findall(r"\.innerHTML = '(.*?)';", str(sc))) for sc in section.find_all("script")]), "html.parser")
			for ambil in xe.find_all("div",{"class":"form-gruop"}):
				href = [geth.get("href") for geth in ambil.find_all("a")]
				reso.append(href[-1])

			print("[✓] Anime ini terdiri dari "+str(len(reso))+" part\n")
			for ep in reso:
				jml += 1
				sttus = download(ep,judul+" part-"+str(jml))
			print(sttus)
	else:
		for section in meh.find_all("section",{"class":"content"}):
			xe = par("".join(["".join(re.findall(r"\.innerHTML = '(.*?)';", str(sc))) for sc in section.find_all("script")]), "html.parser")
			href = "".join([geth.get("href") for geth in xe.find_all("a")])
			sttus = download(href, judul)
		print(sttus)

def getdata2(links):
	gas = par(r.get(links, headers=head).text, "html.parser")
	if "Segera Tayang" in "".join(re.findall("Status\:<\/b> <font color=\".*?\">(.*?)<\/font>", str(gas))):
		exit("[!] Streaming anime ini belum tersedia saat ini.\n    Visit: "+url+"\n")

	titel = gas.find("div",{"class":"releases"})
	titel = "".join(re.findall("\<h3>Episode\s(.*?)\s<font", str(titel)))

	for cek in gas.find_all("ul",{"id":"daftarepisode"}):
		if "Episode 1" in str(cek):
			ech = re.findall(r"\<span class=\"lchx\">\<a href=\"(.*?)\">.*?<\/a><\/span>", str(cek))
			ech.sort()
			print("\n   [NOTE] film terdiri dari \x1b[1;91m"+str(len(ech))+"\x1b[1;97m episode\n          Yakin untuk download semuanya?")
			yakin = input("\n   [****] Mau sampai berapa episode?\n          Enter untuk download semua episode\n          Input: ")
			try:
				while int(yakin) > int(len(ech)):
					yakin = input("          input: ")
			except:
				pass
			if yakin == "":
				print("\n[!] Tunggu sebentar")
				for x in range(len(ech)):
					ngeget = par(r.get(ech[int(x)], headers=head).text, "html.parser")
					ngefind = ngeget.find("iframe")["src"].replace("?embed=true&autoplay=true","")
					getvideo(ngefind, titel+" Episode "+str(x+1))
			elif yakin.isdigit():
				print("\n[!] Tunggu sebentar")
				ngeget = par(r.get(ech[int(yakin)-1], headers=head).text, "html.parser")
				ngefind = ngeget.find("iframe")["src"].replace("?embed=true&autoplay=true","")
				getvideo(ngefind, titel+" Episode "+str(yakin))
		else:
			ech = "".join(re.findall(r"\<span class=\"lchx\">\<a href=\"(.*?)\">.*?<\/a><\/span>", str(cek)))
			print("\n[!] Tunggu sebentar")
			ngeget = par(r.get(ech, headers=head).text, "html.parser")
			ngefind = ngeget.find("iframe")["src"].replace("?embed=true&autoplay=true","")
			getvideo(ngefind, titel)

def getdata(links, query):
	os.system('clear')
	exec(open(".banner","r").read())

	if re.search("[0-9]+", str(links)) is None:
		pageP = "1"
	else:
		pageP = "".join(re.findall("[0-9]", str(links)))

	STFU, no, title = [], 0, []
	query = query.replace(" ","+")
	gas = par(r.get(url+links+query, headers=head).text, "html.parser")
	pageN = [num.text for num in gas.find_all("a",{"class":"page-numbers"})]
	if "Judul yang Anda cari tidak ditemukan" in str(gas):
		exit("[?] Judul yang Anda cari tidak ditemukan\n")
	elif "page-numbers" in str(gas):
		for bsx in gas.find_all("div",{"class":"bsx"}):
			no += 1
			STFU.append(bsx.find("a")["href"])
			judul = bsx.find("div",{"class":"tt"}).text.strip()
			sttus = bsx.find("span",{"class":"sb"}).text.strip()
			if "✓" in sttus:
				sttus = "\x1b[1;92m"+sttus.split(" ✓")[0]+"\x1b[1;97m"
			elif "🔥🔥🔥" in sttus:
				sttus = "\x1b[1;93m"+sttus.replace("🔥🔥🔥","Sedang tayang")+"\x1b[1;97m"
			elif "⏳" in sttus:
				sttus = "\x1b[1;96m"+sttus.replace("⏳","Segera tayang")+"\x1b[1;97m"
			print(" "*3,"["+str(no)+"] "+judul+" | "+sttus)
		if "Sebelumnya" in pageN[-2]:
			pagen = str(pageP)
		else:
			pagen = str(pageN[-2])
		cek = input("\n["+str(pageP)+"/"+pagen+"] * [P] Previous | [N] Next\n[CHOOSE]=> ")
		if re.search("[0-9]+", str(cek)) is not None:
			try:
				chekk = STFU[int(cek) - 1]
			except:
				exit("[×] Angka tidak dapat ditemukan\n")
			getdata2(chekk)
		elif cek in list("Pp"):
			if "prev page-numbers" in str(gas):
				ret = gas.find("a",{"class":"prev page-numbers"})["href"].replace("https://animasu.net/","").replace(query,"")
			else:
				ret = "page/"+gas.find("span",{"class":"page-numbers current"}).text+"/?s="
			getdata(ret.replace("pge","page"),query)
		elif cek in list("Nn"):
			try:
				ret = gas.find("a",{"class":"next page-numbers"})["href"].replace("https://animasu.net/","").replace(query,"")
				getdata(ret.replace("pge","page"),query)
			except TypeError:
				exit("[-] Page sudah habis\n")
		else:
			exit("[?] Menu '"+cek+"' tidak ada\n")
	else:
		for bsx in gas.find_all("div",{"class":"bsx"}):
			no += 1
			STFU.append(bsx.find("a")["href"])
			judul = bsx.find("div",{"class":"tt"}).text.strip()
			sttus = bsx.find("span",{"class":"sb"}).text.strip()
			if "✓" in sttus:
				sttus = "\x1b[1;92m"+sttus.split(" ✓")[0]+"\x1b[1;97m"
			elif "🔥🔥🔥" in sttus:
				sttus = "\x1b[1;93m"+sttus.replace("🔥🔥🔥","Sedang tayang")+"\x1b[1;97m"
			elif "⏳" in sttus:
				sttus = "\x1b[1;96m"+sttus.replace("⏳","Segera tayang")+"\x1b[1;97m"
			print("["+str(no)+"] "+judul+" | "+sttus)
		pil = input("\n[?] Pilih: ")
		while not pil.isdigit() or pil in "0" or int(pil) > len(STFU):
			print("\n    <<= Failed =>>")
			pil = input("\n[?] Pilih: ")
		try:
			chekk = STFU[int(pil)-1]
		except:
			exit("[×] Angka tidak dapat ditemukan\n")
		getdata2(chekk)


if __name__ == "__main__":
	os.system('clear')

	exec(open(".banner","r").read())
	query = input("\x1b[1;97m[?] Search query: ")
	print("[!] Tunggu sebentar...")
	time.sleep(1)
	try:
		getdata("?s=",query)
	except Exception as error:
		exit("\n\n[ERROR]=| "+str(error))
