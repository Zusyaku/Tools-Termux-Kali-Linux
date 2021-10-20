import os,sys,time,requests,re,json,random
from time import sleep
from requests import post
try:
    fi=open('user.txt','r').read()
    ff=re.findall(r'User=(.*?)\n',fi)[0]
    xx=re.findall(r'cookie=(.*?)\n',fi)[0]
    oo=re.findall(r'authorization=(.*?)\n',fi)[0]
    pp=re.findall(r'ts=(.*?)\n',fi)[0]
    ss=re.findall(r'index=(.*?)',fi)[0]
except:
    print('Data Not Found')
    ff=input('\033[1;97mUseragent:\033[96m')
    xx=input('\033[1;97mCookie:\033[96m')
    oo=input('\033[1;97mAuthorization:\033[96m')
    pp=input('\033[1;97mts:\033[96m')
    ss=input('\033[1;97mIndex:\033[96m')
    with open('user.txt','w') as wfile:
         wfile.write('User='+ff+'\ncookie='+xx+'\nauthorization='+oo+'\nts='+pp+'\nindex='+ss)
def login():
    bb={
    "Host": "ai2.caping.co.id",
    "accept-language": "in",
    "networkstate": "FouthG",
    "user-agent": f"{ff}",
    "cookie": f"{xx}",
    "market": "googleplay",
    "appid": "1",
    "content-type": "application/json",
    "accept-encoding": "gzip"
    }
    data={"city":"Jakarta"}
    a=json.dumps(data)
    print ('\033[00mSedang Login\033[91m...\033[00m')
    time.sleep(1)
    r = requests.post("https://ai2.caping.co.id/v2/user/login/visitor", data=a, headers=bb)
    h=json.loads(r.text)
    if "OK" in r.text:
        print ("\033[00mLogin \033[92mSuccess\n\033[00mYourname:\033[96m",h["data"]["user_name"])
    else:
        print ("\033[00mLogin \033[91mFailed\033[00m")
        os.system('rm -rf user.txt')
        os.system('python bot.py')
    d=requests.get("https://ai2.caping.co.id/v2/user/ccsp/detail", headers=bb)
    g=json.loads(d.text)
    if "OK" in d.text:
        print ("\033[00mYourId:\033[96m",g["data"]["uid"],"\n\033[00mYourcoin:\033[96m",g["data"]["total_coin"],"\n\033[00mYourMoney:\033[96m",g["data"]["total_money"])
    else:
        print("\033[00mLogin \033[91mFailed\033[00m")
        os.system('rm -rf user.txt')
        os.system('python bot.py')
def bonus():
    bb={
    "Host": "ai2.caping.co.id",
    "accept-language": "in",
    "networkstate": "FouthG",
    "user-agent": f"{ff}",
    "cookie": f"{xx}",
    "market": "googleplay",
    "appid": "1",
    "authorization": f"{oo}",
    "ts": f"{pp}",
    "index": f"{ss}",
    "accept-encoding": "gzip"
    }
    print ('\033[00mMengambil bonus harian...')
    time.sleep(2)
    r=requests.get("https://ai2.caping.co.id/v2/event/random", headers=bb).text
    h=json.loads(r)
    if h["data"]["get_coin"] == 0:
       print ("\033[93mAnda Sudah Mengambil Bonus\033[00m")
    else:
       print ("\033[00mSuccess Claim Bonus:+\033[92m",h["data"]["get_coin"])
def baca():
    login()
    bonus()
    bb={
    "Host": "ai2.caping.co.id",
    "accept-language": "in",
    "networkstate": "FouthG",
    "user-agent": f"{ff}",
    "cookie": f"{xx}",
    "market": "googleplay",
    "appid": "1",
    "authorization": f"{oo}",
    "ts": f"{pp}",
    "index": f"{ss}",
    "content-type": "application/json",
    "accept-encoding": "gzip"
    }
    print ('\033[00mMembaca Berita...')
    time.sleep(2)
    count=1
    while count <41:
        pg=random.randrange(1,5)
        d=json.dumps({"articleType":1,"page":pg})
        j=requests.post("https://ai2.caping.co.id/v2/news/getNewsList2", data=d, headers=bb).text
        hh=json.loads(j)
        for x in hh["data"]["list"]:
            su=x['ArticleType']
            k=x["NewsId"]
        dat=json.dumps({"reports":[{"action":"browse_news","list":[{"articleType":su,"newsId":k,"status":1,"times":4,"totalms":40},{"articleType":su,"newsId":k,"status":1,"times":3,"totalms":33},{"articleType":su,"newsId":k,"status":1,"times":2,"totalms":31}]}]})
        time.sleep(2)
        r=requests.post("https://ai2.caping.co.id/v2/event/report",data=dat, headers=bb)
        js1=json.loads(r.text)
        if js1['data'] == 0:
           print ("\033[91mGagal Claim\033[00m")
        else:
           print (f"\033[00m[\033[96m{count}\033[00m]Success Claim:+\033[92m",js1['data'])
           count=count+1
def share():
    baca()
    print ('\033[00mShare Konten...')
    for i in range(0,5):
        bb={
        "Host": "ai2.caping.co.id",
        "accept-language": "in",
        "networkstate": "FouthG",
        "user-agent": f"{ff}",
        "cookie": f"{xx}",
        "market": "googleplay",
        "appid": "1",
        "authorization": f"{oo}",
        "ts": f"{pp}",
        "index": f"{ss}",
        "content-type": "application/json",
        "accept-encoding": "gzip"
        }
        pg=random.randrange(1,6)
        d=json.dumps({"articleType":1,"page":pg})
        j=requests.post("https://ai2.caping.co.id/v2/news/getNewsList2", data=d, headers=bb).text
        hh=json.loads(j)
        for x in hh["data"]["list"]:
            su=x['ArticleType']
            k=x["NewsId"]
        k=requests.get(f"https://ai2.caping.co.id/v2/event/share/news/{k}", headers=bb).text
        if "OK" in k:
           print ('\033[00mSuccess Share..')
        else:
           print ('\033[91mgagal share\033[00m...')
share()

