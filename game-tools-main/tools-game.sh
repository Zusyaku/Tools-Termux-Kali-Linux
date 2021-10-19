#!/bin/bash



clear
blue='\033[34;1m'
green='\033[32;1m'
purple='\033[35;1m'
cyan='\033[36;1m'
red='\033[31;1m'
white='\033[37;1m'
yellow='\033[33;1m'
clear

sleep 2
python2 Asu.py | lolcat
sleep 2
echo $cyan"T"
sleep 0.1
echo $green"o"
sleep 0.1
echo $yellow"o"
sleep 0.1
echo $red"l"
sleep 0.1
echo $blue"s"
sleep 0.1
echo $red"update"
sleep 1
echo "."
sleep 1
echo "."
sleep 1
pkg update && pkg upgrade
pkg install python && pkg install python2
pkg install pip2 && pkg install pip
pkg install mechanize && pip install mechanize
pkg install nodejs && gem install lolcat
pkg install gamepy && pkg install figlet
pkg install toilet && pkg install bash
pkg install chmod
pkg install git
sleep 2
echo "." "." "." "." | lolcat
sleep 3
clear
echo "▒▐█▀▀▄▐██▒▄█▀▀█▒▐█▒▐▀▐██" | lolcat
echo "▒▐█▒▐█░█▌▒▀▀█▄▄▒▐██▌░░█" | lolcat
echo "▒▐█▀▄▄▐██▒█▄▄█▀▒▐█▒▐▄▐██" | lolcat
sleep 2
echo
cowsay -f eyes "Game tools" | lolcat
echo
echo $yellow"tampilan andorid kalian"
echo
echo
neofetch
figlet -f slant "Riski Tools"
echo
echo "Silakan pilih tools di bawah ganz" | lolcat
echo "[×××××××××××××××××××××××××××××××××]" | lolcat
echo
sleep 2
echo "1.anti lag al device (masukan sesuai ip internet kalian" | lolcat
sleep 1
echo "0.keluar menu" | lolcat
sleep 2
echo
read -p "pilih menu buat game)" Asu

if [ $Asu = 1 ]
then
sleep 1
python2 j.py | lolcat
sleep 1
echo $blue"masukan Alamat ip internet kalian ganz"
read nick
ping -s1002 $nick
fi

if [ $Asu = 0 ]
then
sleep 2
figlet keluar menu | lolcat
sleep 2
python2 kata.py | lolcat
sleep 2
exit
else
        sleep 2
        figlet by goblok | lolcat
        sleep 2
        silakan ulang kembali kasian oon makanya kalo ngetik di baca dulu ngentot
        fi



