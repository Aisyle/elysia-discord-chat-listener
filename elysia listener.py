from colorama import Fore,Back,Style
from colorama import init
init()
import os
import time
import discord
import asyncio
import pyfiglet
from discord.ext import commands
from utils import *
import pyautogui

elysia_banner = pyfiglet.figlet_format('   ELYSIA LISTENER', font = 'slant')
print(Fore.LIGHTMAGENTA_EX,elysia_banner)

print(Fore.MAGENTA + 'WHAT IS BOT TOKEN ?')
token = input(' >')
os.system('cls')

print(Fore.LIGHTMAGENTA_EX,elysia_banner)



download1 = pyfiglet.figlet_format(' \ ', font = 'slant')
download2 = pyfiglet.figlet_format(' | ', font = 'slant')
download3 = pyfiglet.figlet_format(' / ', font = 'slant')
download4 = pyfiglet.figlet_format(' - ', font = 'slant')

n = 0

for i in (range(101)) :

    n = str(n)

    waiting = pyfiglet.figlet_format(' '+n , font = 'slant')

    print(waiting)

    print(download4)

    time.sleep(0.00001)

    os.system('cls')

    print(waiting)

    print(download1)

    time.sleep(0.00001)

    os.system('cls')

    print(waiting)

    print(download2)

    time.sleep(0.00001)

    os.system('cls')

    print(waiting)

    print(download3)
        
    time.sleep(0.00001)

    os.system('cls')

    n = int(n)

    n += 1 

client = discord.Client()

a = 0

@client.event

async def on_ready () :

    print(Fore.LIGHTMAGENTA_EX,elysia_banner)
    print(Fore.MAGENTA + f'Logged as = {client.user} ( id = {client.user.id})')
    time.sleep(3)
    os.system('cls')

    await client.change_presence (status = discord.Status.invisible)

    print(Fore.LIGHTMAGENTA_EX,elysia_banner)
    print('LISTENINNG SERVERS :')
    print('')

    for guild in client.guilds :

        print ('' ,guild.name)

    time.sleep(5)
    os.system('cls')

    print(Fore.LIGHTMAGENTA_EX,elysia_banner)

    @client.event
    async def on_message (message) : 
        
        global a

        if a == 20 :

            os.system('cls')

            print(Fore.LIGHTMAGENTA_EX,elysia_banner)

            a = 0

        print(message.guild.name ,'->',message.channel ,'->',message.author.name ,'->', message.content)

        a += 1

client.run(token)