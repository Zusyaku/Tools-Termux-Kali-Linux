<?php
print "
Selamat Berhitung

1.Penjumlahan
2.Pengurangan
3.Perkalian
4.Pembagian
>>";
$asu=trim(fgets(STDIN,1024));
if($asu == 1) {
	echo "Masukan Jumlah: ";
	$jmlh1=trim(fgets(STDIN,1024));
	echo "Di Tambah: ";
	$jmlh2=trim(fgets(STDIN,1024));
	$jmlhnya = $jmlh1+$jmlh2;
	echo "Hasil Dari ".$jmlh1."+".$jmlh2." Adalah ".$jmlhnya;
        echo " ";

}
elseif($asu == 2) {
	echo "Masukan Pengurangan: ";
	$pmgn1=trim(fgets(STDIN,1024));
	echo "Di Kurang: ";
	$pmgn2=trim(fgets(STDIN,1024));
	$pmgnnya = $pmgn1-$pmgn2;
	echo "Hasil Dari ".$pmgn1."-".$pmgn2." Adalah ".$pmgnnya;

}
elseif($asu == 3) {
	echo "Masukan Perkalian: ";
	$pkln1=trim(fgets(STDIN,1024));
	echo "Di Kali: ";
	$pkln2=trim(fgets(STDIN,1024));
	$pklnnya = $pkln1*$pkln2;
	echo "Hasil Dari ".$pkln1."*".$pkln2." Adalah ".$pklnnya;

}
elseif($asu == 4) {
	echo "Masukan Pembagian: ";
	$pmbgn1=trim(fgets(STDIN,1024));
	echo "Di Bagi: ";
	$pmbgn2=trim(fgets(STDIN,1024));
	$pmbgnnya = $pmbgn1/$pmbgn2;
	echo "Hasil Dari ".$pmbgn1."/".$pmbgn2." Adalah ".$pmbgnnya;

}
?>
