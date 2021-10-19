#!/usr/bin/bash

#Warna
b='\e[1;34m' #blue
g='\e[1;32m' #green
p='\e[1;35m' #purple
c='\e[1;36m' #cyan
r='\e[1;31m' #red
w='\e[1;37m' #white
y='\e[1;33m' #yellow

banner(){
clear
printf "
$r┻┳|$g―-∩       $c  (FakeSubdomain)
$r┳┻|$g　　ヽ   $y Author: Mr.404rgr
$r┻┳|$g　●   |  $y Team : Rao Cyber Team
$r┳┻|$g▼) _ノ   $y Github : github.com/404rgr
$r┻┳|$g￣　)
$r┳ﾐ$g(￣ ／            Warning!g !!!
$r┻┳T$g￣     Jangan gunakan atau akan terbuly
"
}
menu(){
printf "$c [+] Pilih ? [+]
$y[1]$p randomNumber.url
$y[2]$p [subdo]random.url
$y[3]$p randomNumber[Subdo].url
"
}
banner
menu
read -p "=> " pa

if [ $pa = 1 ]||[ $pa = satu ];
then
read -p "Nama Domain ?=> http://" domain
read -p "Jumlah (1-9999) ?=> " jumlah
read -p "Output (fake.txt) ?=> " output
count=1
while [ $count -le $jumlah ]
do
printf "http://$RANDOM.$domain\n" >> $output
echo "[$count] Generated => $output"
sleep 000.1;
(( count++ ))
done
echo "[+] Berhasil Membuat File [+]"
echo -e $g "  (-) $output (-)"
exit

elif [ $pa = 2 ]||[ $pa = dua ];
then
read -p "Nama Domain ?=> http://" domain
read -p "Subdomain (ex: faker) ?=> " subdo
read -p "Jumlah (1-9999) ?=> " jumlah
read -p "Output (fake.txt) ?=> " output
count=1
while [ $count -le $jumlah ]
do
printf "http://$subdo$RANDOM.$domain\n" >> $output
echo "[$count] Generated => $output"
sleep 000.1;
(( count++ ))
done
echo "[+] Berhasil Membuat File [+]"
echo -e $g "  (-) $output (-)"
exit

else
read -p "Nama Domain ?=> http://" domain
read -p "Subdomain (ex: faker) ?=> " subdo
read -p "Jumlah (1-9999) ?=> " jumlah
read -p "Output (fake.txt) ?=> " output
count=1
while [ $count -le $jumlah ]
do
printf "http://$RANDOM$subdo.$domain\n" >> $output
echo "[$count] Generated => $output"
sleep 000.1;
(( count++ ))
done
echo "[+] Berhasil Membuat File [+]"
echo -e $g "  (-) $output (-)"
exit

fi

