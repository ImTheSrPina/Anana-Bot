
from discord.ext import commands

from functions.functions import apiRequest, embedCreate




class nsfw(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("NSFW prefix commands loaded")




    @commands.command()
    @commands.is_nsfw()
    async def badwaifu(self, ctx):
        jsonResponse = await apiRequest('https://api.waifu.pics/nsfw/waifu')

        if jsonResponse != False:
            await ctx.send(embed = embedCreate(0xFFC0CB, jsonResponse['url']))
        else:
            await ctx.send("La solicitud no se ha completado :(")



    @commands.command()
    @commands.is_nsfw()
    async def blowjob(self, ctx):
        jsonResponse = await apiRequest('https://purrbot.site/api/img/nsfw/blowjob/gif')

        if jsonResponse != False:
            await ctx.send(embed = embedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await ctx.send("La solicitud no se ha completado :(")



    @commands.command()
    @commands.is_nsfw()
    async def badneko(self, ctx):
        jsonResponse = await apiRequest('https://api.waifu.pics/nsfw/neko')

        if jsonResponse != False:
            await ctx.send(embed = embedCreate(0xFFC0CB, jsonResponse['url']))
        else:
            await ctx.send("La solicitud no se ha completado :(")



    @commands.command()
    @commands.is_nsfw()
    async def hentai(self, ctx):
        jsonResponse = await apiRequest('https://api.waifu.im/search/?included_tags=hentai')

        if jsonResponse != False:
            await ctx.send(embed = embedCreate(0xFFC0CB, jsonResponse['images'][0]['url']))
        else:
            await ctx.send("La solicitud no se ha completado :(")



    @commands.command()
    @commands.is_nsfw()
    async def milf(self, ctx):
        jsonResponse = await apiRequest('https://api.waifu.im/search/?included_tags=milf')

        if jsonResponse != False:
            await ctx.send(embed = embedCreate(0xFFC0CB, jsonResponse['images'][0]['url']))
        else:
            await ctx.send("La solicitud no se ha completado :(")



    @commands.command()
    @commands.is_nsfw()
    async def ass(self, ctx):
        jsonResponse = await apiRequest('https://api.waifu.im/search/?included_tags=ass')
        
        if jsonResponse != False:
            await ctx.send(embed = embedCreate(0xFFC0CB, jsonResponse['images'][0]['url']))
        else:
            await ctx.send("La solicitud no se ha completado :(")



    @commands.command()
    @commands.is_nsfw()
    async def oral(self, ctx):
        jsonResponse = await apiRequest('https://api.waifu.im/search/?included_tags=oral')
        
        if jsonResponse != False:
            await ctx.send(embed = embedCreate(0xFFC0CB, jsonResponse['images'][0]['url']))
        else:
            await ctx.send("La solicitud no se ha completado :(")



    @commands.command()
    @commands.is_nsfw()
    async def paizuri(self, ctx):
        jsonResponse = await apiRequest('https://api.waifu.im/search/?included_tags=paizuri')
        
        if jsonResponse != False:
            await ctx.send(embed = embedCreate(0xFFC0CB, jsonResponse['images'][0]['url']))
        else:
            await ctx.send("La solicitud no se ha completado :(")



    @commands.command()
    @commands.is_nsfw()
    async def ecchi(self, ctx):
        jsonResponse = await apiRequest('https://api.waifu.im/search/?included_tags=ecchi')
        
        if jsonResponse != False:
            await ctx.send(embed = embedCreate(0xFFC0CB, jsonResponse['images'][0]['url']))
        else:
            await ctx.send("La solicitud no se ha completado :(")



    @commands.command()
    @commands.is_nsfw()
    async def ero(self, ctx):
        jsonResponse = await apiRequest('https://api.waifu.im/search/?included_tags=ero')
        
        if jsonResponse != False:
            await ctx.send(embed = embedCreate(0xFFC0CB, jsonResponse['images'][0]['url']))
        else:
            await ctx.send("La solicitud no se ha completado :(")



    @commands.command()
    @commands.is_nsfw()
    async def anal (self, ctx):
        jsonResponse = await apiRequest('https://purrbot.site/api/img/nsfw/anal/gif')

        if jsonResponse != False:
            await ctx.send(embed = embedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await ctx.send("La solicitud no se ha completado :(")



    @commands.command()
    @commands.is_nsfw()
    async def cum (self, ctx):
        jsonResponse = await apiRequest('https://purrbot.site/api/img/nsfw/cum/gif')

        if jsonResponse != False:
            await ctx.send(embed = embedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await ctx.send("La solicitud no se ha completado :(")



    @commands.command()
    @commands.is_nsfw()
    async def fuck (self, ctx):
        jsonResponse = await apiRequest('https://purrbot.site/api/img/nsfw/fuck/gif')

        if jsonResponse != False:
            await ctx.send(embed = embedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await ctx.send("La solicitud no se ha completado :(")



    @commands.command()
    @commands.is_nsfw()
    async def pussylick (self, ctx):
        jsonResponse = await apiRequest('https://purrbot.site/api/img/nsfw/pussylick/gif')

        if jsonResponse != False:
            await ctx.send(embed = embedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await ctx.send("La solicitud no se ha completado :(")



    @commands.command()
    @commands.is_nsfw()
    async def solo (self, ctx):
        jsonResponse = await apiRequest('https://purrbot.site/api/img/nsfw/solo/gif')

        if jsonResponse != False:
            await ctx.send(embed = embedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await ctx.send("La solicitud no se ha completado :(")



    @commands.command()
    @commands.is_nsfw()
    async def triofff (self, ctx):
        jsonResponse = await apiRequest('https://purrbot.site/api/img/nsfw/threesome_fff/gif')

        if jsonResponse != False:
            await ctx.send(embed = embedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await ctx.send("La solicitud no se ha completado :(")



    @commands.command()
    @commands.is_nsfw()
    async def trioffm (self, ctx):
        jsonResponse = await apiRequest('https://purrbot.site/api/img/nsfw/threesome_ffm/gif')

        if jsonResponse != False:
            await ctx.send(embed = embedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await ctx.send("La solicitud no se ha completado :(")



    @commands.command()
    @commands.is_nsfw()
    async def triommf (self, ctx):
        jsonResponse = await apiRequest('https://purrbot.site/api/img/nsfw/threesome_mmf/gif')

        if jsonResponse != False:
            await ctx.send(embed = embedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await ctx.send("La solicitud no se ha completado :(")



    @commands.command()
    @commands.is_nsfw()
    async def yuri (self, ctx):
        jsonResponse = await apiRequest('https://purrbot.site/api/img/nsfw/yuri/gif')

        if jsonResponse != False:
            await ctx.send(embed = embedCreate(0xFFC0CB, jsonResponse['link']))
        else:
            await ctx.send("La solicitud no se ha completado :(")



    @commands.command()
    @commands.is_nsfw()
    async def trap (self, ctx):
        jsonResponse = await apiRequest('https://api.waifu.pics/nsfw/trap')

        if jsonResponse != False:
            await ctx.send(embed = embedCreate(0xFFC0CB, jsonResponse['url']))
        else:
            await ctx.send("La solicitud no se ha completado :(")





    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            await ctx.send('Este comando solo puede usarse en canales NSFW')


    
    

async def setup(bot):
    await bot.add_cog(nsfw(bot))