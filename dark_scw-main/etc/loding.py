from time import sleep
import threading, time, requests, sys, os, re, random


def dark_format_auto(text):
        for x in text + '\n':
                sys.stdout.write(x)
                sys.stdout.flush()
                sleep(random.random() * 0.05)
def loding():

    dark_format_auto(f"--------------------------------------------------")
    for x in range(10):
        print(end=f"\r\033[1;37m[\033[90m•\033[1;36m] \033[1;37mCooldown \033[1;33m[\033[1;36m{10-(x+1)}\033[1;33m] ",flush=True)
        time.sleep(1)
