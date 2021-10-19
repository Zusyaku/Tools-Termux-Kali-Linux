# Tema termux






# Settings pertama dan penginstallan


pkg update && pkg upgrade && pkg install git


termux-setup-storage


pkg install python2


pkg install nano


pkg install bash


git clone https://github.com/xxoprt/tema


cd tema


cp promt($) /sdcard

cp tmp.py /$HOME

cp date.sh

cd $HOME


nano tmp.py


# Langkah 1 


di y='FAGHP' di situ ganti jadi y='nama kalian'


di x='Ganteng:v' di situ ganti apa aja x='Terserah kalian'


Teken tombol CTRL dan pencet huruf x trus y trus pencet tombol enter


# langkah 2

Buka apk ZArchiver

Cari naam nya promt($)

Pencet buka di text editor trus nama gw ganti nama kalian

Trus save

Salin semua 

Langjut langkah 3

# langkah 3
cd $HOME


cd ../usr/etc

nano bash.bashrc

Hapus semua dan ketik

clear


python2 tmp.py

PS1='\033[1;34m\]╔━━\[\033[1;31m\]≼\[\033[1;90m\]Nama kalian ganti ok \[\033[00;34m\]● \[\033[1;30m\]\w\[\033[1;31m\] ≽\[\033[1;34m\]
\[\033[1;34m\]╚══\[\033[1;34m\]•\[\033[1;31m\]‣\[\033[1;90m\] '



Teken tombol CTRL dan pencet huruf x trus y trus pencet tombol enter

# langkah terakhir 
kalian tinggal keluar dari termux
Atau exit di termux lalu login lagi
