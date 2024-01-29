import discord
from discord.ext import commands


from functions.functions import modEmbed, checkMention


class mod(commands.Cog):





    def __init__(self, bot):
        self.bot = bot





    @commands.Cog.listener()
    async def on_ready(self):
        print("Mod prefix commands loaded")



    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member = None, *, reason = "Sin especificar"):

        try:
            mention = checkMention(member, ctx.author, self.bot.user)

            if mention is True:
                async with ctx.typing():
                    await member.remove_roles(reason="Expulsado")
                    await member.kick(reason=reason) 
                    await ctx.send(embed = modEmbed(
                        ctx.author.name, 
                        f"{member.name} expulsado!!!", 
                        reason, 
                        member.avatar)
                        )
                
            else:
                await ctx.send(mention)

        except discord.Forbidden:
            await ctx.send("No tengo permisos suficientes para llevar a cabo esta acción")



    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: discord.Member = None, *, reason = "Sin especificar"):

        try:
            mention = checkMention(member, ctx.author, self.bot.user)

            if mention is True:
                async with ctx.typing():
                    await member.remove_roles(reason = "Ban")
                    await ctx.guild.ban(member) 

                    await ctx.send(embed = modEmbed(
                        ctx.author.name, 
                        f"{member.name} baneado!!!", 
                        reason, 
                        member.avatar)
                        )
                
            else:
                await ctx.send(mention)
        

        except discord.Forbidden:
            await ctx.send("No tengo permisos suficientes para llevar a cabo esta acción")


        
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(administrator = True)
    async def unban(self, ctx, *, memberID: int = None):

        if memberID is None:
            await ctx.send("Para desbanear a un usuario, debes dar el ID de usuario de quien deseas desbanear")
        else:
            async with ctx.typing():
                try:
                    ban_entry = await ctx.guild.fetch_ban(discord.Object(id = memberID)) ## Fetch = Buscar
                    
                    await ctx.guild.unban(ban_entry.user)
                    
                    await ctx.send(f"Se ha desbaneado a {ban_entry.user.name}")
                
                except discord.NotFound:
                    await ctx.send("No se encontró una entrada de ban para ese usuario")
              
                except discord.Forbidden:
                    await ctx.send("No tengo permisos suficientes para llevar a cabo esta acción")
    


    @commands.command()
    @commands.has_permissions(administrator = True)
    async def mute(self, ctx, member: discord.Member = None, *, reason = "Sin especificar"):
        async with ctx.typing():
            silence_rol = discord.utils.get(ctx.guild.roles, name="Silenciado")

        if not silence_rol:
            await ctx.send("No existe un rol de silenciado, ejecuta el comando ""rolmute"" para crear uno")

        try:
            mention = checkMention(member, ctx.author, self.bot.user)
            if mention is True:
                async with ctx.typing():
                    await member.add_roles(silence_rol)

                    await ctx.send(embed = modEmbed(
                        ctx.author.name, 
                        f"{member.name} ha sido silenciado!!!", 
                        reason, 
                        member.avatar)
                        )
                
            else:
                await ctx.send(mention)

        except discord.Forbidden:
            await ctx.send("No tengo permisos suficientes para llevar a cabo esta acción")



    @commands.command()
    @commands.has_permissions(administrator = True)
    async def unmute(self, ctx, member: discord.Member = None):
        async with ctx.typing():
            silence_rol = discord.utils.get(ctx.guild.roles, name="Silenciado")

        if not silence_rol:
            await ctx.send("No existe un rol de silenciado, ejecuta el comando rolmute para crear uno")

        mention = checkMention(member, ctx.author, self.bot.user)

        try:
            if mention is True:
                async with ctx.typing():

                    if silence_rol in member.roles:
                        await member.remove_roles(silence_rol)

                        await member.remove_roles(reason = "Ban")
                        await ctx.guild.ban(member) 

                        await ctx.send(embed = modEmbed(
                            ctx.author.name, 
                            f"{member.name} ahora puede enviar mensajes", 
                            "Seguramente mañas del usuario", 
                            member.avatar)
                            )
                    else:
                        await ctx.send("El usuario no se encuentra silenciado")
                
            else:
                await ctx.send(mention)

        except discord.Forbidden:
            await ctx.send("No tengo permisos suficientes para llevar a cabo esta acción")



    @commands.command()
    @commands.has_permissions(administrator = True)
    async def rolmute(self, ctx):
        async with ctx.typing():
            silence_rol = discord.utils.get(ctx.guild.roles, name="Silenciado")

        try:
            if not silence_rol:
                await ctx.send("Creando rol...")

                async with ctx.typing():
                    await ctx.send("Asignando permisos...")

                    rol_color= discord.Colour.from_rgb(0, 0, 0)

                    silence_rol= await ctx.guild.create_role(
                        name="Silenciado", 
                        colour=rol_color,
                        permissions=discord.Permissions(send_messages=False, speak=False))
                    
                    for canal in ctx.guild.text_channels:
                        await canal.set_permissions(silence_rol, send_messages=False, speak=False)

                    await ctx.send(
                        f"\nSe ha creado el rol de Silenciado"
                        f"\nEn dado caso de que el silenciado no funcione, verifica que el rol de silenciado tenga la jerarquia mas alta de roles"
                        f"\nPuedes personalizar el color del rol, pero recuerda, no modifiques para nada el nombre")

            else:
                await ctx.send("El rol de Silenciado ya existe")
        
        except discord.Forbidden:
            await ctx.send("No tengo permisos suficientes para llevar a cabo esta acción")



    @commands.command()
    @commands.has_permissions(administrator = True)
    async def rol(self, ctx, member: discord.Member = None, role: discord.Role = None):
        try:
            mention = checkMention(member, ctx.author, self.bot.user)
            if mention is True:
                async with ctx.typing():
                    if role is None:
                        await ctx.send("Debes mencionar un rol")
                    
                    else:
                        await member.add_roles(role)

                        await ctx.send(embed = modEmbed(
                            ctx.author.name, 
                            f"{member.name} ahora tiene el rol de {role}", 
                            f"Mañas del usuario", 
                            member.avatar)
                            )
                
            else:
                await ctx.send(mention)

        except discord.Forbidden:
            await ctx.send("No tengo permisos suficientes para llevar a cabo esta acción")



    @commands.command(aliases=["revocarol"])
    @commands.has_permissions(administrator = True)
    async def removerol(self, ctx, member: discord.Member = None, role: discord.Role = None):
        try:
            mention = checkMention(member, ctx.author, self.bot.user)
            if mention is True:
                async with ctx.typing():
                    if role is None:
                        await ctx.send("Debes mencionar un rol")
                    
                    else:
                        await member.remove_roles(role)

                        await ctx.send(embed = modEmbed(
                            ctx.author.name, 
                            f"Rol removido para {member.name}", 
                            f"Mañas del usuario", 
                            member.avatar)
                            )
                
            else:
                await ctx.send(mention)

        except discord.Forbidden:
            await ctx.send("No tengo permisos suficientes para llevar a cabo esta acción")



    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("No tienes suficientes permisos para usar este comando.")
        
        if isinstance(error, commands.BadArgument):
            await ctx.send("Debes hacer una mencion al usar este comando")



async def setup(bot):
    await bot.add_cog(mod(bot))