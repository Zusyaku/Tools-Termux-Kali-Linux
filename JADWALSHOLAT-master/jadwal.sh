#!/bin/bash

#Hi..!
#Kepoo yak ster?
#kalem cuman simple coding ^^
#recode?= MEMPERKALUKAN DIRI SENDIRI
#belajar? pahami syntax dan penempatan code nya
#sengaja ga gua encrypt / encode biar yang pemula bisa belajar sedikit ^^
#tau diri aja ^^
#ctrl+x for quit
#CODER BY TUANB4DUT


clear

figlet  "..::TUAN B4DUT::.."  | lolcat

echo         "■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■" | lolcat
echo                             "${y} 👑JADWAL SHOLAT👑" |lolcat
echo                         "${y} 👑AUTHOR : TUAN B4DUT👑  " |lolcat
echo              "${y} 🏛ASSOCIATE : INDONESIAN TERMUX ASSOCIATION🏛  " |lolcat
echo                   "${y} ❓CONTACT : gteam@programmer.net❓ " | lolcat
echo                "${y} 💻GITHUB  : https://github.com/TUANB4DUT💻 " | lolcat
echo                   "${y} 🔰WEBSITE : https://cyberline.ml🔰 " | lolcat
echo         "■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■"  | lolcat
trap ctrl_c INT
ctrl_c() {
clear
cmatrix
sleep 1
exit
}

read -p "MASUKAN NAMA KOTA :" kota
curl https://time.siswadi.com/pray/$kota
echo
python text.py
