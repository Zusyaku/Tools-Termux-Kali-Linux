#!/bash/python3

import sys
import socket
import datetime

# defining target

if (len(sys.argv) == 4): #check if 3 arguments exists or not
    target = socket.gethostbyname(sys.argv[1]) #translate hostname to IPv4
    
else:
    print("Invalid amount of arguments!")
    print("Syntax: python3 portscanner.py <ip> <initial port #> <end port #> ")
    
# adding a basic banner
print("-" * 50)
print("Scanning target: " + target)
print("Time started: " + str(datetime.datetime.now()))
print("-" * 50) 

try:

    for port in range(int(sys.argv[2]), int(sys.argv[3]) + 1 ): #ports to be scanned  
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #specifying the address family and socket type
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port)) # returns an error indicator => 0:success, 1:error
    
        if (result == 0):
            print(f"Port {port} open")
        
        else:
            print(f"Port {port} closed")
        s.close()    #close the connection
    
except KeyboardInterrupt:
    print("\nExiting...")
    sys.exit()
    
except socket.gaierror:
    print("The hostname couldn't be resolved.")
    sys.exit()
    
except socket.error:
    print("Couldn't connect to the server.")
    sys.exit()   
    



