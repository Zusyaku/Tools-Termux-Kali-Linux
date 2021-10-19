<!DOCTYPE HTML>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html">
<title>Fake Email Script | The404Hacking</title>
<link href="css/style.css" rel="stylesheet" type="text/css">
<meta charset="UTF-8">
</head>

<body>

<?php
session_start();
$f_Submit = filter_var($_POST['submit'],FILTER_SANITIZE_STRING);
if ($f_Submit == 'Send')
{
if (strcmp(md5(filter_var($_POST['user_code'],FILTER_SANITIZE_STRING)),$_SESSION['ckey']))
    { 

	$header = "Location: ".basename ( __FILE__,"php")."php?msg=ERROR: Invalid Verification Code";
	header($header);
exit();
  }
    //------------------ Sanitizin the Input Variables ------------------//
	$f_fromname   = filter_var($_POST['fromname'],FILTER_SANITIZE_STRING);
	$f_fromemail  = filter_var($_POST['fromemail'],FILTER_SANITIZE_EMAIL);
	$f_reply      = filter_var($_POST['reply'],FILTER_SANITIZE_EMAIL);
	$f_toemail    = filter_var($_POST['toemail'],FILTER_SANITIZE_EMAIL);
	$f_bccemail   = filter_var($_POST['bccemail'],FILTER_SANITIZE_EMAIL);
	$f_subject    = filter_var($_POST['subject'],FILTER_SANITIZE_STRING);
	$f_message    = filter_var($_POST['message'],FILTER_SANITIZE_STRING);
    $f_clno       = filter_var($_POST['clno'],FILTER_SANITIZE_NUMBER_INT);
	//-------------------------------------------------------------------//
	
    if($f_message=="") {
        $f_message = '
            <html>
            <head>
            <meta charset="UTF-8">
            </head>
            <body bgcolor="#DCEEFC">
            Dear sir,</br>
            your email is compromised.
            </body>
            </html>
            ';
    }

    if($f_reply=="") {
        $f_reply = $f_fromemail;
    }

// Header
    $headers = 'From:'.$f_fromname.' '.'<'.$f_fromemail.'>'. "\r\n";
    $headers .= 'Bcc: '.$f_bccemail. "\r\n";
    $headers .= "MIME-Version: 1.0\r\n";
/*
// Create a boundary so we know where to look for
// the start of the data
    $boundary = uniqid("HTMLEMAIL"); 
    
// First we send a non-html version of our email
    $headers .= "Content-Type: multipart/alternative;".
                "boundary = $boundary\r\n\r\n"; 
    $headers .= "This is a MIME encoded message.\r\n\r\n"; 
    $headers .= "--$boundary\r\n".
                "Content-Type: text/plain; charset=UTF-8\r\n".
                "Content-Transfer-Encoding: base64\r\n\r\n"; 
    $headers .= chunk_split(base64_encode(strip_tags($f_message)));  //$HTML

// Now we attach the HTML version
    $headers .= "--$boundary\r\n".
                "Content-Type: text/html; charset=UTF-8\r\n".
                "Content-Transfer-Encoding: base64\r\n\r\n"; 
                
    $headers .= chunk_split(base64_encode($f_message)); 
*/
// And then send the email ....
while ($f_clno >= 1) {
  $Sent=mail($f_toemail,$f_subject,$f_message,$headers,'-f'.$f_reply);
  sleep(0);
  $f_clno--;
}
if($Sent){
    $header = "Location: ".basename ( __FILE__,"php")."php?msg= Mail Sent.";
} else {
    $header = "Location: ".basename ( __FILE__,"php")."php?msg= Error: Mail Function is disabled.";
}

header($header);
exit();
}

?>



<form action="" method="post" class="basic-grey">
    <h1>Fake Email Script (Version 1)
        <span>Based on Fake Email Prank Script By <a href="https://T.me/Sir4m1R" title="Sir.4m1R Contact !" target="_blank">Sir.4m1R</a> | <a href="https://T.me/The404Hacking" title="The404Hacking Telegram Channel !" target="_blank">The404Hacking</a></span>
    	<span>Please do not misuse this script.</span>
    </h1>
    
	<label>
    	<span>From Name :</span>
        <input type="text" name="fromname" ID="fn" />
    </label>
    
	<label>
    	<span>From Email :</span>
		<input type="email" name="fromemail" ID="fe" />
    </label>

	<label>
    	<span>Reply Email :</span>
		<input type="email" name="reply" ID="re" />
    </label>

	<label>
    	<span>To Email :</span>
		<input type="email" name="toemail" ID="te" />
    </label>
	
	<label>
    	<span>BCC Email :</span>
		<input type="email" name="bccemail" ID="bcc" />
    </label>


	<label>
    	<span>Subject :</span>
        <input type="text" name="subject" ID="sb" />
    </label>

    <label>
    	<span>Your Message :</span>
        <textarea id="message" name="message" ID="ym" ></textarea>
    </label> 	

	<label>
    	<span>Cluster Bomb :</span>
        <input type="number" name="clno" ID="cb" value="1" />
    </label>

	<label>
    	<span>Verification Code :</span>
        <input type="vcode" name="user_code" ID="vc" />
		<img src="capcha/png.php" align="middle">
    </label>	

     <label>
    	<span>&nbsp;</span> 
        <input type="submit" class="button" name="submit" value="Send" />
    </label> 

</form>
</p>
<?php if (isset($_GET['msg'])) { echo "<font color=\"red\"><h3 align=\"center\"> $_GET[msg] </h3></font>"; } ?>
</body>
</html>
