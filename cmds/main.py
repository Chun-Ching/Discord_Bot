import discord
from discord.ext import commands
from Discord_Bot.core.classes import Cog_Extension
import json
import datetime

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Main(Cog_Extension):
    

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(F'{round(self.bot.latency*1000)} (ms)')

    @commands.command()
    async def hi(self, ctx):
        await ctx.send('Hi')

    @commands.command()
    async def em(self, ctx):
        embed=discord.Embed(title="About", url="https://www.youtube.com/", description="About the bot", color=0x008000, timestamp= datetime.datetime.now() )
    
        embed.set_author(name="Bang", url="https://www.youtube.com/", icon_url="https://lh3.googleusercontent.com/proxy/o6xboX7xH88oz-4EbgCyFP9L-gicOconPnPOtWdakYj0vVcQFQHv-K5-7JouPRL0IUlHIAuvH9hM")
        embed.set_thumbnail(url="https://lh3.googleusercontent.com/proxy/o6xboX7xH88oz-4EbgCyFP9L-gicOconPnPOtWdakYj0vVcQFQHv-K5-7JouPRL0IUlHIAuvH9hM")
        embed.add_field(name="1", value="11", inline=False)
        embed.add_field(name="2", value="22", inline=True)
        embed.add_field(name="3", value="33", inline=True)
        embed.add_field(name="4", value="44", inline=True)
        embed.set_footer(text="Bang")
        await ctx.send(embed=embed)

    @commands.command()
    async def said(self, ctx,*, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clean(self, ctx, num:int):
        await ctx.channel.purge(limit=num+1)
        

def setup(bot):
    bot.add_cog(Main(bot))    
