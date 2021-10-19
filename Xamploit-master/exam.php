<?php

function index(){
    include 'config.php';
    @system("clear");
    print "\n";
    print "$cyan      ▄  ██   █▀▄▀█$red █ ▄▄  █    ████▄ ▄█    ▄▄▄▄▀ \n";
    print "$cyan  ▀▄   █ █ █  █ █ █$red █   █ █    █   █ ██ ▀▀▀ █ \n";
    print "$cyan    █ ▀  █▄▄█ █ ▄ █$red █▀▀▀  █    █   █ ██     █ \n";
    print "$cyan   ▄ █   █  █ █   █$red █     ███▄ ▀████ ▐█    █ \n";
    print "$cyan  █   ▀▄    █    █ $red  █        ▀       ▐   ▀ \n";
    print "$cyan   ▀       █    ▀  $red   ▀$white     Ver.2.5\n";
    print "$cyan          ▀        $white \n\n";
}

function dirbrute(){
    include 'config.php';
    print "$cyan [$yellow *$cyan ]$white Directory Brute ...\n";
    sleep(1);
    if (file_exists($dl)){
        @system("rm -rf $cl");
        @system("rm -rf $d");
        $dla = fopen("$dl","r");
        $dlb = filesize("$dl");
        $dlc = fread($dla,$dlb);
        $dllists = explode("\n",$dlc);
        foreach($dllists as $dir){
            foreach($dllists as $dir1){
                foreach($dllists as $dir2){
                $direct = "$targetnya/$dir/$dir1/$dir2";
                $ch = curl_init("$direct");
                curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
                curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
                curl_exec($ch);
                $httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
                curl_close($ch);
                if($httpcode == 200){
                    $handle = fopen("$cl", "a+");
                    $handle1 = fopen("$d", "a+");
                    fwrite($handle, "$direct\n");
                    fwrite($handle1, "$dir/$dir1/$dir2\n");
                    print "\n$cyan [$okegreen OK$cyan ]$red >$white $direct";
                }
                else{
                    print "\n$cyan [$red ERROR$cyan ]$red >$white $direct";
                }
                }
            }
        }
        if (file_exists($d)){
            print "\n\n$cyan [$okegreen *$cyan ]$white Directory list reported to $d\n\n";sleep(1);
        }
        else{
            print "\n\n$white    error creating$red $d\n";
            sleep(1);
            print "$white    type$cyan [$yellow dirbrute$cyan ]$white again or check your connection with exam server\n\n";
            sleep(1);
        }
    }
    else{
        print "\n$white    file$red $dl$white not found\n";
        sleep(1);
        print "$white    type$cyan [$yellow update$cyan ]$white or create $dl\n\n";
        sleep(1);
    }
}

function filebrute(){
    include 'config.php';
    print "$cyan [$yellow *$cyan ]$white PHP file Scanning ...\n";
    sleep(1);
    if (file_exists($d)){
        if (file_exists($pl)){
            @system("rm -rf $p");
            $da = fopen("$d","r");
            $db = filesize("$d");
            $dc = fread($da,$db);
            $dlists = explode("\n",$dc);
            $pla = fopen("$pl","r");
            $plb = filesize("$pl");
            $plc = fread($pla,$plb);
            $pllists = explode("\n",$plc);
            foreach($dlists as $dir){
                foreach($pllists as $php){
                    $phpfile = "$targetnya/$dir/$php";
                    $ch = curl_init("$phpfile");
                    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
                    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
                    curl_exec($ch);
                    $httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
                    curl_close($ch);
                    if($httpcode == 200){
                        $handle = fopen("$p", "a+");
                        fwrite($handle, "$phpfile\n");
                        print "\n$cyan [$okegreen OK$cyan ]$red >$white $phpfile";
                    }
                    else{
                        print "\n$cyan [$red ERROR$cyan ]$red >$white $phpfile";
                    }
                }
            }
            if (file_exists($p)){
                print "\n\n$cyan [$okegreen *$cyan ]$white Directory list reported to $p\n\n";sleep(1);
            }
            else{
                print "\n\n$white    error creating$red $p\n";
                sleep(1);
                print "$white    type$cyan [$yellow filebrute$cyan ]$white again or check your connection with exam server\n\n";
                sleep(1);
            }
        }
        else{
            print "\n$white    file$red $pl$white not found\n";
            sleep(1);
            print "$white    type$cyan [$yellow update$cyan ]$white or create $pl\n\n";
            sleep(1);
        }
    }
    else{
        print "\n$white    file$red $d$white not found\n";
        sleep(1);
        print "$white    type$cyan [$yellow dirbrute$cyan ]$white first to brute dir and create $d\n\n";
        sleep(1);
    }
}

function dirclone(){
    include 'config.php';
    print "$cyan [$yellow *$cyan ]$white Cloning all Directory ...\n";
    sleep(1);
    if (file_exists($cl)){
        @system("rm -rf $target");
        $cla = fopen("$cl","r");
        $clb = filesize("$cl");
        $clc = fread($cla,$clb);
        $cllists = explode("\n",$clc);
        foreach($cllists as $dir){
            if ($dir == ''){
                cmd();
            }
            else{
                print "\n$cyan [$okegreen Cloning$cyan ]$red >$white $dir";
                @system("wget -qr $dir");
            }
        }
        if (file_exists($target)){
            print "\n$cyan [$okegreen *$cyan ]$white Directory clone reported to $target\n\n";sleep(1);
        }
        else{
            print "\n\n$white    error cloning$red $target\n";
            sleep(1);
            print "$white    type$cyan [$yellow dirclone$cyan ]$white again or check your connection with exam server\n\n";
            sleep(1);
        }
    }
    else{
        print "\n$white    file$red $cl$white not found\n";
        sleep(1);
        print "$white    type$cyan [$yellow dirbrute$cyan ]$white first to brute dir and create $cl\n\n";
        sleep(1);
    }
}

function runall(){
    include 'config.php';
    print "$cyan [$yellow *$cyan ]$white Running all Tasks ...\n";sleep(1);
    index();
    dirbrute();
    filebrute();
    dirclone();
}

function info(){
    include 'config.php';
    print "$cyan  [$yellow*$cyan]$white Target$red     :$white   $target\n\n";
    print "$cyan  [$yellow*$cyan]$white Dirlist$red    :$white   $dlx List\n";
    print "$cyan  [$yellow*$cyan]$white PHPlist$red    :$white   $plx List\n";
    print "$cyan  [$yellow*$cyan]$white Chance    $red :$white   $plxx Brute\n\n\n";
}

function help(){
    include 'config.php';
    print "$cyan  [$yellow*$cyan]$white dirbrute$red   =$white   Brute Directory\n";
    print "$cyan  [$yellow*$cyan]$white filebrute$red  =$white   Brute PHP File\n";
    print "$cyan  [$yellow*$cyan]$white dirclone$red   =$white   Clone Directory\n";
    print "$cyan  [$yellow*$cyan]$white runall$red     =$white   Automaticaly Run Tasks\n\n";
    print "$cyan  [$yellow*$cyan]$white help$red       =$white   Show Help\n";
    print "$cyan  [$yellow*$cyan]$white info$red       =$white   Show Info\n";
    print "$cyan  [$yellow*$cyan]$white update$red     =$white   Update Wordlist\n";
    print "$cyan  [$yellow*$cyan]$white exit$red       =$white   Exit\n\n\n";
}

function updatelist(){
    include 'config.php';
    @system("rm -rf $dl");
    @system("rm -rf $pl");
    $url = 'raw.githubusercontent.com';
    $server = "https://$url";
    $dirfile = "N1ght420/Xamploit/master/$dl";
    $phpfile = "N1ght420/Xamploit/master/$pl";
    $dirwordlist = "$server/$dirfile";
    $phpwordlist = "$server/$phpfile";
    print "$cyan [$yellow *$cyan ]$white Downloading Wordlist from Github Server ...\n\n";sleep(1);
    print "$red >$white $dirwordlist\n";
    @system("wget -q $dirwordlist");
    if (file_exists($dl)){
        sleep(1);
    }
    else{
        print "\n$white    error downloading$red $dl\n";
        sleep(1);
        print "$white    type$cyan [$yellow update$cyan ]$white again or check your internet connection\n\n";
        sleep(1);
    }
    print "$red >$white $phpwordlist\n";
    @system("wget -q $phpwordlist");
    if (file_exists($pl)){
        sleep(1);
    }
    else{
        print "\n$white    error downloading$red $pl\n";
        sleep(1);
        print "$white    type$cyan [$yellow update$cyan ]$white again or check your internet connection\n\n";
        sleep(1);
    }
    print "\n";
}

function cmd(){
    include 'config.php';
    print "$white 0X.am$red >$white ";
    $cmd = trim(fgets(STDIN));
    if ($cmd == 'runall' OR $cmd == 'ra' OR $cmd == 'RA' OR $cmd == 'run'){
        index();
        runall();
        cmd();
    }
    elseif ($cmd == 'dirbrute' OR $cmd == 'db' OR $cmd == 'DB'){
        index();
        dirbrute();
        cmd();
    }
    elseif ($cmd == 'filebrute' OR $cmd == 'fb' OR $cmd == 'FB'){
        index();
        filebrute();
        cmd();
    }
    elseif ($cmd == 'dirclone' OR $cmd == 'dc' OR $cmd == 'DC'){
        index();
        dirclone();
        cmd();
    }
    elseif ($cmd == 'help' OR $cmd == 'h' OR $cmd == 'H'){
        index();
        help();
        cmd();
    }
    elseif ($cmd == 'info' OR $cmd == 'i' OR $cmd == 'I'){
        index();
        info();
        cmd();
    }
    elseif ($cmd == 'update' OR $cmd == 'u' OR $cmd == 'U'){
        index();
        updatelist();
        cmd();
    }
    elseif ($cmd == 'clear' OR $cmd == 'c' OR $cmd == 'C'){
        index();
        cmd();
    }
    elseif ($cmd == 'exit' OR $cmd == 'e' OR $cmd == 'E'){
        exit();
    }
    else{
        print "\n$cyan [$yellow ?$cyan ]$white Use System Command (Y/n) ?\n$red   >$white ";
        $com = trim(fgets(STDIN));
        if ($com == 'y' OR $com == 'Y'){
            print "\n";
            @system("$cmd");
            print "\n";
            cmd();
        }
        else{
            print "\n$white    command$red $cmd$white not found\n";
            print "$white    type$cyan [$yellow help$cyan ]$white to show help\n\n";
            cmd();
        }
    }
}

index();
cmd();

?>
