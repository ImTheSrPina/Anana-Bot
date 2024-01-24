import discord

from discord.ext import commands
from discord.ui import Button, View



class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Help commands is here, you can receive help now")

    @commands.command(aliases=["h"])
    async def help(self, ctx):
        emb = discord.Embed(color= 0xFFC0CB)
        emb.add_field(name="Este es el mensaje de ayuda, ¿Puedes verlo?",
                      value="Tomamos la decision de enviarte toda la ayuda de forma personal, sientete comodo de preguntar cualquier cosa :D, solo presiona el boton para recibir el mensaje")

        button = Button(label="Enviar mensaje privado", style=discord.ButtonStyle.secondary)

        async def button_callback(interaction):
            button = Button(label="Mensaje enviado", style=discord.ButtonStyle.secondary, disabled=True)
            view = View() 
            view.add_item(button)
            await interaction.response.edit_message(view = view)

            e = discord.Embed(color= 0xFFC0CB)
            
            e.add_field(name="Mod commands",
                        value="Cuento con los clasicos comandos de moderacion como kick, ban, mute y unban, ademas del comando clear que te permite eliminar hasta 5 mensajes",
                        inline=False)
            
            eA = discord.Embed(color= 0xFFC0CB)

            eA.add_field(name="Mensajes de bienvenida y despedida",
                        value="Puedo enviar mensajes no personalizables de bienvenida y despedida a un canal en especifico, solo debes usar alguno de los anteriores comandos", inline=False)
            eA.add_field(name=">setwelcomechannel", value="", inline=True)
            eA.add_field(name=">setbyechannel", value="", inline=True)
            eA.add_field(name="", value="Escribiendo el comando y mencionando el canal, puedes establecer un canal de bienvenida o despedida", inline=False)
            eA.add_field(name="", value="Puedes desactivar esta caracteristica usando >disablewelcome y >disablebye", inline=False)

            eB = discord.Embed(color= 0xFFC0CB)

            eB.add_field(name="AUTO ROL", value="Puedo asignar un rol de forma automatica cuando un nuevo miembro ingresa al servidor, puedes usar el comando siguiente:", inline=False)
            eB.add_field(name="autorol", value="", inline=True)
            eB.add_field(name="", value="Despues, solo debes mencionar el rol que deseas que asigne a los nuevos miembros", inline=False)
            eB.add_field(name="", value="Puedes desactivar esta caracteristica usando >disableautorol", inline=False)

            e2 = discord.Embed(color= 0xFFC0CB)

            e2.add_field(name="ACCIONES", 
                        value="Hay una gran cantidad de comandos de acciones similares a Nekotina, no se porque lo tengo, preguntale al programador. A continuacion, hay un listado de estos", 
                        inline=False)
            e2.add_field(name="bully", value="", inline=True)
            e2.add_field(name="hug", value="", inline=True)
            e2.add_field(name="cry", value="", inline=True)
            e2.add_field(name="kiss", value="", inline=True)
            e2.add_field(name="lick", value="", inline=True)
            e2.add_field(name="pat", value="", inline=True)
            e2.add_field(name="bonk", value="", inline=True)
            e2.add_field(name="blush", value="", inline=True)
            e2.add_field(name="smile", value="", inline=True)
            e2.add_field(name="hi", value="", inline=True)
            e2.add_field(name="handhold", value="", inline=True)
            e2.add_field(name="eat", value="", inline=True)
            e2.add_field(name="bite", value="", inline=True)
            e2.add_field(name="slap", value="", inline=True)
            e2.add_field(name="tickle", value="", inline=True)
            e2.add_field(name="happy", value="", inline=True)
            e2.add_field(name="wink", value="", inline=True)
            e2.add_field(name="dance", value="", inline=True)
            e2.add_field(name="cringe", value="", inline=True)
            e2.add_field(name="pocke", value="", inline=True)
            e2.add_field(name="", value="Estos comandos pueden variar en el resultado si llegas a mencionar a alguien, giño giño", inline=False)

            e3 = discord.Embed(color= 0xFFC0CB)

            e3.add_field(name="WAIFUS", 
                        value="Las waifus venden y yo quiero vender", 
                        inline=False)
            e3.add_field(name="neko", value="", inline=True)
            e3.add_field(name="awoo", value="", inline=True)
            e3.add_field(name="megumin", value="", inline=True)
            e3.add_field(name="maid", value="", inline=True)
            e3.add_field(name="waifu", value="", inline=True)
            e3.add_field(name="marin", value="", inline=True)
            e3.add_field(name="mori", value="", inline=True)
            e3.add_field(name="raiden", value="", inline=True)
            e3.add_field(name="oppai", value="", inline=True)
            e3.add_field(name="selfie", value="", inline=True)
            e3.add_field(name="uniform", value="", inline=True)
            e3.add_field(name="shiro", value="", inline=True)
            e3.add_field(name="senko", value="", inline=True)
            e3.add_field(name="okami", value="", inline=True)
            e3.add_field(name="kitsune", value="", inline=True)
            e3.add_field(name="holo", value="", inline=True)
            e3.add_field(name="icon", value="", inline=True)
            e3.add_field(name="fluff", value="", inline=True)

            e4 = discord.Embed(color= 0xFFC0CB)

            e4.add_field(name="NSFW", 
                        value="Estos comandos solo pueden ser usados en canales con resticcion de edad, asi que asegurate de tener uno primero", 
                        inline=False)
            e4.add_field(name="badwaifu", value="", inline=True)
            e4.add_field(name="blowjob", value="", inline=True)
            e4.add_field(name="badneko", value="", inline=True)
            e4.add_field(name="hentai", value="", inline=True)
            e4.add_field(name="milf", value="", inline=True)
            e4.add_field(name="ass", value="", inline=True)
            e4.add_field(name="oral", value="", inline=True)
            e4.add_field(name="paizuri", value="", inline=True)
            e4.add_field(name="ecchi", value="", inline=True)
            e4.add_field(name="ero", value="", inline=True)
            e4.add_field(name="anal", value="", inline=True)
            e4.add_field(name="cum", value="", inline=True)
            e4.add_field(name="fuck", value="", inline=True)
            e4.add_field(name="pussylick", value="", inline=True)
            e4.add_field(name="solo", value="", inline=True)
            e4.add_field(name="triofff", value="", inline=True)
            e4.add_field(name="trioffm", value="", inline=True)
            e4.add_field(name="triommf", value="", inline=True)
            e4.add_field(name="yuri", value="", inline=True)
            e4.add_field(name="trap", value="", inline=True)


            e5 = discord.Embed(color= 0xFFC0CB)

            e5.add_field(name="FUNCIONES ADICIONALES", 
                        value="Algunos comandos que te pueden ser de utilidad ;) ", 
                        inline=False)
            e5.add_field(name="avatar", value="", inline=True)
            e5.add_field(name="say", value="", inline=True)
            e5.add_field(name="server", value="", inline=True)
            e5.add_field(name="profile", value="", inline=True)
            e5.add_field(name="emoji", value="", inline=True)
            e5.add_field(name="ñonga", value="", inline=True)


            await ctx.message.author.send("Cuento con una mediana cantidad de comandos que pueden sere de ayuda para ti y los miembros de tu servidor, como los siguientes:")
            await ctx.message.author.send(embed=e)
            await ctx.message.author.send(embed=eA)
            await ctx.message.author.send(embed=eB)
            await ctx.message.author.send(embed=e2)
            await ctx.message.author.send(embed=e3)
            await ctx.message.author.send(embed=e4)
            await ctx.message.author.send(embed=e5)
            await ctx.message.author.send("Por ultimo, tengo una especie de comando secreto secreto my secreto, tal ves demuestra mi Conciencia o los pensamientos del programador...")


        button.callback = button_callback
        
        view = View()
        view.add_item(button)
        await ctx.send(embed=emb, view=view)









    @commands.command(aliases=["soporte"])
    async def suport(self, ctx):
        await ctx.send("Te enviare un mensaje al privado ;) ")
        await ctx.message.author.send("¡¡Hola!!")
        await ctx.message.author.send("Para adquirir soporte tecnico sobre el bot, puedes ingresar a mi servidor y contactar al programador")
        await ctx.message.author.send("https://discord.gg/eearJ7cy")
    

async def setup(bot):
    await bot.add_cog(help(bot))