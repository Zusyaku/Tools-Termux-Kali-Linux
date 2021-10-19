<?php
session_start();
header ("Content-type: image/png");

function genRandomString() {
    $length = 5;
    $characters = "123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"; //0 (zero) is deleted
    $string = "";    
    for ($p = 0; $p < $length; $p++) {
        $string .= $characters[mt_rand(0, strlen($characters))];
    }
    return $string;
}


$rno = genRandomString();
$_SESSION['ckey'] = md5($rno);

$img_handle = imageCreateFromPNG("bg.PNG");
$color = ImageColorAllocate ($img_handle, 0, 0, 0);
ImageString ($img_handle, 5, 20, 13, $rno, $color);
ImagePng ($img_handle);
ImageDestroy ($img_handle);

?>