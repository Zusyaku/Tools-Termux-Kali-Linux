<?php

# Color Start

$blue="\033[1;34m";
$cyan="\033[1;36m";
$okegreen="\033[92m";
$lightgreen="\033[1;32m";
$white="\033[1;37m";
$purple="\033[1;35m";
$red="\033[1;31m";
$yellow="\033[1;33m";

# Color End

# Configuration Start

$target = '192.168.0.155:155';
$dl = 'dirlist.txt';
$pl = 'phplist.txt';
$cl = 'dirlink.txt';
$d = 'dir.txt';
$p = 'php.txt';
$dlx = count(file($dl));
$plx = count(file($pl));
$plxx = $dlx * $plx + $plx;

if(!preg_match("/^http:\/\//",$target) AND !preg_match("/^https:\/\//",$target)){
    $targetnya = "http://$target";
}
else{
    $targetnya = $target;
}

# Configuration End

?>