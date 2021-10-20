import requests, os, sys, time
from bs4 import BeautifulSoup as BS
from PIL import Image
from io import BytesIO

#DEBUG#
#import logging
#logging.basicConfig(level=logging.DEBUG)

ses=requests.Session()

MAINDIR="/storage/emulated/0/Maid"
try:
	os.listdir("/storage/emulated/0")
except PermissionError:
	print("\033[97mNote: Program ini membutuhkan akses internal storage untuk menyimpan hasil download")
	os.system('termux-setup-storage')
	sys.exit()
except FileNotFoundError:
	MAINDIR="result"

try:
	os.mkdir(MAINDIR)
except: pass

def download(cap, url, title, num, pdf):
	MAINPATH=f"{MAINDIR}/{title}"
	PATH=f"{MAINPATH}/{cap[num-1]['cap']}"
	try:
		os.mkdir(MAINPATH)
	except: pass

	if pdf == False:
		try:
			os.mkdir(PATH)
		except: pass

	req=ses.get(url)
	bs=BS(req.text, "html.parser")
	img=bs.find_all("div", {"id": "all"})
	src=img[0].find_all("img")

	n=1
	imgs=[]
	for x in src:
		link=[x["data-src"].replace("//","https://") if x["data-src"][0:2] == "//" else x["data-src"]]
		proges=f"[#] Downloading \"{PATH.split('/')[-1]}/"+"{:02}.jpg\"".format(n)
		print(f"\r{proges}",end="",flush=True)
		if pdf == False:
			with open(f"{PATH}/"+"{:02}.jpg".format(n), "wb") as img:
				req=ses.get(link[0])
				img.write(req.content)
			n+=1
			if n > len(src):
				print(f"\r{' '*len(proges)}", end="", flush=True)
				print(f"\r[✓] Done {PATH.split('/')[-1]}", end="", flush=True)
		else:
			imgs.append(ses.get(link[0]).content)
			n+=1
	if pdf == True:
		print(f"\r{' '*len(proges)}",end="", flush=True)
		print("\r[*] Converting to pdf",end="",flush=True)
		cpdf=[]
		for i in imgs:
			cpdf.append(Image.open(BytesIO(i)).convert('RGB'))
		cpdf[0].save(f"{PATH}.pdf", save_all=True, append_images=cpdf[1:])
		print(f"\r[✓] Done {PATH.split('/')[-1]}   ",end="",flush=True)
	print()

def chap_dl(cap, pilih, title):
	tny=input("[?] Apakah anda ingin menconvert hasil download ke pdf (Y/T) ")
	if tny.lower() == "y":
		pdf=True
	else:
		pdf=False

	if "-" in pilih:
		pilih=pilih.split("-")
		if len(pilih) == 2 and pilih[1] != "":
			ran=range(int(pilih[0]), int(pilih[1])+1)
		else:
			ran=range(int(pilih[0]), len(cap)+1)
		for x in ran:
			download(cap, cap[x-1]["url"], title, x, pdf)
	else:
		download(cap, cap[int(pilih)-1]["url"], title, int(pilih), pdf)

def get_chap(manga):
	_cap=[]
	req=ses.get("https://mangaid.click/manga/"+manga)
	bs=BS(req.text, "html.parser")
	data=bs.find_all("h5", {"class":"chapter-title-rtl"})

	info=bs.find("dl", {"class":"dl-horizontal"})
	rate=info.find("div",{"class":"rating clearfix"})
	genre=", ".join([i.text for i in info.find_all("a")])
	print(f"[•Genre: {genre}•]\n[•Rating: {rate.text.strip()[:-1]}•]")
	time.sleep(2)

	n=0
	for x in data:
		nc=x.text.strip()
		_cap.append([n, nc, x.find("a")["href"]])
		n-=1
	_cap.sort()
	hasil=[{"cap":y[1], "url":y[2]} for y in _cap]
	return hasil

def cari(q):
	req=ses.get("https://mangaid.click/search?query="+q)
	return req.json()

try:
	os.system("clear")
	print("""\033[97m
        [ Maid ( Manga-id ) ]
             - noobie -      
""")
	query=input("Cari: ")
	hasil=cari(query)["suggestions"]
	if len(hasil) > 1:
		n=1
		for x in hasil:
			print(f'{n}. {x["value"]}')
			n+=1
		pil=int(input("Pilih: "))
		lih=hasil[pil-1]["data"]
		title=hasil[pil-1]["value"]
	elif len(hasil) == 1:
		lih=hasil[0]["data"]
		title=hasil[0]["value"]
	else:
		print("!¡ manga tidak tersedia ¡!")
		sys.exit()

	print(f"\n\033[96m[•{title}•]")
	cap=get_chap(lih)
	for y in range(len(cap)):
		print(f"[{y+1}] {cap[y]['cap']}")
	print(f"""[ {len(cap)} (Total) Chapter ditemukan ]

\033[97m[info]
# ketik (misalnya: 10-) untuk mendownload dari nomor 10 sampai akhir
# ketik (misalnya: 10-20) untuk mendownload dari nomor 10 sampai 20
# ketik angka saja tanpa garis untuk mendownload salah satu""")
	pilih=input("noobie/> ")
	chap_dl(cap, pilih, lih)
except Exception as err:
	print(f"Err: {err}")
