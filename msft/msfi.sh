#!/bin/bash
#Metasploit Framework for Termux Install Script by N11rm44L7w44711

echo "Setting up Storage..."
sleep 1.0
termux-setup-storage -y

echo "Updating & Upgrading ..."
sleep 1.0
apt-get update -y
apt-get upgrade -y

echo "Installing git & pythons ..."
sleep 1.0
pkg install git -y
pkg install python2 -y
pkg install python -y

echo "Upgrading PIP ..."
sleep 1.0
pip install --upgrade pip

echo "Installing wget & openssh ..."
sleep 1.0
pkg install wget -y
pkg install openssh -y

echo "Installing ruby ..."
sleep 1.0
pkg install ruby -y
echo "Installing unstable-repo ..."
sleep 1.0
pkg install unstable-repo -y

echo "Finally, Installing Metasploit Framework !!!"
pkg install metasploit -y

echo "Metasploit Framework Sucessfully Installed !"
sleep 2.0
echo "Moving Metasploit to Home Directory !"
sleep 1.0
cd $HOME/../usr/opt
cp metasploit-framework $HOME
cd $HOME/metasploit-framework
echo "Done !"

wget https://github.com/termux/termux-packages/files/2912002/fix-ruby-bigdecimal.sh.txt
bash fix-ruby-bigdecimal.sh.txt

echo "Starting PostgreSQL Database ..."
sleep 1.0
pg_ctl -D $PREFIX/var/lib/postgresql start 

./msfconsole
