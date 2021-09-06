from cogs import reactions
import discord
from discord.ext import commands
from discord import emoji
from discord.guild import Guild


class myreactions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, messagens):
        if "mo gay" == messagens.content:
            await messagens.channel.send("iala mo noia kskksskskk")

        if messagens.content in ('q?', '?', 'que?', 'que ?'):
            msg = messagens
            await msg.add_reaction('🤔')

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        pass



def setup(bot):
    bot.add_cog(myreactions(bot))














# embed.set_footer(text="", icon_url="")