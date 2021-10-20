import argparse,sys,os,shutil,requests,click,json
from bs4 import BeautifulSoup as BS

#remove cache
try:
	shutil.rmtree("src/__pycache__")
except: pass

class Main:
	def __init__(self):
		os.system('clear')
		self.p_link="https://pastebin.com/api/api_post.php"
		self.s_link="https://sfile.mobi/guest.php"
		self.o_link="https://api.openload.cc/upload"

	def upastebin(self):
		print("""
	#####################
	# PASTEBIN UPLOADER #
	#         BY        #
	#     KANG-NEWBIE   #
	#####################
		""")
		dev_key="2bc4f0b150bcd8abc2eb08851b558299"
		user_key="" #input your user key to upload file in your account
		paste_code=open(args['file'],'r').read()
		paste_format=input("[?] format file: ")
		paste_name=input("[?] paste name: ")
		print("\n[!] Uploading your file")
		req=requests.post(self.p_link,data={'api_paste_format':paste_format,'api_option':'paste','api_user_key':user_key,'api_paste_private':'0','api_paste_name':paste_name,'api_paste_expire_date':'N','api_dev_key':dev_key,'api_paste_code':paste_code})
		print(f"[Result] {req.text}")
		ans=input("[?] do you want open link on browser (y/n) ")
		if ans.lower() == 'y':
			click.launch(req.text)

	def upload(self):
		print("""%s
   `.-//////`         `+/:/://:`   
 `:+o++++++++:/-`   `:/++++++++/-` 
`+++o:..---++++s:.::////.....-////`
+++o/.      ---.-/+///-       .+///	%sOPENLOOAD UPLOADER%s
o++o-        `-/++//-`        -+///	%sBY: KANG-NEWBIE%s
o++o:.      -/+++:/+/:.       .+//+
`+o+++:...-/+++o: ./////..../+////`
 `:/+++++++++:/-`   .:/+++++++++-` 
    ``-////``         ``//:/-```   
%s    """%('\033[96m','\033[94m','\033[96m','\033[92m','\033[96m','\033[97m'))
		print("[!] Uploading your file")
		try:
			with open(args['file'],'r').read() as _try:
				pass
			mtd='r'
		except:
			mtd='rb'
		with open(args['file'],mtd) as files:
			req=requests.post(self.o_link,files={'file':files},headers={'x-requested-with':'XMLHttpRequest'})
			jsn=json.loads(req.text)
			if 'true' in req.text:
				print("[OK] Success")
				print("\n[URL]",jsn['data']['file']['url']['short'])
				print("[SIZE]",jsn['data']['file']['metadata']['size']['readable'])
				tanya=input("\n[?] do you want open link on browser (y/n) ")
				if tanya.lower() == 'y':
					click.launch(jsn['data']['file']['url']['short'])
			else:
				print("[!!]",jsn['error']['code']+":",jsn['error']['message'])

	def upsfile(self):
		print("""
`````.:::///+osyyyyyyyyyysoo++//:-.`````
`````.-:/+yyhhhhhhhhhhhhhhhhyyo/:-.`````
``````/shhhhhhhhhhhhhhhhhhhhhhhhs/``````
````-yhhhhhhhhhhhhhhhhhhhhhhhhhhhhy-````
.`-/hhhhhhhhhhhhs/----/shhhhhhhhhhhh/.`.
-:ohhhhhhhhhhhhdo-    -odhhhhhhhhhhhho:.
-oyhhhhhhhhhhhhdo-    -odhhhhhhhhhhhhyo-
+yhhhhhhhhhhs/-:-`    `.:-:ohhhhhhhhhhy+
shhhhhhhhhhhhs/`         :shhhhhhhhhhhhs
yhhhhhhhhhhhhddo.      .+ddhhhhhhhhhhhhy
yhhhhhhs/---..-hh+.  .+yh:...--/shhhhhhy
shhhhhho- .+ssoyhhs::shhyoss+. .ohhhhhhy
+yhhhhho- .shhhhhhhhhhhhhhhhy- .ohhhhhy+
:oyhhhho- .shyyyyyyyyyyyyyyhs- .ohhhhhs-
.:ohhhho- `..................` .ohhhhs/.
.`./hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh+-`.
````-yhhhhhhhhhhhhhhhhhhhhhhhhhhhhy:```.
`````.+shhhhhhhhhhhhhhhhhhhhhhhhs+.`````
`````.:/+oyyhhhhhhhhhhhhhhhhyyo/:-.`````
`````.:////+oosyyyyyhhyyyss+//::::.`````
     [SFILE UPLOADER BY KANG-NEWBIE]
		""")
		print("\n[!] Uploading your files")
		try:
			with open(args['file'],'r').read() as _try:
				pass
			mtd='r'
		except:
			mtd='rb'
		with open(args['file'],mtd) as files:
			req=requests.post(self.s_link,data={'cat':'4'},files={'file1':files},headers={'x-requested-with':'XMLHttpRequest'})
			bs=BS(req.text,'html.parser')
			if 'error' in req.text:
				er=bs.find('div',{'class':'error'})
				print(f"[Err] {er.text[:-7]}")
			else:
				su=bs.find('input')
				print(f"[OK] URL: {su['value']}")
				ans=input("[?] do you want open link on browser (y/n) ")
				if ans.lower() == 'y':
					click.launch(su['value'])


def example():
	print("""
Name Menu 	Description
-----------------------------
openload	max size:20GB & unlimited bandwidth
sfile		max size:100MB & can't upload audio
pastebin	maz size:Unknow & only for text file formats
""")
	print(f"Example: {sys.argv[0]} -f test.txt --up openload")

def help_():
	global args
	parser = argparse.ArgumentParser(description=example())
	parser.add_argument('-f','--file', help='path to File',required=True)
	parser.add_argument('--up',dest='name menu', help='uploading your file',required=True)
	args = vars(parser.parse_args())

print("""
   _   _   _   _   _   _   _   _   _   _  
  / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ 
 ( M ( Y ( U ( P ( L ( O ( A ( D ( E ( R )
  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
                  / \ / \                 
                 ( B ( Y )                
   _   _   _   _  \_/ \_/  _   _   _   _  
  / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ 
 ( K ( A ( N ( G ( N ( E ( W ( B ( I ( E )
  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
  """)
help_()
run=Main()
try:
	if args['name menu'].lower() == 'sfile':
		run.upsfile()
	elif args['name menu'].lower() == 'openload':
		run.upload()
	elif args['name menu'].lower() == 'pastebin':
		run.upastebin()
	else:
		exit("[!] see the menu!")
except Exception as Err:
	print("[Err] %s"%(Err))
