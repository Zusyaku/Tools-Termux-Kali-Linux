clear
blue='\033[34;1m'
green='\033[32;1m'
purple='\033[35;1m'
cyan='\033[36;1m'
red='\033[31;1m'
white='\033[37;1m'
yellow='\033[33;1m'
sleep 1
echo
echo $green"Proses install agak lama cuy, tergantung jaringan Lu...."
sleep 3
echo
echo $white "INSTALL NANO"
pkg install nano
echo $red "INSTALL FIGLET"
pkg install figlet
sleep 1
echo $green "INSTALL PYTHON2"
pkg install python2
sleep 1
echo $blue "INSTALL COWSAY"
pkg install cowsay
sleep 1
echo $yellow "INSTALL RUBY"
pkg install ruby
gem install lolcat
sleep 1
echo $purple "INSTALL TOILET"
pkg install toilet
sleep 1
echo $blue "INSTALL PHP"
pkg install php
sleep 1
echo $green "Install python3"
pkg install python2 && pkg install python3
sleep 1 
echo $yellow "Install gamepy"
pkg install gamepy
sleep 1 
echo $blue "Install tsu"
pkg install tsu
sleep 1 
echo $red "Install sc"
pkg install sc 
sleep 1 
echo $white "Install pip"
pkg install pip2 && pkg install pip3
sleep 1
echo $yellow "Install tqdm"
pkg inatall tqdm && pkg install request
sleep 1 
echo "Install mechanize"
pkg install mechanize && pip install mechanize
sleep 1
echo $blue "Install curl"
pkg install curl
sleep 2
clear
figlet -f slant "*DONE ngab*"
sleep 1 
echo 
figlet -f slant "yok login" | lolcat
sleep 1 
echo
echo $yellow "cara login sh tools.sh"
exit