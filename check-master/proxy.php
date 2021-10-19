<?php
if (!is_dir('OutPut')) {
    mkdir('OutPut');
}
echo "Source Bye : Github.com/kumpulanremaja";
echo "Web : Kumpulanremaja.com";
echo "Fanspage : fb.me/4kumpulanremaja";
echo "\033[1;32mEnter Your Proxy List \033[1;31m:\033[1;0m ";
$list = trim(fgets(STDIN));
echo "\033[1;32mEnter Your Output \033[1;31m:\033[1;0m ";
$file = trim(fgets(STDIN));
$url = "ifconfig.co/json";
$myfile = fopen("OutPut/".$file, "w") or die("Unable to open file!");
$file_lines = file($list);
if (!$file_lines){
   echo "\033[1;31mERROr : Unable Open ".$list."\n";
   exit();
}
echo "\n\n\033[0;32m[\033[1;33m!\033[0;32m] \033[1;33mCek Jumlah Proxy";
sleep(1);
echo " \033[1;0m•";
sleep(1);
echo "•";
sleep(1);
echo "•";
sleep(1);
echo "•";
$no = 0;
foreach ($file_lines as $line) {
    $no++;
}
sleep(1);
echo "•\n";
sleep(1);
echo "\033[0;32m[\033[1;0m•\033[0;32m]\033[1;32m Total Proxy\033[1;31m :\033[1;0m ".$no."\n\n\n";
$i = 0;
foreach ($file_lines as $line) {
    $i++;
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_PROXY, $line);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
    curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 0);
    curl_setopt($ch, CURLOPT_TIMEOUT, 30);
    $result = curl_exec($ch);
    $info = curl_getinfo($ch);
    curl_close($ch);
    $json = json_decode($result, true);
    if ($json["ip"] == true){
       echo "\033[0;32m[\033[1;32m✔\033[0;32m] \033[1;32mTerhubung Ke \033[1;0m".$line;
       echo "\033[1;33m    - \033[1;32mIp \033[1;31m     :\033[1;0m ".$json["ip"]."\n";
       echo "  \033[1;33m  - \033[1;32mCountry\033[1;31m :\033[1;0m ".$json["country"]."\n";
       echo " \033[1;33m   -\033[1;32m City\033[1;31m    :\033[1;0m ".$json["city"]."\n";
       echo "\033[1;33m    -\033[1;32m Speed \033[1;31m  :\033[1;0m ".$info['total_time']." Second\n";
       echo "\033[1;33m    -\033[1;32m No \033[1;31m     : \033[1;0m".$i."\n\n";
       fwrite($myfile, $line);
    }else{
       echo "\033[0;31m[\033[1;31m✖\033[0;31m]\033[1;31m Gagal Terhubung Ke\033[1;0m ".$line;
       echo "\033[0;31m    -\033[1;31m Speed \033[1;31m  :\033[1;0m ".$info['total_time']." Second\n";
       echo " \033[0;31m   -\033[1;31m No  \033[1;31m    :\033[1;0m ".$i."\n\n";
    }
}
echo "\033[0;32m[\033[1;0m•\033[0;32m] \033[1;32mProxy Aktif\033[1;0m ".$i."\n";
fclose($myfile);
