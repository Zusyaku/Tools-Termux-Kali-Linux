"""
Tool Name  : Litor (Lite Calculator)
Version    : V1.0
Author     : Karjok Pangesty
Group      : CRABS (Cracker Noob Squad)
Date       : September 28th, 2018
Thanks To  : Allah, all member of BlackHole Scurity, Anonymous Indonesian Cyber Army, CRABS,
             And my beloved, Agustina Eka Pangesty. 
Country    : Indonesia
Province   : Lampung
Postal Code: 34158

"""
"""
Every one can recode this tool. But, please don't delete Author's name.
Thanks for usage.
"""
"""
Find me at

Telegram : -https://t.me/om_karjok
Instagram: -@om_karjok
Facebook : -not defined
"""


#source strings
s=("   ")
sp=("     ")
#source color
lr=('\033[91m')
lg=('\033[92m')
y=('\033[93m')
lb=('\033[94m')
cy=('\033[36m')
x=('\033[0m')
#source style
bld=('\033[01m')
udl=('\033[04m')



print(bld+lr+"            ______________________________")
print(bld+lr+"     ______|"+x,"         °•°LITOR°•°        ",lr+"|______")
print(bld+lr+"     ======|_______"+x,"Lite Calculator",lr+"______|======")
print(bld+lr+"     ====================",y+"v1.0",lr+"=================="+x)
print("\n")


#rumus
#penjumlahan
def jumlah(x, y): return x + y 
#pengurangan
def kurang(x, y): return x - y 
#perkalian
def kali(x, y): return x * y 
#pembagian
def bagi(x, y): return x / y 
#pangkat
def pangkat(x,y): return x ** y

#operation
print(sp+y+"[!]"+x,"MENU") 
print(sp+s+lr+"1."+x,"Penjumlahan")
print(sp+s+lr+"2."+x,"Pengurangan")
print(sp+s+lr+"3."+x,"Perkalian")
print(sp+s+lr+"4."+x,"Pembagian")
print(sp+s+lr+"5."+x,"Perpangkatan")
print(sp+s+lr+"0."+x,"KELUAR !\n")

#user input
choice=str()
while choice !="1" and choice !="2" and choice !="3" and choice !="4" and choice !="5" and choice !="0":
  choice=str(input(sp+lr+"Litor/> "+x))
  
if choice == "0":
 print(sp+y+"Terimakasih udah pakek Litor v1.0 buat itung-itungan :'v")
 print(sp+y+"Kirim Kritik dan Saran kalian ke https://t.me/om_karjok.")
 print(sp+y+"see you :* !!\n"+x)
 exit()
else:  
 num1 = int(input(sp+s+"Angka Pertama: ")) 
 num2 = int(input(sp+s+"Angka Kedua  : ")) 

 if choice == "1": 
   print(sp+s+bld+y+"Hasil/> "+x, jumlah(num1,num2)) 
 elif choice == "2" : 
   print(sp+s+bld+y+"HASIL/> "+x, kurang(num1,num2)) 
 elif choice == "3" : 
   print(sp+s+bld+y+"HASIL/> "+x, kali(num1,num2)) 
 elif choice == "4" : 
   print(sp+s+nld+y+"HASIL/> "+x, bagi(num1,num2))
 elif choice == "5" :
   print(sp+s+bld+y+"HASIL/> "+x, pangkat(num1,num2))
 else:
   print("Invalid input")
print("\n")
