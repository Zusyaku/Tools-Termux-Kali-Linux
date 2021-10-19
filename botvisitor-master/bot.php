<?php # WARNA
$biru = "\e[34m";
$kuning = "\e[33m";
$cyan = "\e[96m";
$magenta = "\e[35m";
$hijau = "\e[92m";
$merah = "\e[91m";
echo "$cyan ###################################################\n";
echo "$biru /     Auto Visitor Blogger /Wordpress       /\n";
echo "$merah /  Author  : Kumpulan Remaja                         /\n";
echo "$magenta / Website : https://kumpulanremaja.com   /\n";
echo "$hijau / FansPage : https://www.facebook.com/4kumpulanremaja                   /\n";
echo "$kuning / Github :   https://github.com/kumpulanremaja                      /\n";
echo "$cyan ###################################################\n";
echo "$kuning Masukan Salah Satu Link Postingan\n Web Kalian Di Bawah Ini\n";
echo "$hijau [1] Masukan Link Postingan Web : "; 
$url = trim(fgets(STDIN));
echo "$cyan [2] Masukan Jumlah Visit : "; 
$max = trim(fgets(STDIN));

error_reporting(0);
class Random_UA
 {
    
    /**
     * 
     */ 
    var $linux_proc;
    /**
     * 
     */
    var $mac_proc;
    
    /**
     * A
     */
    var $lang;
    
    function __construct()
    {
        $this->linux_proc = array(
            'i686',
            'x86_64'
        );
        
        $this->mac_proc = array(
            'Intel',
            'PPC',
            'U; Intel',
            'U; PPC'
        );
        
        $this->lang = array(
            'en-US',
            'sl-SI'
        );
    }
    
    function firefox() {
        $ver = array(
    	'Gecko/' . date('Ymd', rand(strtotime('2011-1-1'), mktime())) . ' Firefox/' . rand(5, 7) . '.0',
    	'Gecko/' . date('Ymd', rand(strtotime('2011-1-1'), mktime())) . ' Firefox/' . rand(5, 7) . '.0.1',
    	'Gecko/' . date('Ymd', rand(strtotime('2010-1-1'), mktime())) . ' Firefox/3.6.' . rand(1, 20),
    	'Gecko/' . date('Ymd', rand(strtotime('2010-1-1'), mktime())) . ' Firefox/3.8'
        );
    
        $platforms = array(
    	'(Windows NT ' . rand(5, 6) . '.' . rand(0, 1) . '; ' . $this->lang[array_rand($this->lang, 1)] . '; rv:1.9.' . rand(0, 2) . '.20) ' . $ver[array_rand($ver, 1)],
    	'(X11; Linux ' . $this->linux_proc[array_rand($this->linux_proc, 1)] . '; rv:' . rand(5, 7) . '.0) ' . $ver[array_rand($ver, 1)],
    	'(Macintosh; ' . $this->mac_proc[array_rand($this->mac_proc, 1)] . ' Mac OS X 10_' . rand(5, 7) . '_' . rand(0, 9) . ' rv:' . rand(2, 6) . '.0) ' . $ver[array_rand($ver, 1)]
        );
    
        return $platforms[array_rand($platforms, 1)];
    }
    
    function safari() {
        $saf = rand(531, 535) . '.' . rand(1, 50) . '.' . rand(1, 7);
        if (rand(0, 1) == 0) {
    	$ver = rand(4, 5) . '.' . rand(0, 1);
        } else {
    	$ver = rand(4, 5) . '.0.' . rand(1, 5);
        }
    
        $platforms = array(
    	'(Windows; U; Windows NT ' . rand(5, 6) . '.' . rand(0, 1) . ") AppleWebKit/$saf (KHTML, like Gecko) Version/$ver Safari/$saf",
    	'(Macintosh; U; ' . $this->mac_proc[array_rand($this->mac_proc, 1)] . ' Mac OS X 10_' . rand(5, 7) . '_' . rand(0, 9) . ' rv:' . rand(2, 6) . '.0; ' . $this->lang[array_rand($this->lang, 1)] . ") AppleWebKit/$saf (KHTML, like Gecko) Version/$ver Safari/$saf",
    	'(iPod; U; CPU iPhone OS ' . rand(3, 4) . '_' . rand(0, 3) . ' like Mac OS X; ' . $this->lang[array_rand($this->lang, 1)] . ") AppleWebKit/$saf (KHTML, like Gecko) Version/" . rand(3, 4) . ".0.5 Mobile/8B" . rand(111, 119) . " Safari/6$saf",
        );
    
        return $platforms[array_rand($platforms, 1)];
    }
    
    function iexplorer() {
        $ie_extra = array(
    	'',
    	'; .NET CLR 1.1.' . rand(4320, 4325) . '',
    	'; WOW64'
        );
        $platforms = array(
    	'(compatible; MSIE ' . rand(5, 9) . '.0; Windows NT ' . rand(5, 6) . '.' . rand(0, 1) . '; Trident/' . rand(3, 5) . '.' . rand(0, 1) . ')'
        );
    
        return $platforms[array_rand($platforms, 1)];
    }
    
    function opera() {
        $op_extra = array(
    	'',
    	'; .NET CLR 1.1.' . rand(4320, 4325) . '',
    	'; WOW64'
        );
        $platforms = array(
    	'(X11; Linux ' . $this->linux_proc[array_rand($this->linux_proc, 1)] . '; U; ' . $this->lang[array_rand($this->lang, 1)] . ') Presto/2.9.' . rand(160, 190) . ' Version/' . rand(10, 12) . '.00',
    	'(Windows NT ' . rand(5, 6) . '.' . rand(0, 1) . '; U; ' . $this->lang[array_rand($this->lang, 1)] . ') Presto/2.9.' . rand(160, 190) . ' Version/' . rand(10, 12) . '.00'
        );
    
        return $platforms[array_rand($platforms, 1)];
    }
    
    function chrome() {
        $saf = rand(531, 536) . rand(0, 2);
    
        $platforms = array(
    	'(X11; Linux ' . $this->linux_proc[array_rand($this->linux_proc, 1)] . ") AppleWebKit/$saf (KHTML, like Gecko) Chrome/" . rand(13, 15) . '.0.' . rand(800, 899) . ".0 Safari/$saf",
    	'(Windows NT ' . rand(5, 6) . '.' . rand(0, 1) . ") AppleWebKit/$saf (KHTML, like Gecko) Chrome/" . rand(13, 15) . '.0.' . rand(800, 899) . ".0 Safari/$saf",
    	'(Macintosh; U; ' . $this->mac_proc[array_rand($this->mac_proc, 1)] . ' Mac OS X 10_' . rand(5, 7) . '_' . rand(0, 9) . ") AppleWebKit/$saf (KHTML, like Gecko) Chrome/" . rand(13, 15) . '.0.' . rand(800, 899) . ".0 Safari/$saf"
        );
    
        return $platforms[array_rand($platforms, 1)];
    }
    
    /**
     * Main function which will choose random browser
     * @return string user agent
     */
    function generate() {
        $x = rand(1, 5);
        switch ($x) {
    	case 1:
    	    return "Mozilla/5.0 " . $this->firefox();
    	    break;
    	case 2:
    	    return "Mozilla/5.0 " . $this->safari();
    	    break;
    	case 3:
    	    return "Mozilla/" . rand(4, 5) . ".0 " . $this->iexplorer();
    	    break;
    	case 4:
    	    return "Opera/" . rand(8, 9) . '.' . rand(10, 99) . ' ' . $this->opera();
    	    break;
    	case 5:
    	    return 'Mozilla/5.0' . $this->chrome();
    	    break;
        }
    }
    
}

class autovisitor extends Random_UA {

	public function __construct($url) {
		$this->url = $url;
	}

	private function curl() {
		$ch = curl_init();
		CURL_SETOPT($ch, CURLOPT_URL, $this->url);
		CURL_SETOPT($ch, CURLOPT_HTTPHEADER, array('Referer: '.$this->acakReferer(),
												   'User-Agent: '.$this->generate()));
		CURL_SETOPT($ch, CURLOPT_FOLLOWLOCATION, true);
		CURL_SETOPT($ch, CURLOPT_SSL_VERIFYHOST, 0);
		CURL_SETOPT($ch, CURLOPT_SSL_VERIFYPEER, 0);
		CURL_SETOPT($ch, CURLOPT_RETURNTRANSFER, 1);
		CURL_SETOPT($ch, CURLOPT_USERAGENT, $this->generate());
		$result = curl_exec($ch);
		curl_close($ch);

		return $result;
	}

	private function xflush() {
    	static $output_handler = null;
    	if ($output_handler === null) {
        	$output_handler = @ini_get('output_handler');
    	}
    	if ($output_handler == 'ob_gzhandler') {
        	return;
    	}
    	flush();
    	if (function_exists('ob_flush') AND function_exists('ob_get_length') AND ob_get_length() !== false) {
       		@ob_flush();
    	} else if (function_exists('ob_end_flush') AND function_exists('ob_start') AND function_exists('ob_get_length') AND ob_get_length() !== FALSE) {
       		@ob_end_flush();
        	@ob_start();
    	}
	}

	private function acakReferer() {
		$list = array();
		/* Asal traffic yang di submit */ 
		$list[] = "http://facebook.com";
		$list[] = "http://twitter.com";
		$list[] = "http://www.google.com";
		$list[] = "http://www.google.com.af";
		$list[] = "http://www.google.as";
 	   $list[] = "http://www.google.off.ai";
        $list[] = "http://www.google.com.ag";
	    $list[] = "http://www.google.am";
	    $list[] = "http://www.google.com.au";
	    $list[] = "http://www.google.at";
	    $list[] = "http://www.google.az";
	    $list[] = "http://www.google.com.bh";
	    $list[] = "http://www.google.com.bd";
	    $list[] = "http://www.google.be";
	    $list[] = "http://www.google.com.bz";
	    $list[] = "http://www.google.com.bo";
	    $list[] = "http://www.google.ba";
	    $list[] = "http://www.google.co.bw";
	    $list[] = "http://www.google.com.br";
	    $list[] = "http://www.google.vg";
	    $list[] = "http://www.google.bg";
	    $list[] = "http://www.google.bi";
	    $list[] = "http://www.google.ca";
	    $list[] = "http://www.google.cl";
	    $list[] = "http://www.google.cn";
	    $list[] = "http://www.google.com.co";
	    $list[] = "http://www.google.cd";
	    $list[] = "http://www.google.cg";
	    $list[] = "http://www.google.co.ck";
	    $list[] = "http://www.google.co.cr";
        $list[] = "http://www.google.hr";
        $list[] = "http://www.google.com.cu";
		$list[] = "http://www.google.cz";
 	   $list[] = "http://www.google.ci";
        $list[] = "http://www.google.dk";
	    $list[] = "http://www.google.dj";
	    $list[] = "http://www.google.dm";
	    $list[] = "http://www.google.com.do";
	    $list[] = "http://www.google.com.ec";
	    $list[] = "http://www.google.com.eg";
	    $list[] = "http://www.google.com.sv";
	    $list[] = "http://www.google.ee";
	    $list[] = "http://www.google.com.et";
	    $list[] = "http://www.google.com.fj";
	    $list[] = "http://www.google.fi";
	    $list[] = "http://www.google.fr";
	    $list[] = "http://www.google.gm";
	    $list[] = "http://www.google.de";
	    $list[] = "http://www.google.com.gi";
	    $list[] = "http://www.google.com.gr";
	    $list[] = "http://www.google.gl";
	    $list[] = "http://www.google.gg";
	    $list[] = "http://www.google.gt";
	    $list[] = "http://www.google.ht";
	    $list[] = "http://www.google.com.hk";
	    $list[] = "http://www.google.com.hn";
	    $list[] = "http://www.google.hu";
	    $list[] = "http://www.google.is";
        $list[] = "http://www.google.co.id";
        $list[] = "http://www.google.co.in";
		$list[] = "http://www.google.ie";
 	   $list[] = "http://www.google.co.im";
        $list[] = "http://www.google.it";
	    $list[] = "http://www.google.il";
	    $list[] = "http://www.google.com.im";
	    $list[] = "http://www.google.co.je";
	    $list[] = "http://www.google.co.jp";
	    $list[] = "http://www.google.jo";
	    $list[] = "http://www.google.kz";
	    $list[] = "http://www.google.kg";
	    $list[] = "http://www.google.co.ke";
	    $list[] = "http://www.google.lv";
	    $list[] = "http://www.google.co.ls";
	    $list[] = "http://www.google.co.ly";
	    $list[] = "http://www.google.li";
	    $list[] = "http://www.google.lt";
	    $list[] = "http://www.google.lu";
	    $list[] = "http://www.google.mw";
	    $list[] = "http://www.google.com.my";
	    $list[] = "http://www.google.com.mt";
	    $list[] = "http://www.google.mu";
	    $list[] = "http://www.google.fm";
	    $list[] = "http://www.google.com.mx";
	    $list[] = "http://www.google.mn";
	    $list[] = "http://www.google.ms";
	    $list[] = "http://www.google.co.ma";
        $list[] = "http://www.google.com.na";
        $list[] = "http://www.google.com.np";
	    $list[] = "http://www.google.nl";
	    $list[] = "http://www.google.co.nz";
	    $list[] = "http://www.google.com.ni";
	    $list[] = "http://www.google.com.nf";
	    $list[] = "http://www.google.no";
	    $list[] = "http://www.google.com.om";
	    $list[] = "http://www.google.com.pk";
        $list[] = "http://www.google.com.pa";
        $list[] = "http://www.google.com.py";
	    $list[] = "http://www.google.com.pe";
	    $list[] = "http://www.google.com.pn";
	    $list[] = "http://www.google.com.ph";
	    $list[] = "http://www.google.pl";
	    $list[] = "http://www.google.pt";
	    $list[] = "http://www.google.com.pr";
	    $list[] = "http://www.google.ro";
        $list[] = "http://www.google.com.qa";
        $list[] = "http://www.google.ru";
	    $list[] = "http://www.google.rw";
	    $list[] = "http://www.google.sh";
	    $list[] = "http://www.google.sm";
	    $list[] = "http://www.google.com.sa";
	    $list[] = "http://www.google.sn";
	    $list[] = "http://www.google.sc";
	    $list[] = "http://www.google.com.sg";
        $list[] = "http://www.google.sk";
        $list[] = "http://www.google.si";
	    $list[] = "http://www.google.co.za";
	    $list[] = "http://www.google.co.kr";
	    $list[] = "http://www.google.es";
	    $list[] = "http://www.google.lk";
	    $list[] = "http://www.beinyu.com";
	    $list[] = "http://www.google.com.vc";
        $list[] = "http://www.google.se";
        $list[] = "http://www.google.ch";
	    $list[] = "http://www.google.com.tw";
	    $list[] = "http://www.google.com.tj";
	    $list[] = "http://www.google.co.th";
	    $list[] = "http://www.google.bs";
	    $list[] = "http://www.google.to";
        $list[] = "http://www.google.tt";
        $list[] = "https://search.yahoo.com";
        $list[] = "http://www.google.com.tr";
	    $list[] = "http://www.google.tm";
	    $list[] = "http://www.google.co.vi";
	    $list[] = "http://www.google.co.ug";
	    $list[] = "http://www.google.com.ua";
	    $list[] = "http://www.google.ae";
	    $list[] = "http://twitter.com";
        $list[] = "http://www.google.co.uk";
        $list[] = "http://www.google.com.uy";
	    $list[] = "http://www.google.co.uz";
	    $list[] = "http://facebook.com";
	    $list[] = "http://www.google.co.ve";
	    $list[] = "http://www.google.com.vn";
	    $list[] = "http://www.google.co.zm";
        

		$acak = array_rand($list,1);
		return $list[$acak];
	}

	public function jalankan() {
		$this->xflush();

		$this->curl();
		return $this->acakReferer(); 

		$this->xflush();
	}

} 

for($i = 1; $i < $max+1; $i++) {
	$class = new autovisitor($url);
	echo $i.". [200OK] SUKSES MENGIRIM ~ [".$class->Menjalankan Bot()."]\n";
} ?>
