
import os,sys,time

def bersih():
    os.system("clear")

def menu():
    bersih()
    print "\033[31;1m"
    os.system("figlet MTI-Ddos")
    print "\033[37;1m          Tools Instaler Ddos"
    print "\033[31;1m================================================"
    print "\033[37;1m  Author : Panglima Jateng"
    print "  Team   : Mafia Teknologi Indonesia"
    print "  Kontak : +62 882-1235-2864"
    print "\033[31;1m================================================"
    print
    print "\033[37;1m           By Panglima Jateng"
    print "\033[31;1m================================================"
    print "\033[37;1m1). Ddos Wd"
    print "\033[31;1m================================================"
    print "\033[37;1m2). Ddos Lucita Luna"
    print "\033[31;1m================================================"
    print "\033[37;1m3). Ddos Attack"
    print "\033[31;1m================================================"
    print "\033[37;1m4). keluar"
    print "\033[31;1m================================================"
    print
    jateng = raw_input("pilih: ")
    if jateng =='1':
       print "\033[37;1ma). Install Script"
       print "b). Lihat Script"
       print "\033[31;1m======================="
       bot = raw_input("pilih: ")
       if bot =='a':
          os.system("git clone https://github.com/banghyuu/ddosWD")
          os.system("cd ddosWD")
          os.system("sh Ddos.sh")
       if bot =='b':
          print "\033[37;1mini bro scriptnya gunakan dengan bijak"
          print "\033[31;1m=========================================="
          print "\033[37;1m pkg update && pkg upgrade"
          print " pkg install git"
          print " pkg install toilet"
          print " pkg install figlet"
          print " pkg install python"
          print " pkg install python2"
          print " git clone https://github.com/banghyuu/ddosWD"
          print " cd ddosWD"
          print " sh Ddos.sh"
          print
    if jateng =='2':
       print "\033[37;1ma). Install Script"
       print "b). Lihat Script"
       print "\033[31;1m========================"
       eze = raw_input("pilih: ")
       if eze =='a':
          os.system("git clone https://github.com/zlucifer/lucita_ddos")
          os.system("cd lucita_ddos")
          os.system("python pukul.py")
       if eze =='b':
          print "\033[37;1mini bro scriptnya gunakan dengan bijak"
          print "\033[31;1m=============================================="
          print "\033[37;1m pkg update && pkg upgrade"
          print " pkg install git"
          print " pkg install python"
          print " git clone https://github.com/zlucifer/lucita_ddos"
          print " cd lucita_ddos"
          print " python pukul.py"
          print
    if jateng =='3':
       print "\033[37;1ma). Install Script"
       print "b). Lihat Script"
       print "\033[31;1m======================="
       cham = raw_input("pilih: ")
       if cham =='a':
          os.system("git clone https://github.com/MrVirusSpm-07/ddos-attack")
          os.system("cd ddos-attack")
          os.system("python attack-ddos.py")
       if cham =='b':
          print "\033[37;1mini bro scriptnya gunakan dengan bijak"
          print "\033[31;1m=============================================="
          print "\033[37;1m pkg update && pkg upgrade"
          print " pkg install git"
          print " pkg install python"
          print " pkg install figlet"
          print " git clone https://github.com/MrVirusSpm-07/ddos-attack"
          print " cd ddos-attack"
          print " python attack-ddos.py"
    if jateng =='4':
       print "\033[31;1m tanks udah make script saya"
       print
       time.sleep(2)
       os.system("exit")


menu()