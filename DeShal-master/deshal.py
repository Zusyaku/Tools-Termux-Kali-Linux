#Python 3.7.X and Python 2.7.X
#Author: KANG-NEWBIE
from uncompyle6.main import decompile
import marshal,time,sys,os,marcode

def Py3():
	c=input("[*] decompile marshal python 3.7.X\n[?] File output: ")
	x=marshal.loads(marcode.py3)
	xx=decompile(3.7,x,sys.stdout)
	xxx="# Success decompile marshal python 3.7.X\n# At: "+time.ctime()+"\n# By KANG-NEWBIE\n"+xx.text
	with open(c+".py","w") as f:
		f.write(xxx)
	print("\n\n[result] Saved as \033[95m%s.py"%(c))

def Py2():
	c=raw_input("[*]decompile marshal python 2.7.X\n[?] File output: ")
	x=marshal.loads(marcode.py2)
	xx=decompile(2.7,x,sys.stdout)
	xxx="# Success decompile marshal python 2.7.X\n# At: "+time.ctime()+"\n# By KANG-NEWBIE\n"+xx.text
	with open(c+".py","w") as f:
		f.write(xxx)
	print("\n\n[result] Saved as \033[95m%s.py"%(c))

try:
	os.system('clear')
	print("""
		;;;;;;;;;;;;;;;;;;;;;
		; Decompile Marshal ;
		;   By KANG-NEWBIE  ;
		;;;;;;;;;;;;;;;;;;;;;
		""")
	if sys.version[0] in '3':
		Py3()
	elif sys.version[0] in '2':
		Py2()
except Exception as F:
	print("Err: %s"%(F))
