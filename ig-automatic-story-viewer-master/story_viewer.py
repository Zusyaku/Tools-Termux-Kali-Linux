from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


usrnames = ['b31ngd3v']  # Account on which You want to send views

chrome_options = Options()
chrome_options.add_argument(
    '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
browser = webdriver.Chrome(options=chrome_options)

usrname = ['USERNAME1', 'USERNAME2', 'USERNAME3', 'USERNAME4', 'USERNAME5']  # Enter your usernames here
password = 'PASSWORD'  # Enter your password here

for username in usrname:
    browser.get('https://www.instagram.com/accounts/login/')

    time.sleep(2)

    usrname_bar = browser.find_element_by_name('username')  # Find the username bar
    passwrd_bar = browser.find_element_by_name('password')  # Find the password bar

    usrname_bar.send_keys(username)
    passwrd_bar.send_keys(password + Keys.ENTER)

    time.sleep(11)

    for usernames in usrnames:

        browser.get(f'https://www.instagram.com/{usernames}')

        time.sleep(5)

        story_view_btn = browser.find_element_by_class_name('_2dbep')

        story_view_btn.click()

        time.sleep(15)

    browser.delete_all_cookies()

browser.quit()

print(f'''
Python Program by
      ___   ___ _      _         
     | _ \ / __(_)_ _ | |_  __ _ 
     |  _/ \__ \ | ' \| ' \/ _` |
     |_|   |___/_|_||_|_||_\__,_|

    Follow me on Instagram @b31ngdev 

    Github b31ngd3v
''')
