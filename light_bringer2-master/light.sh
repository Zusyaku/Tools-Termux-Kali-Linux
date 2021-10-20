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
light(){
    echo " .   :' . :   .  .'.' '....xxxxx...,'. '   ' .'''"
    sleep 0.03
    echo " ' .  . : . .' :  . ..XXXXXXXXXXXXXXXXXXXXx.    ' "
    sleep 0.03
    echo "  .    . .   .  ..XXXXXXXXWWWWWWWWWWWWWWWWXXXX.  ."
    sleep 0.03
    echo ":  : . : .  ...XXXXXWWW'   W88N88@888888WWWWWXX.   "
    sleep 0.03
    echo "  . :   ...XXXXXXWWW'    M88N88GGGGGG888^8M 'WMBX.   "
    sleep 0.03
    echo "     ..XXXXXXXXWWW'     M88888WWRWWWMW8oo88M   WWMX.  "
    sleep 0.03
    echo " 'XXXXXXXXXXXXWW'       WN8888WWWWW  W8@@@8M    BMBRX. "
    sleep 0.03
    echo "XXXXXXXX=MMWW':  .      W8N888WWWWWWWW88888W      XRBRXX. "
    sleep 0.03
    echo " '''XXXXXMM::::. .        W8@889WWWWWM8@8N8W      . . :RRXx. "
    sleep 0.03
    echo "  ..'''  MMM::.:.  .      W888N89999888@8W      . . ::::'RXV "
    sleep 0.03
    echo "  '''      MMMm::.  .      WW888N88888WW     .  . mmMMMMMRXx "
    sleep 0.03
    echo "            ''MMmm .  .       WWWWWWW   . :. :,miMM'''  : '''"
    sleep 0.03
    echo "      .  .       ''MMMMmm . .  .  .   ._,mMMMM'''  :  ' .  : "
    sleep 0.03
    echo "                       ''MMMMMMMMMMMMM''' .  : . '   .       "
    sleep 0.03
    echo "        .     .    .                   HM                     "
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
get_url=$(curl -s http://zlucifer.com/api/hackbae.php?request=nik)
tips(){
        echo "TIPS: "
        echo " Minta nomor rekening (Atas Nama) dan "
        echo " NIK penjual untuk di cek keasliannya"
        echo
        echo " Penjual tidak mau memberi NIK = Waspada"
        echo " Nama pemilik NIK tidak muncul = Waspada"
        echo " Nama pemilik NIK dan Nama pemilik rekening berbeda = Waspada"
        echo " Nama pemilik NIK sama dengan Nama pemilik rekening = Penjual asli"
        echo " Meskipun penjual asli, tetap waspada"
}
close(){
        exit
}
akhir(){
        echo " Tools ini gratis"
        echo " Spesial 1.000.000 subscriber HackBae"
        echo " Dilarang menjual belikan tools ini"
        echo " Dilarang menyalahgunakan tools ini :)"
        echo "==================================="
}
mulai(){
    echo "Masukan angka 1 untuk tips, dan 2 untuk melakukan pengecekan"
    echo " [1] Tips"
    echo " [2] Cek"
    echo " [3] Close Light Bringer"
    echo "1/2/3?"
    read info
    if [ $info = "1" ]; then
            clear
            light
            tips
            mulai
    elif [ $info = "3" ]; then
            echo "Terimakasih sudah menggunakan Light Bringer Project"
            close
    else
            clear
            light
            echo
            echo "Silahkan masukan NIK target"
            echo " Contoh 1234567890876543"
            read target # masukin NIK
            echo "Silahkan masukan Nama target"
            read nama #nama
            echo
            echo Apakah NIK $target "& Nama "$nama "sudah benar?"
            echo y/n?
            read confirm
            echo
            if [ $confirm = "y" ]; then
                  echo Melakukan Pengecekan NIK $target "& Nama "$nama
                  load
                  clear
                  light
                  cek_target=`curl -s $get_url/nik.php?nik=$target"&nama="$nama`
                  echo -e $cek_target
            else
                  echo Kesalahan, silahkan coba lagi
            fi
            akhir
            mulai
    fi
}
clear
echo "Loading.."
load
clear
light
echo Selamat datang kak, Siapa nick kaka? #tulisan keluar
read nick #membaca yang ditulis
clear
light
echo "==============================="
sleep 2
echo " Light Bringer Project"
sleep 0.7
echo "==============================="
echo " Tools Pencegah Penipuan Online "
echo Selamat datang $nick ":)"
mulai
akhir
