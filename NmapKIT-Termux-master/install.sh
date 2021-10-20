#!/usr/bin/env bash
clear
echo "Installer NmapKIT"
sleep 1
clear
echo "Update Repo"
apt update 
sleep 1
clear
echo "Update Repo Selesai"
sleep 1
clear
echo "Installing Figlet"
apt install figlet -y
sleep 1 
clear
echo "Install Figlet Selesai"
sleep 1
clear
echo "Installing ncurses-utils"
apt install ncurses-utils -y
sleep 1
clear
echo "Installing Nmap"
sleep 1
apt install nmap -y
sleep 1
clear
echo "Install Nmap Selesai"
sleep 1
clear
echo "Install Script NmapKIT"
mv NmapKIT.sh nmapkit
mv nmapkit $PREFIX/bin/
chmod +x $PREFIX/bin/nmapkit
sleep 1
clear
echo "Install Script NmapKIT Selesai"
sleep 1
clear
echo "================== NmapKIT ================== "
echo "Original Script Dracnmap"
echo "Recode IqbalFAF"
echo ""
echo "Untuk Menjalankan Tools nya cukup ketikan"
echo "nmapkit"
echo "Terimakasih ^_^"
echo "================== NmapKIT ================== "

