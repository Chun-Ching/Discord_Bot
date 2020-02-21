import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

bot.run('Njc5NjA3NzQ2NTM0MTc4ODE4.Xkz0SQ.j-8rIAlCsGLTRlhKELXSj7t3z2U')