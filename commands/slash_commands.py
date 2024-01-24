import discord, json, requests

from aiohttp import ClientSession
from discord.ext import commands
from discord import app_commands


async def getWaifu(tag):
        async with ClientSession() as resp:
            async with resp.get(f"https://api.waifu.im/search/?included_tags={tag}") as response:
                data = await response.json()
        return data['images'][0]['url']

async def getWaifuPics(tag):
        animeAPI = requests.get(f"https://api.waifu.pics/nsfw/{tag}")
        waifu = animeAPI.json()["url"]
        return waifu

async def getWaifuPurrbot(tag):
        animeAPI = requests.get(f"https://purrbot.site/api/img/nsfw/{tag}/gif")
        waifu = animeAPI.json()["link"]
        return waifu


class Slash(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Slash commans on ready!")

    @app_commands.command(name = "ping", description = "El hola mundo de los bots")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message("pong")

    @app_commands.command(name = "milf", description = "El comando favorito del desarrollador, no le digas a nadie ;)")
    async def milf(self, interaction: discord.Interaction):
        emb = discord.Embed(color= 0xFFC0CB) 
        emb.set_image(url=await getWaifu("milf"))
        await interaction.response.send_message(embed=emb)

    @app_commands.command(name = "trampa", description = "¡¡Es una trampa!!")
    async def trampa(self, interaction: discord.Interaction):
        emb = discord.Embed(color= 0xFFC0CB)
        emb.set_image(url=await getWaifuPics("trap"))
        await interaction.response.send_message(embed=emb)

    @app_commands.command(name = "urss", description = "Perdoname por todo union sovietica...")
    async def urss(self, interaction: discord.Interaction):
        emb = discord.Embed(color= 0xFFC0CB) 
        emb.set_image(url=await getWaifu("paizuri"))
        await interaction.response.send_message(embed=emb)
    
    @app_commands.command(name = "correr", description = "Miausculos: me corroooo aaaaa!!")
    async def correr(self, interaction: discord.Interaction):
        emb = discord.Embed(color= 0xFFC0CB) 
        emb.set_image(url=await getWaifuPurrbot("cum"))
        await interaction.response.send_message(embed=emb)

    @app_commands.command(name = "kill", description = "/kill")
    async def kill(self, interaction: discord.Interaction):
        await interaction.response.send_message("**Se hace pendeja**")

    

## SLASH COMMANDS FOR MODERATION ___________________________________________
## ESTA PARTE ESTA PENDIENTE
## NO ENCONTRE UNA FORMA DE HACER QUE SEA DE USO EXCLUSIVO PARA ADMINISTRADORES

## Y EL SERVICIO SOCIAL ME CARCOME....

    
    @app_commands.command(name = "rol", description = "Le asigna un rol a un miembro")
    @app_commands.describe(member = "Miembro al que le daras un rol", rol="El rol que vas a asignar")
    async def rol(self, interaction: discord.Interaction, member: discord.Member, rol: discord.Role):
        await interaction.response.send_message(f"El rol {rol.mention} se asigno a {member.mention}")
        await interaction.response.send_message("O eso desearia hacer")
        await interaction.response.send_message(
             "El desarrollador no encontro como limitar el uso de este comando xd")
        """
        await member.add_roles(rol)
        await interaction.response.send_message(f"El rol {rol.mention} se asigno a {member.mention}")

        if interaction.author.guild_permissions.administrator:
                try:
                    await member.add_roles(rol)
                    await interaction.response.send_message(f"El rol {rol.mention} se asigno a {member.mention}")
                except discord.Forbidden:
                    await interaction.response.send_message("No tengo permisos para asignar roles.")
        else:
            await interaction.response.send_message("Este comando solo está disponible para administradores.")
        """
        
    @app_commands.command(
              name = "kick", 
              description = "Expulsa a un miembro",
              )
    @app_commands.describe(miembro="Miembro a expulsar", razon= "Razon de la expulsión" )
    @app_commands.choices(razon=[
         discord.app_commands.Choice(name="Sin razón", value=1),
         discord.app_commands.Choice(name="Mal comportamiento", value=2),
         discord.app_commands.Choice(name="Spam", value=3)

    ])
    async def kick(self, interaction: discord.Interaction, 
                   miembro: discord.Member, 
                   razon: discord.app_commands.Choice[int]):

        await interaction.response.send_message(f"**Lo expulsa** {miembro.name} {razon.name}")





async def setup(bot):
    await bot.add_cog(Slash(bot))