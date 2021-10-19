#!/data/data/com.termux/files/usr/bin/bash
clear
#get current dir
pdir=$(pwd)
#installing necessary packages
apt install figlet toilet -y > /dev/null 2>&1
pkg install ncurses-utils -y > /dev/null 2>&1
# Setting up commands
getCPos() (
	local opt=$*
	exec < /dev/tty
	oldstty=$(stty -g)
	stty raw -echo min 0
	# on my system, the following line can be replaced by the line below it
	echo -en "\033[6n" > /dev/tty
	# tput u7 > /dev/tty    # when TERM=xterm (and relatives)
	IFS=';' read -r -d R -a pos
	stty $oldstty
	# change from one-based to zero based so they work with: tput cup $row $col
	row=$((${pos[0]:2} - 1))    # strip off the esc-[
	col=$((${pos[1]} - 1))
	if [[ $opt =~ .*-row.* ]]
	then
		printf $row
	else
		printf $col
	fi
)
spinner() (
	PID=$!
	stty -echo
	local opt=$*
	tput civis
	cstat(){
		local optstat="$(if [[ ! $opt =~ .*$1.* ]]
						 then
							 echo 0
						 else
							 echo 1
						 fi)"
		#echo $opt
		echo $optstat
	}
	#echo $(cstat -s)
	if [ "$(cstat -s)" -eq 1 ]
	then
		printf '\n'
		# While process is running...
		while kill -0 $PID 2> /dev/null;
		do  
			printf '\u2588\e[1B\e[1D\u2588\e[1A'
    		sleep 0.3
		done
	elif [ "$(cstat -p)" -eq 1 ]
	then
		while kill -0 $PID 2> /dev/null;
		do  
			printf '\u2588\e[1B\e[1D\u2588\e[1A'
    		sleep 0.3
		done
	elif [ "$(cstat -t)" -eq 1 ]
	then
		until [ $(getCPos) -eq $(($(tput cols))) ]
		do
			#echo $(getCPos) >> log.txt
			#getCPos
			#tput cols
			if [ ! $(getCPos) -eq $(($(tput cols)-1)) ]
			then
				printf '\u2588\e[1B\e[1D\u2588\e[1A'
				printf '\u2588\e[1B\e[1D\u2588\e[1A'
			else
				#echo 1
				#echo hi
				local row=$(($(getCPos -row)+1))
				local plen=$(tput cols)
				printf '\u2588'
				tput cup "$row" "$plen"
				printf '\u2588'
				break
			fi
		done
		printf "\n\n\nDone!\n"
	fi
	#echo hh
	tput cnorm
	stty echo
)
#Updating secondary packages
echo Updating Packages....	
pip install mdv > /dev/null 2>&1 & spinner -s
apt-get update > /dev/null 2>&1 & spinner -p
apt-get upgrade -y > /dev/null 2>&1 & spinner -p
apt-get autoremove > /dev/null 2>&1 & spinner -p
apt-get autoclean > /dev/null 2>&1 & spinner -p
apt-get install git -y > /dev/null 2>&1 & spinner -p && spinner -t
clear
#Script starts
#cd $HOME
#cd termuxstyling
echo Script made by:- Dark Warrior
#Uninstall
if [ -e ".user.cfg" ]
then
	uname=$(sed '1q;d' .user.cfg)
	istate=$(sed '2q;d' .user.cfg)
	if [ "$istate" -eq "1" ]
	then
		printf "Uninstall? [Y/N]: "
		read ink1
		case $ink1 in
			[yY][eE][sS]|[yY])
		rm .user.cfg;
		echo $uname > .user.cfg
		echo 0 >> .user.cfg
		cd
		cd /$HOME
		cd ..
		cd usr/etc
		echo "command_not_found_handle() {
        	/data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
		} 
		PS1='\$ '" > bash.bashrc & echo "" & spinner -t && clear
		echo "Welcome to Termux!
		Wiki:            https://wiki.termux.com
		Community forum: https://termux.com/community
		IRC channel:     #termux on freenode
		Gitter chat:     https://gitter.im/termux/termux
		Mailing list:    termux+subscribe@groups.io

		Search packages:   pkg search <query>
		Install a package: pkg install <package>
		Upgrade packages:  pkg upgrade
		Learn more:        pkg help" > motd
		cd
		cd /$HOME
		figlet FemurTech
		echo Now Your Termux is back to Original
		echo "Uninstalled Succesfully"
		exit 0
		;;
			*)
		;;
		esac
	fi
fi
#Assigns Username
if [ ! -e ".user.cfg" ] 
then
	printf "Type your username: "
	read uname
	echo "This is your username: $uname"
	echo "$uname" > .user.cfg
	echo "1" >> .user.cfg
	clear
#Rename Username
else
	printf "Would You Like to Change Your Username[Y/N]: "
	read ink
	case "$ink" in
		[yY][eE][sS]|[yY])
	rm .user.cfg;
	clear
	bash setup.sh;
	;;
	*)
	clear
	echo "Welcome back $uname"
	;;
	esac
fi
#installing script
echo "Installing..."
mkdir -p $PREFIX/var/lib/postgresql > /dev/null 2>&1 & spinner -s
if [ -e "/data/data/com.termux/files/usr/etc/motd" ];then rm ~/../usr/etc/motd;fi & spinner -p
sleep 0.1 & spinner -p && spinner -t
#Set default username if found null
if [ -z "$uname" ]
then
	uname="FemurTech"
fi
#Sets bash.bashrc aka startup
echo "command_not_found_handle() {
        /data/data/com.termux/files/usr/libexec/termux/command-not-found "'$1'"
}
shell() {
	bash \$1.sh 2>/dev/null
	if [ \$? -ne 0 ]
	then 
		bash \$1.bash 2>/dev/null
		if [ \$? -ne 0 ]
		then
			printf '\e[0;31mNo shell script found\n'
		fi
	fi
}
shellx() {
	bash \$1*.sh 2>/dev/null
	if [ \$? -ne 0 ]
	then 
		bash \$1*.bash 2>/dev/null
		if [ \$? -ne 0 ]
		then
			printf '\e[0;31mNo shell script found\n'
		fi
	fi
}
cds() { 
	if [[ \$* == *\"-i\"* ]]
	then
		var=\"\$*\"
		sub=\"\"
		qry=\$( echo \$var | sed 's/-i//g' )
		qry=\$( echo \$qry | sed 's/ //g' )
		echo finding \\\"\$qry\\\"
		cd \"\$( find \"\$(pwd)/\" -maxdepth 3 -not \\( -path \"/sdcard/Android/*\" -prune \\) -type d -iname \"\$qry\" -print -quit )\"
	else
		echo finding \$1
		cd \"\$( find \"\$(pwd)/\" -maxdepth 3 -not \\( -path \"/sdcard/Android/*\" -prune \\) -type d -name \"\$1\" -print -quit )\"
	fi
}
cdp() { 
	if [[ \$* == *\"-i\"* ]]
	then
		var=\"\$*\"
		sub=\"\"
		qry=\$( echo \$var | sed 's/-i//g' )
		qry=\$( echo \$qry | sed 's/ //g' )
		echo finding \\\"\$qry\\\"
		cd \"\$( find \"\$(pwd)/\" -maxdepth 3 -not \\( -path \"/sdcard/Android/*\" -prune \\) -type d -iname \"\$qry\"* -print -quit )\"
	else
		echo finding \$1
		cd \"\$( find \"\$(pwd)/\" -maxdepth 3 -not \\( -path \"/sdcard/Android/*\" -prune \\) -type d -name \"\$1\"* -print -quit )\"
	fi
}
updatedw() {
	ppath=\${pwd};
	cd \$HOME
	if [ -d \"\$HOME/termuxstyling\" ]
	then
		cd termuxstyling
		git fetch >/dev/null
		var=\$(git status | grep 'Your branch')
		# echo \$var
		if [[ \$var == *\"up to date\"* ]];
		then 
			clear && echo \"Already running the latest version!!\" && echo ------------------------------------- && figlet \$(sed '1q;d' 'ver.cfg') && figlet FemurTech
		else
			git pull
			bash setup.sh;
			clear && echo \"Update Success\" && echo -------------- && figlet Success && figlet \$(sed '1q;d' 'ver.cfg') && figlet FemurTech && echo Restart to apply changes
		fi
	else
		git clone https://github.com/darkwarrior3/termuxstyling.git
		cd termuxstyling
		prm sh
		clear
		bash
		bash setup.sh
		wait
		echo \"Update Success\" && echo -------------- && figlet Success && figlet \$(sed '1q;d' '/data/data/com.termux/files/home/termuxstyling/ver.cfg') && figlet FemurTech && echo Restart to apply changes
	fi
	cd \$ppath
}
prm() { chmod +x *.\$1; }
txt() { cat \$1.*; }
figlet $uname
PS1='\033[1;91mroot@termux[\033[1;93m\W\033[1;91m]:
# \033[1;92m'
if [ -d \"\$HOME/termuxstyling\" ]
then
	if grep -q '# 011' \"/data/data/com.termux/files/home/termuxstyling/.user.cfg\"
	then
		lnum=\$( sed '3q;d' \"/data/data/com.termux/files/home/termuxstyling/.user.cfg\" )
		lnum=\$( echo \$lnum | sed 's/# 011//g' )
		lnum=\$( echo \$lnum | sed 's/ //g' )
		echo \$( sed '3q;d' \"/data/data/com.termux/files/home/termuxstyling/.user.cfg\" )
			if [[ ! \$lnum -eq 5 ]]
			then
				lnum=\$((\$lnum+1))
				sed -i \"/.*# 011.*/ c\\ \$lnum # 011\" \"/data/data/com.termux/files/home/termuxstyling/.user.cfg\"
			else
				lnum=1
				sed -i \"/.*# 011.*/ c\\ \$lnum # 011\" \"/data/data/com.termux/files/home/termuxstyling/.user.cfg\"
				cd \$HOME
				cd termuxstyling
				git fetch >/dev/null
				test=\$(git status | grep 'Your branch')
				echo \$test
				sleep 5
				if [[ ! \$test == *\"up to date\"* ]];
				then
					updatedw
				fi
			fi
	else
		echo hi
		echo \"1 # 011\" >> \"/data/data/com.termux/files/home/termuxstyling/.user.cfg\"
	fi
else
	updatedw
fi
cd
alias md=\"mkdir\"
alias msf=\"msfconsole\"
alias msfdb=\"initdb \$PREFIX/var/lib/postgresql;pg_ctl -D \$PREFIX/var/lib/postgresql start \"
alias clear=\"clear;printf '\e[0m';figlet $uname\"
alias dir=\"ls\"
alias ins=\"pkg install\"
alias ains=\"apt install\"
alias cls=\"clear\"
alias rf=\"rm -rf\"
alias gic=\"git clone\"
alias fuck=\"printf '\e[0m';figlet FUCK;figlet OFF\"
alias upg=\"git reset --hard;git pull\"
alias update=\"apt-get update;apt-get upgrade\"" > /data/data/com.termux/files/usr/etc/bash.bashrc
cd /$HOME
cd termuxstyling
echo Script made by
toilet Dark
toilet Warrior
sleep 2
mdv README.md
cd $pdir
echo Subscribe to our YT channel FemurTech
echo tinyurl.com/femurtech
echo Restart to apply changes