#!/bin/bash
#############################################
#                 [ IG-dl ]                 #
#                                           #
# Coded by 4WSec                            #
# Team   : Anon Cyber Team - HAMA Security  #
# Date   : 10/11/2018                       #
# ©Copyright ~ 4WSec                        #
#############################################

clear

#################
PURPLE='\033[95m'
CYAN='\033[96m'
BLUE='\033[94m'
GREEN='\033[92m'
YELLOW='\033[93m'
RED='\033[91m'
NETRAL='\033[0m'
################

########################################################################################
useragent="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0"
########################################################################################

############ HOST #############
URL="https://www.instagram.com"
###############################

function b4nn3r(){
printf "${GREEN}
\t    __________          ____
\t   /  _/ ____/     ____/ / / 
\t   / // / ________/ __  / / 
\t _/ // /_/ /_____/ /_/ / / 
\t/___/\____/      \__,_/_/ 

\t${YELLOW}[*] Author : ${GREEN}4WSec
\t${YELLOW}[*] Team   : ${GREEN}Anon Cyber Team
\t${YELLOW}[*] Download all of the images and videos from a Instagram user.
\t----------------------------------------------------------------
"
}

function m3nU(){
	printf "\t${CYAN}[1] Images  |  [2] Videos \n"
	printf "\t--------------------------\n"
	read -p "    ~> " chs;
	if [[ $chs == 1 ]]; then
		read -p " Input Username : " uSeR;
		gEt_s0m3_imG
	elif [[ $chs == 2 ]]; then
		printf "${YELLOW} Example         : https://www.instagram.com/p/Bp7lIjPgRei/ => 'Bp7lIjPgRei'\n"
		read -p " Input ShortCode : " shRTc0D3;
		gEt_s0m3_viD
	fi
}


function gEt_s0m3_imG(){
	o0o=$(curl -s -L -A "${useragent}" "${URL}/${uSeR}/")
	if [[ $o0o =~ "The link you followed may be broken" ]]; then
		printf "${RED} ✘ User Not Found \n"
	elif [[ $o0o =~ "Get the app." ]] || [[ $o0o =~ "Don't have an account? Sign up" ]] || [[ $o0o =~ "Get the app." ]]; then
		printf "${RED} ✘ User Not Found \n"
	elif [[ $o0o =~ '"is_private":true' ]]; then
		printf "${RED} ✘ This User is Private \n"
	else
		printf "${GREEN} ✔ User Found: ${NETRAL}${uSeR} \n"
		printf "${YELLOW} Please Wait ... \n"
		mkdir Img-Saved_$uSeR
		sleep 2
		curl -s -L -A "${useragent}" "${URL}/${uSeR}/" | grep -Po '(?<="display_url":")[^",]*' >> img.lst
		for dl in $(cat img.lst)
		do
			wget $dl -P Img-Saved_$uSeR &> /dev/null
		done
		printf "${GREEN} ✔ Images of ${NETRAL}${uSeR} ${GREEN}Have Been Downloaded ... \n"
	fi
}

function gEt_s0m3_viD(){
	o00o=$(curl -s -L -A "${useragent}" "${URL}/p/${shRTc0D3}/")
	if [[ $o00o =~ "The link you followed may be broken" ]]; then
		printf "${RED} ✘ Video Not Found \n"
	elif [[ $o00o =~ '"is_private":true' ]]; then
		printf "${RED} ✘ This User is Private \n"
	else
		printf "${GREEN} ✔ Video Found   : ${shRTc0D3} \n"
		printf "${YELLOW} Please Wait ... \n"
		mkdir Vid-Saved_$shRTc0D3
		sleep 2
		curl -s -L -A "${useragent}" "${URL}/p/${shRTc0D3}/" | grep -Po '(?<="video_url":")[^",]*' >> vid.lst
		for dl in $(cat vid.lst)
		do
			wget $dl -P Vid-Saved_$shRTc0D3/ &> /dev/null
		done
		printf "${GREEN} ✔ Video of Short Code ${NETRAL}${shRTc0D3} ${GREEN}Have Been Downloaded ... \n"
	fi
}
b4nn3r
m3nU
rm -f img.lst
rm -f vid.lst
