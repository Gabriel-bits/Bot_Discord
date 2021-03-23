import discord 
from discord.ext import commands
from discord.ext.commands import AutoShardedBot
from discord.ext.commands import errors
import traceback
import asyncio


@client.listen("on_command_error")
async def error_handler(ctx, error):
    error = getattr(error, 'original', error)
    cmd_name = ctx.message.content.split()[0]
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):

        embed=discord.Embed(title=f"@{ctx.author.name} o comando `{cmd_name}` não existe.", color=cor_alert)
        msg = await ctx.send(embed=embed)
        return
    traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
