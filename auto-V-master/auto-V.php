<?php
 //				    //
 // Welcome To Source Code my Tools //
 //  Mau Record ya bro? fix Noob    //
 //    				    //

/*
   	Coded by Zeerx7
   Team : XploitSecurity-ID
*/
if(strtolower(substr(PHP_OS, 0, 3)) == 'win') {
        $R  = "";
        $RR = "";
        $G  = "";
        $GG = "";
        $C  = "";
        $CC = "";
        $B  = "";
        $BB = "";
        $Y  = "";
        $YY = "";
        $P  = "";
        $X  = "";
} else {
        $R  = "\e[91m";
        $RR = "\e[91;7m";
        $G  = "\e[92m";
        $GG = "\e[92;7m";
        $C  = "\e[36m";
        $CC = "\e[36;7m";
        $B  = "\e[94m";
	$BB = "\e[94;7m";
        $Y  = "\e[93m";
        $YY = "\e[93;7m";
        $P  = "\e[35m";
        $X  = "\e[0m";
        system('clear');
}
$__banner = "
$R ╲╲".$Y."╭━━━━━━━╮".$R."╱╱
$R ╲".$Y."╭╯╭━╮ ╭━╮╰╮".$R."╱
$R ╲".$Y."┃ ┃ ▊ ┃ ▊ ┃".$R."╱
$R ╲".$Y."┃ ┗━┛ ┗━┛ ┃".$R."╱
$R ╱".$Y."┃ ┏━━━━━┓ ┃".$R."╲ $B  Auto Visitor
$R ╱".$Y."┃ ┃  ╭━╮┃ ┃".$R."╲ $G  Coded by Zeerx7
$R ╱".$Y."╰╮╰━━┻━┻╯╭╯".$R."╲ $G  Team : XploitSec-ID
$R ╱╱".$Y."╰━━━━━━━╯".$R."╲╲
";
$useragent = [
'Mozilla/5.0 (X11; Linux i686) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5',
'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
'Opera/9.25 (Windows NT 5.1; U; en)',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.102011-10-16 20:23:50',
'Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+2011-10-16 20:21:10',
'Mozilla/5.0 (BlackBerry; U; BlackBerry 9860; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.254 Mobile Safari/534.11+',
'Mozilla/5.0 (BlackBerry; U; BlackBerry 9700; pt) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.546 Mobile Safari/534.8+',
'Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
'Mozilla/5.0 (Linux; U; Android 2.2.1; en-ca; LG-P505R Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
'Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16',
'iTunes/9.1 (Macintosh; U; PPC Mac OS X 10.2',
'Mozilla/5.0 (Linux; U; Android 2.1; en-us; Nexus One Build/ERD62) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17',
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11',
'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.0',
'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6',
'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36',
'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.7) Gecko/20070914 Firefox/2.0.0.7'
];
echo $__banner;
echo "$P [target]->$C ";
$target = trim(fgets(STDIN));
echo "$P [Jumlah]->$C ";
$jumlah = trim(fgets(STDIN));
$i=1;
$sukses[] = '';
$gagal[] = '';
while($i<=$jumlah){
  $agent = $useragent[array_rand($useragent)];
  $_ = view($target,$agent);
  if($_['code']==200){
    echo $G."Berhasil Mengirim $i \n";
    $sukses[] = "true";
  }else{
    echo $R."Gagal $i \n";
    $gagal[] = "false";
  }
  $i++;
}
$o = count($sukses)-1;
$p = count($gagal)-1;
echo $Y."\n[$G Done$Y ] \n";
echo $C."|url =>$B $target \n";
echo $C."|Jumlah Terkirim =>$G $o \n";
echo $C."|Gagal Terkirim =>$R $p \n";
function view($url,$agent){
 $z7 = curl_init();
 curl_setopt($z7, CURLOPT_URL, $url);
 curl_setopt($z7, CURLOPT_REFERER, "https://www.google.com");
 curl_setopt($z7, CURLOPT_HEADER, 0);
 curl_setopt($z7, CURLOPT_FOLLOWLOCATION, true);
 curl_setopt($z7, CURLOPT_RETURNTRANSFER, true);
 curl_setopt($z7, CURLOPT_SSL_VERIFYPEER, false);
 curl_setopt($z7, CURLOPT_TIMEOUT, 10);
 curl_setopt($z7, CURLOPT_USERAGENT, $agent);
 curl_setopt($z7, CURLOPT_ENCODING, "gzip");
 $outp = curl_exec($z7);
 $data = curl_getinfo($z7);
 curl_close($z7);
 $d['code'] = $data['http_code'];
 $d['o'] = $outp;
 return $d;
}
// Bye
?>
