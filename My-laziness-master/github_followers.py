#Author:karim shoair (D4Vinci)
#Extract the famous followers for any github user
import mechanicalsoup as ms
from tqdm import tqdm
import readline,sys
browser = ms.StatefulBrowser()
url = input("Profile link : ")+"?tab=followers"
check_str = "That’s it. You’ve reached the end of"
G,W,B = '\033[92m','\x1b[37m','\033[94m'
end   = '\033[0m'

def grab_users(grab):
	tags = grab.soup.findAll("a",{"class":"d-inline-block no-underline mb-1"})
	profiles = []
	for i in tags:
		try:
			a = i.attrs
		except:
			continue
		profiles.append("http://git-awards.com/users"+a['href'])
	return profiles

def loop_over_pages(link):
	profiles = []
	print("[+] Checked pages ",end="")
	for i in range(1,1000):
		page = browser.open(link+"&page="+str(i))
		if check_str in page.content.decode():
			break
		profiles.extend( grab_users(page) )
		sys.stdout.write(str(i)+" ")
		sys.stdout.flush()
	return profiles

print("[+] Grabing users...")
follow = loop_over_pages(url)
print("\n[+] Fetched "+str(len(follow))+" follower(s)!" )
print("[+] Now searching who's have more than 400 stars at total...\n")

def grab_stars_total(profiles):
	 famous_people = {}
	 with tqdm(total=len(profiles)) as bar:
		 for person in profiles:
			 bar.update(1)
			 page = browser.open(person)
			 try:
				 stars = int(page.soup.findAll("tbody")[0].findAll("td")[-1].text)
			 except:
				 continue
			 if stars>400:
				 famous_people[person.split("/")[-1]]=stars
	 return famous_people

famous = grab_stars_total(follow)
print("[+] Found "+B+str(len(famous))+end+" famous followers and they are :" )
for user in famous.keys():
	print(G+"http://github.com/"+user+W+" | With stars => "+B+str(famous[user]))
print(end+"\n")
