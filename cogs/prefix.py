import discord
from discord.ext import commands

prefixov1 = "?"

class Escolha_do_prefixs(commands.Cog):
    def self.client = client

    @commands.command
    async def novoprefix(self, ctx, *, newpref= None):
        if newpref is None:
            await ctx.send('?novoprefix + ')
            return
        else:
            await ctx.send('Seu prefixo foi redefinido para'+ prefixov1)
            prefixov1 = newpref

def setup(client):
    client.add_cog(Escolha_do_prefixs(client))
