<?php

$config = [
	"delay_per_cycle" => 10, // seconds
	"delay_per_visit" => 5, // seconds
	"connect_timeout" => 60, // seconds
	"file" => __DIR__."/target.txt",
	"delimiter" => "\n",
];


define("UA", 
	[
		"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0",
		"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
		"Opera/9.80 (J2ME/MIDP; Opera Mini/4.2/28.3590; U; en) Presto/2.8.119 Version/11.10",
		"Mozilla/5.0 (Linux; U; Android 4.4.2; id; SM-G900 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/9.9.2.467 U3/0.8.0 Mobile Safari/534.30 evaliant",
		"Mozilla/5.0 (Linux; U; Android 6.0.1; en-US; SM-J700F Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36",
		"Mozilla/5.0 (Linux; U; Android 7.0; en-US; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36",
		"Mozilla/5.0 (Linux; U; Android 7.0; en-US; SM-G610F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36",
		"NokiaC1-01/2.0 (04.40) Profile/MIDP-2.1 Configuration/CLDC-1.1 nokiac1-01/UC Browser7.8.0.95/70/351 UNTRUSTED/1.0",
		"Nokia302/5.0 (14.78) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; Desktop) AppleWebKit/534.13 (KHTML, like Gecko) UCBrowser/9.4.1.377",
		"Mozilla/5.0 (Linux; U; Android 4.2.2; en-US; Micromax A102 Build/MicromaxA102) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.8.855 U3/0.8.0 Mobile Safari/534.30",
		"Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; itel it1407 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.5.809 U3/0.8.0 Mobile Safari/534.30",
		"UCWEB/2.0 (MIDP-2.0; U; Adr 4.0.4; en-US; ZTE_U795) U2/1.0.0 UCBrowser/10.7.6.805 U2/1.0.0 Mobile",
		"Mozilla/5.0 (Linux; U; Android 5.1.1; en-US; SM-J200G Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.4.8.1012 Mobile Safari/537.36"
	]
);
define("UA_COUNT", count(UA));
define("CONNECTTIMEOUT", $config["connect_timeout"]);

return $config;
