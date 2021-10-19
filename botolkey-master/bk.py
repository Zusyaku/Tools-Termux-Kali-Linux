# -*- coding: utf-8 -*-
import os,sys,time,bkey
print
print
print('ALL PACKAGES ARE INSTALLING. PLEASE WAIT 1 OR 2 MINUTES.....')
print
print
os.system('pkg update && pkg upgrade && pkg install python && pkg install python2 && pkg install git && pkg install pip && pkg install pip2')
time.sleep(1)

os.system('pip2 install bkey')
time.sleep(1)

os.system("bkey")
time.sleep(1)
