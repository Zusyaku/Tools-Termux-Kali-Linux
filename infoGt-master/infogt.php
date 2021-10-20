<?php
// jangan ganti kalo mau di hargai
// Kancot1ST - Kancot Team
// Thanks to : https://github.com/mrcakil/InfoGa/
// Install Curl
@system("apt-get install curl ; clear");
//Color
$b="\033[0;34m";
$c="\033[0;36m";
$g="\033[0;35m";
$o="\033[92m";
$l="\033[1;32m";
$w="\033[1;37m";
$r="\033[1;31m";
$y="\033[1;33m";
print "$l |=|============================|=|\n";
print "$y     Kancot Team - Mr.Kancot1ST \n";
print "$y    https://github.com/kancotdiq\n";
print "$l |=|============================|=|\n\n
    $r [1]$l Whois Lookup
    $r [2]$l Traceroute
    $r [3]$l DNS Lookup
    $r [4]$l Reverse DNS Lookup
    $r [5]$l GeoIP Lookup
    $r [6]$l Port Scan
    $r [7]$l Reverse IP Lookup
    $r [8]$l Keluar\n\n";
echo "$b Pilih : $y"; $pilih=trim(fgets(STDIN));
if($pilih=="1"){
		echo "$b Masukkan IP / Domain : $y"; $whois=trim(fgets(STDIN));
		echo "$w" ; @system("curl http://api.hackertarget.com/whois/?q=$whois");
		echo "$l Done$r ... $w";
}
elseif($pilih=="2"){
		echo "$b Masukkan IP / Domain : $y"; $traceroute=trim(fgets(STDIN));
			echo "$w" ; @system("curl https://api.hackertarget.com/mtr/?q=$traceroute");
			echo "$l Done$r ... $w";
}
elseif($pilih=="3"){
		echo "$b Masukkan IP / Domain : $y"; $dns=trim(fgets(STDIN));
         echo "$w" ; @system("curl http://api.hackertarget.com/dnslookup/?q=$dns");
		 echo "$l Done$r ... $w";
}
elseif($pilih=="4"){
		echo "$b Masukkan IP / Domain : $y"; $rev=trim(fgets(STDIN));
      echo "$w" ; @system("curl https://api.hackertarget.com/reversedns/?q=$rev");
	   echo "$l Done$r ... $w";
}
elseif($pilih=="5"){
		echo "$b Masukkan IP / Domain : $y"; $geo=trim(fgets(STDIN));
		echo "$w" ; @system("curl http://api.hackertarget.com/geoip/?q=$geo");
		echo "$l Done$r ... $w";
}
elseif($pilih=="6"){
	echo "$b Masukkan IP / Domain : $y"; $port=trim(fgets(STDIN));
	echo "$w" ; @system("curl http://api.hackertarget.com/nmap/?q=$port");
	echo "$l Done$r ... $w";
}
elseif($pilih=="7"){
	echo "$b Masukkan IP / Domain : $y"; $revip=trim(fgets(STDIN));
	echo "$w" ; @system("wget http://api.hackertarget.com/reverseiplookup/?q=$revip ; clear ; curl http://api.hackertarget.com/reverseiplookup/?q=");
	echo "$b File saved Gan ";
	@system("pwd");
	echo "File : index.html?q=$revip";
}
elseif($pilih=="8"){
echo "$l Keluar$r ... :) ";
@system("sleep 4 ; clear");
}
?>
