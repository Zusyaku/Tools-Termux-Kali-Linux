import requests as rek
import json,os,sys

## Logo/Tampilan
logo = """
        * Spam•Call *
|=========================================|
| {×} Creator : Bayu Riski                |
| {×} Youtube : Pejuang kentang           |
| {×} contac  : 085731184377              |
«~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~»\n"""

os.system('clear')
print(logo)
## Menginput No Target
print("gunakan 08")
target = input(" Target Call : ")

os.system('php login.php')
## Web Api Spam Call
api_url = "https://www.nutriclub.co.id/otp/?phone=0"+target+"&old_phone=0"+target

headers = {
"Host": "www.nutriclub.co.id",
"content-length": "0","accept":
"application/json, text/javascript, */*; q=0.01",
"x-requested-with": "XMLHttpRequest",
"save-data": "on",
"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1853) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
"origin": "https://www.nutriclub.co.id",
"sec-fetch-site": "same-origin",
"sec-fetch-mode": "cors",
"sec-fetch-dest": "empty","referer": "https://www.nutriclub.co.id/account/register",
}

## Merespon dari api_url ke bentuk .text
respon = rek.post(api_url,headers).text
## Status yg suudah di respon, menjadi "StatusMessage"
status = json.loads(respon)["StatusMessage"]
if status == "Request misscall berhasil":
     print("\n {✓} Call to "+ target +" Berhasil \n")
else:
     print("\n {×} Spam sudah dilakukan 3x » Gagal \n")
