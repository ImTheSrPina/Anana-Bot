import discord

from discord.ext import commands
from discord import app_commands

from functions.functions import apiRequest, embedCreate



class slashWaifus(commands.Cog):



    def __init__(self, bot):
        self.bot = bot



    @commands.Cog.listener()
    async def on_ready(self):
        print("Waifus app commands loaded")




    @app_commands.command(name = "neko", description = "a neko image")
    async def neko(self, interaction: discord.Interaction):
        jsonResponse = await apiRequest('https://api.waifu.pics/sfw/neko')

        if jsonResponse != False:
            await interaction.response.send_message(embed = embedCreate(0xFFC0CB, jsonResponse['url']))
        else:
            await interaction.response.send_message("La solicitud no se ha completado :(")



    @app_commands.command(name = "awoo", description = "awoo")
    async def awoo(self, interaction: discord.Interaction):
        jsonResponse = await apiRequest('https://api.waifu.pics/sfw/awoo')

        if jsonResponse != False:
            await interaction.response.send_message(embed = embedCreate(0xFFC0CB, jsonResponse['url']))
        else:
            await interaction.response.send_message("La solicitud no se ha completado :(")



    @app_commands.command(name = "megumin", description = "megumin")
    async def megumin(self, interaction: discord.Interaction):
        jsonResponse = await apiRequest('https://api.waifu.pics/sfw/megumin')

        if jsonResponse != False:
            await interaction.response.send_message(embed = embedCreate(0xFFC0CB, jsonResponse['url']))
        else:
            await interaction.response.send_message("La solicitud no se ha completado :(")



    @app_commands.command(name = "maid", description = "man, i love maids")
    async def maid(self, interaction: discord.Interaction):
        jsonResponse = await apiRequest('https://api.waifu.im/search/?included_tags=maid')

        if jsonResponse != False:
            await interaction.response.send_message(embed = embedCreate(0xFFC0CB, jsonResponse['images'][0]['url']))
        else:
            await interaction.response.send_message("La solicitud no se ha completado :(")



    @app_commands.command(name = "waifu", description = "waifu yeeee")
    async def waifu(self, interaction: discord.Interaction):
        jsonResponse = await apiRequest('https://api.waifu.im/search/?included_tags=waifu')

        if jsonResponse != False:
            await interaction.response.send_message(embed = embedCreate(0xFFC0CB, jsonResponse['images'][0]['url']))
        else:
            await interaction.response.send_message("La solicitud no se ha completado :(")



    @app_commands.command(name = "marin", description = "marin")
    async def marin(self, interaction: discord.Interaction):
        jsonResponse = await apiRequest('https://api.waifu.im/search/?included_tags=marin-kitagawa')

        if jsonResponse != False:
            await interaction.response.send_message(embed = embedCreate(0xFFC0CB, jsonResponse['images'][0]['url']))
        else:
            await interaction.response.send_message("La solicitud no se ha completado :(")



    @app_commands.command(name = "calliope", description = "mori calliope")
    async def calliope(self, interaction: discord.Interaction):
        jsonResponse = await apiRequest('https://api.waifu.im/search/?included_tags=mori-calliope')

        if jsonResponse != False:
            await interaction.response.send_message(embed = embedCreate(0xFFC0CB, jsonResponse['images'][0]['url']))
        else:
            await interaction.response.send_message("La solicitud no se ha completado :(")



    @app_commands.command(name = "raiden", description = "raiden shogun")
    async def raiden(self, interaction: discord.Interaction):
        jsonResponse = await apiRequest('https://api.waifu.im/search/?included_tags=raiden-shogun')

        if jsonResponse != False:
            await interaction.response.send_message(embed = embedCreate(0xFFC0CB, jsonResponse['images'][0]['url']))
        else:
            await interaction.response.send_message("La solicitud no se ha completado :(")



    @app_commands.command(name = "oppai", description = "oppai")
    async def oppai(self, interaction: discord.Interaction):
        jsonResponse = await apiRequest('https://api.waifu.im/search/?included_tags=oppai')

        if jsonResponse != False:
            await interaction.response.send_message(embed = embedCreate(0xFFC0CB, jsonResponse['images'][0]['url']))
        else:
            await interaction.response.send_message("La solicitud no se ha completado :(")



    @app_commands.command(name = "selfie", description = "selfie")
    async def selfie(self, interaction: discord.Interaction):
        jsonResponse = await apiRequest('https://api.waifu.im/search/?included_tags=selfies')

        if jsonResponse != False:
            await interaction.response.send_message(embed = embedCreate(0xFFC0CB, jsonResponse['images'][0]['url']))
        else:
            await interaction.response.send_message("La solicitud no se ha completado :(")



    @app_commands.command(name = "uniform", description = "uniform")
    async def uniform(self, interaction: discord.Interaction):
        jsonResponse = await apiRequest('https://api.waifu.im/search/?included_tags=uniform')

        if jsonResponse != False:
            await interaction.response.send_message(embed = embedCreate(0xFFC0CB, jsonResponse['images'][0]['url']))
        else:
            await interaction.response.send_message("La solicitud no se ha completado :(")



    @app_commands.command(name = "fluff", description = "fluff")
    async def fluff(self, interaction: discord.Interaction):
        jsonResponse = await apiRequest('https://purrbot.site/api/img/sfw/fluff/gif')

        if jsonResponse != False:
            await interaction.response.send_message(embed = embedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await interaction.response.send_message("La solicitud no se ha completado :(")



    @app_commands.command(name = "shiro", description = "shiro")
    async def shiro(self, interaction: discord.Interaction):
        jsonResponse = await apiRequest('https://purrbot.site/api/img/sfw/shiro/img')

        if jsonResponse != False:
            await interaction.response.send_message(embed = embedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await interaction.response.send_message("La solicitud no se ha completado :(")



    @app_commands.command(name = "senko", description = "senko")
    async def senko(self, interaction: discord.Interaction):
        jsonResponse = await apiRequest('https://purrbot.site/api/img/sfw/senko/img')

        if jsonResponse != False:
            await interaction.response.send_message(embed = embedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await interaction.response.send_message("La solicitud no se ha completado :(")



    @app_commands.command(name = "okami", description = "okami")
    async def okami(self, interaction: discord.Interaction):
        jsonResponse = await apiRequest('https://purrbot.site/api/img/sfw/okami/img')

        if jsonResponse != False:
            await interaction.response.send_message(embed = embedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await interaction.response.send_message("La solicitud no se ha completado :(")



    @app_commands.command(name = "kitsune", description = "kitsune")
    async def kitsune(self, interaction: discord.Interaction):
        jsonResponse = await apiRequest('https://purrbot.site/api/img/sfw/kitsune/img')

        if jsonResponse != False:
            await interaction.response.send_message(embed = embedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await interaction.response.send_message("La solicitud no se ha completado :(")





async def setup(bot):
    await bot.add_cog(slashWaifus(bot))