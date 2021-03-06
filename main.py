import discord
import tracemalloc
from discord.ext.commands import AutoShardedBot
from secrect import Secret
from cogs.fuct import load_config
import json, os, sys, asyncio, time

config = load_config()
tracemalloc.start()

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
# _error_ = getattr(error, 'original', error)
# #     if isinstance(error, commands.MissingPermissions):
# #         perms = "\n".join(error.missing_perms)
# #         return await ctx.send(f"Você precisa da permissão `{perms}` para usar este comando")

# #     # outros erros vao aparecer no terminal
# traceback.print_exception(type(_error_), _error_, _error_.__traceback__, file=sys.stderr)

modulos = ['cogs.comandos', "cogs.status", "cogs.erros", "cogs.myreactions"]

if __name__ == "__main__":
    for modulo in modulos:
        client.load_extension(modulo)


client.run(Secret)
