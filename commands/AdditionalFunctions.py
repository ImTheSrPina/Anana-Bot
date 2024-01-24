import discord, json, random

from discord.ext import commands



class AdditionalFunctions(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Additional Functions ready!")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setwelcomechannel(self, ctx, canal: discord.TextChannel):
        servidor_id = str (ctx.guild.id)

        with open('json/WelcomeChannel_IDs.json', 'r') as json_file:
            data = json.load(json_file)

        # Verificar si el servidor ya tiene un canal asociado
        if servidor_id in data:
            del data[servidor_id]
            # Actualizar el ID del canal existente para el servidor actual
            data[servidor_id] = canal.id
            await ctx.send(
                f'Se ha actualizado el canal de bienvenida al canal {canal.mention}.')
            
        else:
            data[servidor_id] = canal.id
            await ctx.send(
                f'Se ha configurado el canal de bienvenida al canal {canal.mention}.')

        # Guardar los IDs actualizados en el archivo JSON
        with open('json/WelcomeChannel_IDs.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setbyechannel(self, ctx, canal: discord.TextChannel):
        servidor_id = str (ctx.guild.id)

        with open('json/ByeChannel_IDs.json', 'r') as json_file:
            data = json.load(json_file)

        # Verificar si el servidor ya tiene un canal asociado
        if servidor_id in data:
            del data[servidor_id]
            # Actualizar el ID del canal existente para el servidor actual
            data[servidor_id] = canal.id
            await ctx.send(
                f'Se ha actualizado el canal de despedidas al canal {canal.mention}.')
            
        else:
            data[servidor_id] = canal.id
            await ctx.send(
                f'Se ha configurado el canal de despedidas al canal {canal.mention}.')

        # Guardar los IDs actualizados en el archivo JSON
        with open('json/ByeChannel_IDs.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def autorol(self, ctx, rol: discord.Role):
        # Obtener el ID del servidor y el ID del rol
        servidor_id = str (ctx.guild.id)

        with open('json/Rol_IDs.json', 'r') as json_file:
            data = json.load(json_file)

        if servidor_id in data:
            del data[servidor_id]
            data[servidor_id] = rol.id
            await ctx.send(
                f"Se ha reconfigurado el rol automatico a {rol.mention} para los nuevos miembros ^_^")

        else:
            data[servidor_id] = rol.id
            await ctx.send(
                f"No te preocupes, ahora me encargare de asignar el rol {rol.mention} a los nuevos miembros ^_^")

        with open('json/Rol_IDs.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def disablewelcome(self, ctx):
        servidor_id = str (ctx.guild.id)

        with open('json/WelcomeChannel_IDs.json', 'r') as json_file:
            data = json.load(json_file)

        if servidor_id in data:
            del data[servidor_id]
            
            with open('json/WelcomeChannel_IDs.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)
            await ctx.send(
                f"Canal de bienvenidas desactivado")
        
        else:
            await ctx.send("No se ha configurado un canal de bienvenidas")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def disablebye(self, ctx):
        servidor_id = str (ctx.guild.id)

        with open('json/ByeChannel_IDs.json', 'r') as json_file:
            data = json.load(json_file)

        if servidor_id in data:
            del data[servidor_id]

            with open('json/ByeChannel_IDs.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)

            await ctx.send(
                f"Canal de despedidas desactivado")
        
        else:
            await ctx.send("No se ha configurado un canal de despedidas")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def disableautorol(self, ctx):
        servidor_id = str (ctx.guild.id)

        with open('json/Rol_IDs.json', 'r') as json_file:
            data = json.load(json_file)

        if servidor_id in data:
            del data[servidor_id]

            with open('json/Rol_IDs.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)
            await ctx.send(
                f"Autoroles desactivado, para volver a activar, usa el comando autorol")
        
        else:
            await ctx.send("No se ha configurado un rol a asignar")



    @setwelcomechannel.error
    async def setwelcomechannel_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("No tienes suficientes permisos para usar este comando.")

    @setbyechannel.error
    async def setbyechannel_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("No tienes suficientes permisos para usar este comando.")

    @autorol.error
    async def autorol_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("No tienes suficientes permisos para usar este comando.")

    @disablewelcome.error
    async def disablewelcome_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("No tienes suficientes permisos para usar este comando.")

    @disablebye.error
    async def disablebye_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("No tienes suficientes permisos para usar este comando.")

    @disableautorol.error
    async def disableautorol_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("No tienes suficientes permisos para usar este comando.")


    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):
        if member is None:
            emb = discord.Embed (title=f"Avatar de {ctx.author.name}",color= 0xFFC0CB)
            emb.set_image(url=ctx.author.avatar)
            await ctx.message.reply(embed=emb)
        else:
            emb = discord.Embed(title=f"Avatar de {member.name}",color= 0xFFC0CB)
            emb.set_image(url=member.avatar.url)
            await ctx.message.reply(embed=emb)


    @commands.command()
    #Cooldownm(No. de intentos, segundos hasta volver a usar)
    @commands.cooldown(5, 43200, commands.BucketType.user)
    async def say(self, ctx, *, user_message):
        if user_message is None:
            await ctx.message.reply("¿Qué quieres que diga?")
            await ctx.message.send("Has desperdiciado tu unica oportunidad de usar este comando")
        
        else:
            await ctx.send(user_message)
            await ctx.message.delete()

    @say.error
    async def say_error(self, ctx, error):
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
            

    @commands.command(aliases=["servidor", "serv", "guild"])
    async def server(self, ctx):
        emb = discord.Embed(title=f"Perfil de servidor", color= 0x000000)
 
        serverData={
            "Servidor" : ctx.guild.name,
            "Propietario" : ctx.guild.owner.mention,
            "ID de servidor" : ctx.guild.id,
            "No. de canales" : len(ctx.guild.channels),
            "Miembros" : ctx.guild.member_count,
            "Description" : ctx.guild.description,
        }

        for [name, value] in serverData.items():
            emb.add_field(name=name+":",value=value, inline=True)

        date=ctx.guild.created_at.strftime("%b-%d-%m-%Y")
        emb.set_footer(text=f"Fecha de creacion: {date}")

        emb.set_thumbnail(url=ctx.guild.icon)

        await ctx.send(embed=emb)

    @commands.command(aliases=["profile", "alex"])
    async def perfil(self, ctx, member: discord.Member = None):
        if member is None:
            emb = discord.Embed(title=f"Perfil de {ctx.author.name}", color= 0x000000)

            serverData={
                "Usuario" : ctx.author.mention,
                "ID" : ctx.author.id,
                "Creacion de cuenta" : ctx.author.created_at.strftime("%b-%d-%m-%Y"),
                "Se unio el..." : ctx.author.joined_at.strftime("%b-%d-%m-%Y"),
                "Rol mas alto" : ctx.author.top_role,
            }

            for [name, value] in serverData.items():
                emb.add_field(name=name+":",value=value, inline=True)


            emb.set_thumbnail(url=ctx.author.avatar)

            await ctx.send(embed=emb)

        else:
            emb = discord.Embed(title=f"Perfil de {member.name}", color= 0x000000)

            serverData={
                "Usuario" : member.mention,
                "ID" : member.id,
                "Creacion de cuenta" : member.created_at.strftime("%b-%d-%m-%Y"),
                "Se unio el..." : member.joined_at.strftime("%b-%d-%m-%Y"),
                "Rol mas alto" : member.top_role,
            }

            for [name, value] in serverData.items():
                emb.add_field(name=name+":",value=value, inline=True)


            emb.set_thumbnail(url=member.avatar.url)

            await ctx.send(embed=emb)

    @commands.command()
    async def emoji(self, ctx, emoji: discord.Emoji = None):

        if emoji is None:
            await ctx.send("Debes decirme que emoji mostrar")

        else:

            await ctx.send(emoji.name)
            await ctx.send(emoji.url)

    @commands.command(aliases=["pija", "banana", "chorizo", "longaniza", "longametro", "pillin", "pirulin"])
    async def ñonga(self, ctx, member: discord.Member = None):
        if member is None:
            largo_de_la_ñonga= "{:.2f}".format(random.uniform(1, 50))
            await ctx.message.reply(f"La ñonga te mide {largo_de_la_ñonga} cm, yo lo confirmo pibes")
        else:
            largo_de_la_ñonga= "{:.2f}".format(random.uniform(1, 50))
            await ctx.message.reply(f"La ñonga de {member.name} mide {largo_de_la_ñonga} cm. ¡¡A la verga!!")

async def setup(bot):
    await bot.add_cog(AdditionalFunctions(bot))