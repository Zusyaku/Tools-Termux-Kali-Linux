#!/bin/bash
#-------------------------------------
#Author : Anubhav Kashyap
#This project is Open-Source
#--------------------------------------
clear
banner(){
python2 banner.py
echo ""
echo -e "  \033[91m[ \033[95mDark Eagle (Web pentesting Framework) \033[91m]"
sleep 0.1
echo -e "          [\033[92mC0DER : \033[96mAnubhav Kashyap \033[92m]"
}

about(){
clear
banner
echo ""
printf "   \e[0m\e[44mDark eagle is a Website Penetration testing framework\e[0m\n"
echo ""
printf "   \e[0m\e[41mDeveloped by Anubhav Kashyap !\e[0m\n"
echo ""
printf "\e[0m\e[92m   Group \e[0m\e[91m         : \e[0m\e[96mDeepWeb Shadows\e[0m\n"
echo ""
printf "\e[0m\e[92m   Github \e[0m\e[91m        : \e[0m\e[96mgithub.com/anubhavanonymous\e[0m\n"
echo ""
printf "\e[0m\e[92m   Instagram \e[0m\e[91m     : \e[0m\e[96minstagram.com/anubhavanonymous\e[0m\n"
echo ""
}

banner
sleep 0.2
echo -e "            \033[91mModules available : \033[93m16"
echo ""
echo -e "\033[93m[+] \033[92mDark Eagle Modules\033[33m"
echo ""
echo -e " \e[1;31m[\e[0m\e[1;77m01\e[0m\e[1;31m]\e[0m\e[1;93m DNS Lookup"
echo -e " \e[1;31m[\e[0m\e[1;77m02\e[0m\e[1;31m]\e[0m\e[1;93m Reverse DNS Lookup"
echo -e " \e[1;31m[\e[0m\e[1;77m03\e[0m\e[1;31m]\e[0m\e[1;93m IP Locator"
echo -e " \e[1;31m[\e[0m\e[1;77m04\e[0m\e[1;31m]\e[0m\e[1;93m Subnet Lookup"
echo -e " \e[1;31m[\e[0m\e[1;77m05\e[0m\e[1;31m]\e[0m\e[1;93m Whois Lookup"
echo -e " \e[1;31m[\e[0m\e[1;77m06\e[0m\e[1;31m]\e[0m\e[1;93m Host Provider Lookup"
echo -e " \e[1;31m[\e[0m\e[1;77m07\e[0m\e[1;31m]\e[0m\e[1;93m Port Scanner"
echo -e " \e[1;31m[\e[0m\e[1;77m08\e[0m\e[1;31m]\e[0m\e[1;93m Page Link Finder"
echo -e " \e[1;31m[\e[0m\e[1;77m09\e[0m\e[1;31m]\e[0m\e[1;93m Traceroute"
echo -e " \e[1;31m[\e[0m\e[1;77m10\e[0m\e[1;31m]\e[0m\e[1;93m HTTP Header"
echo -e " \e[1;31m[\e[0m\e[1;77m11\e[0m\e[1;31m]\e[0m\e[1;93m SQLI Scanner"
echo -e " \e[1;31m[\e[0m\e[1;77m12\e[0m\e[1;31m]\e[0m\e[1;93m DDOS Attack"
echo -e " \e[1;31m[\e[0m\e[1;77m13\e[0m\e[1;31m]\e[0m\e[1;93m Subdomain Finder"
echo -e " \e[1;31m[\e[0m\e[1;77m14\e[0m\e[1;31m]\e[0m\e[1;93m Slowloris Attack"
echo -e " \e[1;31m[\e[0m\e[1;77m15\e[0m\e[1;31m]\e[0m\e[1;93m Admin Page Finder"
echo -e " \e[1;31m[\e[0m\e[1;77m16\e[0m\e[1;31m]\e[0m\e[1;93m Robots Finder"
echo -e " \e[1;31m[\e[0m\e[1;77m99\e[0m\e[1;31m]\e[0m\e[1;93m About"
echo -e " \e[1;31m[\e[0m\e[1;77m00\e[0m\e[1;31m]\e[0m\e[1;93m Exit"
echo ""
read -p $' \e[1;31m[\e[0m\e[1;77m~\e[0m\e[1;31m]\e[0m\e[1;92m Select an option: \e[0m\e[1;96m\en' num
if [ $num -eq 1 ];then
echo ""
echo -e $'\e[1;33m[\e[0m\e[1;77m Dark Eagle \e[0m\e[1;33m]\e[0m\e[32m Input target below'
read -p ">>> " t
work=$(wget http://api.hackertarget.com/dnslookup/?q=$t -q -O result)
echo ""
echo -e "\e[91mLOOKUP STARTED"
echo -e "\e[1;93m‎‎‏‏‎ ‎"
    cat result
echo ""
elif [ $num -eq 2 ];then
echo ""
echo -e $'\e[1;33m[\e[0m\e[1;77m Dark Eagle \e[0m\e[1;33m]\e[0m\e[32m Input target below'
read -p ">>> " t
work=$(wget http://api.hackertarget.com/reversednslookup/?q=$t -q -O result)
echo ""
echo -e "\e[91mLOOKUP STARTED"
echo -e "\e[1;93m‎‎‏‏‎ ‎"
echo "" 
    cat result
echo ""
elif [ $num -eq 3 ];then
echo ""
echo -e $'\e[1;33m[\e[0m\e[1;77m Dark Eagle \e[0m\e[1;33m]\e[0m\e[32m Input target IP or Site below'
read -p ">>> " t
work=$(wget http://api.hackertarget.com/geoip/?q=$t -q -O result)
echo ""
echo -e "\e[91mLOCATING STARTED"
echo -e "\e[1;93m‎‎‏‏‎ ‎"
    cat result
echo ""
elif [ $num -eq 4 ];then
echo ""
echo -e $'\e[1;33m[\e[0m\e[1;77m Dark Eagle \e[0m\e[1;33m]\e[0m\e[32m Input target IP or Site below'
read -p ">>> " t
work=$(wget http://api.hackertarget.com/subnetcalc/?q=$t -q -O result)
echo ""
echo -e "\e[91mLOOKUP STARTED"
echo -e "\e[1;93m‎‎‏‏‎ ‎"
    cat result
echo ""
elif [ $num -eq 5 ];then
echo ""
echo -e $'\e[1;33m[\e[0m\e[1;77m Dark Eagle \e[0m\e[1;33m]\e[0m\e[32m Input target below'
read -p ">>> " t
echo ""
echo -e "\e[91mLOOKUP STARTED"
echo -e "\e[1;93m‎‎‏‏ ‎"
whois $t
echo ""
elif [ $num -eq 6 ];then
echo ""
echo -e $'\e[1;33m[\e[0m\e[1;77m Dark Eagle \e[0m\e[1;33m]\e[0m\e[32m Input target below'
read -p ">>> " t
work=$(wget http://api.hackertarget.com/hostsearch/?q=$t -q -O result)
echo ""
echo LOOKUP STARTED
echo -e "\e[1;93m‎‎‏‏‎ ‎"
    cat result
echo ""
elif [ $num -eq 7 ];then
echo ""
echo -e "\e[32m Enter Domain"
read -p ">>> " t
work=$(wget http://api.hackertarget.com/nmap/?q=$t -q -O result)
echo ""
echo SCANNING STARTED
echo -e "\e[1;93m‎‎‏‏‎ ‎"
    cat result
echo ""
elif [ $num -eq 8 ];then
echo ""
echo -e "\e[32m Enter Domain or IP Address"
read -p ">>> " t
work=$(wget http://api.hackertarget.com/pagelinks/?q=$t -q -O result)
echo ""
echo FINDING STARTED
echo -e "\e[1;93m‎‎‏‏‎ ‎"
    cat result
echo ""
elif [ $num -eq 9 ];then
echo ""
echo -e "\e[32m Enter Domain"
read -p ">>> " t
work=$(wget http://api.hackertarget.com/findshareddns/?q=$t -q -O result)
echo ""
echo LOOKUP STARTED
echo -e "\e[1;93m‎‎‏‏‎ ‎"
    cat result
echo ""
elif [ $num -eq 10 ];then
echo ""
echo -e "\e[32m Enter Domain"
read -p ">>> " t
work=$(wget http://api.hackertarget.com/httpheaders/?q=$t -q -O result)
echo ""
echo LOOKUP STARTED
echo -e "\e[1;93m‎‎‏‏‎ ‎"
    cat result
echo ""
elif [ $num -eq 11 ];then
echo ""
echo LOOKUP STARTED
cd modules
python2 sqll.py
echo ""
elif [ $num -eq 12 ];then
echo ""
cd modules
python2 ddos.py
elif [ $num -eq 13 ];then
echo ""
cd modules
python3 subd.py
elif [ $num -eq 14 ];then
echo -e "\e[95m "
echo STARTING SLOWLORIS
echo -e "\e[96m "
read -p "Enter Domain >>> " domain
read -p "Enter no. of sockets >>> " sockets
echo -e "\e[1;93m‎‎‏‏‎ ‎"
slowloris $domain -s $sockets
elif [ $num -eq 15 ];then
echo ""
cd modules
python3 finder.py
elif [ $num -eq 16 ];then
echo ""
cd modules
python3 robots.py
elif [ $num -eq 99 ];then
echo ""
about
elif [ $num -eq 0 ];then
echo ""
echo -e "\e[91mExiting Dark Eagle !!"
echo ""
exit
fi









