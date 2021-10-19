<?php

// Author : Kingtebe
// Date   : April 29, 05.27 WIB
// Script : Downloader Video Youtube

class down {

	public function __construct() {
		system('clear');
		$this->awokawok();}
		var $baner = "\n\n  ███╗   ███╗██████╗ ██╗  ██╗██████╗\n  ████╗ ████║██╔══██╗██║  ██║██╔══██╗\n  ██╔████╔██║██████╔╝███████║██║  ██║\n  ██║╚██╔╝██║██╔═══╝ ╚════██║██║  ██║\n  ██║ ╚═╝ ██║██║          ██║██████╔╝\n  ╚═╝     ╚═╝╚═╝          ╚═╝╚═════╝\n\n  *_-=[ Video Youtub Downloader ]=-_*\n	   Author : Kingtebe\n      -_=======================_-\n\n\n";

	public function awokawok() {
		try {
			echo $this->baner;
			echo " [+] Link : ";
			$url = trim(fgets(STDIN));sleep(1);
			echo " [!] Loading";
			for ($kata=0;$kata<=4;$kata++) {
				echo ".";
				sleep(1);}
			$api_web = file_get_contents("https://api.zeks.xyz/api/ytmp4?url=$url=tOMFR0nQt48&apikey=apivinz");sleep(1);
			$data = json_decode($api_web);
				echo "\n\n  - Title : ".$data->result->title;
				echo "\n  - Size : ".$data->result->size;
				echo "\n  - Url video : ".$data->result->url_video;
			echo "\n\n [+] Download Now (y/n) : ";
			$down = trim(fgets(STDIN));
			if ($down == 'y' or $down == "Y") {
				$file = "/sdcard/Termux";sleep(2);
				echo "\n [!] Sedang Mendownload";
				for ($kata=0;$kata<=4;$kata++) {
					echo ".";
					sleep(1);}
				$now = file_get_contents($data->result->url_video);
				if(is_dir($file) == false) {
					mkdir($file);
					$file_1 = fopen($file . '/' . "Video.mp4", "w");
					fwrite($file_1, $now);
					fclose($file_1);sleep(2);
				echo "\n [✓] Download Done File Saved To »» /sdcard/Termux/Video.mp4\n";
				} else {
					exit;}
			} elseif ($down == 'n' or $down == 'N') {
			  	echo "\n  Download Video Youtube Dibatalkan !!\n";}
		} catch (Exception $e) {
			die(" Terjadi masalah : ".$e->getMessage());}}}

$run = new down;

?>

