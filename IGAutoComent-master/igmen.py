# Python3
# Author : KANG-NEWBIE (noobie)
# Version: 2.0

# Have fun and nice day ;) UwU

try:
	import requests,os,sys,time,readline,re
	from prompt_toolkit import prompt
except:
	import os,sys,time
	print("[!] requests or prompt_toolkit not installed\n[!] installing module requirement")
	time.sleep(1.5)
	os.system('python3 -m pip install requests prompt_toolkit;python3 '+sys.argv[0])
	sys.exit()
	
class Menig:
	def __init__(self):
		self.req=requests.Session()
		self.user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
		self.csrftoken = requests.get('https://www.instagram.com').cookies['csrftoken']
		self.login()

	def login(self):
		user=input("[In] Your Username: ")
		pas=prompt("[In] Your Password: ", is_password=True)
		self.log = self.req.post('https://www.instagram.com/accounts/login/ajax/', headers={
			'origin': 'https://www.instagram.com',
			'pragma': 'no-cache',
			'referer': 'https://www.instagram.com/accounts/login/',
			'user-agent': self.user_agent,
			'x-csrftoken': self.csrftoken,
			'x-requested-with': 'XMLHttpRequest'
			}, data={
			'username': user,
			'enc_password':f'#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{pas}',
			'queryParams': '{}'
			})

		print(self.log.text)

		if '"authenticated": true' in self.log.text:
			print("[✓] Login succesfully\n")
			self.grep()
		else:
			print("[X] Login failed. Try Again!")
			time.sleep(2)
			self.login()

	def grep(self):
		C=1
		myid=[]
		msg=input("[info] use '\\n' for new line comments\n[In] Commnets: ").replace('\\n','\n')
		count=int(input("[In] Commnets Loop: "))
		mauapa=input("[?] do you want spam specific post? [y/N] ")

		if mauapa.lower() == 'y':
			inlnk=input("[In] Link post: ")
			cek=self.req.get(inlnk)
			if "<title>\nInstagram\n</title>" in cek.text:
				print("[!] Invalid post url. Try again!\n")
				self.grep()
			mid=re.findall('"id":"..................[0-9]',cek.text)[0].replace('"id":"','')
			self.send(mid,msg,count)

		else:
			tar=input("[In] Target account: ")
			cek=self.req.get("https://www.instagram.com/"+tar)
			if "<title>\nInstagram\n</title>" in cek.text:
				print("[!] Invalid username. Try again!\n")
				self.grep()
			mid=re.findall('"id":"..................[0-9]',cek.text)
			if len(mid) == 0:
				print("[!] This account does not have any posts or maybe this is a private account. Try again!\n")
				self.grep()

			maugak=input(f"\nsuccess get [{len(mid)}] media id\n[?] want to spam all? [y/N] ")
			if maugak.lower() == 'y':
				for x in mid:
					self.send(x.replace('"id":"',''),msg,count,all=True)
				print("[✓] All done.\n")
				time.sleep(3)
				self.grep()
			else:
				for i in mid:
					print("#"+str(C),i.replace('"id":"',''))
					myid.append(i.replace('"id":"',''))
					C+=1
				pil=int(input("[In] Choice: "))
				self.send(myid[pil-1],msg,count)
		return True
#		sys.exit()

	def send(self,idku,msg,count,all=False):
		load = {'comment_text' : msg,
		'replied_to_comment_id=' : '',}
		head={'Accept': '*/*',
			'Accept-Language': 'en-US,en;q=0.5',
			'Accept-Encoding': 'gzip, deflate, br',
			'Host': 'www.instagram.com',
			'Referer': 'https://www.instagram.com/',
			'User-Agent': self.user_agent,
			'X-CSRFToken': self.log.cookies['csrftoken'],
			'csrftoken': self.log.cookies['csrftoken'],
			'X-Instagram-AJAX': '1',
			'Content-Type': 'application/x-www-form-urlencoded',
			'X-Requested-With': 'XMLHttpRequest',
			'Connection': 'close' }

		print()
		cc=1
		for i in range(count):
			preq = self.req.post('https://www.instagram.com/web/comments/{}/add/'.format(idku),headers=head,data=load)
			if preq.text == "Please wait a few minutes before you try again.":
				print(f"{cc}. Spam failed [{idku}]")
				for i in range(60):
					print(end=f"\r >> sleep {60-(i+1)}s << ",flush=True)
					time.sleep(1)
				print()
			elif '"status": "ok"' in preq.text:
				print(f"{cc}. Spam succesfully [{idku}]")
			else:
				print(preq.text)
			cc+=1
			time.sleep(5)

		if not all:
			print("[✓] All done.\n")
			time.sleep(3)
			self.grep()

try:
	os.system('clear')
	print("""\033[0;97m
		###########################
		# Instagram Auto Comments #
		###########################
		        <|noobie|>
		""")
	Menig()
except KeyboardInterrupt:
	sys.exit("\n\033[93mInterrupt: exit the program")
except Exception as Err:
	print(f"\033[91mError: {Err}")
