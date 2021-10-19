#!usr/bin/python
#Author: KANG-NEWBIE
'''
Jangan Nakalin Aku kak, Aku masih smp
Udah opensource jangan di recode dong bangsad!
'''
from fbchat import Client
from fbchat.models import *
from os import system
import time
g=('\033[1;32m')
c=('\033[1;36m')
w=('\033[1;37m')
r=('\033[1;31m')

Q=open('q.txt','r').readlines()
A=open('a.txt','r').readlines()
QA={}
for q,a in zip(Q,A):
	QA[q.replace('\n','').lower()]=a.replace('\n','')


class Main_Client(Client):
	QA=QA
	bool=False
	def onMessage(self,author_id,message_object,thread_id=None,thread_type=ThreadType.USER,**kwargs):
		self.markAsRead(author_id)
		print(message_object)
		if message_object.text==None and len(message_object.attachments)>0:
			self.send(Message(text='''bot tidak mengerti pesan yang berupa gambar'''),thread_id=thread_id,thread_type=thread_type)
		else:
			self.msg=message_object.text
			self.msg=self.msg.lower()
			print(self.msg)

		if author_id != self.uid:
			if 'tgl berapa sekarang' in self.msg:
				Main_Client.bool=True
				t=time.ctime()
				self.send(Message(text=t),thread_id=thread_id,thread_type=thread_type)
			elif self.msg in Main_Client.QA.keys():
				getans=Main_Client.QA.get(self.msg)
				self.messge_send=self.send(Message(text=getans),thread_id=thread_id,thread_type=thread_type)
				Main_Client.bool=True
			else:
				Main_Client.bool=True
				qus=open('q.txt','r').read()
				res='bot tidak mengerti apa yang kamu ketik, dibawah ini adalah kata yang dapat bot mengerti:\n{}'.format(qus)
				self.messge_send=self.send(Message(text=res),thread_id=thread_id,thread_type=thread_type)
		self.markAsDelivered(author_id,self.messge_send)

system('clear')
print("""%s
 BOT CHAT%s
 ,_     _‚
 |\\\___//|	%sAuthor: KANG-NEWBIE%s
 |=6   6=|	%sContact: https://t.me/kang_nuubi%s
 \=._Y_.=/	%sGithub: https://github.com/KANG-NEWBIE%s
  )  `  (    ,	%sTEAM: CRABS (t.me/CRABS_ID)%s
 /       \  ((
 |       |   ))
/| |   | |\_//
\| |._.| |/-`
 '"'   '"'
"""%(c,r,g,r,g,r,g,r,g,r))
try:
	email=input('%semail or username:%s '%(g,w))
	passs=input('%sPassword:%s '%(g,w))
	client=Main_Client(email,passs)
	client.listen()
except:
	print("%s[!] ERROR: LOGIN GAGAL, CHECK EMAIL ATAU PASSWORD KAMU\n"%(r))
