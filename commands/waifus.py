
from discord.ext import commands

from functions.functions import apiRequest, imageEmbedCreate




class waifus(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Waifu commands ready!")




    @commands.command()
    async def neko(self, ctx):
        jsonResponse = await apiRequest('https://api.waifu.pics/sfw/neko')

        if jsonResponse != False:
            await ctx.send(embed = imageEmbedCreate(0xFFC0CB, jsonResponse['url']))
        else:
            await ctx.send("La solicitud no se ha completado :(")




    @commands.command()
    async def awoo(self, ctx):
        jsonResponse = await apiRequest('https://api.waifu.pics/sfw/awoo')

        if jsonResponse != False:
            await ctx.send(embed = imageEmbedCreate(0xFFC0CB, jsonResponse['url']))
        else:
            await ctx.send("La solicitud no se ha completado :(")




    @commands.command()
    async def megumin(self, ctx):
        jsonResponse = await apiRequest('https://api.waifu.pics/sfw/megumin')

        if jsonResponse != False:
            await ctx.send(embed = imageEmbedCreate(0xFFC0CB, jsonResponse['url']))
        else:
            await ctx.send("La solicitud no se ha completado :(")




    @commands.command()
    async def maid(self, ctx):
        jsonResponse = await apiRequest('https://api.waifu.im/search/?included_tags=maid')
        
        if jsonResponse != False:
            await ctx.send(embed = imageEmbedCreate(0xFFC0CB, jsonResponse['images'][0]['url']))
        else:
            await ctx.send("La solicitud no se ha completado :(")




    @commands.command()
    async def waifu(self, ctx):
        jsonResponse = await apiRequest('https://api.waifu.im/search/?included_tags=waifu')
        
        if jsonResponse != False:
            await ctx.send(embed = imageEmbedCreate(0xFFC0CB, jsonResponse['images'][0]['url']))
        else:
            await ctx.send("La solicitud no se ha completado :(")




    @commands.command()
    async def marin(self, ctx):
        jsonResponse = await apiRequest('https://api.waifu.im/search/?included_tags=marin-kitagawa')
        
        if jsonResponse != False:
            await ctx.send(embed = imageEmbedCreate(0xFFC0CB, jsonResponse['images'][0]['url']))
        else:
            await ctx.send("La solicitud no se ha completado :(")




    @commands.command()
    async def mori(self, ctx):
        jsonResponse = await apiRequest('https://api.waifu.im/search/?included_tags=mori-calliope')
        
        if jsonResponse != False:
            await ctx.send(embed = imageEmbedCreate(0xFFC0CB, jsonResponse['images'][0]['url']))
        else:
            await ctx.send("La solicitud no se ha completado :(")




    @commands.command()
    async def raiden(self, ctx):
        jsonResponse = await apiRequest('https://api.waifu.im/search/?included_tags=raiden-shogun')
        
        if jsonResponse != False:
            await ctx.send(embed = imageEmbedCreate(0xFFC0CB, jsonResponse['images'][0]['url']))
        else:
            await ctx.send("La solicitud no se ha completado :(")




    @commands.command()
    async def oppai(self, ctx):
        jsonResponse = await apiRequest('https://api.waifu.im/search/?included_tags=oppai')
        
        if jsonResponse != False:
            await ctx.send(embed = imageEmbedCreate(0xFFC0CB, jsonResponse['images'][0]['url']))
        else:
            await ctx.send("La solicitud no se ha completado :(")




    @commands.command()
    async def selfie(self, ctx):
        jsonResponse = await apiRequest('https://api.waifu.im/search/?included_tags=selfies')
        
        if jsonResponse != False:
            await ctx.send(embed = imageEmbedCreate(0xFFC0CB, jsonResponse['images'][0]['url']))
        else:
            await ctx.send("La solicitud no se ha completado :(")




    @commands.command()
    async def uniform(self, ctx):
        jsonResponse = await apiRequest('https://api.waifu.im/search/?included_tags=uniform')
        
        if jsonResponse != False:
            await ctx.send(embed = imageEmbedCreate(0xFFC0CB, jsonResponse['images'][0]['url']))
        else:
            await ctx.send("La solicitud no se ha completado :(")




    @commands.command()
    async def fluff (self, ctx):
        jsonResponse = await apiRequest('https://purrbot.site/api/img/sfw/fluff/gif')

        if jsonResponse != False:
            await ctx.send(embed = imageEmbedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await ctx.send("La solicitud no se ha completado :(")




    @commands.command()
    async def shiro(self, ctx):
        jsonResponse = await apiRequest('https://purrbot.site/api/img/sfw/shiro/img')

        if jsonResponse != False:
            await ctx.send(embed = imageEmbedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await ctx.send("La solicitud no se ha completado :(")




    @commands.command()
    async def senko (self, ctx):
        jsonResponse = await apiRequest('https://purrbot.site/api/img/sfw/senko/img')

        if jsonResponse != False:
            await ctx.send(embed = imageEmbedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await ctx.send("La solicitud no se ha completado :(")




    @commands.command()
    async def okami (self, ctx):
        jsonResponse = await apiRequest('https://purrbot.site/api/img/sfw/okami/img')

        if jsonResponse != False:
            await ctx.send(embed = imageEmbedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await ctx.send("La solicitud no se ha completado :(")




    @commands.command()
    async def kitsune (self, ctx):
        jsonResponse = await apiRequest('https://purrbot.site/api/img/sfw/kitsune/img')

        if jsonResponse != False:
            await ctx.send(embed = imageEmbedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await ctx.send("La solicitud no se ha completado :(")




async def setup(bot):
    await bot.add_cog(waifus(bot))