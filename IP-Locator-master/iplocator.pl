#!/usr/bin/perl
# Ip Geolocation 
#By John Poli Modica @ CybernetiX
# 2-23-2013 
#
# API documentation - http://ip-api.com/docs/
# you can see you external ip using this Bash script :
# read COUNTRY IP <<< $(wget -qO- http://ip-api.com/line/?fields=countryCode,query); echo $IP $COUNTRY
# Now let's start :

use Socket;
use Term::ANSIColor;
use WWW::Mechanize;
use JSON;
  
 
print color 'bold bright_yellow';
 
print q{


                                         _,aggdd888bbgg,,_
                                    ,ad88888YYYYYYYYYYY8888ba,
                                 ,d888P""'              ``""Y88b,
                               ,d888"'                       "Y888,
                              d88P'                            `Y88b,
                            ,d88'                                `Y88,
                           ,888'                                  `Y88,
                          ,d88'                                    `Y8b,
                          d88'                  IP                  `88I
                         ,88P                 Locator                I88
                         I88I                                        I88
                         I88I                                        I8I
                         `888,                                       d8I
                          `888,                                     d88'
                           `888,                                   d8PI
                           ,dP"8b,                               ,8P'd'
                         ,dP'   "Yb,                          _,d8" P'
                       ,dP' ,db,  "Yb,_                    ,ad8P" ,P'
                     ,dP' ,d8888b,  `"Yba,,__        __,ad88P"  ,d"
                   ,dP' ,d88888888b,    "88Y8888888888PP""   _,d"
                 ,dP' ,d888888888888P  ,d"8              _,gd"'
               ,dP' ,d888888888888P' ,d" ,8bbaagggggaaddP""'
             ,dP' ,d888888888888P' ,d" ,d"'
           ,dP' ,d888888888888P' ,d" ,d"
         ,dP' ,d888888888888P' ,d" ,d"     
       ,dP' ,d888888888888P' ,d" ,d"       
     ,dP' ,d888888888888P' ,d" ,d"
   ,dP' ,d888888888888P' ,d" ,d"
 ,dP' ,d888888888888P' ,d" ,d"
dP'  d888888888888P' ,d" ,d"
8"Ya, `888888888P' ,d" ,d"
8  "Ya, `88888P' ,d" ,d"
8a,  "Ya, `8P' ,d" ,d"
 "Ya,  "Ya,  ,d" ,d"
   "Ya,  "Y8P" ,d"
     "Ya,  8 ,d"
       "Ya,8d"
         "YP
02-23-2013

Ip Geolocation Tool  
By : John Poli Modica
	CybernetiX 

------------------------------------
};
 
print color 'reset';
@iphost=$ARGV[0] || die "Usage : ./Iplocation.pl [host] [ip] [domain] \n\nEx:  ./Iplocation.pl  www.google.com \n     ./Iplocation.pl  216.58.210.206\n \n";
my @ip = inet_ntoa(scalar gethostbyname("@iphost")or die "IP or Host invalid!\n");
my @hn = scalar gethostbyaddr(inet_aton(@ip),AF_INET);
 
my $GET=WWW::Mechanize->new();
    $GET->get("http://ip-api.com/json/@ip"); # JSON API OF IP-API.COM
    my $json = $GET->content();
 
 
my $info = decode_json($json);
# Json API Response :
# A successful request will return, by default, the following:
#{
#    "status": "success",
#    "country": "COUNTRY",
#    "countryCode": "COUNTRY CODE",
#    "region": "REGION CODE",
#    "regionName": "REGION NAME",
#    "city": "CITY",
#    "zip": "ZIP CODE",
#    "lat": LATITUDE,
#    "lon": LONGITUDE,
#    "timezone": "TIME ZONE",
#    "isp": "ISP NAME",
#    "org": "ORGANIZATION NAME",
#    "as": "AS NUMBER / NAME",
#   "query": "IP ADDRESS USED FOR QUERY"
# }
# INFOS OF JSON API ...
 
print "  [!] IP: ", $info->{'query'}, "\n";
print "------------------------------------\n"; 
print "  [+] ORG: ", $info->{'as'}, "\n";
print "  [+] ISP: ", $info->{'isp'}, "\n";
print "  [+] Country: ", $info->{'country'}," - ", $info->{'countryCode'}, "\n";
print "  [+] City: ", $info->{'city'}, "\n";
print "  [+] Region: ", $info->{'regionName'}, " - " , $info->{'region'}, "\n";
print "  [+] Geo: ", "Lat: " , $info->{'lat'}, " - Long: ", $info->{'lon'}, "\n";
print "  [+] Geo: ", "Latitude: " , $info->{'lat'}, " - Long: ", $info->{'lat'}, "\n";
print "  [+] Time: ", "timezone: " , $info->{'timezone'}, " - Long: ", $info->{'timezone'}, "\n";
print "  [+] As number/name: ", "as: " , $info->{'as'}, " - Long: ", $info->{'as'}, "\n";
print "  [+] ORG: ", $info->{'as'}, "\n";
print "  [+] Country code: ", $info->{'countryCode'}, "\n"; 
print "  [+] Status: ", $info->{'status'}, "\n"; 
print "\n";
# EOF
