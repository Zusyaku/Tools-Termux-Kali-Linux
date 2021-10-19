# -*- coding: utf-8 -*-
import os,sys,time,datetime, random, hashlib, re,threading, json, getpass, urllib
from multiprocessing.pool import ThreadPool

def load():
    os.system("clear")
    print "\r                \r"
    load2 = [
    '\033[1;97m.','..','...10%', '.', '..', '...30%', '.', '..', '...60%',  '.', '..', '...100%\n', '  \x1b[1;91mAuto Token Detect!!!' ]
    for o in load2:
        print "\r\r\x1b[1;91m[\xe2\x97\x8f]\033[1;92mLoading\033[1;97m" +o, "\033[1;97m",
        sys.stdout.flush()
        time.sleep(0.50)
load()
time.sleep(3)
os.system("clear")
