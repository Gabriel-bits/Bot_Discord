import json, os
import selenium
import time
import asyncio

import discord
from discord.ext import commands
from discord.ext import tasks
from discord.ext.commands.errors import CommandInvokeError
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import random
import googlesearch
from googlesearch import search

cor = 14735616

if not os.path.exists("perfils"):
    os.mkdir("perfils")

if not os.path.exists("templeites"):
    os.mkdir("templeites")

if not os.path.exists("config.json"):
    confg = {"cor":int(0xe0d900) ,"aler":int(0x970a02),"prefix":'?'}
    with open("config.json", "w") as f:
        json.dump(confg ,f)

#=====================================================================#

# DA UM JEITO NISSO AQUI

#=====================================================================#

def salvar_profil(Nome, ima1, ima2):
    perfil = {"nome":Nome, "not_speck":ima1, "speck":ima2}
    if not os.path.exists(f"perfils/{Nome}"):
        with open(f'perfils/{Nome}.json','w') as f:
            json.dump(perfil ,f)

def load_profi(Nome):

    with open(f"perfils/{Nome}.json", "r") as f:
        p = json.load(f)
    return p

#=====================================================================#

def salvar_tample(Nome, ima1, ima2):
    perfil = {"nome":Nome, "id":None, "not_speck":ima1, "speck":ima2}
    if not os.path.exists(f"templeites/{Nome}"):
        with open(f'templeites/{Nome}.json','w') as f:
            json.dump(perfil ,f)

def load_tample(Nome):

    with open(f"templeites/{Nome}.json", "r") as f:
        tample = json.load(f)
    return tample

#======================================================================#

def load_config():

    with open("config.json", "r") as f:
        confg = json.load(f)
    return confg

#======================================================================#

def save_dw_sets(id_channel, file):
    with open(f"./minigames/sala_{id_channel}.json", "w") as f:
        json.dump(file, f)

def load_dw_sets(id_channel):
    with open(f"./minigames/sala_{id_channel}.json", "r") as f:
        sets_sala = json.load(f)

    return sets_sala 

#======================================================================#

def pesq_meme():
    """
    url1 = 
    url2 = 
    url3 =
    url4 =
    """
    drive = webdriver.Chrome(executable_path="C:/Users/Narutinn/Documents/chromedriver_win32/chromedriver.exe")
    drive.get("https://www.google.com.br")


def text_codg(id_p, ima1, ima2):
    """
    para carregar e mod um text de codigos                          
    quendo entregado os seguintes argomentos                        
    """
    id_usuar = str(id_p)
    imag1 = str(ima1)
    imag2 = str(ima2)

    codg_c = '''```CSS
ul.voice-states {
    display: flex;
}
li.voice-state:not([data-reactid*="'''+id_usuar+'''"]) { display:none; }
.avatar {
content:url('''+imag1+''');
height:auto !important;
width:auto !important;
border-radius:0% !important;
filter: opacity(50%);
}

.speaking {
border-color:rgba(0,0,0,0) !important;
position:relative;
animation-name: speak-now;
animation-duration: 1s;
animation-fill-mode:forwards;
filter: brightness(100%);
content:url('''+imag2+''');
}

@keyframes speak-now {
0% { bottom:0px; }
15% { bottom:7px; }
30% { bottom:0px; }
}

li.voice-state{ position: static; }
div.user{ position: absolute; left:40%; bottom:5%; }

body { background-color: rgba(0, 0, 0, 0); margin: 0px auto; overflow: hidden; } ``` '''
    return codg_c

#============================================================================================#

# site_piadas_memes = "https://buzzfeed.com.br/post/50-piadas-horriveis-que-vao-despertar-o-tio-do-pave-dentro-de-voce"
# site_piadas2 = "https://www.maioresemelhores.com/piadas-ruins-engracadas/"
# site_memes_google = "https://www.google.com/search?q=memes+2020+br&tbm=isch&ved=2ahUKEwjJ2L3WhOTuAhVqM7kGHZJ0AvcQ2-cCegQIABAA&oq=memes+2020+br&gs_lcp=CgNpbWcQAzICCAAyAggAMgIIADIGCAAQBRAeMgYIABAFEB4yBggAEAgQHjIGCAAQCBAeMgYIABAIEB4yBggAEAgQHjIGCAAQCBAeOgQIABBDOgQIABAeUL4UWKwdYMshaABwAHgAgAF4iAHKApIBAzEuMpgBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=zEomYMlC6ubk5Q-S6Ym4Dw&bih=672&biw=1034&rlz=1C1CHBD_pt-PTBR909BR910&sfr=gws&gbv=1&sei=bZ4oYLKIM72Y5OUPyYyp4AU"


# lista_imag = []
# optios = Options()
# optios.add_argument('--headless')

# #=====================================================================================

# drive = webdriver.Chrome(executable_path="C:/Users/Narutinn/Documents/chromedriver_win32/chromedriver.exe", options=optios)
# drive.get(site_piadas_memes)

# for clase1 in drive.find_elements_by_class_name("entry-image-box"):
#     image = clase1.find_element_by_tag_name("img")
#     if not image.get_attribute("data-src"):
#         lista_imag.append(image.get_attribute("src"))
#     else:
#         lista_imag.append(image.get_attribute("data-src"))


# #===================================================================================

# drive.get(site_piadas2)

# # site_piadas2
# drive.find_element_by_class_name("article--body")
# for clase1 in drive.find_elements_by_class_name("img"):
#     imagens = clase1.find_element_by_tag_name("img")
#     if not imagens.get_attribute("data-src"):
#         lista_imag.append(imagens.get_attribute("src"))
#     else:
#         lista_imag.append(imagens.get_attribute("data-src"))


# #====================================================================================


# drive.get(site_memes_google)

# # Google
# for imag in drive.find_elements_by_class_name("t0fcAb"):
#     lista_imag.append(imag.get_attribute("src"))

# drive.quit()

# with open("data/memes1_links.json", "w") as f:
#     json.dump(lista_imag, f)


def memes_ale1():
    with open("data/memes1_links.json", "r") as f:
        arqv = json.load(f)
        arqv = random.choice(arqv)
    return arqv


#===========================================================================================

async def pesq_yt(pesquisa):
    embed=discord.Embed(title="**YouTube**", description=f"Resultados" , color=cor)
    for resultado in search(f'"{pesquisa}" youtube', lang='pt',stop=10):
        embed.add_field(name=f'<@{resultado}>' , value=resultado, inline=False)
    
    await embed

#=======================

def embed_rapida(msg):
    embed=discord.Embed(description=msg, color=cor)
    return embed

