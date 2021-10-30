from discord.ext.commands.converter import EmojiConverter
from discord.guild import Guild
from discord.member import Member
from cogs import reactions
from discord import player, user
import discord
from discord import message
from discord import client
from discord import utils
from discord.ext import commands
from discord.ext.commands import Bot, bot
from discord.message import Message
from discord.ext.commands import*
from cogs.fuct import *
import asyncio

config = load_config()

cor = config["cor"]
cor_alert = config["aler"]
Pref = config["prefix"]

# ▀

async def drawingcool_rounds(rounds, jogadores, ctx, bot):
    for round in range(rounds):
        embed=discord.Embed(description=f"Round ► **`{round+ 1}`**", color=cor)
        
        await ctx.send(embed=embed)
        
        for jogador in jogadores:
            jogador = int(jogador)
            
            # message sendo enviada para DM:

            embed_dm=discord.Embed(description=f"Sua vez amigo", color=cor)
            dm_jogador = await discord.Client.fetch_user(bot, jogador)
            await dm_jogador.send(embed=embed_dm)
            embed=discord.Embed(description=f"Esperando o jogado <@{jogador}> aceitar ou enviar a imagem", color=cor)
            await ctx.send(embed=embed)

            # verificação:

            emoji_V = Bot.get_emoji(bot, 887085594696622101)
            emoji_X = Bot.get_emoji(bot, 887088799086149632)

            embed=discord.Embed(description=f"deseja desenhar ?\rcaso tenha duvida de como desenhar e como mandar digite `{Pref}dw.tutor`", color=cor)
            msg = await dm_jogador.send(embed=embed)
            print(f"channel {msg.channel.id}")
            
            await msg.add_reaction(emoji_X)
            await msg.add_reaction(emoji_V)

            def check(reaction, user):
                # print(reaction.message.author.id)
                # print(dm_jogador.id)
                print(1)
                if user.name == dm_jogador.name:
                    print(2)
                    return reaction.message.channel.id == msg.channel.id and reaction.emoji == emoji_V , reaction.emoji == emoji_X

            try:
                reaction, user = await Bot.wait_for(bot, 'reaction_add', timeout=60.0, check=check)
                print(2)
            except asyncio.TimeoutError:
                await msg.delete()
                return

            Tema = "biscoito"
            
            # Verificação do reação

            if reaction.emoji == emoji_V:
                await dm_jogador.send(embed=embed_rapida(f"desenhe {Tema}"))
                await dm_jogador.send(embed=embed_rapida("Pode começar a desenhar... termine rapido ou sua vez sera pulada"))
                await ctx.send("Esta desenhado ...")
                await msg.delete()

                # envio do desenho

                id_channel = msg.channel.id

                def check(m):
                    return m.channel.id == id_channel
                desenho = await Bot.wait_for(bot, 'message', check=check)
                imag = desenho.attachments[0]
                await ctx.send(f"{imag}")

            elif reaction.emoji == emoji_X:
                await ctx.send(f" <@{jogador}> Pulou a vez ...")
                await msg.delete()

            # resposta

            p1 = 'biscoito'
            def check(message):
                if message.content == p1:
                    return message.channel.id == ctx.channel.id

            m = await Bot.wait_for(self=bot, event='message', check=check)

            await ctx.send('boa voce acerto')

            await ctx.send(f'j {jogador}')


class drawingcool(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def teste(self, ctx):
        embed=discord.Embed(description="sla", color=cor)
        embed.set_image(url='https://cdn.discordapp.com/attachments/885603001237135362/889154489683177543/unknown.png')
        embed.video
        await ctx.send(embed=embed)

    @commands.command()
    async def dw__(self, ctx):
        id_channel = ctx.channel.id
        print(id_channel)
        def check(m):
            return m.channel.id == id_channel
        desenho = await Bot.wait_for(self.bot,'message', check=check)
        imag__ = desenho.attachments[0]
        print(imag__)
        await ctx.send(imag__)

    @commands.command(aliases=["dw.i", "dw.iniciar", "dw.init"])
    async def dw_init(self, ctx):
        id_channel = ctx.channel.id

        if not os.path.exists(f"./minigames/sala_{id_channel}.json"):
            minigame = {
                'id_sala':id_channel,
                'participantes': [],
                'quantidade': 0,
                'index': 0,
                'rounds':0
            }
            save_dw_sets(id_channel, minigame)

            embed = discord.Embed(title="Drawing-cool acabou de começar !!",description=f"\rparar participar deigite:\r`{Pref}dw_entrar`\r", color=cor)
            # embed.a
            embed.set_footer(text=f"\rby - @{ctx.author.display_name}")

            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(description=f"Existe um minigame aberto nesse canal", color=cor)
            embed.set_footer(text=f"\rby - @{ctx.author.display_name}")
            await ctx.channel.send(embed=embed)

    @commands.command(aliases=["dw.e", "dw.entrar"])
    async def dw_entrar(self, ctx):
        id_particiante = ctx.author.id
        id_channel = ctx.channel.id
        try:
            sets_sala = load_dw_sets(id_channel)
        except FileNotFoundError:
            embed=discord.Embed(description=f"Não a nem um minigame acontecendo nessa sala.\rPara iniciar uma sala de minigames aqui digite `dw_init`", color=cor)
            await ctx.send(embed=embed)
            # await ctx.send(f"não a nem um minigame acontecendo nessa sala.\rPara iniciar uma sala de minigames aqui digite `dw_init`")
            return

        particps = sets_sala['participantes']
        quantidade_de_parts = sets_sala['quantidade']
        
        if not id_particiante in particps:
            particps.append(id_particiante)
            quantidade_de_parts = len(particps)
            dict(sets_sala).update({'participantes':particps})
            sets_sala['quantidade'] = quantidade_de_parts
            dict(sets_sala).update({"quantidade":int(quantidade_de_parts)})
            
            save_dw_sets(id_channel, sets_sala)

            embed=discord.Embed(description=f"[{ctx.author.mention}] Agora esta participando dessa sala de minigames.", color=cor)
            await ctx.send(embed=embed)
            return
            # await ctx.send(f"{ctx.author.mention} esta participando dessa sala de minigames.")

        else:
            embed=discord.Embed(description=f"[{ctx.author.mention}] Ja esta participando dessa sala de minigames.", color=cor)
            await ctx.send(embed=embed)
            return
            # await ctx.send(f"{ctx.author.mention} ja esta participando dessa sala de minigames.")

    @commands.command(aliases=["dw.p", "dw.play"])
    async def dw_play(self, ctx, rounds:int=None):
        id_channel = ctx.channel.id
        rounds_n = rounds
        if rounds_n == None:
            rounds_n = 3
        sets_sala = load_dw_sets(id_channel)

        quantidade = sets_sala['participantes']
        index_n = quantidade

        # await drawingcool_rounds(rounds=rounds_n, jogadores=quantidade, ctx=ctx, bot=self.bot)

        for round in range(rounds_n):
            embed=discord.Embed(description=f"Round ► **`{round+ 1}`**", color=cor)
            
            await ctx.send(embed=embed)
            
            for jogador in quantidade:
                jogador = int(jogador)
                
                # message sendo enviada para DM:

                embed_dm=discord.Embed(description=f"Sua vez amigo", color=cor)
                dm_jogador = await discord.Client.fetch_user(self.bot, jogador)
                await dm_jogador.send(embed=embed_dm)
                embed=discord.Embed(description=f"Esperando o jogado <@{jogador}> aceitar ou enviar a imagem", color=cor)
                await ctx.send(embed=embed)

                # verificação:

                emoji_V = Bot.get_emoji(self.bot, 887085594696622101)
                emoji_X = Bot.get_emoji(self.bot, 887088799086149632)

                embed=discord.Embed(description=f"Deseja desenhar ?\rdigite `desenhar` para desenhar ou `skip` para pular sua vez (sem colocar o prefixo antes das palavras).\r**Caso tenha duvida de como desenhar e como mandar digite `{Pref}dw.tutor`**", color=cor)
                msg = await dm_jogador.send(embed=embed)
                
                # await msg.add_reaction(emoji_X)
                # await msg.add_reaction(emoji_V)

                def check(message):
                    # print(reaction.message.author.id)
                    # print(dm_jogador.id)
                    if message.content == "desenhar" or message.content == "skip":
                        print(1)
                        return message.channel.id == msg.channel.id and message.author.id == dm_jogador.id

                try:
                    msg_resposta = await Bot.wait_for(self.bot, 'message', timeout=100.0, check=check)
                    print(2)

                except asyncio.TimeoutError:
                    await msg.send(embed=embed_rapida("Sua demora para aceitar/desistir resultou em, sua vez ser passada."))
                    await ctx.channel.send(embed=embed_rapida(f"<@{jogador}> foi pulado."))
                    return

                Tema = "biscoito"
                
                # Verificação do reação

                if msg_resposta.content == "desenhar":
                    await dm_jogador.send(embed=embed_rapida(f"desenhe {Tema}"))
                    await dm_jogador.send(embed=embed_rapida("Pode começar a desenhar... termine rapido ou sua vez sera pulada"))
                    await ctx.send("Esta desenhado ...")
                    await msg.delete()

                    # envio do desenho

                    id_channel = msg.channel.id

                    def check(m):
                        return m.channel.id == id_channel
                    desenho = await Bot.wait_for(self.bot, 'message', check=check)
                    imag = desenho.attachments[0]
                    

                    await ctx.send(f"{imag}")

                    p1 = 'biscoito'
                    def check(message):
                        if message.content == p1:
                            return message.channel.id == ctx.channel.id

                    m = await Bot.wait_for(self.bot, event='message', check=check)

                    await m.add_reaction(emoji_V)

                elif msg_resposta.content == "skip":
                    await ctx.send(f" <@{jogador}> Pulou a vez ...")
                    await msg.delete()

                # resposta

        await ctx.channel.send(embed=embed_rapida("Partida finalizada"))
     

    @commands.command(aliases=["dw.finalizar", "dw.f"])
    async def dw_finalizar(self, ctx):
        id_channel = ctx.channel.id
        
        if os.path.exists(f"./minigames/sala_{id_channel}.json"):

            emoji_V = Bot.get_emoji(self.bot, 887085594696622101)
            emoji_X = Bot.get_emoji(self.bot, 887088799086149632)

            embed=discord.Embed(description="Você que encerrar essa sala de minigames.\r", color=cor)
            embed.set_footer(text=f"\rby - @{ctx.author.display_name}")

            msg = await ctx.send(embed=embed)

            await msg.add_reaction(emoji_X)
            await msg.add_reaction(emoji_V)

            def check(reaction, user):
                if user.name == ctx.author.name:
                    return user.name == ctx.author.name and reaction.emoji == emoji_V , reaction.emoji == emoji_X

            try:
                reaction, user = await Bot.wait_for(self.bot, 'reaction_add', timeout=200.0, check=check)

            except asyncio.TimeoutError:
                await ctx.message.delete()
                return

            if reaction.emoji == emoji_V:
                sala = os.path.realpath(f"minigames/sala_{id_channel}.json")
                os.remove(sala)
                await ctx.message.delete()
                await msg.delete()

            if reaction.emoji == emoji_X:
                await ctx.message.delete()
                await msg.delete()

        else:
            embed=discord.Embed(description="Não a minigame rolando nesse canal.\r", color=cor)
            embed.set_footer(text=f"\rby - @{ctx.author.display_name}")
            msg_erro = await ctx.send(embed=embed, delete_after=60.0)
            await msg_erro.delete()



def setup(bot):
    bot.add_cog(drawingcool(bot))
