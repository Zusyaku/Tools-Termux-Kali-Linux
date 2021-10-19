#!/data/data/com.termux/usr/bin/bash
pkg install figlet -y
pkg install neofetch -y
clear
sleep 2
echo '''

                         
 _____ _____ _____ _____ 
|   __|  |  | __  |   __|
|__   |  |  | __ -|__   |
|_____|_____|_____|_____|
                         
     '''
sleep 2
xdg-open https://youtube.com/channel/UCXpOIsauw8NjH0t4tSXSY-Q
sleep 2
clear
sleep 2
echo '''

                                                             
 ____  _____ _____ _____       _____ _____ _____ _____ _____ 
|    \|  _  | __  |  |  |     |_   _|  |  |   __|     |   __|
|  |  |     |    -|    -|       | | |     |   __| | | |   __|
|____/|__|__|__|__|__|__|_____  |_| |__|__|_____|_|_|_|_____|
                        |_____|                              

     '''
echo '[+] Author : NOT BURIQ'
echo '[+] Team : DARK NETWORK/BC'
echo '[+] Github : https://www.github.com/DARK-02'
echo ''
echo ''
read -p $'\e[32mNama Anda :\e[0m ' target
cd $HOME
cd ..
cd usr
cd etc
rm bash.bashrc
cat <<LOGIN>bash.bashrc
if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
        command_not_found_handle() {
                /data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
        }
fi
clear
echo "
             *********
           *************
          *****     *****
         ***           ***
        ***             ***
        **    0     0    **
        **               **                  ____
        ***             ***             //////////
        ****           ****        ///////////////
        *****         *****    ///////////////////
        ******       ******/////////         |  |
      *********     ****//////               |  |
   *************   **/////*****              |  |
  *************** **///***********          *|  |*
 ************************************    ****| <=>*
*********************************************|<===>*
*********************************************| <==>*
***************************** ***************| <=>*
******************************* *************|  |*
********************************** **********|  |*
     *-------------------------------*
     |  KITA SEMUA PASTI AKAN MATI   |
     *-------------------------------*
"
sleep 4
clear
sleep 2
echo 'Hello $target '
sleep 3
neofetch
echo '
          ┈┈╱▔▔▔▔▔▔▔▔▔▔▔▏
          ┈╱╭▏╮╭┻┻╮╭┻┻╮╭▏
          ▕╮╰▏╯┃╭╮┃┃╭╮┃╰▏
          ▕╯┈▏┈┗┻┻┛┗┻┻┻╮▏
          ▕╭╮▏╮┈┈┈┈┏━━━╯▏
          ▕╰╯▏╯╰┳┳┳┳┳┳╯╭▏
          ▕┈╭▏╭╮┃┗┛┗┛┃┈╰▏
          ▕┈╰▏╰╯╰━━━━╯┈┈▏
...:::::::: HELLO ADMIN ::::::::...
'
nifce=$(ip r show | cut -d " " -f 3)


r='\[\e[1;31m\]'
g='\[\e[1;32m\]'
y='\[\e[1;33m\]'
b='\[\e[1;34m\]'
p='\[\e[1;35m\]'
c='\[\e[1;36m\]'
w='\[\e[1;37m\]'

# simple kali prompt
PS1="\e[1;32m> "

# 2nd prompt
#PS1="\n$r╔═[ $c\@ $r] [ $c\V $r] [ $c$nifce $r] [ $c\W $r] [ $c\j $r]\n$r║ \n$r╚═[$c th3unkn0n $r] $c>> "

# corsor and it's color
echo -e '\e[3 q'
echo -ne "\033]12;#00ff00\007"
LOGIN
echo -e "\e[1;32mLu Berhasil Mempercantik Terminal eluuu BTW SUBREK \e[0m"
exit
