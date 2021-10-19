# python 3.7
# author: Karjok Pangesty (https://github.com/karjok)
# dimodifikasi oleh KANG-NEWBIE (https://github.com/KANG-NEWBIE)
# source code: https://github.com/karjok/bukashop

import requests,json,os,sys,time,click,random
from bs4 import BeautifulSoup as BS
from multiprocessing.pool import ThreadPool

class Bukasop:
	def __init__(self):
		self.data=[]
		self.urls=[]
		self.head={'user-agent':'Opera/9.80 (Android; Opera Mini/12.0.1987/37.7327; U; pl) Presto/2.12.423 Version/12.16'}
		self.b='https://m.bukalapak.com'
		self.s='https://shopee.co.id/api/v2'
		self.banner()

	def banner(self):
		count=0
		urls=[]
		mod=random.randint(0,10)
		mod2=random.randint(0,10)
		os.system('clear')
		print(f'''\033[95m
     _          \033[0m __       _ \033[95m
    |_)    |  _ \033[0m(_ |_  _ |_)\033[95m
    |_)|_| |<(_|\033[0m__)| |(_)|  \033[95mfb.me/om.karjok
    |\033[0mBukalapak x Shopee price sorter
    
    MOD: \033[9{mod}mKANG-NEWBIE \033[9{mod2}m(t.me/kang_nuubi)\033[0m
    ''')
		self.q=input('[?] query: ')
		print("[!] tunggu sebentar gan...")
		self.bl()
		self.sp()
		self.data.sort()
		for i in self.data:
			if len(str(i[0])) <= 6:
				har=len(str(i[0]))-3
				harga=str(i[0])[:har]+'.'+str(i[0])[har:]
			elif len(str(i[0])) > 6:
				ha=len(str(i[0]))-3
				har=len(str(i[0]))-6
				harga=str(i[0])[:har]+'.'+str(i[0])[har:][:-3]+'.'+str(i[0])[ha:]
			print(f'''
nomor [{count+1}]
Produk : {i[1]}
Harga  : Rp{harga},-
Toko   : {i[2]}
++++++++++++++++++++++++++++++++++++++''')
			urls.append(i[3])
			count+=1
		print('\n[!] CTRL+C untuk keluar')
		while True:
			try:
				pil=int(input("[?] pilih no: "))
				print("Meluncur gann..");time.sleep(1)
				click.launch(urls[pil-1])
			except KeyboardInterrupt:
				exit("BYE BYE :*")

	def bl(self):
		url=[self.b+'/products?keywords='+self.q+'&search[sort_by]=_score:desc']
		no=0
		while True:
			if len(self.data) == 50:
				break		
			try:
				r=requests.get(url[no]).text
				bs=BS(r,'html.parser')
				no+=1
				for i in bs.find_all('article'):
					if len(self.data) == 50:
						break
					ur=self.b+i.get('data-url')
					nama=i.get('data-name')
					harga=i.find('div',{'class':'product-price'}).get('data-reduced-price')
					toko = '\033[95mBukalapak\033[0m'
					self.data.append((int(harga),nama,toko,ur))
				url.append(self.b+bs.find('a',{'class':'next_page'}).get('href'))
			except: break

	def sp(self):
		def res(r):
			try:
				rr = requests.get(f'https://shopee.co.id/api/v2/item/get?itemid={r[0]}&shopid={r[1]}').json()
				url = f'https://shopee.co.id/product-i.{r[1]}.{r[0]}'
				harga = round(rr['item']['price']/100000)
				nama = rr['item']['name']
				toko = '\033[93mShopee\033[0m'
				self.data.append((harga,nama,toko,url))
			except: pass
		q=self.q.replace(' ','%20')
		r=requests.get(self.s+'/search_items/?by=relevancy&keyword='+q+'&limit=50&newest=0&order=desc&page_type=search',headers=self.head).json()
		go = [(i['itemid'],i['shopid']) for i in r['items']]
		ThreadPool(15).map(res,go)

try:
	Bukasop()
except Exception as EF:
	print(f'Err: {EF}')
