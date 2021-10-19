import requests as r, os, threading
from time import sleep

ses = r.Session()

def animate(teks):
	load = list("\|-/")
	titk = [".   ","..  ","... "]
	for x,y in zip(load,titk):
		print("\r["+x+"] "+str(teks)+y, end="")
		sleep(1)

def get_data(id, type):
	run = ses.get("https://loader.to/ajax/download.php?start=1&end=1&format="+str(type)+"&url=https%3A%2F%2Fyoutu.be/"+id).json()
	cek = ses.get("https://loader.to/ajax/progress.php?id="+run["id"]).json()

	if "https://youtu.be" in run["title"]:
		return "invalid"
	else:
		while cek["text"] == "Initialising" or cek["text"] == "Downloading" or cek["text"] == "Converting":
			animate("Converting")
			cek = ses.get("https://loader.to/ajax/progress.php?id="+run["id"]).json()
		return cek["download_url"]

def download(url, save, ex):
	con = r.get(url)
	with open(save+ex, "wb") as sv:
		sv.write(con.content)

def main():
	os.system("clear")
	print("""
_____.___. __                .___.__
\__  |   |/  |_            __| _/|  |
 /   |   \   __\  ______  / __ | |  |
 \____   ||  |   /_____/ / /_/ | |  |__
 / ______||__|           \____ | |____/
 \/                           \/

     * Author: RizkyDev
     * Github: https://github.com/hekelpro
     * Team  : XiuzCode
""")
	url = input("[-] URL YouTube: ")
	if "youtu.be"not in url:
		print("[×] URL invalid!")
		sleep(2); main()
	pil = input("[+] Download Video or Audio? [V/A]: ")
	while pil == "":
		pil = nput("[+] Download Video or Audio? [V/A]: ")
	if pil.lower() == "v":
		func, senpai = "1080", ".mp4"
	elif pil.lower() == "a":
		func, senpai = "mp3", ".mp3"
	else:
		print("[×] List not found")
		sleep(2); main()

	try:
		cepat = get_data(url.replace("https://youtu.be/",""), func)
	except Exception as exr:
		exit("\n[!] ERROR: "+str(exr))
	if cepat == "invalid":
		exit("[×] Content not found\n")
	else:
		sv = input("\n[?] Save content: ").replace(" ","_")
		td = threading.Thread(name="download", target=download, args=(cepat,sv,senpai,))
		td.start()
		while td.is_alive():
			animate("is saving data")
		print("\n[✓] Done...\n    * result: "+sv+senpai+"\n")

if __name__ == "__main__":
	main()
