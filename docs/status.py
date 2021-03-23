from discord.ext import commands, tasks
from discord.ext.commands import AutoShardedBot
import discord
import random
import datetime


class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.lista_games = ["Mine", "Bed Wars", "O lixo fora", "Dead Cells"]
        self.lista_assistir = []
        self.change_status.start()

    def cog_unload(self):
        self.change_status.cancel()

    @tasks.loop(minutes=10)
    async def change_status(self):
        await self.bot.wait_until_ready()
        await self.bot.change_presence(activity=discord.Game(name=random.choice(self.lista_games)))

def setup(bot):
    bot.add_cog(Status(bot))
