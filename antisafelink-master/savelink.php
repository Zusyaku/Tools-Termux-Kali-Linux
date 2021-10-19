<?php
include "simple_html_dom.php";
echo 'masukkan url : ';
$url = trim(fgets(STDIN));
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_COOKIEJAR, 'cookie.txt');
curl_setopt($ch, CURLOPT_COOKIEFILE, 'cookie.txt');
$hasil = curl_exec($ch);
$anu = new simple_html_dom();
$anu->load($hasil);
$csrf = $anu->find('a',3);
$a = explode('"', $csrf);
$b = explode('r=', $a[1]);
$c = base64_decode($b[1]);
$d = explode('url=', $c);
$e = base64_decode($d[1]);
echo "link download : $e\n"; 
?>
