import discord
from discord.ext import commands
from discord.ext.commands import AutoShardedBot, when_mentioned_or
from discord.ext.commands.errors import*
from discord.ext import tasks
from discord.ext.commands import*
import traceback
import multiprocessing
import json, os, sys, asyncio, time

    
client = AutoShardedBot("?", None)

class Test(AutoShardedBot.listen):
    def __init__(self, client):
        self.client = client
        self.client = AutoShardedBot("?", None)
    
    @client.listen(self, "on_command_error")
    async def error_handler(ctx, error):  
        error = getattr(error, 'original', error)
        cmd_name = ctx.message.content.split()[0]
        if isinstance(error, discord.ext.commands.errors.CommandNotFound):
            embed=discord.Embed(title=f"@{ctx.author.display_name} o comando `{cmd_name}` não existe.", color=cor_alert)
            msg = await ctx.send(embed=embed)

    
def setup(client):
    client.add_cog(Test(client))
