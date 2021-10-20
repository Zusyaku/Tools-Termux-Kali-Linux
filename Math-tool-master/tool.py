import math
import os
# Python 3

W  = '\033[0m'  # white (default)
R  = '\033[1;31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[1;33m' # orange
B  = '\033[1;34m' # blue
P  = '\033[1;35m' # purple
C  = '\033[1;36m' # cyan
GR = '\033[1;37m' # gray

def banner():


                                      
    print (C+'  _____     _   _      _____         _ ')
    print (' |     |___| |_| |_   |_   _|___ ___| |')
    print (' | | | | .\'|  _|   |    | | | . | . | |')
    print (' |_|_|_|__,|_| |_|_|    |_| |___|___|_|')
    print ('')
    print (W+' =========================['+O+' V.3.0 '+W+']=====')
    print ('')
    print (G+' By'+R+'   :'+W+' N1ght.Hax0r')
    print (G+' With'+R+' :'+W+' 5 Function')
    print ('')
    print (W+' =========['+O+' Code Your Freedom '+W+']=========')

def prima():
    num = int(input(G+' Masukkan Bilangan'+R+' > '+W))
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print (G+' Angka'+W, num ,R+' Bukan Bilangan Prima'+W)
                print (G+' Karena '+W, i ,G+' Dikali '+W, num//i ,R+' = '+W, num)
                break
        else:
            print (G+' Angka'+W, num ,G+' Adalah Bilangan Prima'+W)

    else:
        print (G+' Angka'+W, num ,R+' Bukan Bilangan Prima'+W)

def fakt(x):
    print ("")
    print (G+' Faktor Dari'+W+ x +G+' Adalah'+W)
    for i in range(1, x+1):
        if x % i == 0:
            print (" ", i)

def faktor():
    num = int(input(G+' Masukkan Bilangan'+R+' > '+W))
    fakt(num)

def mean():
    data = str(input(G+' Masukkan Data'+R+' > '+W))
    a = str(round(sum(data) / len(data), 2))
    print(G+' Mean'+R+' > '+W+ a)

def median():
    data = str(input(G+' Masukkan Data'+R+' > '+W))
    data.sort()
    if len(data) % 2 == 0:
        a = int(len(data) / 2)
        b = (data[a - 1] + data[a]) / 2
        median = str(b)

    else:
        a = int((len(data) + 1) / 2)
        median = str(data[a - 1])
        
    print(G+' Median'+R+' > '+W, median)

def modus():
    data = str(input(G+' Masukkan Data'+R+' > '+W))
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
    
    print(G+' Modus'+R+' > '+W, modus)

def keliling_persegi () :
    x= float(input(G+' Sisi'+R+' > '+W))
    keliling = 4*x
    print (' ' )
    print (G+' Keliling'+R+' > '+W, keliling ,G+'cm'+W)
    
def luas_kubik () :
	x=float(input(G+' Sisi'+R+' > '+W))
	luas= 6*x*x
	print (' ' )
	print (G+' Luas'+R+' > '+W, luas ,G+'cm2'+W)
    
def keliling_persegipanjang () :
    x= float(input(G+' Panjang'+R+' > '+W))
    y= float(input(G+' Lebar'+R+' > '+W))
    keliling = 2*(x+y)
    print (' ' )
    print (G+' Keliling'+R+' > '+W, keliling ,G+'cm'+W)
    
def luas_balok () :
	x= float(input(G+' Panjang'+R+' > '+W))
	y= float(input(G+' Lebar'+R+' > '+W))
	z= float(input(G+' Tinggi'+R+' > '+W))
	luas= 2*((x*y)+(x*z)+(y*z))
	print (' ' )
	print (G+' Luas'+R+' > '+W, luas ,G+'cm2'+W)
    
def volume_limas () :
	x= float(input(G+' Luas Alas'+R+' > '+W))
	y= float(input(G+' Tinggi'+R+' > '+W))
	volume = 1/3*x*y
	print (' ' )
	print (G+' Volume'+R+' > '+W, volume ,G+'cm3'+W)
	
def keliling_segitiga () :
    ab= float(input(G+' Panjang AB'+R+' > '+W))
    bc= float(input(G+' Panjang BC'+R+' > '+W))
    ca= float(input(G+' Panjang CA'+R+' > '+W))
    keliling = ab+bc+ca
    print (' ' )
    print (G+' Keliling'+R+' > '+W, keliling ,G+'cm'+W)
    
def luas_bola () :
	x = float(input(G+' Jari Jari'+R+' > '+W))
	luas = 4*22/7*x*x
	print ('')
	print (G+' Luas'+R+' > '+W, luas ,G+'cm2'+W)
              
def keliling_jajargenjang () :
    ab= float(input(G+' Panjang AB'+R+' > '+W))
    bc= float(input(G+' Panjang BC'+R+' > '+W))
    cd= float(input(G+' Panjang CD'+R+' > '+W))
    da= float(input(G+' Panjang DA'+R+' > '+W))
    keliling = ab+bc+cd+da
    print ('')
    print (G+' Keliling'+R+' > '+W, keliling ,G+'cm'+W)

def keliling_trapesium () :
    ab= float(input(G+' Panjang AB'+R+' > '+W))
    bc= float(input(G+' Panjang BC'+R+' > '+W))
    cd= float(input(G+' Panjang CD'+R+' > '+W))
    da= float(input(G+' Panjang DA'+R+' > '+W))
    keliling = ab+bc+cd+da
    print ('')
    print (G+' Keliling'+R+' > '+W, keliling ,G+'cm'+W)
             
def keliling_ketupat () :
    z= float(input(G+' Sisi'+R+' > '+W))
    keliling = 4*z
    print ('')
    print (G+' Keliling'+R+' > '+W, keliling ,G+'cm'+W)
    
def keliling_layang () :
	ab= float(input(G+' Panjang AB'+R+' > '+W))
	bc= float(input(G+' Panjang BC'+R+' > '+W))
	keliling = 2*(ab+bc)
	print (' ' )
	print (G+' Keliling'+R+' > '+W, keliling ,G+'cm'+W)

def luas_persegi () :
    x= float(input(G+' Sisi'+R+' > '+W))
    luas= x*x
    print (' ' )
    print (G+' Luas'+R+' > '+W, luas ,G+'cm2'+W)
    
def volume_kubik () :
    x=float(input(G+' Sisi'+R+' > '+W))
    volume= x*x*x
    print (' ' )
    print (G+' Volume'+R+' > '+W, volume ,G+'cm3'+W)
    
def luas_persegipanjang () :
    x= float(input(G+' Panjang'+R+' > '+W))
    y= float(input(G+' Lebar'+R+' > '+W))
    luas= x*y
    print (' ' )
    print (G+' Luas'+R+' > '+W, luas ,G+'cm2'+W)
    
def volume_balok () :
    x= float(input(G+' Panjang'+R+' > '+W))
    y= float(input(G+' Lebar'+R+' > '+W))
    z= float(input(G+' Tinggi'+R+' > '+W))
    volume= x*y*z
    print (' ' )
    print (G+' Volume'+R+' > '+W, volume ,G+'cm3'+W)
    
def luas_segitiga () :
    x= float(input(G+' Alas'+R+' > '+W))
    y= float(input(G+' Tinggi'+R+' > '+W))
    luas=0.5*x*y
    print (' ' )
    print (G+' Luas'+R+' > '+W, luas ,G+'cm2'+W)

def luas_lingkaran () :
    x = float(input(G+' Jari Jari'+R+' > '+W))
    luas = 22/7*x*x
    print ('')
    print (G+' Luas'+R+' > '+W, luas ,G+'cm2'+W)

def volume_bola () :
    x = float(input(G+' Jari Jari'+R+' > '+W))
    volume = 4/3*22/7*x*x*x
    print ('')
    print (G+' Volume'+R+' > '+W, volume ,G+'cm3'+W)
              
def luas_jajargenjang () :
    x= float(input(G+' Tinggi'+R+' > '+W))
    y= float(input(G+' Alas'+R+' > '+W))
    luas = x*y
    print ('')
    print (G+' Luas'+R+' > '+W, luas ,G+'cm2'+W)

def luas_trapesium () :
    x= float(input(G+' Sisi Atas'+R+' > '+W))
    y= float(input(G+' Sisi Bawah'+R+' > '+W))
    z= float(input(G+' Tinggi'+R+' > '+W))
    luas = (x+y)*z/2
    print ('')
    print (G+' Luas'+R+' > '+W, luas ,G+'cm2'+W)
             
def luas_ketupat () :
    x= float(input(G+' Diagonal 1'+R+' > '+W))
    y= float(input(G+' Diagonal 2'+R+' > '+W))
    luas = 0.5*x*y
    print ('')
    print (G+' Luas'+R+' > '+W, luas ,G+'cm2'+W)
    
def luas_layang () :
    x= float(input(G+' Diagonal 1'+R+' > '+W))
    y= float(input(G+' Diagonal 2'+R+' > '+W))
    luas = 0.5*x*y
    print (' ' )
    print (G+' Luas'+R+' > '+W, luas ,G+'cm2'+W)
	
def tanya_3M() :      
    print ('')
    print (G+' 01'+R+' :'+W+' Mean')
    print (G+' 02'+R+' :'+W+' Median')
    print (G+' 03'+R+' :'+W+' Modus')
    print ('')
    menu = int(input(G+' Menu '+R+'> '+W))

    if menu == 1 :
        mean()
    elif menu == 2 :
        median()
    elif menu == 3 :
        modus()
    else :
        banner()
def tanya_persegi():
    print ('')
    print (G+' 01'+R+' :'+W+' Keliling')
    print (G+' 02'+R+' :'+W+' Luas')
    print (G+' 03'+R+' :'+W+' Volume')
    print ('')
    ans='0'
    ans=str(input(G+' Menu '+R+'> '+W))
    if ans=='01'or ans=='1':
        keliling_persegi()
    
    elif ans=='02'or ans=='2':
        luas_persegi()

    elif ans=='03'or ans=='3':
        pilbangundatar()      
    else:
        print ('[!]==// Abort')
        exit()

def tanya_persegipanjang():
    print ('')
    print (G+' 01'+R+' :'+W+' Keliling')
    print (G+' 02'+R+' :'+W+' Luas')
    print (G+' 03'+R+' :'+W+' Volume')
    print ('')
    ans='0'
    ans=str(input(G+' Menu '+R+'> '+W))
    if ans=='01'or ans=='1':
        keliling_persegipanjang()
    
    elif ans=='02'or ans=='2':
        luas_persegipanjang()

    elif ans=='03'or ans=='3':
        pilbangundatar()      
    else:
        print ('[!]==// Abort')
        exit()

def tanya_layang():
    print ('')
    print (G+' 01'+R+' :'+W+' Keliling')
    print (G+' 02'+R+' :'+W+' Luas')
    print (G+' 03'+R+' :'+W+' Volume')
    print ('')
    ans='0'
    ans=str(input(G+' Menu '+R+'> '+W))
    if ans=='01'or ans=='1':
        keliling_layang()
    
    elif ans=='02'or ans=='2':
        luas_layang()

    elif ans=='03'or ans=='3':
        pilbangundatar()      
    else:
        print ('[!]==// Abort')
        exit()

def tanya_ketupat():
    print ('')
    print (G+' 01'+R+' :'+W+' Keliling')
    print (G+' 02'+R+' :'+W+' Luas')
    print (G+' 03'+R+' :'+W+' Volume')
    print ('')
    ans='0'
    ans=str(input(G+' Menu '+R+'> '+W))
    if ans=='01'or ans=='1':
        keliling_ketupat()
    
    elif ans=='02'or ans=='2':
        luas_ketupat()

    elif ans=='03'or ans=='3':
        pilbangundatar()      
    else:
        print ('[!]==// Abort')
        exit()

def tanya_trapesium():
    print ('')
    print (G+' 01'+R+' :'+W+' Keliling')
    print (G+' 02'+R+' :'+W+' Luas')
    print (G+' 03'+R+' :'+W+' Volume')
    print ('')
    ans='0'
    ans=str(input(G+' Menu '+R+'> '+W))
    if ans=='01'or ans=='1':
        keliling_trapesium()
    
    elif ans=='02'or ans=='2':
        luas_trapesium()

    elif ans=='03'or ans=='3':
        pilbangundatar()      
    else:
        print ('[!]==// Abort')
        exit()

def tanya_jajargenjang():
    print ('')
    print (G+' 01'+R+' :'+W+' Keliling')
    print (G+' 02'+R+' :'+W+' Luas')
    print (G+' 03'+R+' :'+W+' Volume')
    print ('')
    ans='0'
    ans=str(input(G+' Menu '+R+'> '+W))
    if ans=='01'or ans=='1':
        keliling_jajargenjang()
    
    elif ans=='02'or ans=='2':
        luas_jajargenjang()

    elif ans=='03'or ans=='3':
        pilbangundatar()      
    else:
        print ('[!]==// Abort')
        exit()

def tanya_segitiga():
    print ('')
    print (G+' 01'+R+' :'+W+' Keliling')
    print (G+' 02'+R+' :'+W+' Luas')
    print (G+' 03'+R+' :'+W+' Volume')
    print ('')
    ans='0'
    ans=str(input(G+' Menu '+R+'> '+W))
    if ans=='01'or ans=='1':
        keliling_segitiga()
    
    elif ans=='02'or ans=='2':
        luas_segitiga()

    elif ans=='03'or ans=='3':
        pilbangundatar()      
    else:
        print ('[!]==// Abort')
        exit()

def tanya_lingkaran():
    print ('')
    print (G+' 01'+R+' :'+W+' Keliling')
    print (G+' 02'+R+' :'+W+' Luas')
    print (G+' 03'+R+' :'+W+' Volume')
    print ('')
    ans='0'
    ans=str(input(G+' Menu '+R+'> '+W))
    if ans=='01'or ans=='1':
        pilbangundatar()
    
    elif ans=='02'or ans=='2':
        luas_lingkaran()

    elif ans=='03'or ans=='3':
        pilbangundatar()      
    else:
        print ('[!]==// Abort')
        exit()

def tanya_bola():
    print ('')
    print (G+' 01'+R+' :'+W+' Keliling')
    print (G+' 02'+R+' :'+W+' Luas')
    print (G+' 03'+R+' :'+W+' Volume')
    print ('')
    ans='0'
    ans=str(input(G+' Menu '+R+'> '+W))
    if ans=='01'or ans=='1':
        pilbangunruang()
    
    elif ans=='02'or ans=='2':
        luas_bola()

    elif ans=='03'or ans=='3':
        volume_bola()      
    else:
        print ('[!]==// Abort')
        exit()

def tanya_balok():
    print ('')
    print (G+' 01'+R+' :'+W+' Keliling')
    print (G+' 02'+R+' :'+W+' Luas')
    print (G+' 03'+R+' :'+W+' Volume')
    print ('')
    ans='0'
    ans=str(input(G+' Menu '+R+'> '+W))
    if ans=='01'or ans=='1':
        pilbangunruang()
    
    elif ans=='02'or ans=='2':
        luas_balok()

    elif ans=='03'or ans=='3':
        volume_balok()      
    else:
        print ('[!]==// Abort')
        exit()

def tanya_kubik():
    print ('')
    print (G+' 01'+R+' :'+W+' Keliling')
    print (G+' 02'+R+' :'+W+' Luas')
    print (G+' 03'+R+' :'+W+' Volume')
    print ('')
    ans='0'
    ans=str(input(G+' Menu '+R+'> '+W))
    if ans=='01'or ans=='1':
        pilbangunruang()
    
    elif ans=='02'or ans=='2':
        luas_kubik()

    elif ans=='03'or ans=='3':
        volume_kubik()      
    else:
        print ('[!]==// Abort')
        exit()

def tanya_limas():
    print ('')
    print (G+' 01'+R+' :'+W+' Keliling')
    print (G+' 02'+R+' :'+W+' Luas')
    print (G+' 03'+R+' :'+W+' Volume')
    print ('')
    ans='0'
    ans=str(input(G+' Menu '+R+'> '+W))
    if ans=='01'or ans=='1':
        pilbangunruang()
    
    elif ans=='02'or ans=='2':
        pilbangunruang()

    elif ans=='03'or ans=='3':
        volume_limas()      
    else:
        print ('[!]==// Abort')
        exit()

def pilbangundatar() :		
    print ('')
    print (G+' 01'+R+' :'+W+' Persegi')
    print (G+' 02'+R+' :'+W+' Persegi Panjang')
    print (G+' 03'+R+' :'+W+' Segitiga')
    print (G+' 04'+R+' :'+W+' Lingkaran')
    print (G+' 05'+R+' :'+W+' Jajar Genjang')
    print (G+' 06'+R+' :'+W+' Trapesium')
    print (G+' 07'+R+' :'+W+' Belah Ketupat')
    print (G+' 08'+R+' :'+W+' Layang Layang')
    print ('')
    menu = int(input(G+' Menu '+R+'> '+W))

    if menu == 1 :
        tanya_persegi()
    elif menu == 2 :
        tanya_persegipanjang()
    elif menu == 3 :
        tanya_segitiga()
    elif menu == 4 :
        tanya_lingkaran()
    elif menu == 5 :
        tanya_jajargenjang()
    elif menu == 6 :
        tanya_trapesium()
    elif menu == 7 :
        tanya_ketupat()
    elif menu == 8 :
        tanya_layang()
    else :
        banner()
def pilbangunruang() :      
    print ('')
    print (G+' 01'+R+' :'+W+' Kubik')
    print (G+' 02'+R+' :'+W+' Balok')
    print (G+' 03'+R+' :'+W+' Limas')
    print (G+' 04'+R+' :'+W+' Bola')
    print ('')
    menu = int(input(G+' Menu '+R+'> '+W))

    if menu == 1 :
        tanya_kubik()
    elif menu == 2 :
        tanya_balok()
    elif menu == 3 :
        tanya_limas()
    elif menu == 4 :
        tanya_bola()
    else :
        banner()

def menu() :
    print ('')
    print (G+' 01'+R+' :'+W+' Bangun Datar')
    print (G+' 02'+R+' :'+W+' Bangun Ruang')
    print (G+' 03'+R+' :'+W+' Bilangan Prima')
    print (G+' 04'+R+' :'+W+' Faktor Bilangan')
    print (G+' 05'+R+' :'+W+' Mean / Median / Modus')
    print (G+' 00'+R+' :'+W+' Exit')
    print ('')
    menu = int(input(G+' Menu '+R+'> '+W))

    if menu == 1 :
        pilbangundatar()
    elif menu == 2 :
        pilbangunruang()
    elif menu == 3 :
        prima()
    elif menu == 4 :
        faktor()
    elif menu == 5 :
        tanya_3M()
    elif menu == 0 :
        exit()
    else :
        banner()
        menu()
banner()
menu()
