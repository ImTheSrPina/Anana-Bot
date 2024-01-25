
from discord.ext import commands

from functions.functions import apiRequest, imageEmbedCreate




class nsfw(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("NSFW commands ready!")




    @commands.command()
    @commands.is_nsfw()
    async def badwaifu(self, ctx):
        async with ctx.typing():
            jsonResponse = await apiRequest('https://api.waifu.pics/nsfw/waifu')

        if jsonResponse != False:
            await ctx.send(embed = imageEmbedCreate(0xFFC0CB, jsonResponse['url']))
        else:
            await ctx.send("La solicitud no se ha completado :(")



    @commands.command()
    @commands.is_nsfw()
    async def blowjob(self, ctx):
        async with ctx.typing():
            jsonResponse = await apiRequest('https://purrbot.site/api/img/nsfw/blowjob/gif')

        if jsonResponse != False:
            await ctx.send(embed = imageEmbedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await ctx.send("La solicitud no se ha completado :(")



    @commands.command()
    @commands.is_nsfw()
    async def badneko(self, ctx):
        async with ctx.typing():
            jsonResponse = await apiRequest('https://api.waifu.pics/nsfw/neko')

        if jsonResponse != False:
            await ctx.send(embed = imageEmbedCreate(0xFFC0CB, jsonResponse['url']))
        else:
            await ctx.send("La solicitud no se ha completado :(")



    @commands.command()
    @commands.is_nsfw()
    async def hentai(self, ctx):
        async with ctx.typing():
            jsonResponse = await apiRequest('https://api.waifu.im/search/?included_tags=hentai')

        if jsonResponse != False:
            await ctx.send(embed = imageEmbedCreate(0xFFC0CB, jsonResponse['images'][0]['url']))
        else:
            await ctx.send("La solicitud no se ha completado :(")



    @commands.command()
    @commands.is_nsfw()
    async def milf(self, ctx):
        async with ctx.typing():
            jsonResponse = await apiRequest('https://api.waifu.im/search/?included_tags=milf')

        if jsonResponse != False:
            await ctx.send(embed = imageEmbedCreate(0xFFC0CB, jsonResponse['images'][0]['url']))
        else:
            await ctx.send("La solicitud no se ha completado :(")



    @commands.command()
    @commands.is_nsfw()
    async def ass(self, ctx):
        async with ctx.typing():
            jsonResponse = await apiRequest('https://api.waifu.im/search/?included_tags=ass')
        
        if jsonResponse != False:
            await ctx.send(embed = imageEmbedCreate(0xFFC0CB, jsonResponse['images'][0]['url']))
        else:
            await ctx.send("La solicitud no se ha completado :(")



    @commands.command()
    @commands.is_nsfw()
    async def oral(self, ctx):
        async with ctx.typing():
            jsonResponse = await apiRequest('https://api.waifu.im/search/?included_tags=oral')
        
        if jsonResponse != False:
            await ctx.send(embed = imageEmbedCreate(0xFFC0CB, jsonResponse['images'][0]['url']))
        else:
            await ctx.send("La solicitud no se ha completado :(")



    @commands.command()
    @commands.is_nsfw()
    async def paizuri(self, ctx):
        async with ctx.typing():
            jsonResponse = await apiRequest('https://api.waifu.im/search/?included_tags=paizuri')
        
        if jsonResponse != False:
            await ctx.send(embed = imageEmbedCreate(0xFFC0CB, jsonResponse['images'][0]['url']))
        else:
            await ctx.send("La solicitud no se ha completado :(")



    @commands.command()
    @commands.is_nsfw()
    async def ecchi(self, ctx):
        async with ctx.typing():
            jsonResponse = await apiRequest('https://api.waifu.im/search/?included_tags=ecchi')
        
        if jsonResponse != False:
            await ctx.send(embed = imageEmbedCreate(0xFFC0CB, jsonResponse['images'][0]['url']))
        else:
            await ctx.send("La solicitud no se ha completado :(")



    @commands.command()
    @commands.is_nsfw()
    async def ero(self, ctx):
        async with ctx.typing():
            jsonResponse = await apiRequest('https://api.waifu.im/search/?included_tags=ero')
        
        if jsonResponse != False:
            await ctx.send(embed = imageEmbedCreate(0xFFC0CB, jsonResponse['images'][0]['url']))
        else:
            await ctx.send("La solicitud no se ha completado :(")



    @commands.command()
    @commands.is_nsfw()
    async def anal (self, ctx):
        async with ctx.typing():
            jsonResponse = await apiRequest('https://purrbot.site/api/img/nsfw/anal/gif')

        if jsonResponse != False:
            await ctx.send(embed = imageEmbedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await ctx.send("La solicitud no se ha completado :(")



    @commands.command()
    @commands.is_nsfw()
    async def cum (self, ctx):
        async with ctx.typing():
            jsonResponse = await apiRequest('https://purrbot.site/api/img/nsfw/cum/gif')

        if jsonResponse != False:
            await ctx.send(embed = imageEmbedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await ctx.send("La solicitud no se ha completado :(")



    @commands.command()
    @commands.is_nsfw()
    async def fuck (self, ctx):
        async with ctx.typing():
            jsonResponse = await apiRequest('https://purrbot.site/api/img/nsfw/fuck/gif')

        if jsonResponse != False:
            await ctx.send(embed = imageEmbedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await ctx.send("La solicitud no se ha completado :(")



    @commands.command()
    @commands.is_nsfw()
    async def pussylick (self, ctx):
        async with ctx.typing():
            jsonResponse = await apiRequest('https://purrbot.site/api/img/nsfw/pussylick/gif')

        if jsonResponse != False:
            await ctx.send(embed = imageEmbedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await ctx.send("La solicitud no se ha completado :(")



    @commands.command()
    @commands.is_nsfw()
    async def solo (self, ctx):
        async with ctx.typing():
            jsonResponse = await apiRequest('https://purrbot.site/api/img/nsfw/solo/gif')

        if jsonResponse != False:
            await ctx.send(embed = imageEmbedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await ctx.send("La solicitud no se ha completado :(")



    @commands.command()
    @commands.is_nsfw()
    async def triofff (self, ctx):
        async with ctx.typing():
            jsonResponse = await apiRequest('https://purrbot.site/api/img/nsfw/threesome_fff/gif')

        if jsonResponse != False:
            await ctx.send(embed = imageEmbedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await ctx.send("La solicitud no se ha completado :(")



    @commands.command()
    @commands.is_nsfw()
    async def trioffm (self, ctx):
        async with ctx.typing():
            jsonResponse = await apiRequest('https://purrbot.site/api/img/nsfw/threesome_ffm/gif')

        if jsonResponse != False:
            await ctx.send(embed = imageEmbedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await ctx.send("La solicitud no se ha completado :(")



    @commands.command()
    @commands.is_nsfw()
    async def triommf (self, ctx):
        async with ctx.typing():
            jsonResponse = await apiRequest('https://purrbot.site/api/img/nsfw/threesome_mmf/gif')

        if jsonResponse != False:
            await ctx.send(embed = imageEmbedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await ctx.send("La solicitud no se ha completado :(")



    @commands.command()
    @commands.is_nsfw()
    async def yuri (self, ctx):
        async with ctx.typing():
            jsonResponse = await apiRequest('https://purrbot.site/api/img/nsfw/yuri/gif')

        if jsonResponse != False:
            await ctx.send(embed = imageEmbedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await ctx.send("La solicitud no se ha completado :(")



    @commands.command()
    @commands.is_nsfw()
    async def trap (self, ctx):
        async with ctx.typing():
            jsonResponse = await apiRequest('https://api.waifu.pics/nsfw/trap')

        if jsonResponse != False:
            await ctx.send(embed = imageEmbedCreate(0xFFC0CB, jsonResponse['url']))
        else:
            await ctx.send("La solicitud no se ha completado :(")





    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        async with ctx.typing():
            if isinstance(error, commands.NSFWChannelRequired):
                await ctx.send('Este comando solo puede usarse en canales NSFW')


    
    

async def setup(bot):
    await bot.add_cog(nsfw(bot))