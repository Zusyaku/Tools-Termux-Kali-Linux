#!/bin/bash
#-------------------------------------
#Credits : Spooky Sec
#Author : Anubhav Kashyap
#This project is Open-Source
#--------------------------------------
clear
apt install clang
apt install figlet -y
clear
echo -e "\e[92m‎‎‏‏‎ ‎"
figlet -c CipherClaw
sleep 1
printf """
\033[38;5;197m～●～●～●～●～●～●～●～●～●～●～●～●～●～●～●～●～●～●～●
\033[38;5;200m★★★   \033[1;93mAuthor    \033[1;97m−−\033[1;90m⋙⋙⋙ \033[1;93mAnubhav Kashyap               \033[38;5;200m★★★
\033[38;5;200m★★★   \033[1;90mGroup     \033[1;97m−−\033[1;90m⋙⋙⋙ \033[1;90mDeepweb Shadows               \033[38;5;200m★★★
\033[38;5;200m★★★   \033[1;92mGithub    \033[1;97m−−\033[1;90m⋙⋙⋙ \033[1;92mgithub.com/anubhavanonymous   \033[38;5;200m★★★
\033[38;5;197m～●～●～●～●～●～●～●～●～●～●～●～●～●～●～●～●～●～●～●
"""

encode() {
echo -e "\e[1;34m‎‎‏‏‎ ‎"
read -p 'Enter Text to Encode >>> ' txtte
echo -e "\e[91m "
read -p 'Enter The File name >>> ' fname
clang encode.c
./a.out $txtte $fname
echo ""
echo -e "\e[93m "
printf "Encrypted file $fname is created"
echo ""
echo ""
ls
echo ""
}

decode() {
echo -e "\e[1;34m‎‎‏‏‎ ‎"
read -p 'Enter The File to Decode >>> ' encf
echo -e "\e[91m "
clang decode.c
./a.out $encf
echo ""
}

echo ""
printf "\e[1;92m[\e[0m 1\e[1;92m ]\e[0m>>>\e[1;93m Encode \e[0m\n"
printf "\e[1;92m[\e[0m 2\e[1;92m ]\e[0m>>>\e[1;93m Decode \e[0m\n"
printf "\e[1;92m[\e[0m 3\e[1;92m ]\e[0m>>>\e[1;93m Exit \e[0m\n"
printf "\n"
echo -e "\e[36m "
read -p 'Select Option !! >>> ' options

if [ "$options" -eq "1" ];then
        encode

fi
if [ "$options" -eq "2" ];then
        decode
fi

if [ "$options" -eq "3" ];then
        echo ""
        echo -e "\e[91mThanks for using CipherClaw"
        echo ""
        exit
        exit
        exit
fi
