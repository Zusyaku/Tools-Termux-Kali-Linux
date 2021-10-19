#!/usr/bin/python
# coding=utf-8

''''Coded by : MR.K7C8NG?
read me up .good luck & i have added this script new secret to break facebook checkpoint
enjoy it .Jjk 
email: pashayogi52@gmail.com
Instagram : @pranata_pasha
githup: https://github.com/pashayogi
team: InDoNeSiA CYBER ErRoR SyStEm'''
import sys
import os
import time
import bs4
import requests
white = '\033[1;37m' # White 
prred = '\033[31m' # red
orange = '\033[33m' # orange
blue = '\033[34m' # blue
p  = '\033[35m' # purple
C  = '\033[36m' # cyan
green = ("\033[92m")
pryellow = ("\033[93m")
prLightPurple=("\033[94m")
prCyan=("\033[96m")
prgray = ("\033[97m")
prBlack=("\033[98m")

     #//class login & checker 
class shit3:
  def __init__(self):
      self.ree=requests.Session()
      self.mee = bs4.BeautifulSoup
      self.cadow=[]
      self.header={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36'}
      print (pryellow+'          []Login Facebok Account')
      print
      time.sleep(1)
      self._email = raw_input('[]Enter Email/Id: ')
      print
      time.sleep(1)
      self._passwr = raw_input('[]Enter Password: ')
      print
      time.sleep(1)
      self._url=('https://mbasic.facebook.com/')
      self.dem= self.mee(self.ree.get(self._url,headers=self.header).text,features='html.parser')
      for aa in self.dem('form'):
          if "login" in aa["action"]:
              self.action=aa['action']
              for xx in self.dem('input'):
                  if 'lsd' in xx['name']:
                      self.lsd=xx['value']
                  elif 'jazoest' in xx['name']:
                      self.jaz=xx['value']
                  elif 'li' in xx['name']:
                      self.li=xx['value']
                  elif 'm_ts' in xx['name']:
                      self.m_ts=xx['value']
                  elif 'login' in xx['name']:
                      self.submit=xx['value']
                      return self.login()
                      break          
  def login(self):
      self.html= {'lsd':self.lsd,'jazoest':self.jaz,'li':self.li,'m_ts':self.m_ts,'email':self._email,'pass':self._passwr,'login':self.submit}
      self._login= self.ree.post(self.action,headers=self.header,data=self.html).url
      if 'save-device' in self._login or 'm_sess' in self._login:
          print ('{[]}Login Successful')
          print '-'*43
          return self.mess()
          
      else:
          print (prred+'{[]}Login Faild')
          print pryellow+'-'*43
          exit()
  def mess(self):
      self.id = raw_input('[]Enter Target Id: ')
      print
      self.tar=self._url+self.id
      self.cad = self.mee(self.ree.get(self.tar,headers=self.header).text,features="html.parser")
      self._uu = ('https://mbasic.facebook.com')
      for x in self.cad.find_all('a',href=True):
          if '/messages/thr' in x['href']:
              self.mm=x['href']
              self.uhoh= self._uu+self.mm
              self.cade = self.mee(self.ree.get(self.uhoh,headers=self.header).text,features="html.parser")
              for x in self.cade('input'):
                  try:
                      if 'fb_dtsg' in x['name']:
                          self.fb1=x['value']
                      elif 'jazoest' in x['name']:
                          self.fb2=x['value']
                      elif 'send' in x['name']:
                          self.sub=x['value']
                      elif 'ids' in x['name']:
                          self.fb3=x['name']
                          self.cadow.append(self.fb3)
                          self.fb4=x['value']
                          self.cadow.append(self.fb4)
                          return self.go()
                          break
                  except:pass
  def go(self):
      time.sleep(0.2)
      print
      self.cc = open(raw_input('[]Enter Wordlist File: ')).read().splitlines()
      
      try:
          for x in self.cc:
              self.snd(x)
           
      except Exception as g:
          print ('[] This Persion Is Not Ur Friends')
          return self.mess()
  def snd(self,msgs):
      print ('[]Sending: '+msgs+' to '+self.id)
      self.act=('/messages/send/?icm=1')
      self.html2= {'fb_dtsg':self.fb1,'jazoest':self.fb2,'body':msgs,'send':self.sub,self.cadow[0]:self.cadow[1]}
      self._lo= self.ree.post(self._uu+self.act,headers=self.header,data=self.html2).url
      if 'send_success' in self._lo:
          print ('[()]Message sended')
         
      else:
          print (prred+'[]Sending Message Error')
          exit()