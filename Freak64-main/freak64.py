#!/usr/bin/python
#Coded by Anubhav Kashyap !
#don't use my code with giving me credit
#if you use without giving me credit then you won't became a programmer !
import base64



print("\033[92m _______  _______  _______  _______  _         ______    ___   ")
print("\033[92m(  ____ \(  ____ )(  ____ \(  ___  )| \    /\ / ____ \  /   )  ")
print("\033[92m| (    \/| (    )|| (    \/| (   ) ||  \  / /( (    \/ / /) |  ")
print("\033[92m| (__    | (____)|| (__    | (___) ||  (_/ / | (____  / (_) (_ ")
print("\033[92m|  __)   |     __)|  __)   |  ___  ||   _ (  |  ___ \(____   _)")
print("\033[92m| (      | (\ (   | (      | (   ) ||  ( \ \ | (   ) )    ) (  ")
print("\033[92m| )      | ) \ \__| (____/\| )   ( ||  /  \ \( (___) )    | |  ")
print("\033[92m|/       |/   \__/(_______/|/     \||_/    \/ \_____/     (_)  ")

print("\033[93m--------------------------------------------------------------")
print("Coder: Anubhav Kashyap !")
print("Github: github.com/anubhavanonymous")
print("Instagram: instagram.com/anubhavanonymous")

def Decode():
    test= input("\033[95mEnter Base64 >> ")
    data_encoded = base64.b64decode(test)
    print("\033[94mDecoding ....")
    print("\n")
    print(data_encoded.decode())
    print("\n")
    input("\033[37mPress Enter to exit..")

def Encode():
    test = input("\033[95mEnter text for Encoding >> ")
    data = base64.b64encode(test.encode())
    print("\033[94mEncoding....")
    print("\n")
    print(data.decode())
    print("\n")
    input("\033[37mPress Enter to exit...")

print("\033[93m-----------------------------------------------------------")
choice = input("\033[34m Enter Option !\n \033[92m[1] Encode Base64\n \033[36m[2] Decode Base64\n")

if choice == "2":
    Decode()
if choice == "1":
    Encode()
else:
    print("\033[31mExiting Freak64 !")




