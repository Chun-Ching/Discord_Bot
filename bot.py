import discord
from discord.ext import commands
import json
import random
import os
from _ast import For

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['Welcome_channel']))
    await channel.send(F'{member} join!')


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['Leave_channel']))
    await channel.send(F'{member} leave!') 







bot.run(jdata['TOKEN'])