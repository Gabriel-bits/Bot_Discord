import discord
from discord import client
from discord import mentions
from discord import embeds
from discord.ext import commands
from cogs.fuct import*
from discord import emoji
from googlesearch import search
import json, os
import asyncio


config = load_config()

cor = config["cor"]
cor_alert = config["aler"]
Pref = config["prefix"]


class comandos(commands.Cog):
    def __init__(self, client):
        self.client = client

        embed=discord.Embed(title="comandos primários do bot", description="temos uma função especial que se você estiver em duvida sobre os prefixos dos outros bots você \rpode usar o comando abaixo (prefixos).", color=cor)
        embed.set_author(name="ZEN Comandos", url="https://discord.com/api/oauth2/authorize?client_id=745030751636029530&permissions=8&scope=bot" , icon_url="")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/745030751636029530/f79fa139030a22e568cd122e63bf84dc.webp?size=1024")
        embed.add_field(name="Comandos", value=f"`{Pref}cmds`", inline=True)
        embed.add_field(name="Bots", value=f"`{Pref}bots`", inline=True)
        embed.add_field(name="Link do bot", value=f"`{Pref}link_bot`", inline=True)
        embed.add_field(name="Perfil animado...", value=f"`{Pref}Perfil_A`", inline=True)
        embed.add_field(name="Repositorio", value=f"`{Pref}repositorio`", inline=True)
        embed.add_field(name="Suporte", value=f"**[{'Click Me'}]({'https://discord.gg/R3pcFs9'})**", inline=True)
        self.embed_help = embed

    '''
    Comandos primarios:
    ==========================================================================]
    '''
    @commands.cooldown(1,2, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def heLp(self, ctx):
        # embed=discord.Embed(title="comandos primários do bot", description="temos uma função especial que se você estiver em duvida sobre os prefixos dos outros bots você \rpode usar o comando abaixo (prefixos).", color=cor)
        # embed.set_author(name="ZEN Comandos", url="https://discord.com/api/oauth2/authorize?client_id=745030751636029530&permissions=8&scope=bot" , icon_url="")
        # embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/745030751636029530/f79fa139030a22e568cd122e63bf84dc.webp?size=1024")
        # embed.add_field(name="Comandos", value=f"`{Pref}cmds`", inline=True)
        # embed.add_field(name="Bots", value=f"`{Pref}bots`", inline=True)
        # embed.add_field(name="Link do bot", value=f"`{Pref}link_bot`", inline=True)
        # embed.add_field(name="Perfil animado...", value=f"`{Pref}Perfil_A`", inline=True)
        # embed.add_field(name="Repositorio", value=f"`{Pref}repositorio`", inline=True)
        # embed.add_field(name="Suporte", value=f"**[{'Click Me'}]({'https://discord.gg/R3pcFs9'})**", inline=True)
        help_eact = await ctx.send(embed=self.embed_help)
        await help_eact.add_reaction('👍')


    @commands.Cog.listener()
    async def on_message(self, messagens):
        mention = str(messagens.content)
        if str(self.client.user.mention) == mention or str(self.client.user.display_name) == mention:
            help_eact = await messagens.channel.send(embed=self.embed_help)
            await help_eact.add_reaction('👍')


    @commands.command()
    async def LiNk_bot(self, ctx):
        embed=discord.Embed(title="☝ e so clicar para add nosso bot ao seu servem", color=cor)
        embed.set_author(name="Click aqui", url="https://discord.com/api/oauth2/authorize?client_id=745030751636029530&permissions=8&scope=bot")
        embed.set_thumbnail(url="https://www.freeiconspng.com/thumbs/add-icon-png/add-1-icon--flatastic-1-iconset--custom-icon-design-0.png")
        await ctx.send(embed=embed)


    @commands.command()
    async def cmds(self, ctx):
        embed=discord.Embed(title="divirta-se", color=cor)
        embed.set_author(name="Comandos",url="https://emoji.gg/assets/emoji/7277_green_flame.gif" , icon_url="https://emoji.gg/assets/emoji/7277_green_flame.gif")
        embed.add_field(name=f"* `{Pref}fala`", value="ex:( ?falar comida) ele mandara uma mensagem com o que vc escreveu na frente do comando.", inline=False)
        embed.add_field(name=f"* `{Pref}inf`", value=f"pode ser usado para saber as informaçoes do menbro ex:( ?inf @users).")
        embed.set_footer(text="por enquanto e so.\r")
        await ctx.send(embed=embed)


    @commands.command()
    async def bots(self, ctx):
        embed1 = discord.Embed(title='titulo', url="https://discord.com/api/oauth2/authorize?client_id=745030751636029530&permissions=8&scope=bot", color = cor)
        embed=discord.Embed(title=f"Não disponível no momento {embed1}", color=cor)
        await ctx.send(embed=embed)


    @commands.command()
    async def repositorio(self, ctx):
        embed=discord.Embed(title="https://github.com/Gabriel-bits/Bot-discord_v1", color=cor)
        await ctx.send(embed=embed)


    @commands.command()
    async def Perfil_A(self, ctx):
        embed=discord.Embed(title="Perfil animado pra ser usado no obs", description="Seguindo os comandos abaixo vc recebera o codg do seu perfil animado para ser usado no obs se seguindo a seguinte instrução( Obs -> add obj na cena -> add browser -> espaço para codg CSS ) para mais informações {Pref}Pa_tutorial." , color=cor)
        embed.set_author(name="Stream_perfil",url="https://emoji.gg/assets/emoji/7277_green_flame.gif" , icon_url="https://emoji.gg/assets/emoji/7277_green_flame.gif")
        embed.add_field(name=f"* `{Pref}Pa_perfil`", value=f"ex:({Pref}Pa_perfil + @você + imagem/gif_1 + imagem/gif2) \rimagem/gif_1 que ficara visível quando você parar de falar.\rimagem/gif_2 que ficara visível quando você falar algo.", inline=False)
        embed.add_field(name=f"* `{Pref}Pa_tample`", value=f"ex:({Pref}Pa_tample + Nome_do_templeite + imagem/gif_1 + imagem/gif2) \rVocê podera criar uma templeite que ficara salvo e podera ser reutilizado por outras pessoas", inline=False)
        embed.add_field(name=f"* `{Pref}Pa_codg_t`", value=f"ex:({Pref}Pa_codg_t + Nome_do_templeite + @pessoa_que_vai_utilizar)\rO e necessário por o nome do templeite existente colocar o nome do templeite e so mencionar você ou outra pessoa, loga apos vai receber mensagem com o codígo CSS. ", inline=False)
        embed.add_field(name=f"* `{Pref}Pa_tem_p`", value=f"ex:({Pref}Pa_tem_p) Para olhar/ver quantos templeites existe e mostra o nome deles enforma de lista.", inline=False)
        embed.add_field(name=f"* `{Pref}Str_tutorial`", value=f"ex:({Pref}Str_codg) \rindisponível por em quanto vai tmnc passei tres dia fazendo cada codg dessa aba.", inline=False)
        embed.set_footer(text="por enquanto e so.\r")
        await ctx.send(embed=embed)


    '''
    cmds dos bot:
    ==========================================================================]
    '''

    @commands.command()
    async def meu_criador(self, ctx):
        await ctx.send()


    @commands.command()
    async def fala(self, ctx , *, frase= None):
        if frase is None:
            await ctx.send(Pref+"fala + alguma coisa")
            return
        await ctx.message.delete()
        await ctx.send(f"{frase}")


    @commands.command()
    async def tts(self, ctx , *, frase= None):
        if frase is None:
            await ctx.send(Pref+"fala + alguma coisa")
            return
        await ctx.message.delete()
        await ctx.send(f"{frase}",tts=True)


    @commands.command()
    async def inf(self, ctx , *, usuario:discord.Member= None):
        if usuario is None:
            await ctx.send(Pref+"inf + @usuário")
            return
        usuario
        embed=discord.Embed(title="Informação do usuário ", color=cor)
        embed.set_thumbnail(url=usuario.avatar_url)
        embed.add_field(name="Nome:", value="`{}`".format(usuario.name), inline=True)
        embed.add_field(name="Apelido:", value="`@{}`".format(usuario.display_name), inline=True)
        embed.add_field(name="Id:", value="`{}`".format(usuario.id), inline=False)
        embed.add_field(name="Conta criada:", value="`{}`".format(usuario.created_at), inline=False)
        embed.add_field(name="Avatar:", value=usuario.avatar_url, inline=True)
        await ctx.send(embed=embed)


    @commands.command()
    async def palma(self, ctx , *frase):
        f = str(frase)
        f = f.replace(' ', '👏')
        f = f.replace("'", "")
        f = f.replace(",", "")
        f = f.replace("(", "")
        f = f.replace(")", "")
        await ctx.message.delete()
        await ctx.send(f)

        """
        discord.Permissions(permissions=0, **kwargs)
        Attributes
        add_reactions
        administrator
        """
    @commands.command(aliases=['cler', 'clr', 'cls'])
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx , *, quantia: int= None):

        if quantia != int:
            if quantia == None:
                embed=discord.Embed(title=f"**Erro no comando e necessário de uma quantia ex:({Pref}Clear + [Numero]**", color=cor_alert)
                await ctx.send(embed=embed)
                return
            megs = await ctx.channel.history(limit=quantia + 1).flatten()
            for mensagem in megs:
                await mensagem.delete()
        else:
            embed=discord.Embed(title="**Erro no comando e necessário de uma quantia ex:({Pref}Clear + [Numero] ... numero se lembrem**", color=cor_alert)
            await ctx.send(embed=embed)


    @commands.command()
    async def test(self, ctx ):

        await ctx.message.delete()
        await ctx.send(file=['C:/Users/Narutinn/Documents/Meus projetos/Meu Bot_Discord/main.py'])


    @commands.command(aliases=['sch_yt'])
    async def pesquisa_yt(self, ctx, *, pesquisa):

        """
        embed=discord.Embed(title="**YouTube**", description=f"Resultados" , color=cor)
        for resultado in search(f'"{pesquisa}" youtube', lang='pt',stop=10):
            embed.add_field(name=f'<@{resultado}>' , value=resultado, inline=False)    

        loop = asyncio.get_event_loop()
        loop.run_until_complete(pesq_yt(pesquisa))
        """

        pes = pesq_yt(pesquisa)
        
        embed = pes

        await ctx.send(embed=embed)


    @commands.command(aliases=['mems', 'mms', 'meme'])
    async def memes(self, ctx):
        await ctx.message.delete()
        meme = memes_ale1()
        await ctx.send(meme)

    """
    Perfil animado:
    ==========================================================================]

    @commands.command()
    async def Str_nome(self, ctx, *, id_user:discord.Member= None):
        
        if id_user == None:
            embed=discord.Embed(title=f"Confira, se digitou o comando corretamente.\rexp: ```{Pref}Str_nome``` + @voce", color=cor)
            await ctx.send(embed=embed)
            return
        salvar_profil(id_user.id, ima1= None, ima2= None)

        embed=discord.Embed(title=f"O usuario <@!{id_user.id}> foi iniciado, e sera fechado apos o ultimo comondo ou seja ```{Pref}imag_speck```.", color=cor)
        await ctx.send(embed=embed)
    """

    @commands.command()
    async def Pa_codg(self, ctx, args:discord.Member= None, args2= None, *, args3= None):
        '''
        !! cuidado area perigosa !!
        args = id do usuario
        args2 = imagem not_speak
        args3 = imagem speak
        '''

        if args == None is args2 == None is args3 == None:
            embed=discord.Embed(title=f"Confira, se digitou o comando corretamente.\rexp: ```{Pref}Str_perfil``` + @voce + imagem_defalt + imagem_falando", color=cor)
            await ctx.send(embed=embed)
            return
        try:
            salvar_profil(args.id, args2, args3)

        except:
            embed=discord.Embed(title=f"Ocorreu um erro, confira se digitou o comando corretamente.\rexp: ```{Pref}Str_perfil``` + @voce + imagem_defalt + imagem_falando", color=cor)
            await ctx.send(embed=embed)
            return
        
        codg_c = text_codg(args.id, args2, args3)

        await ctx.send(f"@{ctx.author.name}:\r{codg_c}")


    @commands.command()
    async def Pa_temple(self, ctx, nome=None, not_speck=None , *, speck=None):
        
        # if not_speck == None is speck == None:
        #     embed=discord.Embed(title=f"Seu comando foi salvo mesmo não tendo uma das imagems, quiser pode deletar esse templeite com o comando ... mas se quiser tentar denovo verifique se o comando foi digitado corretamente como o exemplo a seguir.\rexp: ```{Pref}Str_falando``` + @voce", color=cor)
        #     await ctx.send(embed=embed)
        
        if not_speck == None is speck == None:
            embed=discord.Embed(title=f"O comando não foi digitado corretamente tente seguir o exemplo abaixo.\rexp: ```{Pref}Str_falando``` + @voce", color=cor)
            await ctx.send(embed=embed)
            return
        try:
            salvar_tample(nome, ima1=not_speck, ima2= speck)

        except Exception as ee:
            await ctx.send(f"Erro -> {ee}")

        embed=discord.Embed(title="Discord Streamkit", url="https://streamkit.discord.com/overlay", description="Link pra o streamkit ⬆", color=cor)
        embed.set_author(name=f"___________________________________________")
        embed.set_thumbnail(url=f"{not_speck}")
        embed.add_field(name=f"@{ctx.author.name} \rO templaite **`{nome}`** foi salvo com sucesso !.\rPara acessa esse templeite digite o seguinte comando:", value=f"`{Pref}Pa_codg_t`", inline=False)
        embed.set_footer(text=f"by {ctx.author.name}")
        msg = await ctx.send(embed=embed)
        await msg.add_reaction('✅')


    @commands.command()
    async def Pa_codg_t(self, ctx, nome= None, *,id_p:discord.Member= None):

        if not os.path.exists(f"templeites/{nome}.json"):
            embed=discord.Embed(title=f"Templeite **`{nome}`** não encontrado, verifique se o nome não foi digitado errado", color=cor)
            await ctx.send(embed=embed)
            return
        
        global temple
        global codg_c
        temple = None

        try:
            temple = load_tample(nome)

        except FileNotFoundError:
            embed=discord.Embed(title=f"Templeite **`{nome}`** não encontrado, verifique se o nome não foi digitado errado", color=cor)
            await ctx.send(embed=embed)
            return

        codg_c = text_codg(id_p.id, temple["not_speck"], temple["speck"])

        await ctx.send(f"@{ctx.author.name}:\r{codg_c}")


    @commands.command()
    async def Pa_tem_p(self, ctx):

        templeites_folder = "./templeites"
        num = 0
        lista_nomes = []
        for root, subFolder, fileName in os.walk(templeites_folder):
            for files in fileName:
                lista_nomes.append(files)
                num += 1

        nomes = str(lista_nomes)
        nomes = nomes.replace("'", "")
        nomes = nomes.replace(",", "")
        nomes = nomes.replace("[", "")
        nomes = nomes.replace("]", "")
        nomes = nomes.replace(' ', '\r')
        nomes = nomes.replace(' ', '')
        nomes = nomes.replace('.json', '')

        embed=discord.Embed(title="**Pasta Templeites**", description=f"Todos os templeites existentes no banco de dados" , color=cor)
        embed.set_thumbnail(url="https://image.flaticon.com/icons/png/512/2015/2015190.png")
        embed.add_field(name=f"`{num}` Templeites:\r**------------◄►------------**\r", value=f"**`{nomes}`**", inline=False)

        await ctx.send(embed=embed)



    """
    Uncknoc:
    ==========================================================================]
    """

    @commands.command()
    async def join(self, ctx):
        if not ctx.message.author.voice:
            await ctx.send("You are not connected to a voice channel")
            return
        else:
            channel = ctx.message.author.voice.channel

        await channel.connect()

def setup(client):
    client.add_cog(comandos(client))
