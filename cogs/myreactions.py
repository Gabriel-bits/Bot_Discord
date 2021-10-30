from discord import guild
from discord import client
from discord.client import Client
from discord.ext.commands import bot
from discord.ext.commands.converter import EmojiConverter
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
        msg = messagens
        if "mo gay" == messagens.content:
            await messagens.channel.send("iala mo noia kskksskskk")

        if messagens.content in ('q?', '?', 'que?', 'que ?'):
            __emoji = Client.get_emoji(self.bot ,725831269329404094)
            # await msg.add_reaction('🤔')
            await msg.add_reaction(__emoji)

        if messagens.content in ('lixo', 'trash'):
            await msg.add_reaction("\U0001F5D1")


    # @commands.Cog.listener()
    # async def on_reaction_add(self, reaction, user):
    #     # print(reaction.emoji)
    #     # pass

def setup(bot):
    bot.add_cog(myreactions(bot))














# embed.set_footer(text="", icon_url="")