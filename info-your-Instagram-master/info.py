from colorama import Fore
from six.moves import input
import requests, sys, threading, time
import argparse,json
CheckVersion = str(sys.version)

green_color = "\033[1;32m"

sessionId = input("sessionid => ")

print('\n----------------------------')

headers = {'Host': 'www.instagram.com',
           'Content-Type': 'application/json; charset=utf-8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept': '*/*',
           'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
           'Connection': 'close',
           'X-IG-App-ID': '936619743392459',
           'X-Requested-With': 'XMLHttpRequest',
           'X-IG-WWW-Claim': 'hmac.AR0uQ3YRnOII5ROjBT7pKkMy1bjATWrSkfZCgwbaUBjNv-rw',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
           'Referer': 'https://www.instagram.com/accounts/access_tool/former_phones',
           'Cookie': 'ig_cb=1; ig_did=69205DC3-D787-47E5-B250-1C4A7ADC3A05; csrftoken=HKmRQ2ZwuqCZjpMycM3xOVIjDUBo5HWd; mid=XoSg-AAEAAHRshuq4BlxladvlcbE; datr=HmBKXyPTk86RJpmkaUQ7eM5w; urlgen="{\"51.36.8.205\": 43766}:1kLnkz:ZHs58RZnu4USDtTqolZcEXDJp7s"; rur=ATN; ds_user_id=37466401585',
           'DNT': '1'
           }

cookies = {'sessionid': sessionId}
data = ''
url = 'https://www.instagram.com/accounts/access_tool/former_usernames?__a=1'
response = requests.request("GET", url, data=data, headers=headers , cookies=cookies)
info = json.loads(response.text)
print(green_color +"اليوزرات منذ انشاء الحساب : "+str(info["data"]))

############################
print('\n----------------------------')

headers = {'Host': 'www.instagram.com',
           'Content-Type': 'application/json; charset=utf-8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept': '*/*',
           'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
           'Connection': 'close',
           'X-IG-App-ID': '936619743392459',
           'X-Requested-With': 'XMLHttpRequest',
           'X-IG-WWW-Claim': 'hmac.AR0uQ3YRnOII5ROjBT7pKkMy1bjATWrSkfZCgwbaUBjNv-rw',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
           'Referer': 'https://www.instagram.com/accounts/access_tool/former_phones',
           'Cookie': 'ig_cb=1; ig_did=69205DC3-D787-47E5-B250-1C4A7ADC3A05; csrftoken=HKmRQ2ZwuqCZjpMycM3xOVIjDUBo5HWd; mid=XoSg-AAEAAHRshuq4BlxladvlcbE; datr=HmBKXyPTk86RJpmkaUQ7eM5w; urlgen="{\"51.36.8.205\": 43766}:1kLnkz:ZHs58RZnu4USDtTqolZcEXDJp7s"; rur=ATN; ds_user_id=37466401585',
           'DNT': '1'
           }

cookies = {'sessionid': sessionId}
data = ''
url = 'https://www.instagram.com/accounts/access_tool/former_phones?__a=1'
response = requests.request("GET", url, data=data, headers=headers , cookies=cookies)
info = json.loads(response.text)
print(green_color +"ارقام الهواتف منذ انشاء الحساب : "+str(info["data"]))
############################
print('\n----------------------------')

headers = {'Host': 'www.instagram.com',
           'Content-Type': 'application/json; charset=utf-8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept': '*/*',
           'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
           'Connection': 'close',
           'X-IG-App-ID': '936619743392459',
           'X-Requested-With': 'XMLHttpRequest',
           'X-IG-WWW-Claim': 'hmac.AR0uQ3YRnOII5ROjBT7pKkMy1bjATWrSkfZCgwbaUBjNv-rw',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
           'Referer': 'https://www.instagram.com/accounts/access_tool/former_phones',
           'Cookie': 'ig_cb=1; ig_did=69205DC3-D787-47E5-B250-1C4A7ADC3A05; csrftoken=HKmRQ2ZwuqCZjpMycM3xOVIjDUBo5HWd; mid=XoSg-AAEAAHRshuq4BlxladvlcbE; datr=HmBKXyPTk86RJpmkaUQ7eM5w; urlgen="{\"51.36.8.205\": 43766}:1kLnkz:ZHs58RZnu4USDtTqolZcEXDJp7s"; rur=ATN; ds_user_id=37466401585',
           'DNT': '1'
           }

cookies = {'sessionid': sessionId}
data = ''
url = 'https://www.instagram.com/session/login_activity/?__a=1'
response = requests.request("GET", url, data=data, headers=headers , cookies=cookies)
info = json.loads(response.text)
print(green_color +"الهواتف التي سجلت دخول الي الحساب منذ انشاء الحساب : "+str(info["data"]))
############################
print('\n----------------------------')

headers = {'Host': 'www.instagram.com',
           'Content-Type': 'application/json; charset=utf-8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept': '*/*',
           'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
           'Connection': 'close',
           'X-IG-App-ID': '936619743392459',
           'X-Requested-With': 'XMLHttpRequest',
           'X-IG-WWW-Claim': 'hmac.AR0uQ3YRnOII5ROjBT7pKkMy1bjATWrSkfZCgwbaUBjNv-rw',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
           'Referer': 'https://www.instagram.com/accounts/access_tool/former_phones',
           'Cookie': 'ig_cb=1; ig_did=69205DC3-D787-47E5-B250-1C4A7ADC3A05; csrftoken=HKmRQ2ZwuqCZjpMycM3xOVIjDUBo5HWd; mid=XoSg-AAEAAHRshuq4BlxladvlcbE; datr=HmBKXyPTk86RJpmkaUQ7eM5w; urlgen="{\"51.36.8.205\": 43766}:1kLnkz:ZHs58RZnu4USDtTqolZcEXDJp7s"; rur=ATN; ds_user_id=37466401585',
           'DNT': '1'
           }

cookies = {'sessionid': sessionId}
data = ''
url = 'https://www.instagram.com/accounts/access_tool/former_emails?__a=1'
response = requests.request("GET", url, data=data, headers=headers , cookies=cookies)
info = json.loads(response.text)
print(green_color +"الاميلات التي سجلت في الحساب : "+str(info["data"]))

############################
print('\n----------------------------')

headers = {'Host': 'www.instagram.com',
           'Content-Type': 'application/json; charset=utf-8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept': '*/*',
           'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
           'Connection': 'close',
           'X-IG-App-ID': '936619743392459',
           'X-Requested-With': 'XMLHttpRequest',
           'X-IG-WWW-Claim': 'hmac.AR0uQ3YRnOII5ROjBT7pKkMy1bjATWrSkfZCgwbaUBjNv-rw',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
           'Referer': 'https://www.instagram.com/accounts/access_tool/former_phones',
           'Cookie': 'ig_cb=1; ig_did=69205DC3-D787-47E5-B250-1C4A7ADC3A05; csrftoken=HKmRQ2ZwuqCZjpMycM3xOVIjDUBo5HWd; mid=XoSg-AAEAAHRshuq4BlxladvlcbE; datr=HmBKXyPTk86RJpmkaUQ7eM5w; urlgen="{\"51.36.8.205\": 43766}:1kLnkz:ZHs58RZnu4USDtTqolZcEXDJp7s"; rur=ATN; ds_user_id=37466401585',
           'DNT': '1'
           }

cookies = {'sessionid': sessionId}
data = ''
url = 'https://www.instagram.com/emails/emails_sent/?__a=1'
response = requests.request("GET", url, data=data, headers=headers , cookies=cookies)
info = json.loads(response.text)
print(green_color +"النشاط الاخير في الحساب : "+str(info["data"]))

############################
print('\n----------------------------')

headers = {'Host': 'www.instagram.com',
           'Content-Type': 'application/json; charset=utf-8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept': '*/*',
           'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
           'Connection': 'close',
           'X-IG-App-ID': '936619743392459',
           'X-Requested-With': 'XMLHttpRequest',
           'X-IG-WWW-Claim': 'hmac.AR0uQ3YRnOII5ROjBT7pKkMy1bjATWrSkfZCgwbaUBjNv-rw',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
           'Referer': 'https://www.instagram.com/accounts/access_tool/former_phones',
           'Cookie': 'ig_cb=1; ig_did=69205DC3-D787-47E5-B250-1C4A7ADC3A05; csrftoken=HKmRQ2ZwuqCZjpMycM3xOVIjDUBo5HWd; mid=XoSg-AAEAAHRshuq4BlxladvlcbE; datr=HmBKXyPTk86RJpmkaUQ7eM5w; urlgen="{\"51.36.8.205\": 43766}:1kLnkz:ZHs58RZnu4USDtTqolZcEXDJp7s"; rur=ATN; ds_user_id=37466401585',
           'DNT': '1'
           }

cookies = {'sessionid': sessionId}
data = ''
url = 'https://www.instagram.com/accounts/access_tool/accounts_following_you?__a=1'
response = requests.request("GET", url, data=data, headers=headers , cookies=cookies)
info = json.loads(response.text)
print(green_color +"الحسابات التي تتابعك في اخر الوقت : "+str(info["data"]))

############################
print('\n----------------------------')

headers = {'Host': 'www.instagram.com',
           'Content-Type': 'application/json; charset=utf-8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept': '*/*',
           'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
           'Connection': 'close',
           'X-IG-App-ID': '936619743392459',
           'X-Requested-With': 'XMLHttpRequest',
           'X-IG-WWW-Claim': 'hmac.AR0uQ3YRnOII5ROjBT7pKkMy1bjATWrSkfZCgwbaUBjNv-rw',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
           'Referer': 'https://www.instagram.com/accounts/access_tool/former_phones',
           'Cookie': 'ig_cb=1; ig_did=69205DC3-D787-47E5-B250-1C4A7ADC3A05; csrftoken=HKmRQ2ZwuqCZjpMycM3xOVIjDUBo5HWd; mid=XoSg-AAEAAHRshuq4BlxladvlcbE; datr=HmBKXyPTk86RJpmkaUQ7eM5w; urlgen="{\"51.36.8.205\": 43766}:1kLnkz:ZHs58RZnu4USDtTqolZcEXDJp7s"; rur=ATN; ds_user_id=37466401585',
           'DNT': '1'
           }

cookies = {'sessionid': sessionId}
data = ''
url = 'https://www.instagram.com/accounts/access_tool/accounts_you_follow?__a=1'
response = requests.request("GET", url, data=data, headers=headers , cookies=cookies)
info = json.loads(response.text)
print(green_color +"الحسابات التي تابعتها في اخر الوقت : "+str(info["data"]))


############################
print('\n----------------------------')

headers = {'Host': 'www.instagram.com',
           'Content-Type': 'application/json; charset=utf-8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept': '*/*',
           'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
           'Connection': 'close',
           'X-IG-App-ID': '936619743392459',
           'X-Requested-With': 'XMLHttpRequest',
           'X-IG-WWW-Claim': 'hmac.AR0uQ3YRnOII5ROjBT7pKkMy1bjATWrSkfZCgwbaUBjNv-rw',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
           'Referer': 'https://www.instagram.com/accounts/access_tool/former_phones',
           'Cookie': 'ig_cb=1; ig_did=69205DC3-D787-47E5-B250-1C4A7ADC3A05; csrftoken=HKmRQ2ZwuqCZjpMycM3xOVIjDUBo5HWd; mid=XoSg-AAEAAHRshuq4BlxladvlcbE; datr=HmBKXyPTk86RJpmkaUQ7eM5w; urlgen="{\"51.36.8.205\": 43766}:1kLnkz:ZHs58RZnu4USDtTqolZcEXDJp7s"; rur=ATN; ds_user_id=37466401585',
           'DNT': '1'
           }

cookies = {'sessionid': sessionId}
data = ''
url = 'https://www.instagram.com/accounts/access_tool/current_follow_requests?__a=1'
response = requests.request("GET", url, data=data, headers=headers , cookies=cookies)
info = json.loads(response.text)
print(green_color +"طلبات المتابعة الحالية منذ انشاء الحساب : "+str(info["data"]))


print('\n----------------------------')

headers = {'Host': 'www.instagram.com',
           'Content-Type': 'application/json; charset=utf-8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept': '*/*',
           'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
           'Connection': 'close',
           'X-IG-App-ID': '936619743392459',
           'X-Requested-With': 'XMLHttpRequest',
           'X-IG-WWW-Claim': 'hmac.AR0uQ3YRnOII5ROjBT7pKkMy1bjATWrSkfZCgwbaUBjNv-rw',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
           'Referer': 'https://www.instagram.com/accounts/access_tool/former_phones',
           'Cookie': 'ig_cb=1; ig_did=69205DC3-D787-47E5-B250-1C4A7ADC3A05; csrftoken=HKmRQ2ZwuqCZjpMycM3xOVIjDUBo5HWd; mid=XoSg-AAEAAHRshuq4BlxladvlcbE; datr=HmBKXyPTk86RJpmkaUQ7eM5w; urlgen="{\"51.36.8.205\": 43766}:1kLnkz:ZHs58RZnu4USDtTqolZcEXDJp7s"; rur=ATN; ds_user_id=37466401585',
           'DNT': '1'
           }

cookies = {'sessionid': sessionId}
data = ''
url = 'https://www.instagram.com/accounts/access_tool/accounts_you_blocked?__a=1'
response = requests.request("GET", url, data=data, headers=headers , cookies=cookies)
info = json.loads(response.text)
print(green_color +"الحسابات التي قمت بحظرها منذ انشاء الحساب : "+str(info["data"]))

print('\n----------------------------')

headers = {'Host': 'www.instagram.com',
           'Content-Type': 'application/json; charset=utf-8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept': '*/*',
           'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
           'Connection': 'close',
           'X-IG-App-ID': '936619743392459',
           'X-Requested-With': 'XMLHttpRequest',
           'X-IG-WWW-Claim': 'hmac.AR0uQ3YRnOII5ROjBT7pKkMy1bjATWrSkfZCgwbaUBjNv-rw',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
           'Referer': 'https://www.instagram.com/accounts/access_tool/former_phones',
           'Cookie': 'ig_cb=1; ig_did=69205DC3-D787-47E5-B250-1C4A7ADC3A05; csrftoken=HKmRQ2ZwuqCZjpMycM3xOVIjDUBo5HWd; mid=XoSg-AAEAAHRshuq4BlxladvlcbE; datr=HmBKXyPTk86RJpmkaUQ7eM5w; urlgen="{\"51.36.8.205\": 43766}:1kLnkz:ZHs58RZnu4USDtTqolZcEXDJp7s"; rur=ATN; ds_user_id=37466401585',
           'DNT': '1'
           }

cookies = {'sessionid': sessionId}
data = ''
url = 'https://www.instagram.com/accounts/access_tool/former_links_in_bio?__a=1'
response = requests.request("GET", url, data=data, headers=headers , cookies=cookies)
info = json.loads(response.text)
print(green_color +"الروابط السابقة في الصفحة الشخصيه منذ انشاء الحساب : "+str(info["data"]))

print('\n----------------------------')

headers = {'Host': 'www.instagram.com',
           'Content-Type': 'application/json; charset=utf-8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept': '*/*',
           'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
           'Connection': 'close',
           'X-IG-App-ID': '936619743392459',
           'X-Requested-With': 'XMLHttpRequest',
           'X-IG-WWW-Claim': 'hmac.AR0uQ3YRnOII5ROjBT7pKkMy1bjATWrSkfZCgwbaUBjNv-rw',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
           'Referer': 'https://www.instagram.com/accounts/access_tool/former_phones',
           'Cookie': 'ig_cb=1; ig_did=69205DC3-D787-47E5-B250-1C4A7ADC3A05; csrftoken=HKmRQ2ZwuqCZjpMycM3xOVIjDUBo5HWd; mid=XoSg-AAEAAHRshuq4BlxladvlcbE; datr=HmBKXyPTk86RJpmkaUQ7eM5w; urlgen="{\"51.36.8.205\": 43766}:1kLnkz:ZHs58RZnu4USDtTqolZcEXDJp7s"; rur=ATN; ds_user_id=37466401585',
           'DNT': '1'
           }

cookies = {'sessionid': sessionId}
data = ''
url = 'https://www.instagram.com/accounts/access_tool/former_bio_texts?__a=1'
response = requests.request("GET", url, data=data, headers=headers , cookies=cookies)
info = json.loads(response.text)
print(green_color +"الكتابات السابقة في الصفحة الشخصيه منذ انشاء الحساب : "+str(info["data"]))



print('\n----------------------------')

headers = {'Host': 'www.instagram.com',
           'Content-Type': 'application/json; charset=utf-8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept': '*/*',
           'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
           'Connection': 'close',
           'X-IG-App-ID': '936619743392459',
           'X-Requested-With': 'XMLHttpRequest',
           'X-IG-WWW-Claim': 'hmac.AR0uQ3YRnOII5ROjBT7pKkMy1bjATWrSkfZCgwbaUBjNv-rw',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
           'Referer': 'https://www.instagram.com/accounts/access_tool/former_phones',
           'Cookie': 'ig_cb=1; ig_did=69205DC3-D787-47E5-B250-1C4A7ADC3A05; csrftoken=HKmRQ2ZwuqCZjpMycM3xOVIjDUBo5HWd; mid=XoSg-AAEAAHRshuq4BlxladvlcbE; datr=HmBKXyPTk86RJpmkaUQ7eM5w; urlgen="{\"51.36.8.205\": 43766}:1kLnkz:ZHs58RZnu4USDtTqolZcEXDJp7s"; rur=ATN; ds_user_id=37466401585',
           'DNT': '1'
           }

cookies = {'sessionid': sessionId}
data = ''
url = 'https://www.instagram.com/accounts/access_tool/search_history?__a=1'
response = requests.request("GET", url, data=data, headers=headers , cookies=cookies)
info = json.loads(response.text)
print(green_color +"سجل البحث منذ انشاء الحساب : "+str(info["data"]))

print('\n----------------------------')

headers = {'Host': 'www.instagram.com',
           'Content-Type': 'application/json; charset=utf-8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept': '*/*',
           'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
           'Connection': 'close',
           'X-IG-App-ID': '936619743392459',
           'X-Requested-With': 'XMLHttpRequest',
           'X-IG-WWW-Claim': 'hmac.AR0uQ3YRnOII5ROjBT7pKkMy1bjATWrSkfZCgwbaUBjNv-rw',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
           'Referer': 'https://www.instagram.com/accounts/access_tool/former_phones',
           'Cookie': 'ig_cb=1; ig_did=69205DC3-D787-47E5-B250-1C4A7ADC3A05; csrftoken=HKmRQ2ZwuqCZjpMycM3xOVIjDUBo5HWd; mid=XoSg-AAEAAHRshuq4BlxladvlcbE; datr=HmBKXyPTk86RJpmkaUQ7eM5w; urlgen="{\"51.36.8.205\": 43766}:1kLnkz:ZHs58RZnu4USDtTqolZcEXDJp7s"; rur=ATN; ds_user_id=37466401585',
           'DNT': '1'
           }

cookies = {'sessionid': sessionId}
data = ''
url = 'https://www.instagram.com/download/request/?__a=1'
response = requests.request("GET", url, data=data, headers=headers , cookies=cookies)
info = json.loads(response.text)
print(green_color +"الاميل الموثق حاليا هو  : "+str(info["email_hint"]))
