import discord

from discord.ext import commands
from discord import app_commands

from functions.functions import apiRequest, embedCreate



class slashNSFW(commands.Cog):



    def __init__(self, bot):
        self.bot = bot



    @commands.Cog.listener()
    async def on_ready(self):
        print("NSFW app commands loaded")




    @app_commands.command(name = "milf", description = "El comando favorito del desarrollador, no le digas a nadie ;)")
    async def milf(self, interaction: discord.Interaction):
        jsonResponse = await apiRequest('https://api.waifu.im/search/?included_tags=milf')

        if jsonResponse != False:
            await interaction.response.send_message(embed = embedCreate(0xFFC0CB, jsonResponse['images'][0]['url']))
        else:
            await interaction.response.send_message("La solicitud no se ha completado :(")



    @app_commands.command(name = "waifubutnsfw", description = "NSFW Waifu")
    async def waifuButNSFW(self, interaction: discord.Interaction):
        jsonResponse = await apiRequest('https://api.waifu.pics/nsfw/waifu')

        if jsonResponse != False:
            await interaction.response.send_message(embed = embedCreate(0xFFC0CB, jsonResponse['url']))
        else:
            await interaction.response.send_message("La solicitud no se ha completado :(")



    @app_commands.command(name = "blowjob", description = "blowjob image")
    async def blowjob(self, interaction: discord.Interaction):
        jsonResponse = await apiRequest('https://purrbot.site/api/img/nsfw/blowjob/gif')

        if jsonResponse != False:
            await interaction.response.send_message(embed = embedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await interaction.response.send_message("La solicitud no se ha completado :(")



    @app_commands.command(name = "nekobutnsfw", description = "NSFW Neko")
    async def nekoButNSFW(self, interaction: discord.Interaction):
        jsonResponse = await apiRequest('https://api.waifu.pics/nsfw/neko')

        if jsonResponse != False:
            await interaction.response.send_message(embed = embedCreate(0xFFC0CB, jsonResponse['url']))
        else:
            await interaction.response.send_message("La solicitud no se ha completado :(")



    @app_commands.command(name = "hentai", description = "hentai")
    async def hentai(self, interaction: discord.Interaction):
        jsonResponse = await apiRequest('https://api.waifu.im/search/?included_tags=hentai')

        if jsonResponse != False:
            await interaction.response.send_message(embed = embedCreate(0xFFC0CB, jsonResponse['images'][0]['url']))
        else:
            await interaction.response.send_message("La solicitud no se ha completado :(")



    @app_commands.command(name = "ass", description = "ass image")
    async def ass(self, interaction: discord.Interaction):
        jsonResponse = await apiRequest('https://api.waifu.im/search/?included_tags=ass')
        
        if jsonResponse != False:
            await interaction.response.send_message(embed = embedCreate(0xFFC0CB, jsonResponse['images'][0]['url']))
        else:
            await interaction.response.send_message("La solicitud no se ha completado :(")



    @app_commands.command(name = "oral", description = "oral image or gif?")
    async def oral(self, interaction: discord.Interaction):
        jsonResponse = await apiRequest('https://api.waifu.im/search/?included_tags=oral')
        
        if jsonResponse != False:
            await interaction.response.send_message(embed = embedCreate(0xFFC0CB, jsonResponse['images'][0]['url']))
        else:
            await interaction.response.send_message("La solicitud no se ha completado :(")



    @app_commands.command(name = "paizuri", description = "paizuri? What is this?")
    async def paizuri(self, interaction: discord.Interaction):
        jsonResponse = await apiRequest('https://api.waifu.im/search/?included_tags=paizuri')
        
        if jsonResponse != False:
            await interaction.response.send_message(embed = embedCreate(0xFFC0CB, jsonResponse['images'][0]['url']))
        else:
            await interaction.response.send_message("La solicitud no se ha completado :(")



    @app_commands.command(name = "ecchi", description = "ecchi...")
    async def ecchi(self, interaction: discord.Interaction):
        jsonResponse = await apiRequest('https://api.waifu.im/search/?included_tags=ecchi')
        
        if jsonResponse != False:
            await interaction.response.send_message(embed = embedCreate(0xFFC0CB, jsonResponse['images'][0]['url']))
        else:
            await interaction.response.send_message("La solicitud no se ha completado :(")



    @app_commands.command(name = "ero", description = "ero sennin?")
    async def ero(self, interaction: discord.Interaction):
        jsonResponse = await apiRequest('https://api.waifu.im/search/?included_tags=ero')
        
        if jsonResponse != False:
            await interaction.response.send_message(embed = embedCreate(0xFFC0CB, jsonResponse['images'][0]['url']))
        else:
            await interaction.response.send_message("La solicitud no se ha completado :(")



    @app_commands.command(name = "anal", description = "anal gifs")
    async def anal(self, interaction: discord.Interaction):
        jsonResponse = await apiRequest('https://purrbot.site/api/img/nsfw/anal/gif')

        if jsonResponse != False:
            await interaction.response.send_message(embed = embedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await interaction.response.send_message("La solicitud no se ha completado :(")



    @app_commands.command(name = "cum", description = "welcome to the cum zone")
    async def cum(self, interaction: discord.Interaction):
        jsonResponse = await apiRequest('https://purrbot.site/api/img/nsfw/cum/gif')

        if jsonResponse != False:
            await interaction.response.send_message(embed = embedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await interaction.response.send_message("La solicitud no se ha completado :(")



    @app_commands.command(name = "fuck", description = "the f word")
    async def fuck(self, interaction: discord.Interaction):
        jsonResponse = await apiRequest('https://purrbot.site/api/img/nsfw/fuck/gif')

        if jsonResponse != False:
            await interaction.response.send_message(embed = embedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await interaction.response.send_message("La solicitud no se ha completado :(")



    @app_commands.command(name = "fuck", description = "the f word")
    async def fuck(self, interaction: discord.Interaction):
        jsonResponse = await apiRequest('https://purrbot.site/api/img/nsfw/fuck/gif')

        if jsonResponse != False:
            await interaction.response.send_message(embed = embedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await interaction.response.send_message("La solicitud no se ha completado :(")



    @app_commands.command(name = "pussylick", description = "rico")
    async def pussylick(self, interaction: discord.Interaction):
        jsonResponse = await apiRequest('https://purrbot.site/api/img/nsfw/pussylick/gif')

        if jsonResponse != False:
            await interaction.response.send_message(embed = embedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await interaction.response.send_message("La solicitud no se ha completado :(")



    @app_commands.command(name = "solo", description = "que podrias hacer estando solo?")
    async def solo(self, interaction: discord.Interaction):
        jsonResponse = await apiRequest('https://purrbot.site/api/img/nsfw/solo/gif')

        if jsonResponse != False:
            await interaction.response.send_message(embed = embedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await interaction.response.send_message("La solicitud no se ha completado :(")



    @app_commands.command(name = "threesome_fff", description = "yes, a nsfw command")
    async def threesome_fff(self, interaction: discord.Interaction):
        jsonResponse = await apiRequest('https://purrbot.site/api/img/nsfw/threesome_fff/gif')

        if jsonResponse != False:
            await interaction.response.send_message(embed = embedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await interaction.response.send_message("La solicitud no se ha completado :(")



    @app_commands.command(name = "threesome_ffm", description = "yes, another nsfw command")
    async def threesome_ffm(self, interaction: discord.Interaction):
        jsonResponse = await apiRequest('https://purrbot.site/api/img/nsfw/threesome_ffm/gif')

        if jsonResponse != False:
            await interaction.response.send_message(embed = embedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await interaction.response.send_message("La solicitud no se ha completado :(")



    @app_commands.command(name = "threesome_mmf", description = "just use this command")
    async def threesome_mmf(self, interaction: discord.Interaction):
        jsonResponse = await apiRequest('https://purrbot.site/api/img/nsfw/threesome_mmf/gif')

        if jsonResponse != False:
            await interaction.response.send_message(embed = embedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await interaction.response.send_message("La solicitud no se ha completado :(")



    @app_commands.command(name = "yuri", description = "just a normal nsfw command")
    async def yuri(self, interaction: discord.Interaction):
        jsonResponse = await apiRequest('https://purrbot.site/api/img/nsfw/yuri/gif')

        if jsonResponse != False:
            await interaction.response.send_message(embed = embedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await interaction.response.send_message("La solicitud no se ha completado :(")



    @app_commands.command(name = "trampa", description = "¡¡Es una trampa!!")
    async def trampa(self, interaction: discord.Interaction):
        jsonResponse = await apiRequest('https://api.waifu.pics/nsfw/trap')

        if jsonResponse != False:
            await interaction.response.send_message(embed = embedCreate(0xFFC0CB, jsonResponse['url']))
        else:
            await interaction.response.send_message("La solicitud no se ha completado :(")






async def setup(bot):
    await bot.add_cog(slashNSFW(bot))