import discord
from discord.ext import commands


class Escolha_do_prefix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command
    async def novoprefix(self, ctx, *, newpref= None):
        await ctx.send("comando ainda em desenvolvimento")
        # if newpref is None:
        #     await ctx.send('?novoprefix + ')
        #     return

        # else:
        #     await ctx.send('Seu prefixo foi redefinido para'+ prefixov1)
        #     prefixo = newpref

def setup(bot):
    bot.add_cog(Escolha_do_prefix(bot))
