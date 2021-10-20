from toutatis import *
from six.moves import input
import requests
import hmac
import hashlib
import random
import string
import json
import argparse




fa = print('''\033[1;37m
-------------------------------
.:: Instagram account maker and extract info ::.
    by FaLah - 0xfff0800       
    Snapchat - flaah999     
-------------------------------
Fetching the username info

Create a bot account


\033[1;37m''')

 
if fa == '1':
  parser = argparse.ArgumentParser()


username = input('username -> ')
sessionsId = input('sessionsId -> ') 
infos = getAllInfos(username,sessionsId)

print("Informations about : "+infos["username"])
print("Full Name : "+infos["FullName"]+" userID : "+infos["userID"])

info = getInfo(username,sessionsId)
print("Verified : "+str(info['is_verified'])+" Is buisness Acount : "+str(info["is_business"]))
print("Is private Account : "+str(info["is_private"]))
print("Follower : "+str(info["follower_count"]) + " Following : "+str(info["following_count"]))
print("Number of posts : "+str(info["media_count"]))
print("Number of tag in posts : "+str(info["following_tag_count"]))
print("External url : "+info["external_url"])
print("IGTV posts : "+str(info["total_igtv_videos"]))
if len(infos["biography"]) >1:
    infos["biography"]="Not found"

print("Biography : "+infos["biography"])

if len(infos["publicEmail"])==0:
    infos["publicEmail"]="Not found"

print("Public Email : "+infos["publicEmail"])

if infos["recoveryEmail"]=="NULL":
    infos["recoveryEmail"]=="Not found"

print("Recovery Email : "+infos["recoveryEmail"])

if len(infos["public_phone_number"])<1:
    infos["public_phone_number"]="Not found"

print("Public Phone number : "+infos["public_phone_number"])
print("Profile Picture : "+infos["ProfilePicture"])
########
if fa == '2':
  def HMAC(text):
    key = '3f0a7d75e094c7385e3dbaa026877f2e067cbd1a4dbcf3867748f6b26f257117'
    hash = hmac.new(key,msg=text,digestmod=hashlib.sha256)
    return hash.hexdigest()

def randomString(size):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))


print("")
print("")
print(" \033[1;31mNow you want to create an Instagram account? \033[1;31m")
print("")
print(" No ? -> ( Ctrl + C ) ")
def main():
 banner()
parser = argparse.ArgumentParser()
name = input("name -> ")
username = input("username -> ")
email = input("email -> ")
password = input("password -> ")


getHeaders = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0)',
               'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Accept-Encoding':'gzip, deflate, sdch',
               'Accept-Language':'en-US,en;q=0.8',
               'upgrade-insecure-requests':'1'}

s = requests.Session()
s.get('https://instagram.com',headers=getHeaders)
guid = randomString(8) + '-' + randomString(4) + "-" + randomString(4) + '-' + randomString(4) + '-' +randomString(12)
device_id = 'android-' + str(HMAC(str(random.randint(1000,9999))))[0:min(64,16)]
information = {'username':username,'first_name':name,'password':password,'email':email,'device_id':device_id,'guid':guid}
js = json.dumps(information)
payload = {'signed_body': HMAC(js) + '.' + js,'ig_sig_key_version':'4'}
postHeaders = {'Host':'i.instagram.com',
                  'User-Agent':'Instagram 7.1.1 Android (21/5.0.2; 480dpi; 1080x1776; LGE/Google; Nexus 5; hammerhead; hammerhead; en_US)',
                  'Accept-Language':'en-US',
                  'Accept-Encoding':'gzip',
                  'Cookie2':'$Version=1',
                  'X-IG-Connection-Type':'WIFI',
                  'X-IG-Capabilities':'BQ=='
                  }
x = s.post('https://i.instagram.com/api/v1/accounts/create/',headers=postHeaders,data=payload)
result = json.loads(x.content)
if result['status'] != 'fail':
        if result['account_created'] == True:
            print ('Account has been created successfully')
        else:
            print ('Error:')
            for i in result['errors']:
                print (str(result['errors'][i][0]))
else:
        if result['spam'] == True:
            print ('Instagram blocks your IP due to spamming behaviour.')


if __name__ == '__main__':
    main()
