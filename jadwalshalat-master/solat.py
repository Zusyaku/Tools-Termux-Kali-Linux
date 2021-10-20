# Uler gerak-gerak versi 27
# Rekode nah, dapet duit aku

#module
import os,sys,time
import requests,json
author = "rezadkim"
#Warna

merah  = "\033[1;91m"
lime   = "\033[1;92m"
kuning = "\033[1;93m"
biru   = "\033[1;94m"
ungu   = "\033[1;95m"
blue   = "\033[1;96m"
putih  = "\033[1;97m"
tutup  = "\033[0m"

def main():
    os.system("reset")
    print "        [ Sholat-gan ]"+kuning+"v0.2"+tutup
    print tutup+"["+lime+"#"+tutup+"] Coded  : \033[1;96m@rezadkim\033[0m ]"
    print tutup+"["+lime+"#"+tutup+"] Source : \033[1;92mhttps://github.com/rezadkim\033[0m ]"
    print ""
    cari = raw_input("["+biru+"+"+tutup+"] Kota : "+lime)
    print tutup+"[*] Sabar Coeq ..."
    time.sleep(2)
    print ""
    try:
        r = requests.get("https://time.siswadi.com/pray/"+cari)
        q = json.loads(r.text)
        subuh = q["data"]["Fajr"]
        dzuhur = q["data"]["Dhuhr"]
        ashar = q["data"]["Asr"]
        magrib = q["data"]["Maghrib"]
        isha = q["data"]["Isha"]
        date = q["time"]["date"]
        waktu = q["time"]["time"]
        lokasi = q["location"]["address"]
        print tutup+"["+lime+">"+tutup+"] Subuh   : "+lime+subuh
        print tutup+"["+lime+">"+tutup+"] Dzuhur  : "+lime+dzuhur
        print tutup+"["+lime+">"+tutup+"] Ashar   : "+lime+ashar
        print tutup+"["+lime+">"+tutup+"] Maghrib : "+lime+magrib
        print tutup+"["+lime+">"+tutup+"] Isya    : "+lime+isha
        print tutup+"["+lime+"*"+tutup+"] Date    : "+lime+date
        print tutup+"["+lime+"*"+tutup+"] Time    : "+lime+waktu
        print tutup+"["+lime+"*"+tutup+"] Address : "+lime+lokasi
        print tutup+"["+lime+"*"+tutup+"] Status  : "+lime+q["status"]
        print tutup+"Done."
    except KeyError:
        print tutup+"["+merah+"!"+tutup+"] Tidak Ditemukan."
        exit()
        
if __name__=="__main__":
    main()
