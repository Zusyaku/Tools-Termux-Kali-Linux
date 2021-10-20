#!/usr/bin/python3

# Mau Ngapain Bro, Tinggal Pake Aja
# Gak Usah Rikod Anjim

red = '\x1b[1;31m'
yellow = '\x1b[1;33m'
green = '\x1b[32m'
blue = '\x1b[1;34m'
purple = '\x1b[1;95m'
cyan = '\x1b[1;36m'
black = '\x1b[1;30m'
white = '\x1b[1;37m'
bl = '\x1b[101m'
sih = '\033[0m'

import os
import sys
import time
import bs4
from time import sleep
from bs4 import BeautifulSoup

try:
    import requests
except ImportError:
    print(f"\n {white}[{red}!{white}] Not install module requests {red}!")
    print(f"    {white}Ketik {red}: {yellow}pip install requests \n")
    sys.exit()

clear = lambda: os.system('clear')

class MainGoogle:

	def __init__(self):
		self.rek = requests.Session()
		self.Main()

	def Main(self):
		try:
			__import__("os").system("clear")
			print(f'''\n	  {blue}#HH||                   {green}#|\n	 {blue}##      {red}#H|   {yellow}#H|   {blue}#HH| {green}#|   {red}#H|\n	 {blue}## H|| {red}## H| {yellow}## H| {blue}## H| {green}#|  {red}##HH|\n	 {blue}##  || {red}## H| {yellow}## H|  {blue}#HH| {green}#|  {red}##\n	 {blue} #HH||  {red}#H|   {yellow}#H|     {blue}H| {green}#H|  {red}#HH|\n                    	     {blue}##H|            \n\n         {yellow}*{white}{green}_--={white}[ {white}{bl} Creator : Kingtebe {sih} {white}]{green}=--_{yellow}*\n\n''')

			search = input(f" {green}[{white}+{green}] {white}Search {red}: {white}")
			self.url = f"https://www.google.com/search?&q={search}"
			sia = self.rek.get(self.url)
			proses = BeautifulSoup(sia.text,"html.parser")
			exnx = proses.find("div",class_="BNeawe").text
			print(f' {green}[{white}+{green}] {white}Result {red}: {green}',exnx)
		except(KeyboardInterrupt,EOFError):sys.exit()
		self.back()

	def back(self):
		ip=input(f"\n {green}[{white}?{green}] {white}Gunakan lagi ? \n {green}[{white}y{green}/{white}n{green}]\n {green}•{white}> ")
		if ip == 'y':
			self.Main()
		elif ip == 'n':
			sys.exit(f'\n {red}[+] {white}Sampai Jumpa Lagi, Semoga Tools Nya Bermanfaat ... \n')


if __name__=='__main__':
	MainGoogle()
