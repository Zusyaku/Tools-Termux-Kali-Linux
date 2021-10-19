#!/system/bin/python
#Coder by jimmyromanticdevil
#Recoder by ./Mr.Java404
#Date & Time 10/07/2017 [06:09]
#Team N45HT (Exploiting and Creativity)
import urllib2
import urllib
import sys
import time
import random
import re
import os
os.system("clear")
#Warna
B = '\033[1m' #Bold
R = '\033[31m' #Red
G = '\033[32m' #Green
Y = '\033[33m' #Yellow
BL = '\033[34m' #Blue
P = '\033[35m' #Purple
W = '\033[37m' #White
U = '\033[2m' #Underline
N = '\033[0m' #Normal
#Pastikan Proxy List 1 Dir Dengan Script Python Ini
proxy_list = "proxylist.txt"
bacod = ['Mozilla/4.0 (compatible; MSIE 5.0; SunOS 5.10 sun4u; X11)',
		   'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.2pre) Gecko/20100207 Ubuntu/9.04 (jaunty) Namoroka/3.6.2pre',
		   'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser;',
		   'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)',
		   'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1)',
		   'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6)',
		   'Microsoft Internet Explorer/4.0b1 (Windows 95)',
		   'Opera/8.00 (Windows NT 5.1; U; en)',
		   'amaya/9.51 libwww/5.4.0',
		   'Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)',
		   'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
		   'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
		   'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; ZoomSpider.net bot; .NET CLR 1.1.4322)',
		   'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; QihooBot 1.0 qihoobot@qihoo.net)',
		   'Mozilla/4.0 (compatible; MSIE 5.0; Windows ME) Opera 5.11 [en]']#Hargai Pembuat!.. Coding Ga Gampang!..
gblk = ['http://google.com','http://bing.com','http://facebook.com','http://twitter.com','http://yahoo.com']
print B+G+""
print " _     _           __"
print "| \   / |____     |_ |_____ __    __ _____"
print "|  \_/  |  - /     | |     |\ \  / /|     |"
print "|       |  _/      | | [-] | \ \/ / | [-] |"
print "| |\_/| |  \      _| |  _  |  \  /  |  _  |"
print "|_|   |_|_|_\ [] |___|_| |_|   \/   |_| |_|"
print B+R+""
print "   __   ___     __"
print "  /  | |   |   /  |"
print " / o | |   |  / o |"
print "/_   | | 0 | /_   |"
print "  |  | |   |   |  |"
print "  |__| |___|   |__|"
time.sleep(2)
print ''
print B+BL+'#-----------------------------------------#'
print B+R+'               \!/WARNING\!/'
print B+BL+'#-----------------------------------------#'
print B+W+'[x] Matikan Data Terlebih Dahulu dan Aktifkan Kembali'
print B+W+'[x] Pastikan Url Diawalinya Dengan http or https'
print B+W+'[x] Saat Memasukan [Url Visitor] Tidak Terlihat'
print B+W+'[x] Jika Kesalahan Dalam Url Silahkan Close Terminal and Open Kembali'
print B+W+'[x] Jika Saat Bot Sedang Berjalan Lalu [Proxy Error] Coba Matikan Data dan Nyalakan Kembali'
print B+BL+'#-----------------------------------------#'
print B+R+'               \!/WARNING\!/'
print B+BL+'#-----------------------------------------#'
ini_url = raw_input (B+Y+"[+] Masukan Url Visitor : ")
print ''
print B+Y+'[+] Url Visitor Anda => '+B+BL+'|'+B+W,ini_url
print B+BL+'#-----------------------------------------#'
def Autoclicker(proxy1):
    try:
	proxy = proxy1.split(":")
        print B+BL+"#-----------------------------------------#\n"+B+W+'[-]',proxy1, ""+B+P+"=> Process"+N
        time.sleep(2)
	proxy_set = urllib2.ProxyHandler({"http" : "%s:%d" % (proxy[0], int(proxy[1]))})
	opener = urllib2.build_opener(proxy_set, urllib2.HTTPHandler)
	opener.addheaders = [('User-agent', random.choice(bacod)),
						('Refferer', random.choice(gblk))]
	urllib2.install_opener(opener)
	f = urllib2.urlopen(ini_url)
	#187034
	if "google.com" in f.read():
	   print B+G+"[*] 200 OK"+"\n"+B+BL+"#-----------------------------------------#\n"+N
	else:
	   print B+R+"[*] Link Gagal Di Kunjungi !\n"+B+BL+"#-----------------------------------------#\n"+N
           print B+R+"[!] Proxy / Connection Failed\n"+B+BL+"#-----------------------------------------#\n"+N
    except:
           print B+R+"[!] Proxy Error\n"+B+BL+"#-----------------------------------------#\n"+N
           time.sleep(5)
           pass

def loadproxy():
    try:
	get_file = open(proxy_list, "r")
	proxylist = get_file.readlines()
	count = 0
        proxy = []
	while count < len(proxylist):
	      proxy.append(proxylist[count].strip())
	      count += 1
        for i in proxy:
            Autoclicker(i)
    except IOError:
	print B+W+"\n[-] Error : Proxy List Tidak Ditemukan / Belum Dibuat\n"+N
	sys.exit(1)
def main():
   print """
"""+N
   loadproxy()
if __name__ == '__main__':
    main()