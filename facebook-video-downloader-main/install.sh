#!/bin/bash
pkg update -y
pkg upgrade -y
pip install --upgrade pip
clear
echo
echo
echo
clear
mkdir /sdcard/FBVIDEO
cd /sdcard/FBVIDEO
curl https://raw.githubusercontent.com/rixon-cochi/rixon-cochi/main/fbvideo.py >> fbvideo.py
clear
curl https://raw.githubusercontent.com/rixon-cochi/rixon-cochi/main/requirements.txt >> requirements.txt
clear
echo " code developer TECH COCHI "
sleep 6
xdg-open https://www.youtube.com/c/TECHCOCHI2
echo 
sleep 6
echo " now enter bash run.sh "
sleep 10
echo " create account on cashkaro.com "
echo " set your browser "
termux-open-url https://cashkaro.com?r=8026255&fname=Rixon
echo ""
echo " DOWNLOAD VIDEO ON YOUR SDCARD FOLDER NAME FBVIDEO "
