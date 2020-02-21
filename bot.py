import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(680334124392644608)
    await channel.send(F'{member} join!')


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(680334244311990279)
    await channel.send(F'{member} leave!')   

bot.run('Njc5NjA3NzQ2NTM0MTc4ODE4.Xk-XUw.dMEiSlkWaJ_ZLKD94U8KTXkQoGk')