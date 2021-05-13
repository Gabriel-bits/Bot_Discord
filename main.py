import discord
from cogs.fuct import*
from discord.ext.commands import AutoShardedBot, when_mentioned_or
from discord.ext.commands.errors import *
from discord.ext import tasks
from secrect import Secret
from cogs import comandos

import traceback
import multiprocessing
import json, os, sys, asyncio, time

config = load_config()

cor = config["cor"]
cor_alert = config["aler"]
Pref = config["prefix"]

client = discord.Client()
client = AutoShardedBot(command_prefix=Pref, case_insensitive=True)
client.remove_command('help')

@client.event
async def on_ready():
    print("Bot on")
    print(client.user.name)
    print(client.user.id)
    
    # game = discord.Game("pica na sua mina")
    # await client.change_presence(status=discord.Status.idle, activity=game)
    # await client.change_presence(activity=discord.Streaming(name=Pref+'help', url='https://www.twitch.tv/narutozini'))


# @client.listen("on_command_error")
# async def error_handler(ctx, error):
#     error = getattr(error, 'original', error)
#     cmd_name = ctx.message.content.split()[0]
#     if isinstance(error, discord.ext.commands.errors.CommandNotFound):
#         embed=discord.Embed(title=f"@{ctx.author.display_name} o comando `{cmd_name}` não existe.", color=cor_alert)
#         msg = await ctx.send(embed=embed)
#         return

# outros erros vao aparecer no terminal
#    traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

@client.listen("on_command_error")
async def error_handler(ctx, error):
    error = getattr(error, 'original', error)
    if isinstance(error, commands.MissingPermissions):
        perms = "\n".join(error.missing_perms)
        return await ctx.send(f"Você precisa da permissão `{perms}` para usar este comando")

    # outros erros vao aparecer no terminal
    traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

modulos = ['cogs.comandos', "cogs.status"]

if __name__ == "__main__":
    for modulo in modulos:
        client.load_extension(modulo)


client.run(Secret)
