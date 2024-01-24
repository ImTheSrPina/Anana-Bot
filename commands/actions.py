import discord, requests

from discord.ext import commands


# FUNCTIONS: GET IMAGES AND GIFS

async def getWaifuPics(tag):
        animeAPI = requests.get(f"https://api.waifu.pics/sfw/{tag}")
        waifu = animeAPI.json()["url"]
        return waifu


async def getWaifuPurrbot(tag):
        animeAPI = requests.get(f"https://purrbot.site/api/img/sfw/{tag}/gif")
        waifu = animeAPI.json()["link"]
        return waifu


class actions(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Action commands ready!")


    @commands.command()
    async def bully(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("Debes mencionar alguna persona")
        else:
            emb = discord.Embed(title=f"{ctx.author.name} molesta a {member.name}", color= 0xFFC0CB)
            emb.set_image(url=await getWaifuPics("bully"))
            await ctx.send(embed=emb)

    @commands.command(aliases=["hug"])
    async def abrazo(self, ctx, member: discord.Member = None):
        if member is None:
            emb = discord.Embed(title=f"{ctx.author.name} necesita un abrazo :( ", color= 0xFFC0CB)
            emb.set_image(url=await getWaifuPurrbot("hug"))
            await ctx.send(embed=emb)
        elif member == ctx.author:
            await ctx.send("No puedes abrazarte a ti mismo. Deja hago eso por ti...")
            await ctx.send(f">abrazo {ctx.author.mention}")
            emb = discord.Embed(title=f"{self.bot.user} abraza a {ctx.author.name} >_<", color= 0xFFC0CB)
            emb.set_image(url=await getWaifuPurrbot("hug"))
            await ctx.send(embed=emb)
        elif member == self.bot.user:
            await ctx.send("Se supone que debes mencionar alguna persona, no a mi... 🗿")
        else:
            emb = discord.Embed(title=f"{ctx.author.name} abraza a {member.name}", color= 0xFFC0CB)
            emb.set_image(url=await getWaifuPurrbot("hug"))
            await ctx.send(embed=emb)

    @commands.command(aliases=["cry"])
    async def llorar(self, ctx):
        emb = discord.Embed(title=f"{ctx.author.name} comenzó a llorar :(", color= 0xFFC0CB)
        emb.set_image(url=await getWaifuPurrbot("cry"))
        await ctx.send(embed=emb)

    @commands.command(aliases=["kiss"])
    async def beso(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("Debes mencionar alguna persona")
        elif member == ctx.author:
            await ctx.send("No creo que te puedas besar a ti mismo, a no ser que uses un espejo 🙂")
        elif member == self.bot.user:
            await ctx.send("*Se asusta*")
        else:
            emb = discord.Embed(title=f"{ctx.author.name} besó a {member.name} >_<", color= 0xFFC0CB)
            emb.set_image(url=await getWaifuPurrbot("kiss"))
            await ctx.send(embed=emb)

    @commands.command(aliases=["lick"])
    async def lamer(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("Debes mencionar alguna persona")
        elif member == ctx.author:
            await ctx.send("Vas a lamer tu mano, ¿O algo asi?")
        elif member == self.bot.user:
            await ctx.message.reply("No creo que puedas lamerme, a no ser que lamas tu celular, lo que sea que uses para ver discord")
        else:
            emb = discord.Embed(title=f"{ctx.author.name} lamio a {member.name} >_<", color= 0xFFC0CB)
            emb.set_image(url=await getWaifuPurrbot("lick"))
            await ctx.send(embed=emb)

    @commands.command(aliases=["pat"]) 
    async def acariciar(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("Debes mencionar alguna persona")
        elif member == ctx.author:
            await ctx.send("¿Vas a intentar acariciarte a ti mismo? Deja hago eso por ti...")
            await ctx.send(f">acariciar {ctx.author.mention}")
            emb = discord.Embed(title=f"{self.bot.user} acaricio a {ctx.author.mention} >_<", color= 0xFFC0CB)
            emb.set_image(url=await getWaifuPurrbot("pat"))
            await ctx.send(embed=emb)
        elif member == self.bot.user:
            await ctx.message.reply("gracias... supongo")
        else:
            emb = discord.Embed(title=f"{ctx.author.name} acaricio a {member.name} >_<", color= 0xFFC0CB)
            emb.set_image(url=await getWaifuPurrbot("pat"))
            await ctx.send(embed=emb)

    @commands.command()
    async def bonk(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("Debes mencionar alguna persona")
        elif member == ctx.author:
            await ctx.send("La autolesion no es buena :( ")
        elif member == self.bot.user:
            emb = discord.Embed(title=f"{self.bot.user} responde con un golpe a {ctx.author.name}", color= 0xFFC0CB)
            emb.set_image(url=await getWaifuPics("bonk"))
            await ctx.message.reply(embed=emb)
        else:
            emb = discord.Embed(title=f"{ctx.author.name} golpea a {member.name} 🙀", color= 0xFFC0CB)
            emb.set_image(url=await getWaifuPics("bonk"))
            await ctx.send(embed=emb)

    @commands.command(aliases=["blush"])
    async def verguenza(self, ctx):
        emb = discord.Embed(title=f"{ctx.author.name} siente vergüenza", color= 0xFFC0CB)
        emb.set_image(url=await getWaifuPurrbot("blush"))
        await ctx.send(embed=emb)

    @commands.command(aliases=["smile"])
    async def sonrreir(self, ctx):
        emb = discord.Embed(title=f"{ctx.author.name} esta sonrriendo", color= 0xFFC0CB)
        emb.set_image(url=await getWaifuPurrbot("smile"))
        await ctx.send(embed=emb)

    @commands.command(aliases=["hola", "wave"])
    async def hi(self, ctx, member: discord.Member = None):
        if member is None:
            emb = discord.Embed(title=f"{ctx.author.name} saluda a todo el mundo :D ", color= 0xFFC0CB)
            emb.set_image(url=await getWaifuPics("wave"))
            await ctx.send(embed=emb)
        elif member == ctx.author:
            await ctx.send("Deberias tratar de saludar a alguien mas, intenta mencionar a alguna persona :) ")
        elif member == self.bot.user:
            emb = discord.Embed(title=f"Hola {ctx.author.name} 😃", color= 0xFFC0CB)
            emb.set_image(url=await getWaifuPics("wave"))
            await ctx.message.reply(embed=emb)
        else:
            emb = discord.Embed(title=f"{ctx.author.name} saluda a {member.name}", color= 0xFFC0CB)
            emb.set_image(url=await getWaifuPics("wave"))
            await ctx.send(embed=emb)

    @commands.command(aliases=["handhold"])
    async def tomar(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("Debes mencionar alguna persona")
        elif member == ctx.author:
            await ctx.message.reply("¿Tratas de tomar tu mano? ¿Por qué harias algo asi?")
        elif member == self.bot.user:
            await ctx.message.reply("Gracias, pero yo no tengo manos")
        else:
            emb = discord.Embed(title=f"{ctx.author.name} toma la mano de {member.name}", color= 0xFFC0CB)
            emb.set_image(url=await getWaifuPics("handhold"))
            await ctx.send(embed=emb)

    @commands.command(aliases=["eat"])
    async def comer(self, ctx):
        emb = discord.Embed(title=f"{ctx.author.name} está comiendo, ñom", color= 0xFFC0CB)
        emb.set_image(url=await getWaifuPics("nom"))
        await ctx.send(embed=emb)

    @commands.command(aliases=["bite"])
    async def morder(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("Debes mencionar alguna persona")
        elif member == ctx.author:
            await ctx.message.reply("¡¡Espera!! no te muerdas a ti mismo")
        elif member == self.bot.user:
            emb = discord.Embed(
                title=f"{ctx.author.name} muerde el cable de su internet sin ningun exito", 
                color= 0xFFC0CB)
            emb.set_image(url=await getWaifuPurrbot("bite"))
            await ctx.send(embed=emb)
        else:
            emb = discord.Embed(title=f"{ctx.author.name} mordió a {member.name}", color= 0xFFC0CB)
            emb.set_image(url=await getWaifuPurrbot("bite"))
            await ctx.send(embed=emb)

    @commands.command(aliases=["slap"])
    async def abofetear(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("Debes mencionar alguna persona")
        elif member == ctx.author:
            await ctx.message.reply("Esto, es raro ¿no?")
        elif member == self.bot.user:
            await ctx.message.reply("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        else:
            emb = discord.Embed(title=f"{ctx.author.name} abofeteó a {member.name}", color= 0xFFC0CB)
            emb.set_image(url=await getWaifuPurrbot("slap"))
            await ctx.send(embed=emb)

    @commands.command(aliases=["tickle"])
    async def cosquillas (self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("Debes mencionar alguna persona")
        elif member == ctx.author:
            await ctx.message.reply("¿Es posible hacerte cosquillas a ti mismo? No, no es posible hacerte cosquillas a ti mismo en el sentido tradicional de la experiencia física. Las cosquillas son una respuesta nerviosa a estímulos impredecibles y a menudo inesperados en áreas sensibles de la piel. Esta respuesta se origina en parte en el cerebro y es difícil de replicar conscientemente en uno mismo.")
        elif member == self.bot.user:
            await ctx.message.reply("Como soy un simple programa de python, me es imposible sentir algo...")
        else:
            emb = discord.Embed(title=f"{ctx.author.name} le hace cosquillas a {member.name}", color= 0xFFC0CB)
            emb.set_image(url=await getWaifuPurrbot("tickle"))
            await ctx.send(embed=emb)

    @commands.command()
    async def happy(self, ctx):
        emb = discord.Embed(title=f"{ctx.author.name} está feliz :)", color= 0xFFC0CB)
        emb.set_image(url=await getWaifuPics("happy"))
        await ctx.send(embed=emb)

    @commands.command(aliases=["wink"])
    async def confia(self, ctx):
        emb = discord.Embed(title="Solo confien", color= 0xFFC0CB)
        emb.set_image(url=await getWaifuPics("wink"))
        await ctx.send(embed=emb)

    @commands.command(aliases=["dance"])
    async def bailar(self, ctx):
        emb = discord.Embed(title=f"{ctx.author.name} comenzó a bailar", color= 0xFFC0CB)
        emb.set_image(url=await getWaifuPurrbot("dance"))
        await ctx.send(embed=emb)

    @commands.command()
    async def cringe(self, ctx):
        emb = discord.Embed(color= 0xFFC0CB)
        emb.set_image(url=await getWaifuPics("cringe"))
        await ctx.send(embed=emb)

    @commands.command(aliases=["pocke"])
    async def tocar(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("Debes mencionar alguna persona")
        elif member == ctx.author:
            await ctx.message.reply("Tu y yo sabemos que si lo digo sonara raro")
        elif member == self.bot.user:
            await ctx.message.reply("Tocamé esta")
        else:
            emb = discord.Embed(title=f"{ctx.author.name} tocó a {member.name}", color= 0xFFC0CB)
            emb.set_image(url=await getWaifuPurrbot("poke"))
            await ctx.send(embed=emb)

async def setup(bot):
    await bot.add_cog(actions(bot))





# si usas la tecla windos+'.' puedes ver los emojis 