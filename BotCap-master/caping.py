import requests,os,time,random,re,json

class Main:
	def __init__(self):
		self.cek()
		self.header={'Accept':'application/json',
		'Accept-Language':'in',
		'NETWORKSTATE':'FouthG',
		'User-Agent':'Mozilla/5.0 (Linux; Android 8.1.0; CPH1823 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.100 Mobile Safari/537.36;CapingNews/5.0.6',
		'Cookie':'u='+self.uid+'; n='+self.nid,
		'Market':'googleplay',
		'Appid':'1',
		'Content-Lenght':'0',
		'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
		'Host':'ai.caping.co.id',
		'Connection':'Keep-Alive',
		'Accept-Encoding':'gzip',
		'city':'Jakarta',
		}
		self.lay=float(input("[?] Delay (recomended: 10): "))
		print()
		self.rcode()
		for n,v in zip(self.newscode,self.vidcode):
			try:
				time.sleep(1)
				self.tuyul(n,v)
			except KeyboardInterrupt:
				exit("[Exit] Bye kak >//<")
			except:
				print("Something error: continue")
				continue

	def cek(self):
		try:
			ufile=open('user.txt','r').read()
			self.uid=re.findall(r'uid=(.*?)\n',ufile)[0]
			self.nid=re.findall(r'nid=(.*?)',ufile)[0]
		except:
			print("[!] File Userid Not Found")
			self.uid=input("[?] Your uid: ")
			self.nid=input("[?] Your nid: ")
			with open('user.txt','w') as wfile:
				wfile.write('uid='+self.uid+'\n'+'nid='+self.nid)

	def rcode(self):
		self.newscode=[]
		self.vidcode=[]
		rcd1=requests.post('https://ai.caping.co.id/news/getNewsList',headers=self.header)
		rcd2=requests.post('https://ai.caping.co.id/video/getVideoList',headers=self.header)
		if rcd1.status_code == 200 and rcd2.status_code == 200:
			js1=json.loads(rcd1.text)
			for n in js1['NewsListItems']:
				self.newscode.append(n['NewsId'])

			js2=json.loads(rcd2.text)
			for v in js2['VideoList']:
				self.vidcode.append(v['VideoListId'])
		else:
			if rcd1.status_code != 200 and rcd2.status_code != 200:
				exit(f"[!] requests timed out. error_code1:{rcd1.status_code}, error_code2:{rcd2.status_code}")
			elif rcd1.status_code != 200:
				exit(f"[!] requests timed out. error_code1:{rcd1.status_code}, error_code2:-")
			elif rcd2.status_code != 200:
				exit(f"[!] requests timed out. error_code1:-, error_code2:{rcd2.status_code}")

	def tuyul(self,nid,vid):
		res6=requests.get('https://ai.caping.co.id/v2/event/signin',headers=self.header)
		time.sleep(1)
		res7=requests.get('https://ai.caping.co.id/v2/event/random',headers=self.header)

		res1=requests.get('https://ai.caping.co.id/v2/event/share/code',headers=self.header)
		jsn1=json.loads(res1.text)
		print(f"[*] Share code  | status [{jsn1['message']}]")
		time.sleep(self.lay)

		res2=requests.get('https://ai.caping.co.id/v2/event/video/view/'+str(vid),headers=self.header)
		jsn2=json.loads(res2.text)
		print(f"[*] View video  | status [{jsn2['message']}]")
		time.sleep(self.lay)

		res3=requests.get('https://ai.caping.co.id/v2/event/news/view/'+str(nid),headers=self.header)
		jsn3=json.loads(res3.text)
		print(f"[*] Read news   | status [{jsn3['message']}]")
		time.sleep(self.lay)

		res4=requests.get('https://ai.caping.co.id/v2/event/share/click/push',headers=self.header)
		jsn4=json.loads(res4.text)
		print(f"[*] Push notif  | status [{jsn4['message']}]")
		time.sleep(self.lay)

		res5=requests.get('https://ai.caping.co.id/v2/event/share/news/'+str(nid),headers=self.header)
		jsn5=json.loads(res5.text)
		print(f"[*] Share news  | status [{jsn5['message']}]")

		res8=requests.get('https://ai.caping.co.id/v2/user/ccsp/detail',headers=self.header)
		jsn8=json.loads(res8.text)
		print(f"[!] Your coin: {jsn8['data']['coin']} | Total coin: {jsn8['data']['total_coin']}")
		print("="*40)
		time.sleep(self.lay)

os.system('clear')
_c='\033[96m'
_g='\033[92m'
_w='\033[97m'
_r='\033[91m'
print("""
%s\t#############################
\t#      %s[ NUYUL CAPING ]     %s#
\t#     %s[ BY KANG-NEWBIE ]    %s#
\t#############################
%sNote: Author tidak bertanggung jawab atas apapun yang terjadi pada akun/diri anda
%s"""%(_c,_g,_c,_g,_c,_r,_w))
try:
	while True:
		Main()
		lop=input("[?] Mau nuyul lagi (y/n) ")
		if lop.lower() == 'y':
			Main()
		elif lop.lower() == 'n':
			exit("Oke deh bambank:*")
		else:
			exit("GOBLOK!")
except Exception as F:
	print("[Err] %s"%(F))