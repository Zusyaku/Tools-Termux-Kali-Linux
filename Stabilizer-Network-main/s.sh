#!/bin/sh

#warna

m='\033[31;1m'
h='\033[32;1m'
p='\033;37;1m'

#install bahan
clear
pkg update
pkg upgrade
pkg install screenfetch
pkg install python
pkg install python2
pip2 install netaddr
pip install netaddr
pkg install apt
apt-get install python3
pip3 install netaddr
clear
#Loading
echo "///////////////////////////////////////////////////////" | lolcat -a -d 190
sleep 1
#Tampialn
clear
echo $h
toilet -f mini Stabilizer Network
echo $m
echo "======================================"
echo "(+)Author : MR.FAGHP BLACK-404/F   (+)"
echo "(+)Grup   : BLACK SQUAD, MTI, SCT  (+)"
echo "(+)Teman  : MR.AM, PANGLIAMA JATENG(+)"
echo "======================================"
echo "======================================"
echo "(1). Stabilizer Network            (★)"
echo "(2). Admin Whatsapp  	           (★)"
echo "(3). Subscribe to my channel       (★)"
echo "====================================="
read -p "[=]>" Input

#data 1
if [ $Input = 1 ]
then
    clear
    echo $m
    figlet -f mini Faghp hengekel tyz
    ping -s 1000 1.1.1.1
#data 2
fi
if [ $Input = 2 ]
then
    clear
    echo $h
    toilet -f slant  Admin Whatsapp
    xdg-open "https://wa.me/6281313537943/?text=Assalamualaikum+warahmatullahi+wabarakatuh+admin+apa+kabar"
#data 3
fi
if [ $Input = 3 ]
then
    clear
    echo "   ____     __               _ __"
    echo "  / __/_ __/ /  ___ ________(_) /  ___"
    echo " _\ \/ // / _ \(_-</ __/ __/ / _ \/ -_)"
    echo "/___/\_,_/_.__/___/\__/_/ /_/_.__/\__/"
    xdg-open "https://youtube.com/channel/UCFggfLWFCmGGyb2VH2EBfBQ"
fi


