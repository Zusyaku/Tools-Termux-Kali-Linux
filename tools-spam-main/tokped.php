<?php
include 'bomtokped.php';

/*
    https://github.com/nee48/BomTelpSmsTokped
    Made by Handika Pratama
    Modified by まやちゃん
*/

$init = new Bom();

//Eksekusi Call/Sms Boomber (Limit 3x/Jam)
echo "Nomor Target (tanpa 62/0)\nInput : ";
$a = trim(fgets(STDIN));
echo "Type 1 for sms, 2 for call\nInput : ";
$b = trim(fgets(STDIN));
$init->type = "$b";
$init->no = "$a";

if ($init->type == 1) {
	for ($i=0; $i < 2; $i++) { 
	    $init->Verif($init->no,$init->type);
	}
}elseif ($init->type == 2) {
	 $init->Verif($init->no,$init->type);
}
