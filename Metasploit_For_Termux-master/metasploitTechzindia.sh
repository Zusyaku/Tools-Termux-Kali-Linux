#!/data/data/com.termux/files/usr/bin/bash
echo "##############################################"
echo " TechZindia, PLZ SUBSCRIBE TechZindia YouTube CHANNEL"
echo "##############################################"

echo "WAIT UNTIL INSTALLING............" 

echo "####################################"
apt install autoconf bison clang coreutils curl findutils git apr figlet apr-util libffi-dev libgmp-dev libpcap-dev postgresql-dev readline-dev libsqlite-dev openssl-dev libtool libxml2-dev libxslt-dev ncurses-dev pkg-config postgresql-contrib wget make ruby-dev libgrpc-dev ncurses-utils termux-tools -y
echo "####################################"
echo "Downloading & Extracting....."

cd $HOME
curl -LO https://github.com/rapid7/metasploit-framework/archive/4.16.4.tar.gz
tar -xf $HOME/4.16.4.tar.gz
mv $HOME/metasploit-framework-4.16.4 $HOME/metasploit-framework
cd $HOME/metasploit-framework
sed '/rbnacl/d' -i Gemfile.lock
sed '/rbnacl/d' -i metasploit-framework.gemspec

#Install bundler
gem install bundler

#Install nokogiri
echo "nokogiri is installing......"
gem install nokogiri -- --use-system-libraries

#Install grpc gem
sed 's|grpc (.*|grpc (1.4.1)|g' -i $HOME/metasploit-framework/Gemfile.lock
gem unpack grpc -v 1.4.1
cd grpc-1.4.1
curl -LO https://raw.githubusercontent.com/grpc/grpc/v1.4.1/grpc.gemspec
curl -L https://wiki.termux.com/images/b/bf/Grpc_extconf.patch -o extconf.patch
patch -p1 < extconf.patch
gem build grpc.gemspec
gem install grpc-1.4.1.gem
cd ..
rm -r grpc-1.4.1

#Bundle Install
echo "bundle and all other dependencies are installing......"
cd $HOME/metasploit-framework
bundle install -j5

#Fixing Shebang
$PREFIX/bin/find -type f -executable -exec termux-fix-shebang \{\} \;
rm ./modules/auxiliary/gather/http_pdf_authors.rb
ln -s $HOME/metasploit-framework/msfconsole /data/data/com.termux/files/usr/bin/

echo "###############################"
echo "Thanks  To  Vishalbiswani & Auxilus "
echo "###############################"
figlet TechZindia
echo "###############################################"
echo "Hello Guys,  Subscribe  My TechZindia YouTube channel"
figlet Subscribe
echo "###############################################"
echo "###############################"
echo "For More Hacking video At TechZindia YT Channel"
echo "###############################"
figlet TechZindia
echo "####################################"
echo " NOW YOU CAN RUN METASPLOIT BY JUST EXECUTE THE COMMAND :=>  ./msfconsole"
echo "####################################"
figlet Finish
