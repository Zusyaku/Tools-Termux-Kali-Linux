#!/data/data/com.termux/files/usr/bin/bash

#             -=[ open source ]=-             #

######################################
#      -=[ code by polygon ]=-       #
#				     #
#  tidak ada yg membuat script ini   #
#  selain polygon		     #
#				     #
#  yg recode keluarga lu akan mati   #
#   mengenaskan amin                 #
# 				     #
# belajar lah menghargai karya orang #
#  merubah author itu sama seperti   #
#    mencuri karya orang lain        #
#				     #
#    coba kalo kalo karya kalian     #
#    di curi orang gimana rasanya    #
#    kalian buat susah susah         #
#    malah di curi orang             #
#    kalo pengen bisa berusaha lah   #
#    kamu di kasi tangan kasi kaki   #
#    kasi pemikiran di kasi tubuh    #
#    yg lengkap itu semua buat apa   #
#    sekarang ada internet beda sama #
#    dulu sekarang belajar lebih     #
#    gampang ada google ada youtube  #
#    				     #
#    saran jng suka mengambil karya  #
#             orang lain	     #
######################################

# di sini saya memakai function

function add(){

# ip=$(curl untuk melakukan requests) # pacth get
ip=$(
     curl -sX GET "ifconfig.me/all")

#  variabel ini untuk melakukan perintah ke if

out=$(echo "$ip" | grep -o "ip_addr:")

if test "$out" == "ip_addr:"; then
         sleep 1
       out=$(echo "$ip" | head -1 | tr -d "ip_addr: ")

 # frame
  delay=0.1
 text="ip kamu $out"
  inp=${#text}
  num=0
  fr="$num<=100"
 Ifs=$'\n'

# loop while
    while (($num<=100)); do
	     n=$((inp*num / 80))
             printf "\e[00;36m\r[\e[93m%-${inp}s\e[96m]\e[00m" "${text:0:n}"
             ((num += RANDOM%10))
		command sleep $delay
            done
fi
  }

function banner(){

banner=$(figlet -f smmono12 "enc-python")


set consol python2
python2 -c '
import time,os,sys

ku="\033[95m"
bi="\033[94m"
me="\033[91m"
ij="\033[92m"
pu="\033[97m"
cy="\033[96m"
st="\033[00m"

def bct(teks):
 for i in teks + "\n":
  sys.stdout.write(i)
  sys.stdout.flush()
  time.sleep(0.01)
bct(me +"▗▄▄▖ ▄▖ ▗▄▗▄▄▄▖▗▖ ▗▖ ▗▄▖ ▗▄ ▗▖     ▗▄▄▄▖▗▄ ▗▖  ▄▄"+ st)
bct(me +"▐▛▀▜▖▐▙ ▟▌▝▀█▀▘▐▌ ▐▌ █▀█ ▐█ ▐▌     ▐▛▀▀▘▐█ ▐▌ █▀▀▌"+ st)
bct(me +"▐▌ ▐▌ █▄█   █  ▐▌ ▐▌▐▌ ▐▌▐▛▌▐▌     ▐▌   ▐▛▌▐▌▐▛"+ st)
bct(me +"▐██▛  ▝█▘   █  ▐███▌▐▌ ▐▌▐▌█▐▌     ▐███ ▐▌█▐▌▐▌"+ st)
bct(pu +"▐▌     █    █  ▐▌ ▐▌▐▌ ▐▌▐▌▐▟▌ ██▌ ▐▌   ▐▌▐▟▌▐▙"+ st)
bct(pu +"▐▌     █    █  ▐▌ ▐▌ █▄█ ▐▌ █▌     ▐▙▄▄▖▐▌ █▌ █▄▄▌"+ st)
bct(pu +"▝▘     ▀    ▀  ▝▘ ▝▘ ▝▀▘ ▝▘ ▀▘     ▝▀▀▀▘▝▘ ▀▘  ▀▀"+ st)
'
}

function main(){
command clear
         banner
                IFS=$"\n"
        { printf "$IFS" }
          }
            add
          echo
        printf "\e[1;104m                                ==[ code by Polygon ]==                                \e[00m\n" && sleep 2 && echo && sleep 0.1
       printf "
                            \e[1;33mprogram \e[91m: \e[97mbash py\e[00m\n                            \e[1;32myoutube \e[91m: \e[96mpejuang kentang\e[00m\n
" && sleep 0.1
       printf "\e[1;41m                                   -=[ compile ]=-                                     \e[00m\n" && echo

       read -p $'\e[00mMasukan nama file nya \e[91m: \e[96m' firs
     echo && sleep 5
       read -p $'\e[00mmasukan output \e[91m: \e[92m' trr

          local set test
        command echo

      if test "$trr" == "$trr"; then
               sleep 0.1
                         count=0
                         total=34
                         pstr="compile $firs"

			   printf "\e[93m"
                           while [ $count -lt $total ]; do
                              sleep 0.5 # loop
                              count=$(( $count + 1 ))
                              pd=$(( $count*73 / $total ))
                                printf "\r%3d.%1d%% %.${pd}s" $(( $count * 100 / $total )) $(( ($count * 1000 / $total) % 10 )) $pstr
                       done
               echo
                 echo
                      pip=$(emojify -i $firs -o $trr >> tem)

                     out=$(cat tem | grep -o "done :)")
                  
                     if test "$out" == "done :)"; then
			     command echo && printf "\e[92mBerhasil..\e[00m\n" && command sleep 1 && command echo && rm -rf tem && command exit 1
	             else
    			 command echo && printf "\e[97m[ \e[91mx \e[97m] \e[00mGAGAL..\n" && command sleep 1 && command echo && rm -rf tem && command exit 0
                 fi
                    rm -rf tem
            fi

}
      { set main }
         }

main
