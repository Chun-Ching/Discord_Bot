import discord
from discord.ext import commands
from Discord_Bot.core.classes import Cog_Extension
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata['Welcome_channel']))
        await channel.send(F'{member} join!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata['Leave_channel']))
        await channel.send(F'{member} leave!')

    @commands.Cog.listener()
    async def on_message(self, msg):
        keyword = ['帥哥', '很帥']
        if msg.content in keyword:
            await msg.channel.send('真的帥!')

def setup(bot):
    bot.add_cog(Event(bot)) 