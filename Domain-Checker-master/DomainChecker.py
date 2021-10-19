#!/usr/bin/env python
print '''
______                      _         _____ _               _             
|  _  \                    (_)       /  __ \ |             | |            
| | | |___  _ __ ___   __ _ _ _ __   | /  \/ |__   ___  ___| | _____ _ __ 
| | | / _ \| '_ ` _ \ / _` | | '_ \  | |   | '_ \ / _ \/ __| |/ / _ \ '__|
| |/ / (_) | | | | | | (_| | | | | | | \__/\ | | |  __/ (__|   <  __/ |   
|___/ \___/|_| |_| |_|\__,_|_|_| |_|  \____/_| |_|\___|\___|_|\_\___|_|   
                                                                          
# Check Domains & Subdomains Response
# Coded By kareem Shoair | D4Vinci
# All Copyright To Squnity Company Team & Deveolopers   '''


import requests,urllib,sys,threading,time
def main():
    if len(sys.argv)<2:
        print """Help:
    Usage:DomainsChecker.py wordlist.txt"""
        sys.exit(0)
    wordlist=sys.argv[1]
    a=open(wordlist,"r").readlines()
    start_time = time.time()
    for url in a:
        if "http" not in url or "https" not in url:
            url="http://"+str(url)
        try:
            response=urllib.urlopen(url).getcode()
            if response in xrange(200,400) or response in xrange(100,101):
                print "["+str(response)+"] "+str(url)
                response=requests.get(url)
                if response.history:
                    for res in response.history:
                        print "\tRedirected To : "+"[Response:"+str(res.status_code)+"] "+str(res.url)
                    print "\tFinal Redirection : "+"[Response:"+str(response.status_code)+"] "+str(response.url)
        except IOError:
            pass
    print "\n[!]Finished In {} Second(s).".format(int(time.time() - start_time))

faster = threading.Thread(target=main)
faster.start()
faster.join()