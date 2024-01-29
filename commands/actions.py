import discord, requests
from discord.ext import commands


from functions.functions import actionsFunction, apiRequest, botResponse




class actions(commands.Cog):



    def __init__(self, bot):
        self.bot = bot



    @commands.Cog.listener()
    async def on_ready(self):
        print("Action commands ready!")



    @commands.command()
    async def bully(self, ctx, member: discord.Member = None):
        url = "https://api.waifu.pics/sfw/bully"
        apiResponse = await apiRequest(url)
        
        response = actionsFunction("bully", ctx.author, member, self.bot.user.mention, apiResponse["url"])

        if member == self.bot.user:
            message = botResponse()
            if message:
                await ctx.send(message)
                return

        if response == False:
            await ctx.send("No hace nada")

        if isinstance(response, discord.Embed):
            await ctx.send(embed=response)

        elif isinstance(response, str):
            await ctx.send(response)





    @commands.command(aliases=["hug"])
    async def abrazo(self, ctx, member: discord.Member = None):

        url = "https://purrbot.site/api/img/sfw/hug/gif"
        apiResponse = await apiRequest(url)
        
        response = actionsFunction("hug", ctx.author, member, self.bot.user.mention, apiResponse['link'])

        if member == self.bot.user:
            message = botResponse()
            if message:
                await ctx.send(message)
                return
            
        if member == ctx.author:
            await ctx.send(f"\nNo puedes abrazarte a ti mismo. Deja hago eso por ti..."
                           f"\n>hug {ctx.author.mention}")

        if response == False:
            await ctx.send("No hace nada")

        if isinstance(response, discord.Embed):
            await ctx.send(embed=response)

        elif isinstance(response, str):
            await ctx.send(response)



    @commands.command(aliases=["cry"])
    async def llorar(self, ctx, member: discord.Member = None):

        url = "https://purrbot.site/api/img/sfw/cry/gif"
        apiResponse = await apiRequest(url)
        
        response = actionsFunction("cry", ctx.author, member, self.bot.user.mention, apiResponse['link'])

        if member == self.bot.user:
            message = botResponse()
            if message:
                await ctx.send(message)
                return

        if response == False:
            await ctx.send("No hace nada")

        if isinstance(response, discord.Embed):
            await ctx.send(embed=response)

        elif isinstance(response, str):
            await ctx.send(response)



    @commands.command(aliases=["kiss"])
    async def beso(self, ctx, member: discord.Member = None):

        url = "https://purrbot.site/api/img/sfw/kiss/gif"
        apiResponse = await apiRequest(url)
        
        response = actionsFunction("kiss", ctx.author, member, self.bot.user.mention, apiResponse['link'])

        if member == self.bot.user:
            message = botResponse()
            if message:
                await ctx.send(message)
                return

        if response == False:
            await ctx.send("No hace nada")

        if isinstance(response, discord.Embed):
            await ctx.send(embed=response)

        elif isinstance(response, str):
            await ctx.send(response)



    @commands.command(aliases=["lick"])
    async def lamer(self, ctx, member: discord.Member = None):

        url = "https://purrbot.site/api/img/sfw/lick/gif"
        apiResponse = await apiRequest(url)
        
        response = actionsFunction("lick", ctx.author, member, self.bot.user.mention, apiResponse['link'])

        if member == self.bot.user:
            message = botResponse()
            if message:
                await ctx.send(message)
                return

        if response == False:
            await ctx.send("No hace nada")

        if isinstance(response, discord.Embed):
            await ctx.send(embed=response)

        elif isinstance(response, str):
            await ctx.send(response)



    @commands.command(aliases=["pat"]) 
    async def acariciar(self, ctx, member: discord.Member = None):

        url = "https://purrbot.site/api/img/sfw/pat/gif"
        apiResponse = await apiRequest(url)
        
        response = actionsFunction("pat", ctx.author, member, self.bot.user.mention, apiResponse['link'])

        if member == self.bot.user:
            message = botResponse()
            if message:
                await ctx.send(message)
                return
            
        if member == ctx.author:
            await ctx.send(f"\nNecesitas alguien que te acaricie?"
                           f"\n>pat {ctx.author.mention}")

        if response == False:
            await ctx.send("No hace nada")

        if isinstance(response, discord.Embed):
            await ctx.send(embed=response)

        elif isinstance(response, str):
            await ctx.send(response)



    @commands.command()
    async def bonk(self, ctx, member: discord.Member = None):

        url = "https://api.waifu.pics/sfw/bonk"
        apiResponse = await apiRequest(url)
        
        response = actionsFunction("bonk", ctx.author, member, self.bot.user.mention, apiResponse['url'])

        if member == self.bot.user:
            message = botResponse()
            if message:
                await ctx.send(message)
                return

        if response == False:
            await ctx.send("No hace nada")

        if isinstance(response, discord.Embed):
            await ctx.send(embed=response)

        elif isinstance(response, str):
            await ctx.send(response)



    @commands.command(aliases=["blush"])
    async def verguenza(self, ctx, member: discord.Member = None):

        url = "https://purrbot.site/api/img/sfw/blush/gif"
        apiResponse = await apiRequest(url)
        
        response = actionsFunction("blush", ctx.author, member, self.bot.user.mention, apiResponse['link'])

        if member == self.bot.user:
            message = botResponse()
            if message:
                await ctx.send(message)
                return

        if response == False:
            await ctx.send("No hace nada")

        if isinstance(response, discord.Embed):
            await ctx.send(embed=response)

        elif isinstance(response, str):
            await ctx.send(response)



    @commands.command(aliases=["smile"])
    async def sonrreir(self, ctx, member: discord.Member = None):

        url = "https://purrbot.site/api/img/sfw/smile/gif"
        apiResponse = await apiRequest(url)
        
        response = actionsFunction("smile", ctx.author, member, self.bot.user.mention, apiResponse['link'])

        if member == self.bot.user:
            message = botResponse()
            if message:
                await ctx.send(message)
                return

        if response == False:
            await ctx.send("No hace nada")

        if isinstance(response, discord.Embed):
            await ctx.send(embed=response)

        elif isinstance(response, str):
            await ctx.send(response)


## CAMBIAR POR EL DE LA OTRA API POR FAVOR
    @commands.command(aliases=["hola", "wave"])
    async def hi(self, ctx, member: discord.Member = None):

        url = "https://api.waifu.pics/sfw/wave"
        apiResponse = await apiRequest(url)
        
        response = actionsFunction("wave", ctx.author, member, self.bot.user.mention, apiResponse['url'])

        if member == self.bot.user:
            message = botResponse()
            if message:
                await ctx.send(message)
                return

        if response == False:
            await ctx.send("No hace nada")

        if isinstance(response, discord.Embed):
            await ctx.send(embed=response)

        elif isinstance(response, str):
            await ctx.send(response)



    @commands.command(aliases=["handhold"])
    async def tomar(self, ctx, member: discord.Member = None):

        url = "https://api.waifu.pics/sfw/handhold"
        apiResponse = await apiRequest(url)
        
        response = actionsFunction("handhold", ctx.author, member, self.bot.user.mention, apiResponse['url'])

        if member == self.bot.user:
            message = botResponse()
            if message:
                await ctx.send(message)
                return

        if response == False:
            await ctx.send("No hace nada")

        if isinstance(response, discord.Embed):
            await ctx.send(embed=response)

        elif isinstance(response, str):
            await ctx.send(response)



    @commands.command(aliases=["eat", "nom"])
    async def comer(self, ctx, member: discord.Member = None):

        url = "https://api.waifu.pics/sfw/nom"
        apiResponse = await apiRequest(url)
        
        response = actionsFunction("nom", ctx.author, member, self.bot.user.mention, apiResponse['url'])

        if member == self.bot.user:
            message = botResponse()
            if message:
                await ctx.send(message)
                return

        if response == False:
            await ctx.send("No hace nada")

        if isinstance(response, discord.Embed):
            await ctx.send(embed=response)

        elif isinstance(response, str):
            await ctx.send(response)



    @commands.command(aliases=["bite"])
    async def morder(self, ctx, member: discord.Member = None):

        url = "https://purrbot.site/api/img/sfw/bite/gif"
        apiResponse = await apiRequest(url)
        
        response = actionsFunction("bite", ctx.author, member, self.bot.user.mention, apiResponse['link'])

        if member == self.bot.user:
            message = botResponse()
            if message:
                await ctx.send(message)
                return

        if response == False:
            await ctx.send("No hace nada")

        if isinstance(response, discord.Embed):
            await ctx.send(embed=response)

        elif isinstance(response, str):
            await ctx.send(response)



    @commands.command(aliases=["slap"])
    async def abofetear(self, ctx, member: discord.Member = None):

        url = "https://purrbot.site/api/img/sfw/slap/gif"
        apiResponse = await apiRequest(url)
        
        response = actionsFunction("slap", ctx.author, member, self.bot.user.mention, apiResponse['link'])

        if member == self.bot.user:
            message = botResponse()
            if message:
                await ctx.send(message)
                return

        if response == False:
            await ctx.send("No hace nada")

        if isinstance(response, discord.Embed):
            await ctx.send(embed=response)

        elif isinstance(response, str):
            await ctx.send(response)



    @commands.command(aliases=["tickle"])
    async def cosquillas (self, ctx, member: discord.Member = None):

        url = "https://purrbot.site/api/img/sfw/tickle/gif"
        apiResponse = await apiRequest(url)
        
        response = actionsFunction("tickle", ctx.author, member, self.bot.user.mention, apiResponse['link'])

        if member == self.bot.user:
            message = botResponse()
            if message:
                await ctx.send(message)
                return
            
        if member == ctx.author:
            await ctx.send(f"\nNo puedes hacer eso"
                           f"\n>tickle {ctx.author.mention}")

        if response == False:
            await ctx.send("No hace nada")

        if isinstance(response, discord.Embed):
            await ctx.send(embed=response)

        elif isinstance(response, str):
            await ctx.send(response)



    @commands.command()
    async def happy(self, ctx, member: discord.Member = None):

        url = "https://api.waifu.pics/sfw/happy"
        apiResponse = await apiRequest(url)
        
        response = actionsFunction("happy", ctx.author, member, self.bot.user.mention, apiResponse['url'])

        if member == self.bot.user:
            message = botResponse()
            if message:
                await ctx.send(message)
                return

        if response == False:
            await ctx.send("No hace nada")

        if isinstance(response, discord.Embed):
            await ctx.send(embed=response)

        elif isinstance(response, str):
            await ctx.send(response)



    @commands.command(aliases=["wink"])
    async def confia(self, ctx, member: discord.Member = None):

        url = "https://api.waifu.pics/sfw/wink"
        apiResponse = await apiRequest(url)
        
        response = actionsFunction("wink", ctx.author, member, self.bot.user.mention, apiResponse['url'])

        if member == self.bot.user:
            message = botResponse()
            if message:
                await ctx.send(message)
                return

        if response == False:
            await ctx.send("No hace nada")

        if isinstance(response, discord.Embed):
            await ctx.send(embed=response)

        elif isinstance(response, str):
            await ctx.send(response)



    @commands.command(aliases=["dance"])
    async def bailar(self, ctx, member: discord.Member = None):

        url = "https://purrbot.site/api/img/sfw/dance/gif"
        apiResponse = await apiRequest(url)
        
        response = actionsFunction("dance", ctx.author, member, self.bot.user.mention, apiResponse['link'])

        if member == self.bot.user:
            message = botResponse()
            if message:
                await ctx.send(message)
                return

        if response == False:
            await ctx.send("No hace nada")

        if isinstance(response, discord.Embed):
            await ctx.send(embed=response)

        elif isinstance(response, str):
            await ctx.send(response)



    @commands.command()
    async def cringe(self, ctx,  member: discord.Member = None):

        url = "https://api.waifu.pics/sfw/cringe"
        apiResponse = await apiRequest(url)
        
        response = actionsFunction("cringe", ctx.author, member, self.bot.user.mention, apiResponse['url'])

        if member == self.bot.user:
            message = botResponse()
            if message:
                await ctx.send(message)
                return

        if response == False:
            await ctx.send("No hace nada")

        if isinstance(response, discord.Embed):
            await ctx.send(embed=response)

        elif isinstance(response, str):
            await ctx.send(response)



    @commands.command(aliases=["pocke"])
    async def tocar(self, ctx, member: discord.Member = None):

        url = "https://purrbot.site/api/img/sfw/poke/gif"
        apiResponse = await apiRequest(url)
        
        response = actionsFunction("poke", ctx.author, member, self.bot.user.mention, apiResponse['link'])

        if member == self.bot.user:
            message = botResponse()
            if message:
                await ctx.send(message)
                return

        if response == False:
            await ctx.send("No hace nada")

        if isinstance(response, discord.Embed):
            await ctx.send(embed=response)

        elif isinstance(response, str):
            await ctx.send(response)





async def setup(bot):
    await bot.add_cog(actions(bot))





# si usas la tecla windos+'.' puedes ver los emojis 