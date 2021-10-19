from colorama import Fore, init
import json
import os
import discord
init(convert=True)


from discord.ext import (
    commands,
    tasks
)



client = discord.Client()
client = commands.Bot(
    command_prefix="!",
    self_bot=True
)
client.remove_command('help')

with open('config.json') as f:
    config = json.load(f)
    
token = config.get("token")
os.system('cls')

print(f"{Fore.WHITE}[ {Fore.CYAN}§ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Discord token Scraper made by {Fore.WHITE}LnX & Rezizt{Fore.LIGHTBLACK_EX} | Licensed under {Fore.WHITE}MIT {Fore.LIGHTBLACK_EX}License")
print(f"{Fore.WHITE}[ {Fore.CYAN}§ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}You can follow us on Github: {Fore.GREEN}https://github.com/lnxcz {Fore.LIGHTBLACK_EX}& {Fore.GREEN}https://github.com/6uv {Fore.RESET}") 

print(f"\n{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Bot on stanby...")
print(f"{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Write {Fore.WHITE}!scrape <number of messages>{Fore.LIGHTBLACK_EX} to log tokens\n")

def Init():
    if config.get('token') == "token-here":
        os.system('cls')
        print(f"\n\n{Fore.WHITE}[ {Fore.RED}E {Fore.WHITE}] {Fore.LIGHTBLACK_EX}You didnt put your token in the config.json file\n\n"+Fore.RESET)
        exit()
    else:
        token = config.get('token')
        try:
            client.run(token, bot=False, reconnect=True)
            os.system(f'Discord token scraper')
        except discord.errors.LoginFailure:
            print(f"\n\n{Fore.WHITE}[ {Fore.RED}E {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Token is invalid\n\n"+Fore.RESET)
            exit()


@client.command()
async def scrape(ctx, amount: int):
    f = open(f"scraped/{ctx.message.channel}.txt","w+", encoding="UTF-8")
    total = amount
    print(f"{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Scraping {Fore.WHITE}{amount}!")
    async for message in ctx.message.channel.history(limit=amount):
        attachments = [attachment.url for attachment in message.attachments if message.attachments]
        try:
            if 'mfa' in message.content:
                f.write(f"{message.content}\n")
                print(f"{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Scraped token")
            elif 'Nz' in message.content:
                f.write(f"{message.content}\n")
                print(f"{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Scraped token")
            elif 'NT' in message.content:
                f.write(f"{message.content}\n")
                print(f"{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Scraped token")
            elif 'Nj' in message.content:
                f.write(f"{message.content}\n")
                print(f"{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Scraped token")
            else:
                print(f"{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Not a token")
        except Exception as e:
            print(f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Cannot scrape tokens from {Fore.WHITE}{message.author}")
            print(f"{Fore.WHITE}[ {Fore.RED}E {Fore.WHITE}] {Fore.LIGHTBLACK_EX} {Fore.WHITE}{e}")
            total = total - 1        
    
    print(f"{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Succesfully scraped {Fore.WHITE}{total} {Fore.LIGHTBLACK_EX}tokens!\n\n{Fore.WHITE}")


@client.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, discord.errors.Forbidden):
        print(f"{Fore.WHITE}[ {Fore.RED}E {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Discord error: {error}"+Fore.RESET)    
    else:
        print(f"{Fore.WHITE}[ {Fore.RED}E {Fore.WHITE}] {Fore.LIGHTBLACK_EX}{error_str}"+Fore.RESET)

Init()
