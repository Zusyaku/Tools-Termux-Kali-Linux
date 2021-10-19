from requests import get,post
from misc.headerz import headerz as hdz
import re,time,os


def cookie():
	user = []
	for i in os.listdir("."):
		if ".txt" in i:
			user.append(i)
	if len(user) != 0:
		print("Select User:")
		for i in range(len(user)):
			print(f"{lb}{i+1}.{lx} {user[i].replace('.txt','')}")
		u = int(input("User index: ")) - 1
		hds = open(user[u],'r').read()
		hdr = hdz()
		hdx = hdr.parser(hds)
		kuki = hdr.cookie_builder(hdx["cookie"])
		return {"Cookie":kuki}
	else:
		print("No user available.\nTutorial to add user visit https://karjokpangesty.blogspot.com")
		return None

def get_msg_list(url):
	urls = [url]
	msgs = []
	print("Getting message lists..")
	for i in range(5):
		r = get(urls[i],cookies=kuki).text
		msg = re.findall(r'\"(\/messages\/read\/\?.*?)\"\>(.*?)\<',r)
		for i in msg:
			if i not in msgs:
				msgs.append(i)
			print(f"\r{len(msgs)} messages collected..",end="",flush=True)
			time.sleep(0.1)
	#	msgs = msgs + [*msg]
		try:
			older_msg = re.search(r'\<a href\=\"(\/messages\/\?pageNum.*?see\_older\_newer.*?)\"',r).group(1)
		except:
			break
		older = "https://mbasic.facebook.com"+older_msg.replace("&amp;","&")
		urls.append(older)
			
		time.sleep(5)
	return msgs
	
def msg_deletor(url):
	r = get("https://mbasic.facebook.com"+url,cookies=kuki).text
	#print(r)
	try:
		f = re.search(r'\<form\ method\=\"post\"\ action\=\"(\/messages\/action\_redirect\?tid\=.*?)\".*?\"\>.*?</form\>',r)
		form = f.group()
		url_post = f.group(1)
		hidden = re.findall(r'type\=\"hidden\"\ name\=\"(.*?)\"\ value\=\"(.*?)\"',form)
		data = {"delete":"Hapus"}
		for i in hidden:
			data[i[0]] = i[1]
		x = post("https://mbasic.facebook.com"+url_post.replace("&amp;","&"),data=data,cookies=kuki).text
		del_url = re.search(r'href\=\"(\/messages\/action\/\?mm\_action.*?)\" class.*?Hapus',x).group(1)
		get("https://mbasic.facebook.com"+del_url.replace("&amp;","&"),cookies=kuki)
		print("    *deleted.")
	except:
		print(f"    {lr}*error. passed.{lx}")
def main():
	msgs = get_msg_list("https://mbasic.facebook.com/messages/?ref_component=mbasic_home_header&ref_page=%2Fwap%2Fhome.php&refid=8")
	print('\n')
	for i in range(len(msgs)):
		print(f"{lb}{i+1}.{lx} {msgs[i][1]}")
	selected = int(input(f"\nNumber 1-{len(msgs)} {lr}wich don't want to delete{lx}: ")) - 1
	banner()
	print("program is running..")
	print(f"deleting all messages in list except {msgs[selected][1]}..")
	msgs.pop(selected)
	for i  in range(len(msgs)):
		print(f"{i+1}. deleting {msgs[i][1]}'s message..")
		msg_deletor(msgs[i][0])
		for i in range(10):
			print(f"\r    *delay please wait {9-i}..",end="",flush=True)
			time.sleep(1)
		print('\n')

def banner():
	os.system('clear')
	print(f"""{lb}
	################################
	# {lx}Facebook Old Messages Eraser {lb}#
	################################
\033[90mTutorial at https://karjokpangesty.blogspot.com\033[0m""")
	print('\n')
if __name__=='__main__':
	lx = "\033[0m"
	lr = "\033[91m"
	lg = "\033[92m"
	ly = "\033[93m"
	lb = "\033[94m"
	banner()
	kuki = cookie()
	if kuki:
		banner()
		main()
	
