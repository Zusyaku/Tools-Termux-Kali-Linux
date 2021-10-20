import requests,re,os,json,click,sys,logging
from bs4 import BeautifulSoup as Bs
from tqdm import tqdm
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

logging.basicConfig(level=logging.DEBUG)
ses=requests.Session()
retries = Retry(total=5, backoff_factor=1, status_forcelist=[ 502, 503, 504, 103 ])
ses.mount('http://', HTTPAdapter(max_retries=retries))
ses.mount('https://', HTTPAdapter(max_retries=retries))
info={
	'title':[],
}

def search(query):
	global pil
	c=1
	req=ses.get('http://149.56.24.226/?s='+query)
	bs=Bs(req.text, 'html.parser')
	hsl=bs.find_all('div',{'class':'col-xs-9 col-sm-10 search-content'})
	for i in hsl:
		tit=i.find('a',{'rel':'bookmark'})
		info['title'].append((tit.text, tit['href']))
	if len(info['title']) == 0:
		print("Tidak dapat menemukan judul film")
		return True
	
	print("\n\t[ Result ]")
	for x in info['title']:
		print(f"{c}. {x[0]}")
		c+=1

	pil=int(input("_> pilih: "))
	if pil <= 0:
		print("index out of ranges")
		return True

	print(" *Bypassing, please wait...")
	bypass(info['title'][pil-1][1], info['title'][pil-1][0])

def bypass(url,judul):
	cc=1
	req=ses.get(url)
	bs=Bs(req.text, 'html.parser')
	link=bs.find('a',{'class':'btn btn-success'})['href']
#	print(link)

	req2=ses.get(link)
	rg=re.findall(r'<frame src="(.*)">',req2.text)[0]
#	print(rg)

	blin=link.split('/')[2]
	req3=ses.get(f"http://{blin}{rg}")
	bs2=Bs(req3.text, 'html.parser')
	link2=bs2.find('a',{'target':'_parent'})['href']
#	print(link2)

	req4=ses.get(f"http://{blin}{link2}")
	rg2=re.findall(r'post\("(.*?)", {',req4.text)[0]
#	print(rg2)

	blin2=req4.url.split('/')[2]
#	print(blin2)
	head={
	'Host':blin2,
	'accept':'*/*',
	'origin':f'http://{blin2}',
	'x-requested-with':'XMLHttpRequest',
	'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
	'content-type':'application/x-www-form-urlencoded;charser=UTF-8',
	'referer':link2,
	'accept-encoding':'gzip, deflate, br',
	'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
	}
	req5=ses.post(f"http://{blin2}{rg2}",headers=head)
#	print(req5.text)
	try:
		rg3=re.findall(r'https://layarkacaxxi.icu/f/(.*?)"',req5.text)[0]
	except:
		print("\n !Failed to bypass")
		tan=input("[?] Anda ingin melanjutkannya ke website layarkaca21 (y/n) ")
		if tan.lower() == 'y':
			click.launch(info['title'][pil-1][1])
		else:
			sys.exit("okay bye bye:*")
#	print(rg3)

	req6=ses.get(f'https://layarkacaxxi.icu/f/{rg3}')
	try:
		rg4=re.findall(r"post\('(.*?)', ",req6.text)[0]
	except:
		raise Exception("\nDCMATakedown: Video tidak tersedia")
#	print(rg4)

	req7=ses.post(f'https://layarkacaxxi.icu{rg4}')
	js=json.loads(req7.text)

	print("\n\t[ Resulution ]")
	for x in js['data']:
		print(f"{cc}. {x['label']}")
		cc+=1

	lih=int(input("_> pilih: "))
	if lih <= 0:
		print("index out of ranges")
		return True

	downld2(js['data'][lih-1]['file'], f"{judul} {js['data'][lih-1]['label']}")

def downld2(url,judul):
	r = ses.get(url, stream=True)
	total_size = int(r.headers.get('content-length', 0))
	print(f"\n# Downloading {judul}")
#	print(f"['{url}']")
	block_size = 1024
	t=tqdm(total=total_size, unit='iB', unit_scale=True)
	with open(f'result/{judul.replace("/",",")}.mp4','wb') as f:
		for data in r.iter_content(chunk_size=block_size):
			if data:
				t.update(len(data))
				f.write(data)
	t.close()
	if total_size != 0 and t.n != total_size:
		print("\n[Warn] Download GAGAL")
		tan=input("[?] anda ingin melanjutkannya ke website layarkaca21 (y/n) ")
		if tan.lower() == 'y':
			click.launch(info['title'][pil-1][1])
		else:
			sys.exit("okay bye bye:*")
	print('\n[OK] File saved in result\n')

if __name__ == "__main__":
	os.system('clear')
	print("""
	[ LayarKaca21 Downloader ]
	      | by: Noobie |
""")
	try:
		os.mkdir('result')
	except: pass

	try:
		que=input("query search: ")
		search(que)
	except Exception as Err:
		print(Err)
