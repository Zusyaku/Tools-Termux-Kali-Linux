#!/usr/bin/env python



from __future__ import absolute_import
from __future__ import print_function
import sys, os, time, signal, webbrowser, platform, subprocess
from six.moves import input

#~~~~ Keybord interruption ~~~~
def signal_handler(signal, frame):
		KURO()
		LOGO()
		print('\033[1;m [\033[1;31mX\033[1;m] You pressed Ctrl+C!')
		time.sleep(2)
		EXITMENU()
signal.signal(signal.SIGINT, signal_handler)

#~~~ Function KURO ~~~~
def KURO():
	if os.name == 'nt':
            os.system('cls')
	else:
            os.system('clear')

#~~~~ M E N U ~~~~
def LOGO():
	KURO()

print('==========================================')
print('       Searching for Users (v3)           ') 
print('==========================================')

def menu():

	LOGO()
	time.sleep(1) 
	print("""\033[1;37m
	1. Name (New)
	2. Phone number
	3. picture (New)
	4. IP
	5. snapchat falah
	\033[1;m""")

	OPT = input("  Select: ")
	if OPT == "1":
         ID()
	elif OPT == "2":
		 PHONE()
	elif OPT == "3":
		 DEAD()
	elif OPT == "4":
		 IP()
	elif OPT == "5":
		KURO()
		webbrowser.open('https://www.snapchat.com/add/flaah999')
		menu()
	else:
		KURO()
		LOGO()
		print("\033[1;31m[ERROR]\033[1;m selection invalid!")
		time.sleep(3)
		menu()

def ID():
	KURO()
	LOGO()  
	time.sleep(1)
	Name = input(" Name: ")
	F_name = input(" First name: ")

	print("""\033[1;37m
 1. snapchat 	  10. Twitter
 2. Facebook      11. Beenverified
 3. Spokeo   	  12. Peoplelooker     
 4. instagram     13. Myspace 
 5. Linkedin      14. Pagesjaunes   
 6. Google plus   15. Libramemoria
 7. Tumblr        16. Avis-de-deces	 
 8. Youtube       17. SaveIG instagram 
 9. Peekyou       18. Save Twitter
==============================
        
		\033[1;m""")
	Tracker = input(" ")

	if Tracker == "1":
		KURO()
		webbrowser.open('https://www.snapchat.com/add/'+Name+''+F_name)
		time.sleep(2)
		menu()
	elif Tracker == "2":
		KURO()
		webbrowser.open('https://www.facebook.com/search/top/?init=quick&q='+Name+' '+F_name)
		time.sleep(2)
		menu()
	elif Tracker == "3":
		KURO()
		webbrowser.open('https://www.spokeo.com/'+Name+'-'+F_name)
		time.sleep(2)
		menu()
	elif Tracker == "4":
		KURO()
		webbrowser.open('https://www.instagram.com/explore/tags/'+Name+'')
		time.sleep(2)
		menu()
	elif Tracker == "5":
		KURO()
		webbrowser.open('https://fr.linkedin.com/pub/dir/'+Name+'/'+F_name)
		time.sleep(2)
		menu()
	elif Tracker == "6":
		KURO()
		webbrowser.open('https://plus.google.com/s/'+Name+' '+F_name+'/people')
		time.sleep(2)
		menu()
	elif Tracker == "7":
		KURO()
		webbrowser.open('https://www.tumblr.com/search/'+Name+'+'+F_name)
		time.sleep(2)
		menu()
	elif Tracker == "8":
		KURO()
		webbrowser.open('http://www.youtube.com/results?search_query='+Name+'+'+F_name)
		time.sleep(2)
		menu()
	elif Tracker == "9":
		KURO()
		webbrowser.open('https://www.peekyou.com/'+Name+'_'+F_name)
		time.sleep(2)
		menu()
	elif Tracker == "10":
		KURO()
		webbrowser.open('https://mobile.twitter.com/search?q='+Name+'+'+F_name)
		time.sleep(2)
		menu()
	elif Tracker == "11":
		KURO()
		webbrowser.open('https://www.beenverified.com/lp/e030ee/1/loading?utm_id=peekyou_Peekyou_Contact_Address_Results_Button&age=&bvid=&city=&fn='+Name+'&ln='+F_name)
		time.sleep(2)
		menu()
	elif Tracker == "12":
		KURO()
		webbrowser.open('https://www.peoplelooker.com/lp/5ee6b8/1/loading?utm_id=peekyou_peekyou_PL_phonebook_widget_web&fn='+Name+'&ln='+F_name+'&city=&state=&age=&bvid=&utm_source=peekyou&utm_medium=channel_partner&utm_campaign=peekyou_PL_phonebook_widget_web&utm_content=static#.')
		time.sleep(2)
		menu()
	elif Tracker == "13":
		KURO()
		webbrowser.open('https://myspace.com/search?q='+Name+' '+F_name)
		time.sleep(2)
		menu()
	elif Tracker == "14":
		KURO()
		webbrowser.open('https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui='+Name+'+'+F_name)
		time.sleep(2)
		menu()
	elif Tracker == "15":
		KURO()
		webbrowser.open('http://www.libramemoria.com/avis/?Nom='+Name+'&Prenom='+F_name)
		time.sleep(2)
		menu()
	elif Tracker == "16":
		KURO()
		webbrowser.open('https://www.avis-de-deces.net/avis/par-nom/?lastname='+Name+'&firstname='+F_name)
		time.sleep(2)
		menu()
	elif Tracker == "17":
		KURO()
		webbrowser.open('https://downloadgram.com')
		time.sleep(2)
		menu()
	elif Tracker == "18":
		KURO()
		webbrowser.open('https://download-twitter-videos.com/ar/')
		time.sleep(2)
		menu()
	elif Tracker == "00":
		KURO()
		webbrowser.open('https://pipl.com/search/?q='+Name+'+'+F_name)
		time.sleep(2)
		webbrowser.open('https://www.facebook.com/search/top/?init=quick&q='+Name+' '+F_name)
		time.sleep(2)
		webbrowser.open('https://www.spokeo.com/'+Name+'-'+F_name)
		time.sleep(2)
		webbrowser.open('https://www.flickr.com/search/people/?username='+Name+' '+F_name)
		time.sleep(2)
		webbrowser.open('https://www.linkedin.com/pub/dir/'+Name+'/'+F_name)
		time.sleep(2)
		webbrowser.open('https://plus.google.com/s/'+Name+' '+F_name+'/people')
		time.sleep(2)
		webbrowser.open('https://www.tumblr.com/search/'+Name+'+'+F_name)
		time.sleep(2)
		webbrowser.open('http://www.youtube.com/results?search_query='+Name+'+'+F_name)
		time.sleep(2)
		webbrowser.open('https://www.peekyou.com/'+Name+'_'+F_name)
		time.sleep(2)
		webbrowser.open('https://twitter.com/search?f=users&vertical=default&q= '+Name+' '+F_name)
		time.sleep(2)
		webbrowser.open('https://www.beenverified.com/lp/e030ee/1/loading?utm_id=peekyou_Peekyou_Contact_Address_Results_Button&age=&bvid=&city=&fn='+Name+'&ln='+F_name)
		time.sleep(2)
		webbrowser.open('https://www.peoplelooker.com/lp/5ee6b8/1/loading?utm_id=peekyou_peekyou_PL_phonebook_widget_web&fn='+Name+'&ln='+F_name+'&city=&state=&age=&bvid=&utm_source=peekyou&utm_medium=channel_partner&utm_campaign=peekyou_PL_phonebook_widget_web&utm_content=static#.')
		time.sleep(2)
		webbrowser.open('https://myspace.com/search?q='+Name+' '+F_name)
		time.sleep(2)
		webbrowser.open('https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui='+Name+'+'+F_name)
		time.sleep(2)
		webbrowser.open('http://www.libramemoria.com/avis/?Nom='+Name+'&Prenom='+F_name)
		time.sleep(2)
		webbrowser.open('https://www.avis-de-deces.net/avis/par-nom/?lastname='+Name+'&firstname='+F_name)
		time.sleep(2)
		menu()
	elif Tracker == "99":
		KURO()
		webbrowser.open('https://mobile.twitter.com/0xfff0800')
		time.sleep(2)
		menu()
	elif Tracker == "0":
		KURO()
		EXITMENU()
	else:
		KURO()
		LOGO()
		print("\033[1;31m[ERROR]\033[1;m selection invalid!")
		time.sleep(3)
		menu()

def PHONE():
	KURO()
	LOGO()  
	time.sleep(1)
	Num = input(" Number: ")

	print("""\033[1;37m
  1. Okcaller        
  2. Facebook     
  3. France-inverse   
  4. Whitepages     
  5. KSA-Numbers            
  6. Canada411      
  7. Pagesjaunes     
 
		\033[1;m""")
	Tracker = input("")

	if Tracker == "1":
		KURO()
		webbrowser.open('http://www.okcaller.com/'+Num)
		time.sleep(2)
		menu()
	elif Tracker == "2":
		KURO()
		webbrowser.open('https://www.facebook.com/search/top/?init=quick&q='+Num)
		time.sleep(2)
		menu()
	elif Tracker == "3":
		KURO()
		webbrowser.open('http://www.france-inverse.com/annuaire-inverse/'+Num)
		time.sleep(2)
		menu()
	elif Tracker == "4":
		KURO()
		webbrowser.open('https://www.whitepages.com/phone/'+Num)
		time.sleep(2)
		menu()
	elif Tracker == "5":
		KURO()
		webbrowser.open('https://storage.googleapis.com/ksa-n/index.html')
		time.sleep(2)
		menu()
	elif Tracker == "6":
		KURO()
		webbrowser.open('http://canada411.pagesjaunes.ca/fs/'+Num)
		time.sleep(2)
		menu()
	elif Tracker == "7":
		KURO()
		webbrowser.open('https://www.pagesjaunes.fr/annuaireinverse/recherche?quoiqui='+Num)
		time.sleep(2)
		menu()
	elif Tracker == "00":
		KURO()
		webbrowser.open('http://www.okcaller.com/'+Num)
		time.sleep(2)
		webbrowser.open('https://www.facebook.com/search/top/?init=quick&q='+Num)
		time.sleep(2)
		webbrowser.open('http://www.france-inverse.com/annuaire-inverse/'+Num)
		time.sleep(2)
		webbrowser.open('https://www.whitepages.com/phone/'+Num)
		time.sleep(2)
		webbrowser.open('https://www.anywho.com/phone/'+Num)
		time.sleep(2)
		webbrowser.open('http://canada411.pagesjaunes.ca/fs/'+Num)
		time.sleep(2)
		webbrowser.open('https://www.pagesjaunes.fr/annuaireinverse/recherche?quoiqui='+Num)
		time.sleep(2)
		menu()
	elif Tracker == "99":
		KURO()
		menu()
	elif Tracker == "0":
		KURO()
		EXITMENU()
	else:
		KURO()
		LOGO() 
		print(" selection invalid!")
		time.sleep(3)
		menu()

def DEAD():
	KURO()
	LOGO()
	
	print("""\033[1;37m
 
  1. yandex  
  2. bing
  3. labnol 
=============================

		\033[1;m""")
	Tracker = input(" ")
	if Tracker == "1":
		KURO()
		webbrowser.open('https://www.yandex.com/images/')
		time.sleep(2)
		menu()
	elif Tracker == "2":
		KURO()
		webbrowser.open('https://www.bing.com/visualsearch?FORM=IDPSBC')
		time.sleep(2)
		menu()
	elif Tracker == "3":
		KURO()
		webbrowser.open('https://www.labnol.org/internet/mobile-reverse-image-search/29014/')
		time.sleep(2)
		menu()
	elif Tracker == "00":
		KURO()
		time.sleep(2)
		webbrowser.open('http://www.libramemoria.com/avis/?Nom='+Name+'&Prenom='+F_name)
		time.sleep(2)
		webbrowser.open('https://www.avis-de-deces.net/avis/par-nom/?lastname='+Name+'&firstname='+F_name)
		time.sleep(2)
		webbrowser.open('http://enmemoria.lavanguardia.com/buscar?keywords='+Name+'+'+F_name+'&type=death&_fstatus=search')
		time.sleep(2)
		menu()
	elif Tracker == "99":
		KURO()
		menu()
	elif Tracker == "0":
		KURO()
		EXITMENU()
	else:
		KURO()
		LOGO()
		print(" selection invalid!")
		time.sleep(3)
		menu()

def IP():
	KURO()
	LOGO()
	ip = input(" Ip:")

	print("""\033[1;37m
 
  1. G-force 
  2. whatismyipaddress
  3. Whois

==============================

		\033[1;m""")	
	Tracker = input(" ")
	if Tracker == "1":
		KURO()
		webbrowser.open('https://www.g-force.ca/en/hosting/ip-whois?ip='+ip)
		time.sleep(2)
		menu()
	elif Tracker == "2":
		KURO()
		webbrowser.open('http://whatismyipaddress.com/ip/'+ip)
		time.sleep(2)
		menu()
	elif Tracker == "3":
		KURO()
		webbrowser.open('https://dig.whois.com.au/ip/'+ip)
		time.sleep(2)
		menu()
	elif Tracker == "00":
		KURO()
		time.sleep(2)
		webbrowser.open('https://www.g-force.ca/en/hosting/ip-whois?ip='+ip)
		time.sleep(2)
		webbrowser.open('http://whatismyipaddress.com/ip/'+ip)
		time.sleep(2)
		webbrowser.open('https://dig.whois.com.au/ip/'+ip)
		time.sleep(2)
		menu()
	elif Tracker == "99":
		KURO()
		menu()
	else:
		KURO()
		LOGO()
		print(" selection invalid!")
		time.sleep(3)
		menu()

#~~~~ EXIT ~~~~
def EXITMENU():
	KURO()
	LOGO()
	time.sleep(1)
	print("\033[1;m Thanks for using Dr.falah\033[1;m")
	time.sleep(2)
	print()
	print("...Closing")
	time.sleep(1)
	KURO()
	sys.exit()
		
menu()
