import discord, time, json, discord.ext, webbrowser, colorama, pynput, random, asyncio
from discord import *
from time import *
from json import *
from discord.ext import commands
from colorama import Fore, Style
from asyncio import *

with open ('config.json') as f:
    data = json.load(f)

client_prefix = '$' # Ya can change this

token = data['token']

client = commands.Bot(
description='Discord Self Bot', 
command_prefix= f'{client_prefix}',
self_bot=True
)
client.remove_command('help')

@client.event
async def on_connect():
    print()
    print(f'{Fore.WHITE}[ {Fore.YELLOW}? {Fore.WHITE}] {Fore.CYAN}Dank Memer Farmer made by "Destinity')
    print(f'{Fore.WHITE}[ {Fore.YELLOW}- {Fore.WHITE}] {Fore.CYAN}Join my discord server for help https://discord.gg/nc6Y6UR9rU')
    print(f'{Fore.WHITE}[ {Fore.YELLOW}! {Fore.WHITE}] {Fore.CYAN}Logged in as {client.user.name}#{client.user.discriminator}')
    print(f'{Fore.WHITE}[ {Fore.YELLOW}+ {Fore.WHITE}] {Fore.CYAN}Type {client_prefix}begin to start...' + Style.RESET_ALL)
    print()
    print(f'{Fore.WHITE}]{Fore.WHITE}========================={Fore.WHITE}[')
    print()

@client.command()
async def begin(ctx):
    print()
    print(f'{Fore.WHITE}]{Fore.WHITE}========================={Fore.WHITE}[')
    print()
    print(f'{Fore.WHITE}[ {Fore.CYAN}x {Fore.WHITE}] {Fore.GREEN}Farming Commands...')
    print()
    print(f'{Fore.WHITE}]{Fore.WHITE}========================={Fore.WHITE}[')
    print()

    while True:
        await ctx.send("wh")
        print(f'{Fore.WHITE}- {Fore.RED}Executed Command "owo hunt"')
        await asyncio.sleep(30)
        await ctx.send("wb")
        print(f'{Fore.WHITE}- {Fore.RED}Executed Command "owo battle"')
        await asyncio.sleep(15)
        await ctx.send("w sacrifice c")
        print(f'{Fore.WHITE}- {Fore.RED}Executed Command "owo sacrifice common"')
        await asyncio.sleep(20)
        await ctx.send("w sacrifice uc")
        print(f'{Fore.WHITE}- {Fore.RED}Executed Command "owo sacrifice uncommon"')
        await asyncio.sleep(20)
        await ctx.send("w sacrifice r")
        print(f'{Fore.WHITE}- {Fore.RED}Executed Command "owo sacrifice rare"')
        await asyncio.sleep(20)
        await ctx.send("w wc all")
        print(f'{Fore.WHITE}- {Fore.RED}Executed Command "owo weaponcrates all"')
        await asyncio.sleep(10)
        ctx.send("w lb all")
        await print(f'{Fore.WHITE}- {Fore.RED}Executed Command "owo lootboxes all"')
        await asyncio.sleep(10)

client.run(token, bot=False)
