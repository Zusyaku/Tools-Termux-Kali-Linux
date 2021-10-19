<?php


/*
Author : Kingtebe
Date   : 24 Mei 2021 15.30 WIB
Script : Nuyul Faucetpay To Doge With Termux
*/


class faucetpay {

	public function __construct(){
		system('clear');
		$this->doge_crypto();}
		var $logo = "\n           \e[37m/\e[33m^-^\e[37m\ \n          \e[37m/ o o \e[37m\ \n         \e[37m/   \e[31mY   \e[37m\               \e[31m[ \e[32mONLINE \e[31m]\n         \e[31mV \e[37m\ v \e[37m/ \e[31mV\n           \e[37m/ \e[31m- \e[37m\      Nuyul doge with termux Vers.Cli\n          \e[37m/    |          made by \e[34mkingtebe \e[37m© 2021\n    \e[33m(    \e[37m/     |\n     \e[33m===\e[37m/___) ||\n\n\n";

	public function doge_crypto(){
		echo $this->logo;
		echo "\e[34m• \e[37mYour wallet doge : \e[32m";
		$doge = trim(fgets(STDIN)); echo "\n";

		$url = "http://uptocoin.tk/fp/faucet.php?address=D6awpBs4XhGfdoYt72qB6iJEdKZMaYRTYq&currency=DOGE&key=a3c1a742d80309d9fed7b3c6ec253956";
		while(true){
			$header = array("user-agent: Mozilla/5.0 (Linux; Android 8.1.0; CPH1853) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36","Host : uptocoin.tk","Accept : text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","referer : https://uptocoin.tk/fp/");
			$api = "https://uptocoin.tk/fp/verify.php";
			$data = "address=$doge&currency=DOGE";

			$ch = curl_init();
			curl_setopt($ch, CURLOPT_URL, $api);
			curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
			curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
			curl_setopt($ch, CURLOPT_POST, 1);
			curl_setopt($ch, CURLOPT_HTTPHEADER, $header);
			curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
			curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
			$result = curl_exec($ch);
			$ch = curl_init();
			curl_setopt($ch, CURLOPT_URL, $url);
			curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
			curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
			curl_setopt($ch, CURLOPT_HTTPHEADER, $header);
			curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
			$res = curl_exec($ch);
				$hemkel_pro = explode('<div class="alert alert-success">', $result);
				$repr_true = explode('<a target="_blank"', $hemkel_pro[1]);
				$execute = $repr_true[0];
				echo "\e[33m$execute"."\e[33mfaucetpay\n";
			for($coli=60;$coli>-1;$coli--){
 			        echo "\r                                             \r";
		                        echo "\e[34m• \e[37mWait \e[32m$coli \e[37mSecond ";sleep(1);
			        echo "\r                                             \r";}}}}

new faucetpay;


?>
