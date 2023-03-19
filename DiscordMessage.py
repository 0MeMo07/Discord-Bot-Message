import discord
from pystyle import Colors, Colorate
import time
import os

os.system("cls")

def slow_input(prompt, delay=0.1):
    for char in prompt:
        print(char, end='', flush=True)
        time.sleep(delay)
    return input()

print(Colorate.Vertical(Colors.blue_to_purple,"""
░██████╗███╗░░░███╗░█████╗░██╗░░██╗███████╗
██╔════╝████╗░████║██╔══██╗██║░██╔╝██╔════╝
╚█████╗░██╔████╔██║███████║█████═╝░█████╗░░
░╚═══██╗██║╚██╔╝██║██╔══██║██╔═██╗░██╔══╝░░
██████╔╝██║░╚═╝░██║██║░░██║██║░╚██╗███████╗
╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝

"""))

BotToken = slow_input(Colorate.Vertical(Colors.blue_to_purple,"Bot Token:"))
channelid = int(slow_input(Colorate.Vertical(Colors.blue_to_purple,"channel id:")))
Message = slow_input(Colorate.Vertical(Colors.blue_to_purple,"Message:"))
print(Colorate.Vertical(Colors.red_to_purple,"====================================================================="))

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    guild = client.get_guild(channelid)
    members = guild.members
    message = f"{Message}"
    for member in members:
        try:
            await member.send(message)
        except:
            pass

client.run(f'{BotToken}')


