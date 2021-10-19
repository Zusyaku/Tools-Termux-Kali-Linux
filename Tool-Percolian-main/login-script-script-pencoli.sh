#!/bin/sh


#warna script mang
biru='\033[34;1m'
hijau='\033[32;1m'
ungu='\033[35;1m'
cyan='\033[36;1m'
merah='\033[31;1m'
putih='\033[37;1m'
kuning='\033[33;1m'


#login mastodddd


clear

echo $cyan

figlet Login

echo $kuning

read -p 'user : ' user
if [ $user = Subrek ]
then
   sleep 2
fi

read -p 'pasw : ' pasw
if [ $pasw = FAGHP ]
then
   echo $hijau'berhasil'
   sh script-pencoli.sh
 else
  sleep 1
  echo $merah'gagal'
  sleep 1
  echo 'silahkan hub admin jika tidak tau passowrd nya'
  sleep 1
  xdg-open 'https://wa.me/6281313537943/?text=Assalamualaikum+Warahmatullahi+Wabarakatuh+Mastah+Apa+Passowrd+nya '
  sh login-script-script-pencoli.sh

fi

