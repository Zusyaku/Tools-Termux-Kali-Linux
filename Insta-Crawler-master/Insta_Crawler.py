#!/usr/bin/env python
import urllib,threading,string,random,time

def gen():
    alp= string.letters + string.digits + string.punctuation
    return 'BI'+"".join(random.sample(alp,9))

def main():
    print "[#] Generating random pictures ids"
    while True:
        url="https://www.instagram.com/p/"+str(gen())+"/"
        try:
            response=urllib.urlopen(url).getcode()
            if response==200 or response==301:
                print "\n["+str(response)+":Ok] "+str(url)
        except:
            print "\n[!]Finished In {} Second(s).".format(int(time.time() - start_time))
            exit()

faster = threading.Thread(target=main)
faster.start()
faster.join()
