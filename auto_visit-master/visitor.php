<?php

/**
 * @author Ammar Faizi <ammarfaizi2@gmail.com> https://www.facebook.com/ammarfaizi2
 * @license MIT
 * @version 0.0.1
 * @link https://www.ammarfaizi.net/
 */

$config = require __DIR__."/data/config.php";

if (! isset($config["file"])) {
	error("Please define target file!");
}

if (! file_exists($config["file"])) {
	error("File ".$config["file"]." does not exist!");
}

if (! isset($config["delimiter"])) {
	error("Please define delimiter!");
}
$cycle = 1;
while(true) {
	print "Running cycle ".$cycle."...\n\n";
	$handle = fopen($config["file"], "r");
	flock($handle, LOCK_EX);
	while (! feof($handle)) {
		$link = "";
		while (($r = fread($handle, 1)) !== $config["delimiter"] && ! feof($handle)) {
			$link .= $r;
		}
		echo $r;
		print "Visiting ".$link."...\n";
		$v = visit($link);
		print "Done, Status: ".($v["info"]["http_code"])."\n";
		if ($config["delay_per_visit"] > 0) {
			print "Sleep ".$config["delay_per_visit"]." second".($config["delay_per_visit"]>1?"s":"");
			$s = $config["delay_per_visit"];
			while ($s) {
				echo ".";
				sleep(1);
				$s--;
			}
		}
		print "\n\n";
	}
	fclose($handle);
	print "Cycle ".($cycle++)." has finished!\n\n";
	if ($config["delay_per_cycle"] > 0) {
		print "Sleep cycle...\n";
		print "Sleep ".$config["delay_per_cycle"]." second".($config["delay_per_cycle"]>1?"s":"");
		$s = $config["delay_per_cycle"];
		while ($s) {
			echo ".";
			sleep(1);
			$s--;
		}
		print "\n\n";
	}
	print "==================================================================\n\n";
}

function visit($url)
{
	$ch = curl_init($url);
	curl_setopt_array($ch,
		[
			CURLOPT_RETURNTRANSFER => true,
			CURLOPT_FOLLOWLOCATION => true,
			CURLOPT_SSL_VERIFYPEER => false,
			CURLOPT_SSL_VERIFYHOST => false,
			CURLOPT_CONNECTTIMEOUT => CONNECTTIMEOUT,
			CURLOPT_TIMEOUT => CONNECTTIMEOUT,
			CURLOPT_USERAGENT => UA[rand(0, UA_COUNT - 1)]
		]
	);
	$out = curl_exec($ch);
	$info = curl_getinfo($ch);
	curl_close($ch);
	return [
		"out" => $out,
		"info" => $info
	];
}

function error($msg, $code = 1)
{
	print $msg."\n";
	exit($code);
}
