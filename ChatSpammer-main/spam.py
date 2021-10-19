import keyboard
from time import sleep
a = input('enter no of msgs: ')
msg = input('enter message: ')
print('10 secs to place cursor')
for i in range(10,0,-1):
    print(i)
    sleep(1)
for l in range(int(a)):
    keyboard.write(msg)
    keyboard.press_and_release('Ctrl+Enter')
    sleep(0.5)
print('done')