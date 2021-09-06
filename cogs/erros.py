import discord
from discord.ext import commands
from discord.ext.commands import*
from discord.ext.commands.errors import CommandNotFound
from cogs.fuct import load_config
import traceback
import json, os, sys


class Test(commands.Cog):
    def __init__(self, client):
        self.client = client
        config = load_config()

        self.cor = config["cor"]
        self.cor_alert = config["aler"]



    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):  
    
        cmd_name = ctx.message.content.split()[0]
        _error_ = getattr(error, 'original', error)
        
        if isinstance(error, CommandNotFound):
            embed=discord.Embed(title=f"@{ctx.author.display_name} o comando `{cmd_name}` não existe.", color=self.cor_alert)
            await ctx.send(embed=embed)

        if isinstance(error, commands.MissingPermissions):
            perms = "\n".join(error.missing_perms)
            return await ctx.send(f"Você precisa da permissão `{perms}` para usar este comando")

        # outros erros vao aparecer no terminal
        traceback.print_exception(type(_error_), _error_, _error_.__traceback__, file=sys.stderr)



    
def setup(client):
    client.add_cog(Test(client))
