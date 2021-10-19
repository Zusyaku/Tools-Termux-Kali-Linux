from time import sleep
import threading, time, requests, sys, os, re, random


def dark_format_auto(text):
        for x in text + '\n':
                sys.stdout.write(x)
                sys.stdout.flush()
                sleep(random.random() * 0.05)
def loding():
     time.sleep(1)
def dark_cooldown():
    for x in range(35):
        print(end=f"\r\033[1;37m[\033[90m•\033[1;36m] \033[1;37mTunggu 35 detik untuk call cok! \033[1;33m[\033[1;36m{35-(x+1)}\033[1;33m]\t ",flush=True)
        time.sleep(1)
