#!/bin/bash
#author ./Lolz
#thanks to javaghost - @bashid.org

#warna(bold)
red='\e[1;31m'
green='\e[1;32m'
yellow='\e[1;33m'
blue='\e[1;34m'
magenta='\e[1;35m'
cyan='\e[1;36m'
white='\e[1;37m'

#package yang dibutuhin
dependencies=( "pv" "curl" "bc" )
for i in "${dependencies[@]}"
do
    command -v $i >/dev/null 2>&1 || {
        echo -e >&2 "${yellow}$i ${white}: belum terinstall - tools akan menginstallnya"
        #mencoba untuk menginstall
        apt-get install $i -y
        echo -e "${yellow}okeh semua sudah terinstall, tunggu sebentar tools akan berjalan secara otomatis\n${white}-Zan"
	sleep 2
        clear
    }
done

#data yang diperlukan
host='http://sms.payuterus.biz'
cookie=$(curl -s -I "$host/alpha/send.php" | grep -o "PHPSESSID=.*" | cut -d ";" -f1)
user_agent='Mozilla/5.0 (Linux; Android 9; SM-A205F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.143 Mobile Safari/537.36'

#banner
echo '''
			  ____  ____  _  _ 
			 (  __)/ ___)( \/ )
			  ) _) \___ \/ \/ \
			 (__)  (____/\_)(_/
			{ Free Send Message }

'''
#asking
read -p $'nomor: \e[1;33m' num
read -p $'\e[1;37mpesan: \e[1;33m' message

#mengambil value yang diperlukan dan mengambil captcha
data=$(curl -s "$host/alpha/index.php?a=keluar" \
			-H "User-Agent: ${user_agent}" \
			-H "Cookie: ${cookie};" \
			-H "Referer: $host/alpha/send.php")
			#siap mengirim
			send=$(curl -s -X POST "$host/alpha/send.php" \
						-H "User-Agent: ${user_agent}" \
						-H "Cookie: ${cookie};" \
						-H "Referer: $host/alpha" \
						-d "nohp=${num}&pesan=${message}&captcha="$(echo "$data" | grep "<span>.*"  | cut -d ">" -f2 | cut -d "=" -f1 | bc)"&key="$(echo "$data" | grep -o 'name="key" value=".*' | cut -d '"' -f4))
						#if statment
						if [[ $send =~ "SMS Gratis Telah Dikirim" ]]; then
							echo -e "${blue}[${yellow}+${blue}] ${green}pesan terkirim ke${white}: ${yellow}$num${white}" | pv -qL 25
						else
							echo -e "${blue}[${red}!${blue}] ${red}pesan tidak terkirim${white}"
							echo -e "${green}kemungkinan${white}: \n > nomor salah\n > nomor yang anda kirim pesan sudah mencapai batas limit\n > sinyal anda jelek\n > dan anda jelek." | pv -qL 35
						fi
#end
