use strict;
use warnings;
use feature "say";
use Time::HiRes qw(sleep);
use utf8;
use open qw(:std :encoding(UTF-8));


#               code by polygon
#               bahasa : perl
#####################################
my $bla = "\e[90m";
my $me = "\e[91m";
my $ij = "\e[92m";
my $ku = "\e[93m";
my $bi = "\e[94m";
my $m = "\e[95m";
my $cy = "\e[96m";
my $pu = "\e[97m";
my $st = "\e[00m";
                   system("clear");
			printf("\e[91m╔╗╔═╗╔═══╗╔╗───╔╗╔═╗╔╗─╔╗╔╗───╔═══╗╔════╗╔═══╗╔═══╗\e[00m\n");
		sleep("0.1");
			printf("\e[91m║║║╔╝║╔═╗║║║───║║║╔╝║║─║║║║───║╔═╗║║╔╗╔╗║║╔═╗║║╔═╗║\e[00m\n");
		sleep("0.1");
			printf("\e[91m║╚╝╝─║║─║║║║───║╚╝╝─║║─║║║║───║║─║║╚╝║║╚╝║║─║║║╚═╝║\e[00m\n");
		sleep("0.1");
			printf("\e[97m║╔╗║─║╚═╝║║║─╔╗║╔╗║─║║─║║║║─╔╗║╚═╝║──║║──║║─║║║╔╗╔╝\e[00m\n");
		sleep("0.1");
			printf("\e[97m║║║╚╗║╔═╗║║╚═╝║║║║╚╗║╚═╝║║╚═╝║║╔═╗║──║║──║╚═╝║║║║╚╗\e[00m\n");
		sleep("0.1");
			printf("\e[97m╚╝╚═╝╚╝─╚╝╚═══╝╚╝╚═╝╚═══╝╚═══╝╚╝─╚╝──╚╝──╚═══╝╚╝╚═╝\e[00m\n");
		sleep("0.1");
       say "";
		sleep("0.1");
		        print("${bi}<${ij}>${ku}==================${me}=====================${ij}==========${ku}<${bi}>\n");
		sleep("0.1");
			print("                  ${bi}Au${ku}thor ${me}: ${cy}Pol${ku}gon\n");
		sleep("0.1");
			print("                  ${ij}you${m}tube${me}: ${bi}pej${cy}uang ${me}ken${ku}tang\n");
		sleep("0.1");
			print("${bi}<${ij}>${ku}==================${me}=====================${ij}==========${ku}<${bi}>\n");
say "";
printf("            ${bi}ty${ku}pe ${me}kalku${ku}lator ${m}: ${ij}penju${bi}mlahan${st}                         \n");
say "";

print("${ij}[${bi}*${ij}]${st} masukan nilai awal : ");
$a = <STDIN>;
             say "";
print("${bi}[${ku}¥${bi}]${st} masukan nilai kedua : ");
$b = <STDIN>;

say "";

STDOUT->autoflush(1);


WAIT: {
    my $tot_sleep;
    while (1) {
        for ('🕛', '🕐', '🕑', '🕒', '🕓', '🕔', '🕕', '🕖', '🕗', '🕘', '🕙') {
            print("\r${ij}[${m}▶${ij}]${st} memproses "); print; $tot_sleep += sleep 0.1;
            last WAIT if $tot_sleep >= 5;
        };   
    };
};

print("\n\n${bi}>[${ku}€${bi}]<${st} hasil : ", ( $a + $b ));
      say "\n";
