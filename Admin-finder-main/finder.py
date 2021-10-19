#!/usr/bin/env python3
#Coded by CyberCommads
import os
import sys
import requests
from time import sleep

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    #print("\033[34m[*] \033[0mTarget Url e.g. http://example.com")
    #url = input("Enter Target Url: ")
    url = sys.argv[1]

    start = "Start Scanning...\n"
    for s in start:
        sys.stdout.write(s)
        sys.stdout.flush()
        sleep(0.1)
    
    file = open("admin_panels.txt", "r")	#Open files containing possible admin directories.
    try:
        for link in file.read().splitlines():
            curl = url + link
            res = requests.get(curl)
            if res.status_code == 200:
                print("*" * 20)
                print("\033[32mAdmin panel found --> {} \033[0m".format(curl))
                print("*" * 20)
            else:
                print("\033[91m[-] Not found --> {} \033[0m".format(curl))
    
    except KeyboardInterrupt:
        print("\033[91mShutdown Request ! \033[0m")
    except:
        print("\033[91mUnknown Error ! \033[0m")
    
    file.close()

if __name__ == "__main__":
    main()
