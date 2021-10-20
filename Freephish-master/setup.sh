#!/bin/bash
echo ""
clear
echo ""
pkg update -y
pkg upgrade -y
echo ""
pkg install figlet
echo ""
clear
echo ""
echo ""
figlet -c Downloading Requirements !!
sudo apt-get install apache2 -y
apt install apache2 -y
apt install php -y
apt install jq -y
apt install tail -y
apt install curl -y
apt install wget
rm ngrok
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip
unzip ngrok-stable-linux-arm.zip
rm ngrok-stable-linux-arm.zip
chmod +x freephish.sh
clear
echo ""
echo ""
figlet -c Done !!
sleep 2
clear
