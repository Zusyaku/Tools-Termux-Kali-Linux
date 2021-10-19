<?php

// Color
$blue="\033[1;34m";
$cyan="\033[1;36m";
$okegreen="\033[92m";
$lightgreen="\033[1;32m";
$white="\033[1;37m";
$purple="\033[1;35m";
$red="\033[1;31m";
$yellow="\033[1;33m";

$base = 1000;
print "$cyan Total ID$red >$white ";
$jumlah = trim(fgets(STDIN));
print "\n";

function random($panjang){
    $karakter = '';
    $karakter .= '1234567890';
    $string = '';
    for ($i=0; $i < $panjang; $i++){
        $pos = rand(0, strlen($karakter)-1);
        $string .= $karakter{$pos};
    }
    return $string;
}
for ($i=0; $i < $jumlah; $i++){
    $acak = $base.random(15-strlen($base))."\n";
    $open = fopen("list.txt", 'a');
    fwrite($open, $acak);
    fclose($open);
    print "$white$acak";
}

exit;

?>
