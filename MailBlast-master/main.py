#!/usr/bin/python
import smtplib
import time
import os
import getpass
import sys

class bcolors:
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'


def bomb():
	os.system('clear')
	print bcolors.OKGREEN + '''
              
  __  __       _ _ ____  _           _   
 |  \/  |     (_) |  _ \| |         | |  
 | \  / | __ _ _| | |_) | | __ _ ___| |_ 
 | |\/| |/ _` | | |  _ <| |/ _` / __| __|
 | |  | | (_| | | | |_) | | (_| \__ \ |_ 
 |_|  |_|\__,_|_|_|____/|_|\__,_|___/\__|

                                     Author: Anubhav Kashyap ''' + bcolors.ENDC


os.system('clear')
try:
	file1 = open('Banner.txt', 'r')
	print(' ')
	print bcolors.OKGREEN + file1.read() + bcolors.ENDC
	file1.close()
except IOError:
	print('Banner File not found')

#Input
print(bcolors.WARNING + '''
Choose a Mail Service:
1) Gmail
2) Yahoo
''' + bcolors.ENDC + '--------------------------------------------------------------')
try:
	server = raw_input(bcolors.OKGREEN + 'Mail Server: ' + bcolors.ENDC)
	user = raw_input(bcolors.OKGREEN + 'Your Email: ' + bcolors.ENDC)
	pwd = getpass.getpass(bcolors.OKGREEN + 'Password: ' + bcolors.ENDC)
	to = raw_input(bcolors.OKGREEN + 'To: ' + bcolors.ENDC)
	subject = raw_input(bcolors.OKGREEN + 'Subject (Optional): ' + bcolors.ENDC)
	body = raw_input(bcolors.OKGREEN + 'Message: ' + bcolors.ENDC)
	nomes = input(bcolors.OKGREEN + 'Number of Emails to send: ' + bcolors.ENDC)
	no = 0
	message = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
except KeyboardInterrupt:
	print bcolors.FAIL + '\nCanceled' + bcolors.ENDC
	sys.exit()

#Gmail

if server == '1' or server == 'gmail' or server == 'Gmail':
	bomb()
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.ehlo()
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		print bcolors.FAIL + '''Your Username or Password is incorrect, please try again using the correct credentials
		Or you need to enable less secure apps
		On Gmail: https://myaccount.google.com/lesssecureapps ''' + bcolors.ENDC
		sys.exit()
	while no != nomes:
		try:
			server.sendmail(user, to, message)
			print bcolors.WARNING + 'Successfully sent ' + str(no+1) + ' emails' + bcolors.ENDC
			no += 1
			time.sleep(.8)
		except KeyboardInterrupt:
			print bcolors.FAIL + '\nCanceled' + bcolors.ENDC
			sys.exit()
		except:
			print "Failed to Send "
	server.close()
	
#Yahoo
elif server == '2' or server == 'Yahoo' or server == 'yahoo':
	server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
	bomb()
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		print bcolors.FAIL + '''Your Username or Password is incorrect, please try again using the correct credentials
		Or you need to enable less secure apps
		On Yahoo: https://login.yahoo.com/account/security?.scrumb=Tiby8TXUvJt#less-secure-apps
		''' + bcolors.ENDC
		sys.exit()
	while no != nomes:
		try:
			server.sendmail(user, to, message)
			print bcolors.WARNING + 'Successfully sent ' + str(no + 1) + ' emails' + bcolors.ENDC
			no += 1
			time.sleep(.8)
		except KeyboardInterrupt:
			print bcolors.FAIL + '\nCanceled' + bcolors.ENDC
			sys.exit()
		except:
			print "Failed to Send"
	server.close()
	

	
else:
	print 'It Works only with Gmail and  Yahoo !!'
	sys.exit()
