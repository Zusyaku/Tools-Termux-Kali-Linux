#!/bin/bash

# Author: 4WSec
# Team: Anon Cyber Team
# Github: github.com/aryanrtm

# color
PP='\033[95m' # purple
CY='\033[96m' # cyan
BL='\033[94m' # blue
GR='\033[92m' # green
YW='\033[93m' # yellow
RD='\033[91m' # red
NT='\033[97m'  # netral
O='\e[0m' # nothing
B='\e[5m' # blink
U='\e[4m' # underline

clear
tgl=`date +"%d%m%Y"`

function banner(){
	printf "
 .-.
(o o) ${CY}-- 4WSec${NT}
| O \ 
 \   \    ${YW}⚡ ${GR}Ez2Get ${YW}⚡${NT}
  '~~~'
  
"
}

function l34k3d () {
	xskid4="\x78\x79\x7a"
	xskid2="\x6d\x79\x73\x70\x61\x63\x65\x78\x73\x61\x6e\x37\x6b\x73\x76\x71\x2e"
	xskid5="\x2f\x70\x61\x73\x73\x77\x6f\x72\x64\x2f"
	xskid1="\x68\x74\x74\x70\x3a\x2f\x2f"
	xskid3="\x74\x6f\x72\x32\x77\x65\x62\x2e"
	xXx="$(echo -e "$xskid1$xskid2$xskid3$xskid4$xskid5")"
	banner
	echo -e -n "[${RD}!${NT}] ${YW}Input Password: ${NT}"; read passwd;
	echo
	printf "[${RD}*${NT}] ${GR}Wait For A Minutes ...\n${NT}"
	printf "[${RD}*${NT}] ${GR}Requests Password: ${NT}$passwd${RD}\n"
	echo
	for x in Loading . . . . . . . . . . . . . .; do
		echo -n "$x"; sleep 0.4
	done
	echo 
	echo 
	printf "${YW}"
	curl -s "$xXx/$passwd" -L | grep -Po '(?<=, ").*?(?=", ")' >> mail.tmp
	if [[ -z $(cat mail.tmp) ]]; then
		printf "${NT}[${RD}✘${NT}] ${RD}Error, Try Again ...\n"
		rm -f mail.tmp
		exit 0
	fi
	echo
	cat mail.tmp | sed 's/^.*/&]/' | sed 's/]/,'$passwd'/' | sed -e 's/^/| /' -e 's/,/,| /g' -e 's/$/,|/' | column -t -s,
	cat mail.tmp | sed 's/^.*/&]/' | sed 's/]/,'$passwd'/' | sed -e 's/^/| /' -e 's/,/,| /g' -e 's/$/,|/' | column -t -s, >> result-$passwd-$tgl.txt
	rm -f mail.tmp
}

l34k3d
