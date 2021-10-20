'''
Port Scanner
Scan All Open Ports Of The Target IP
Coded By .::Shayan::.
'''
#!/usr/bin/python2
import socket, sys, random, time, os, ctypes
def Print():
    Cls = '\x1b[0m'
    Colors = [37,31,32,36,30,35,34,33]
    Logo = '''
          <<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>
          <                In The Name Of God                >
          <              Port Scanner - Ver 1.0              >
          <             Programmer: .::Shayan::.             >
          <                  Our Channels:                   >
          <             Github.com/ShayanDeveloper           >
          <   Youtube.com/channel/UCG4F9NK2kLdiON8J0mCzwYA   >
          <              Aparat.com/ShayanDeveloper          >
          <                    T.me/SD_SOFT                  >
          <<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>
        '''
    for N,Line in enumerate(Logo.split('\n')):
        sys.stdout.write('\x1b[1;%dm%s%s\n' % (random.choice(Colors), Line, Cls))
        time.sleep(0.08)
def Clear():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])
def Checker(ip):
    ports = [20,21,22,23,25,53,67,68,69,110,123,137,138,139,143,161,162,179,389,443,636,989,990,3389,80]
    for p in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            res = s.connect_ex((getIP,p))
            if res == 0:
                print g+'[+]'+getIP+':'+str(p)+' --> This Port Is Open!'
                o = open('Open Ports['+ip+'].txt','a')
                o.write(getIP+':'+str(p)+'\n')
                o.close()
            else :
                print m+'[-]'+getIP+':'+str(p)+' --> This Port Is Close!'
                o = open('Close Ports['+ip+'].txt','a')
                o.write(getIP+':'+str(p)+'\n')
                o.close()
            s.close()
        except Exception as x:
            print r+'Error!\nMessage:  '+x.message
    time.sleep(3)
    Clear()
    print random.choice(color_array)+'Checking Port Has Been Finished!'+'\n'+random.choice(color_array)+'Restarting...!'
    time.sleep(4)
while True:
    ctypes.windll.kernel32.SetConsoleTitleA('Port Scanner ~ By .::Shayan::.')
    Clear()
    Print()
    r = '\033[31m'
    g = '\033[32m'
    y = '\033[33m'
    b = '\033[34m'
    m = '\033[35m'
    c = '\033[36m'
    w = '\033[37m'
    color_array = ['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m', '\033[39m']
    print '\n'+random.choice(color_array)+'[~]Please Enter The Target IP :'+'\n'
    getIP = raw_input(random.choice(color_array)+'> ')
    if getIP != '':
        Clear()
        Checker(getIP)
    else:
        sys.exit()