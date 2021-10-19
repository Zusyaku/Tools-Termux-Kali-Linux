<?php

/*
Author : Kingtebe
Date   : May 11 2021, 09.29 WIB
Script : Create Script Deface

>[ Silahkan Kembangkan Kode HTML nya, Tapi Jangan Nge-Rikod Anjng ]<
*/

class Pepes {

	public function __construct(){
		system("clear");
		$this->awokawokngentod();}
		var $baner = "\n\n	    \e[37mCreate Scrip Deface\n          made by \e[34mkingtebe\e[37m © 2021\n\n                 \e[33mƪ(‾_‾)ʃ\n\n  \e[31m* \e[33mNote \e[37m: Gunakan tanda \e[31m<br> \e[37mJika Ingin Memulai Garis Baru \e[37m!!\n           \e[37mLink Gambar Only format \e[37m( \e[31m.jpg \e[37m/ \e[31m.png \e[37m)\n           Link Lagu Only Format ( \e[31m.Mp3 \e[37m)\n\n";

	public function awokawokngentod() {

		global $title,$hacked,$kata,$gambar,$lagu,$team;

		echo $this->baner;
		echo " \e[37m[\e[34m+\e[37m] Title : \e[37m"; $title = trim(fgets(STDIN));
		echo " \e[37m[\e[34m+\e[37m] Hacked By : \e[37m"; $hacked = trim(fgets(STDIN));
		echo " \e[37m[\e[34m+\e[37m] Message : \e[37m"; $kata = trim(fgets(STDIN));
		echo " \e[37m[\e[34m+\e[37m] Link Gambar : \e[37m"; $gambar = trim(fgets(STDIN));
		echo " \e[37m[\e[34m+\e[37m] Link Lagu : \e[37m"; $lagu = trim(fgets(STDIN));
		echo " \e[37m[\e[34m+\e[37m] Team : \e[37m"; $team = trim(fgets(STDIN));sleep(1.2);

		echo "\n \e[37m[\e[33m!\e[37m] \e[37mCreate Script Deface";
		for ($load=0;$load<=5;$load++){
			echo ".";
			sleep(1);}

		$file = "<html>\n<head>\n  	<meta charset='utf-8'>\n  	<title>$title</title>\n<style>\nbody{\n  background:black;\n  background-image: url(http://i958.photobucket.com/albums/ae69/putrablidz/storm.gif);\n  background-size:cover;\n}\n#font{\n  font-family:Courier;\n  color:white;\n  position:absolute;\n  left:0;\n  left:0;\n  right:0;\n  top:10%;\n}\nimg {\n  opacity:0.5;-webkit-transition:all 250ms ease;-moz-transition:all 250ms ease;-o-transition:all 250ms ease;transition:all 250ms ease;\n  margin-top:-10px;\n}\nimg:hover{\n  opacity:1\n}\nhr {\n  width:250px;\n}\na{\n  color:white;\n  text-decoration:none\n}\na.hover{\n  color:white;\n}\n</style>\n</head>\n<body oncontextmenu='return false;' onkeydown='return false;' onmousedown='return false;'>\n <center>\n <br>\n 	<div id='font' align='center'>\n		<div id=''><br>\n     			<img src='$gambar' width='350' height='350'> <br>\n     			<font color='#9E9E9E' size='10'>&nbsp;&nbsp;&nbsp;&nbsp; Hacked By<font color='red'> $hacked<font color='#FFFFFF'> </font> <font style='color:#ffffff;text-shadow:#FF0099 0px 0px 10px' size='6'> &nbsp;&nbsp;&nbsp;&nbsp;<br><br>$kata<br><br></font> </font></font>\n    		</div>\n    		<font color='#9E9E9E' size='10'><font color='red'>\n      		<table width='820px'>\n        	<tr>\n         	<td align='center'> <span style='font: 15px Courier;size:15px;color:#9E9E9E;'> <strong>\n            		<marquee direction='left' scrollamount='5' style='border:1px solid;' width='70%'>\n             		<font color='white' face='courier' size='5'>-=|[ Team : $team ]|=-</font>\n            		</marquee> </strong></span></td>\n        	</tr>\n      </table></font></font> <br><br>\n    		<audio src='$lagu' controls autoplay></audio>\n   	</div>\n</center>\n</body>\n</html>";echo "\n";sleep(1.2);

		$f = fopen("/sdcard/jadi.html", "w");
		fwrite($f, $file);
		fclose($f);

		echo "\n \e[37m[\e[34m!\e[37m] Created Success !\n" , " \e[37m[\e[34m✓\e[37m] File Saved To >> \e[33m/sdcard/jadi.html\n\n"," \e[37m>>> \e[33mJangan Lupa Follow Github Gw Nya Anjeeeng \e[34m^_^ \e[37m<<< \n\n";}}
new Pepes;

?>
