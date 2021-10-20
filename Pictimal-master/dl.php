<?php

include 'config.php';

function index(){
    include 'config.php';
    @system("clear");
    print "\n";
    print "$cyan      ____  _     $okegreen __  _                 __\n";
    print "$cyan     / __ \(_)____$okegreen/ /_(_)___ ___  ____ _/ /\n";
    print "$cyan    / /_/ / / ___$okegreen/ __/ / __ `__ \/ __ `/ / \n";
    print "$cyan   / ____/ / /__$okegreen/ /_/ / / / / / / /_/ / /  \n";
    print "$cyan  /_/   /_/\___/$okegreen\__/_/_/ /_/ /_/\__,_/_/   \n";
    print "\n";
    print "$cyan 01$red :$white Cat Pict & Gif\n";
    print "$cyan 02$red :$white Dog Pict & Videos\n";
    print "$cyan 03$red :$white Fox Pict\n";
    print "\n";
    print "$red >$white ";
    $cmd = trim(fgets(STDIN));
    print "$cyan Total$red >$white ";
    $total = trim(fgets(STDIN));
    print "\n";
    if ($cmd == '1'){
        cat($total);
    }
    elseif ($cmd == '2'){
        dog($total);
    }
    elseif ($cmd == '3'){
        fox($total);
    }
    else{
        index();
    }
}

function cat($total){
    include 'config.php';
    for ($i=0; $i < $total; $i++){
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_URL,'https://aws.random.cat/meow');
        $result=curl_exec($ch);
        $json = json_decode($result, true);
        $url = $json['file'];
        print "$cyan [$white Downloading$cyan ]$red >$white $url\n";
        @system("wget -q $url");
    }
    print "\n";
}

function dog($total){
    include 'config.php';
    for ($i=0; $i < $total; $i++){
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_URL,'https://random.dog/woof.json');
        $result=curl_exec($ch);
        $json = json_decode($result, true);
        $url = $json['url'];
        print "$cyan [$white Downloading$cyan ]$red >$white $url\n";
        @system("wget -q $url");
    }
    print "\n";
}

function fox($total){
    include 'config.php';
    for ($i=0; $i < $total; $i++){
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_URL,'https://randomfox.ca/floof/');
        $result=curl_exec($ch);
        $json = json_decode($result, true);
        $url = $json['image'];
        print "$cyan [$white Downloading$cyan ]$red >$white $url\n";
        @system("wget -q $url");
    }
    print "\n";
}

index();

?>
