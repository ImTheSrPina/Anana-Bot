import discord, json

from discord.ext import commands


from functions.functions import modEmbed



class mod(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Mod commands ready!")


    

    @commands.command()
    async def testembedmod(self, ctx):
        await ctx.send(embed = modEmbed(ctx, f"{ctx.author.name} expulsado!!!", "Test de embed de administración"))



    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member = None, *, reason="Sin especificar"):
        if member is None:
            await ctx.send("Debes mencionar a un miembro")

        elif member == ctx.author:
            await ctx.send("Si deseas salir de aqui, solo hazlo!")

        elif member == self.bot.user:
            await ctx.send("Ustedes... Me quieren expulsar :( ?")

        elif member is not None:
            await member.remove_roles(reason="Expulsado")

            await member.kick(reason=reason) 
            emb=discord.Embed(
                title= f"¡{member.name} expulsado!", 
                description=f"Un miembro ha sido expulsado por {ctx.author.name}", 
                color=0xFF0000
                )
            emb.add_field(
                name= "User name", 
                value=f"{member.mention}"
                )
            emb.add_field(
                name= "Motivo", 
                value=f"{reason}"
                )
            await ctx.send(embed=emb)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member = None, *, reason="Sin especificar"):
        if member is None:
            await ctx.send("Debes mencionar a un miembro")

        elif member == ctx.author:
            await ctx.send("Imposible, no te puedo banear a ti, hazlo tu...")

        elif member == self.bot.user:
            await ctx.send("Emotiza insana")

        else:
            await member.remove_roles(reason="Ban")

            await ctx.guild.ban(member) 
            emb=discord.Embed(
                title= f"¡{member.name} baneado!", 
                description=f"Un miembro ha sido baneado por {ctx.author.name}", 
                color=0xFF0000
                )
            emb.add_field(
                name= "User name", 
                value=f"{member.mention}"
                )
            emb.add_field(
                name= "Motivo", 
                value=f"{reason}"
                )
            await ctx.send(embed=emb)
        
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("Debes mencionar a un miembro")

        elif member == ctx.author:
            await ctx.send("No creo que te encuentres baneado... o si?")

        elif member == self.bot.user:
            await ctx.send("Des ban eada")

        else:
            user= discord.Object(id=member.id)
            await ctx.guild.unban(user)
            emb = discord.Embed(color= 0xFF0000, title="¡¡Des Ban eado!!", description="")
            await ctx.send(embed=emb)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, count: int):
        count = count + 1

        if count > 6:
            await ctx.send("Solo puedes eliminar 5 mensajes a la vez, esto solo es un medio de seguridad")

        else:
            try:
                dato_int = int(count)
                await ctx.channel.purge(limit=count)
                await ctx.send(f"{dato_int-1} mensajes eliminados con exito")

            except ValueError:
                await ctx.send("Debes escribir un numero, no puedo leer palabras o numeros decimales en este comando")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, member: discord.Member = None):
        silence_rol = discord.utils.get(ctx.guild.roles, name="Silenciado")
        if not silence_rol:
            await ctx.send("No existe un rol de silenciado, ejecuta el comando rolmute para crear uno")

        elif member is None:
            await ctx.send("Debes mencionar a un miembro")

        elif member == ctx.author:
            await ctx.send("No creo que quieras silenciarte a ti mismo")

        elif member == self.bot.user:
            await ctx.send("No puedes sileciarme, yo soy la que silencia!!")

        else:
            await member.add_roles(silence_rol)
            await ctx.send(f"{member.mention} ha sido silenciado")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unmute(self, ctx, member: discord.Member = None):
        silence_rol = discord.utils.get(ctx.guild.roles, name="Silenciado")

        if not silence_rol:
            await ctx.send("No existe un rol de silenciado, ejecuta el comando rolmute para crear uno")
        
        elif member is None:
            await ctx.send("Debes mencionar a un miembro")

        elif member == ctx.author:
            await ctx.send("¿Tratas de quitarte un silencio? ¿Por qué?")

        elif member == self.bot.user:
            await ctx.send("Actualmente no estoy silenciada, pero si deseas que lo esté, intentalo...")

        elif silence_rol in member.roles:
            await member.remove_roles(silence_rol)
            await ctx.send(f"Se ha revocado el silencio a {member.mention}")

        else:
            await ctx.send(f"{member.mention} no se encuentra silenciado")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def rolmute(self, ctx):
        # Crear rol de silencio
        silence_rol = discord.utils.get(ctx.guild.roles, name="Silenciado")

        if not silence_rol:
            async with ctx.typing():
                await ctx.send("Creando rol...")
                rol_color= discord.Colour.from_rgb(0, 0, 0)
                silence_rol= await ctx.guild.create_role(
                    name="Silenciado", 
                    colour=rol_color,
                    permissions=discord.Permissions(send_messages=False, speak=False))
                
                await ctx.send("Asignando permisos...")
                for canal in ctx.guild.text_channels:
                    await canal.set_permissions(silence_rol, send_messages=False, speak=False)

                await ctx.send("Permisos asignados")
                await ctx.send("Se ha creado el rol de Silenciado")
                await ctx.send(
                    "En dado caso de que el silenciado no funcione, verifica que el rol de silenciado tenga la jerarquia mas alta de roles")
                await ctx.send("Puedes personalizar el color del rol, pero recuerda, no modifiques para nada el nombre")

        else:
            await ctx.send("El rol de Silenciado ya existe")


    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("No tienes suficientes permisos para usar este comando.")

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("No tienes suficientes permisos para usar este comando.")

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("No tienes suficientes permisos para usar este comando.")
            
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("No tienes suficientes permisos para usar este comando.")
        
    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("No tienes suficientes permisos para usar este comando.")

    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("No tienes suficientes permisos para usar este comando.")
    
    @rolmute.error
    async def rolmute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("No tienes suficientes permisos para usar este comando.")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def rol(self, ctx, member: discord.Member=None, role: discord.Role=None):
        if member is None:
            await ctx.send("Debes mencionar a alguien")
        
        elif member is ctx.author:
            await ctx.send("Si vas a asginarte un rol, hazlo tu mismo desde las configuraciones del servidor")

        elif member is self.bot.user:
            await ctx.send("Gracias pero no gracias")

        else:
            if role is None:
                await ctx.send("Debes mencionar un rol")
            
            else:
                await member.add_roles(role)
                await ctx.send(f"Rol asignado a {member.mention}")

    @commands.command(aliases=["revocarol"])
    @commands.has_permissions(administrator=True)
    async def removerol(self, ctx, member: discord.Member=None, role: discord.Role=None):
        if member is None:
            await ctx.send("Debes mencionar a alguien")
        
        elif member is ctx.author:
            await ctx.send("No puedo quitarte un rol")

        elif member is self.bot.user:
            await ctx.send("Gracias pero no gracias")

        else:
            if role is None:
                await ctx.send("Debes mencionar un rol")
            
            else:
                await member.remove_roles(role)
                await ctx.send(f"Rol revocado a {member.mention}")

    @rol.error
    async def rol_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("No tienes suficientes permisos para usar este comando.")

    @removerol.error
    async def removerol_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("No tienes suficientes permisos para usar este comando.")


async def setup(bot):
    await bot.add_cog(mod(bot))