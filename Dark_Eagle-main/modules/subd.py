import requests
from requests import get
print("Starting Subdomain Enumeration")
print("ex - youtube.com")
print("")
domain = input("\033[95mEnter domain >>> ")
print("\n")
file = open('wordlist.txt','r')
content = file.read()

subdomains = content.splitlines()

for subdomain in subdomains:
	url1 = f"http://{subdomain}.{domain}"
	url2 = f"https://{subdomain}.{domain}"
	try:
		requests.get(url1)
		print(f"\033[94m   Discovered URL: {url1}")
		requests.get(url2)
		print(f"\033[94m   Discovered URL: {url2}")
	except requests.ConnectionError:
		pass
print("\n")
