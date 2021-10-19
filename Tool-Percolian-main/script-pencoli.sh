#!/bin/sh
#yg mau recode gpp ikhlas gw

#warna
#warna script mang
biru='\033[34;1m'
hijau='\033[32;1m'
ungu='\033[35;1m'
cyan='\033[36;1m'
merah='\033[31;1m'
putih='\033[37;1m'
kuning='\033[33;1m'

#Input pilihan


clear
echo $kuning'         (+)MR.FAGHP BLACK-404/F(+)'
echo $kuning'(+)---------------------------------------(+)'
echo $biru'1).link nnton full semua'
echo $biru'2).link app simontok'
echo $biru'3).link app nekopoi'
echo $biru'4). Keluar'
echo $kuning'(+)---------------------------------------(+)'
echo $cyan
read -p 'Input slurr = ' int

if [ $int = 1 ]
then
    clear
    echo $ungu
    figlet -f smslant Full-Link
    cat xxx.txt

fi
if [ $int = 2 ]
then
    clear
    echo $merah
    figlet -f smslant Simontok
    cat apksinmontok.txt

fi
if [ $int = 3 ]
then
    clear
    echo $kuning
    figlet -f smslant Nekopoi
    cat apknekopoi.txt

fi
if [ $int = 4 ]
then
   clear
   exit

fi
