#jangan ganti , hargai creator

import PORT
from PORT.albania import *
from PORT.argentina import *
from PORT.bangladesh import *
from PORT.brazil import *
from PORT.bulgaria import *
from PORT.canada import *
from PORT.china import *
from PORT.colombia import *
from PORT.germany import *
from PORT.india import *
from PORT.indonesia import *
from PORT.singapore import *
from PORT.thailand import *
from PORT.ukraine import *
from PORT.unitedkingdom import *
from PORT.unitedstates import *
import requests,os,re
from time import sleep


def main():
	os.system('clear')
	print """
 ____                             ____                           _             
|  _ \ _ __ _____  ___   _       / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
| |_) | '__/ _ \ \/ / | | |_____| |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
|  __/| | | (_) >  <| |_| |_____| |_| |  __/ | | |  __/ | | (_| | || (_) | |   
|_|   |_|  \___/_/\_\\__,  |      \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                     |___/"""
	print"==============================================================================="
	print"|                              Codec By : HVmbl3                              |"
	print"|                    Thanks buat team - Kanc0t Cyber Team                     |"
	print"|                        https://github.com/kancotdiq      - versi 1          |"
	print"==============================================================================="
	print "" 
	print "    [01] Albania"
	print "    [02] Argentina"
	print "    [03] Bangladesh"
	print "    [04] Brazil"
	print "    [05] Bulgaria"
	print "    [06] Canada"
	print "    [07] China"
	print "    [08] Colombia"
	print "    [09] Germany"
	print "    [10] India"
	print "    [11] Indonesia"
	print "    [12] Singapore"
	print "    [13] Thailand"
	print "    [14] Ukraine"
	print "    [15] United Kingdom"
	print "    [16] United States"
	print "    [99] Keluar"
	print ""
	select = input("proxy@select~#")
	if select == 1:
		albania()
	elif select == 2 :
		argentina()
	elif select == 3 :
		bangladesh()
	elif select == 4 :
		brazil()
	elif select == 5 :
		bulgaria()
	elif select == 6 :
		canada()
	elif select == 7 :
		china()
	elif select == 8 :
		colombia()
	elif select == 9 :
		germany()
	elif select == 10 :
		india()
	elif select == 11:
		indonesia()
	elif select == 12:
		singapore()
	elif select == 13:
		thailand()
	elif select == 14:
		ukraine()
	elif select == 15:
		unitedkingdom()
	elif select == 16:
		unitedstates()
	elif select == 99:
		print "Keluar ..."
		os.sys.exit()
	else:
		print "Pilihan tidak ada ..."
		sleep(1)
		print "Keluar ..."
		os.sys.exit()

				
if __name__ == "__main__":
	main()