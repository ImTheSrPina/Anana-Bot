import discord, random
from discord.ext import commands


from functions.functions import embedCreate


class utilities(commands.Cog):



    def __init__(self, bot):
        self.bot = bot





    @commands.Cog.listener()
    async def on_ready(self):
        print("Utilities ready!")





    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.message.reply(embed = embedCreate((0xFFFFFF), (ctx.author.avatar), (f"Avatar de {ctx.author.name}")))
        else:
            await ctx.message.reply(embed = embedCreate((0xFFFFFF), (member.avatar.url), (f"Avatar de {member.name}")))



    @commands.command()
    #Cooldownm(No. de intentos, segundos hasta volver a usar)
    @commands.cooldown(5, 43200, commands.BucketType.user)
    async def say(self, ctx, *, user_message):
        if user_message is None:
            await ctx.message.reply(f"\n¿Qué quieres que diga?"
                                    f"\nHas desperdiciado tu unica oportunidad de usar este comando")
        else:
            await ctx.message.delete()
            await ctx.send(user_message)
        
            

    @commands.command(aliases=["servidor", "serv", "guild"])
    async def server(self, ctx):

        date=ctx.guild.created_at.strftime("%b-%d-%m-%Y")

        serverData={
            "Servidor" : ctx.guild.name,
            "ID de servidor" : ctx.guild.id,
            "Fecha de creacion" : date,
            "Propietario" : ctx.guild.owner.mention,
            "No. de canales" : len(ctx.guild.channels),
            "Miembros" : ctx.guild.member_count,
            "Description" : ctx.guild.description,
        }
        emb = embedCreate(0x000000, title = "Perfil de servidor", tumbail = f"{ctx.guild.icon}", objetItems = serverData)
        await ctx.send(embed = emb)



    @commands.command(aliases=["profile", "alex"])
    async def perfil(self, ctx, member: discord.Member = None):
        if member is None:

            serverData={
                "Usuario" : ctx.author.mention,
                "ID" : ctx.author.id,
                "Creacion de cuenta" : ctx.author.created_at.strftime("%b-%d-%m-%Y"),
                "Se unio el" : ctx.author.joined_at.strftime("%b-%d-%m-%Y"),
                "Rol mas alto" : ctx.author.top_role,
            }
            emb = embedCreate(0x000000, title = "Perfil de usuario", tumbail = f"{ctx.author.avatar}", objetItems = serverData)
            await ctx.send(embed = emb)

        else:
            emb = discord.Embed(title=f"Perfil de {member.name}", color= 0x000000)

            serverData={
                "Usuario" : member.mention,
                "ID" : member.id,
                "Creacion de cuenta" : member.created_at.strftime("%b-%d-%m-%Y"),
                "Se unio el" : member.joined_at.strftime("%b-%d-%m-%Y"),
                "Rol mas alto" : member.top_role,
            }
            emb = embedCreate(0x000000, title = "Perfil de usuario", tumbail = f"{member.avatar}", objetItems = serverData)
            await ctx.send(embed = emb)



    @commands.command()
    async def emoji(self, ctx, emoji: discord.Emoji = None):

        if emoji is None:
            await ctx.send("Debes decirme que emoji mostrar")
        else:
            await ctx.send(embed = embedCreate(0xEA9262, url = f"{emoji.url}", title = f"{emoji.name}"))



    @commands.command(aliases=["pija", "banana", "chorizo", "longaniza", "longametro", "pllin", "pirulin"])
    async def ñonga(self, ctx, member: discord.Member = None):
        if member is None:
            largo_de_la_ñonga= "{:.2f}".format(random.uniform(1, 50))
            await ctx.message.reply(f"La ñonga te mide {largo_de_la_ñonga} cm, yo lo confirmo pibes")
        else:
            largo_de_la_ñonga= "{:.2f}".format(random.uniform(1, 50))
            await ctx.message.reply(f"La ñonga de {member.name} mide {largo_de_la_ñonga} cm. ¡¡A la verga!!")




    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if isinstance(error, commands.MissingPermissions):
            await ctx.send("No tienes suficientes permisos para usar este comando.")
        
        if isinstance(error, commands.CommandOnCooldown):
            time = round(error.retry_after)

            if time < 60:
                await ctx.send(
                    f"No puedes usar este comando en {time} segundos")
                
            elif time > 360:
                horas = int (time / 3600)
                await ctx.send(
                    f"No puedes usar este comando en {horas} horas")

            else:
                minutos = int (time / 60)
                await ctx.send(
                    f"No puedes usar este comando en {minutos} minutos")

async def setup(bot):
    await bot.add_cog(utilities(bot))