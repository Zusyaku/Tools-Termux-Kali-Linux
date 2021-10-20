#!/bin/bash

clear
# color
f=3 b=4s
for j in f b; do
  for i in {0..7}; do
    printf -v $j$i %b "\e[${!j}${i}m"
  done
done

# user agent
useragent="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0"


banner(){
printf "\t${f3}                             ___\n"
printf "\t                     /======/\n"
printf "\t            _____   //      \___       ,\n"
printf "\t             | \ \ //           :,   ./\n"
printf "\t     |_______|__|_//            ;:; /\n"
printf "\t    _L_____________\o           ;;;/\n"
printf "\t____(CCCCCCCCCCCCCC)____________-/__________\n"
}

menu(){
	printf "\t${f2}[${f1}1${f2}]${f6} Gempa Terkini              ${f7}Author: ${f5}4WSec\n"
	printf "\t${f2}[${f1}2${f2}]${f6} Gempa Dirasakan\n"
	printf "\t${f2}[${f1}3${f2}]${f6} Tsunami\n"
	printf "\t${f2}[${f1}4${f2}]${f6} Pesan BMKG\n"
	echo ""
	read -p "${f2}Choose ${f5}~> " choose;
	echo ""
	if [[ $choose == 1 ]]; then
		echo "- GEMPA TERKINI -"
		get_gempa_terkini
	elif [[ $choose == 2 ]]; then
		echo "- GEMPA DIRASAKAN -"
		get_gempa_terakhir
		elif [[ $choose == 3 ]]; then
			echo "- TSUNAMI -"
			get_tsunami_terakhir
		elif [[ $choose == 4 ]]; then
			echo "- PESAN BMKG -"
			pesan_bmkg
	fi
}

get_gempa_terkini(){
	curl -s -A "${useragent}" "http://data.bmkg.go.id/autogempa.xml" >> resu.lt
	if [[ -z $(cat resu.lt) ]]; then
		echo "${f1}[!] Error, Try Again!"
	else
		echo "${f6}Tanggal    : ${f2}$(cat resu.lt | grep -Po '(?<=<Tanggal>).*?(?=<)')"
		echo "${f6}Jam        : ${f2}$(cat resu.lt | grep -Po '(?<=<Jam>).*?(?=<)')"
		echo "${f6}Lintang    : ${f2}$(cat resu.lt | grep -Po '(?<=<Lintang>).*?(?=<)')"
		echo "${f6}Bujur      : ${f2}$(cat resu.lt | grep -Po '(?<=<Bujur>).*?(?=<)')"
		echo "${f6}Magnitude  : ${f2}$(cat resu.lt | grep -Po '(?<=<Magnitude>).*?(?=<)')"
		echo "${f6}Kedalaman  : ${f2}$(cat resu.lt | grep -Po '(?<=<Kedalaman>).*?(?=<)')"
		echo "${f6}Wilayah 1  : ${f2}$(cat resu.lt | grep -Po '(?<=<Wilayah1>).*?(?=<)')"
		echo "${f6}Wilayah 2  : ${f2}$(cat resu.lt | grep -Po '(?<=<Wilayah2>).*?(?=<)')"
		echo "${f6}Wilayah 3  : ${f2}$(cat resu.lt | grep -Po '(?<=<Wilayah3>).*?(?=<)')"		
	fi
}

get_tsunami_terakhir(){
	curl -s -A "${useragent}" "http://data.bmkg.go.id/lasttsunami.xml" >> resu.lt
	if [[ -z $(cat resu.lt) ]]; then
		echo "${f1}[!] Error, Try Again!"
	else
		echo "${f6}Tanggal    : ${f2}$(cat resu.lt | grep -Po '(?<=<Tanggal>).*?(?=<)')"
		echo "${f6}Jam        : ${f2}$(cat resu.lt | grep -Po '(?<=<Jam>).*?(?=<)')"
		echo "${f6}Lintang    : ${f2}$(cat resu.lt | grep -Po '(?<=<Lintang>).*?(?=<)')"
		echo "${f6}Bujur      : ${f2}$(cat resu.lt | grep -Po '(?<=<Bujur>).*?(?=<)')"
		echo "${f6}Magnitude  : ${f2}$(cat resu.lt | grep -Po '(?<=<Magnitude>).*?(?=<)')"
		echo "${f6}Kedalaman  : ${f2}$(cat resu.lt | grep -Po '(?<=<Kedalaman>).*?(?=<)')"
		echo "${f6}Area       : ${f2}$(cat resu.lt | grep -Po '(?<=<Area>).*?(?=<)')"

	fi
}

get_gempa_terakhir(){
	curl -s -A "${useragent}" "http://data.bmkg.go.id/lastgempadirasakan.xml" >> resu.lt
	if [[ -z $(cat resu.lt) ]]; then
		echo "${f1}[!] Error, Try Again!"
	else
		echo "${f6}Tanggal    : ${f2}$(cat resu.lt | grep -Po '(?<=<Tanggal>).*?(?=<)')"
		echo "${f6}Jam        : ${f2}$(cat resu.lt | grep -Po '(?<=<Jam>).*?(?=<)')"
		echo "${f6}Lintang    : ${f2}$(cat resu.lt | grep -Po '(?<=<Lintang>).*?(?=<)')"
		echo "${f6}Bujur      : ${f2}$(cat resu.lt | grep -Po '(?<=<Bujur>).*?(?=<)')"
		echo "${f6}Magnitude  : ${f2}$(cat resu.lt | grep -Po '(?<=<Magnitude>).*?(?=<)')"
		echo "${f6}Kedalaman  : ${f2}$(cat resu.lt | grep -Po '(?<=<Kedalaman>).*?(?=<)')"
		echo "${f6}Keterangan : ${f2}$(cat resu.lt | grep -Po '(?<=<Keterangan>).*?(?=<)')"
		echo "${f6}Dirasakan  : ${f2}$(cat resu.lt | grep -Po '(?<=<Dirasakan>).*?(?=<)')"		
	fi
}

pesan_bmkg(){
	wget -q http://data.bmkg.go.id/pesan.txt
	if [[ -z $(cat pesan.txt) ]]; then
		echo "${f1}[!] Error, Try Again!"
	else
		echo "${f6}Pesan BMKG: ${f2}(`cat pesan.txt`)"
	fi
}

banner
menu
rm -f resu.lt
rm -f pesan.txt
