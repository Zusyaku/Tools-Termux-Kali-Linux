import requests, os, time
os.system('clear')
i=int(0)
print(" INI BANNER!!"*3,"\n")
print("="*40)
try:
	while True:
		r=requests.get('https://api.getproxylist.com/proxy')
		print("ip      :",r.json()["ip"])
		print("port    :",r.json()["port"])
		print("protocol:",r.json()["protocol"])
		print("country :",r.json()["country"])
		print("="*40)
		i+=1
		if i == 10:
			break
		else:
			continue
except KeyError:
	print("[!] Error: you've exceeded your daily usage, wait 24 hours\n")
	exit()
except KeyboardInterrupt:
	print("[!] KeyboardInterrupt: Exiting...\n")
	time.sleep(1)
	exit()
