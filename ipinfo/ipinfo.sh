#ip-info by Niirmaal Twaatii
#GitHub : https://github.com/niirmaaltwaatii/ipinfo

clear
cat bnr

while [ 0==0 ];
do
    cat opt.txt
    read -p "[]=> " o
    if [ $o -eq "1" ];
    then
        read -p "IP Address : " ip
        cd ipdata
        curl http://ip-api.com/json/$ip > "$ip.json"
        sleep 1
        echo " "
        echo "[∆] Data for $ip :-"
        cat "$ip.json"
        cd ..
        echo ""
        echo "[✓] IP-Data saved as "$ip".json at /ipdata directory !"
        sleep 1.5
    elif [ $o -eq "0" ];
    then
        exit
    elif [ $o -eq "2" ];
    then
        echo " "
        cd ipdata
        rm *
        cd ..
        echo "[✓] All Saved data Deleted ! "
    else
        echo "[×] Invalid Command !"
        exit
    fi

done

