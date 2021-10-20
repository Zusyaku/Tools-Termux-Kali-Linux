import os
import sys
import webbrowser

######################################################
#Educational purpose only                            #
######################################################
#Thanks to APNIC Whois Service                       #
#because of there servicr this script was possible   #
######################################################
#SUBSCRIBE: https://www.youtube.com/channel/UCKAmv8p_TRvUNrJlfiB8qBQ

os.system("clear")

print "\033[1;32;40m"
print "                       _____                _____              _             "
print "                      |  __ \              |_   _|            | |            "
print "                      | |  \/ ___  ___ ______| |_ __ __ _  ___| | _____ _ __ "
print "                      | | __ / _ \/ _ \______| | '__/ _` |/ __| |/ / _ \ '__|"
print "                      | |_\ \  __/ (_) |     | | | | (_| | (__|   <  __/ |   "
print "                       \____/\___|\___/      \_/_|  \__,_|\___|_|\_\___|_|   "
print "                                                                             "
print "               ========================================================================"
print "                                    Created By: TheTechHacker                          "
print "                                 Server Name APNIC Whois Service                       "
print "               ========================================================================"
print " "
ip = raw_input("                     IP> ")
os.system("curl http://api.hackertarget.com/whois/?q=" + ip)

if ip == "exit":
    os.system("clear")
    os.system("exit")
elif ip == "SUB":
    os.system("clear")
    webbrowser.open("https://www.youtube.com/channel/UCKAmv8p_TRvUNrJlfiB8qBQ")
elif ip == "sub":
    os.system("clear")
    webbrowser.open("https://www.youtube.com/channel/UCKAmv8p_TRvUNrJlfiB8qBQ")

print "\033[1;m"
