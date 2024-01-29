import discord

from discord.ext import commands
from discord import app_commands

from functions.functions import checkMention, modEmbed



class slashMod(commands.Cog):



    def __init__(self, bot):
        self.bot = bot



    @commands.Cog.listener()
    async def on_ready(self):
        print("Mod app commands loaded")



    @app_commands.command(name = "rol", description = "Le asigna un rol a un miembro")
    @app_commands.describe(member = "Miembro al que le daras un rol", rol="El rol que vas a asignar")
    @app_commands.checks.has_permissions(administrator=True)
    async def rol(self, interaction: discord.Interaction, member: discord.Member, rol: discord.Role):

        try:
            mention = checkMention(member, interaction.user, self.bot.user)

            if mention is True:
                    await member.add_roles(rol)
                    await interaction.response.send_message(embed = modEmbed(
                        interaction.user, 
                        f"{member.name} ahora tiene el rol de {rol.name}", 
                        f"Mañas del usuario", 
                        member.avatar)
                        )
                    
            else:
                await interaction.response.send_message(mention) 

        except discord.Forbidden:
           await interaction.response.send_message("No tengo permisos suficientes para llevar a cabo esta acción")



    @app_commands.command(name = "removerol", description = "Le revoca un rol a un miembro")
    @app_commands.describe(member = "Miembro al que le quitaras el rol", rol="El rol que vas a quitar")
    @app_commands.checks.has_permissions(administrator=True)
    async def removerol(self, interaction: discord.Interaction, member: discord.Member, rol: discord.Role):
        try:
            mention = checkMention(member, interaction.user, self.bot.user)
            if mention is True:
                await member.remove_roles(rol)

                await interaction.response.send_message(embed = modEmbed(
                    interaction.user, 
                    f"Rol removido para {member.name}", 
                    f"Mañas del usuario", 
                    member.avatar)
                    )
        
            else:
                await interaction.response.send_message(mention)

        except discord.Forbidden:
            await interaction.response.send_message("No tengo permisos suficientes para llevar a cabo esta acción")



    @app_commands.command(name = "kick", description = "Expulsa a un miembro",)
    @app_commands.describe(member="Miembro a expulsar", reason= "Razon de la expulsión" )
    @app_commands.checks.has_permissions(administrator=True)
    async def kick(self, interaction: discord.Interaction, member: discord.Member, *, reason: str = "Sin espcificar"):
        try:
            mention = checkMention(member, interaction.user, self.bot.user)

            if mention is True:
                    await member.kick(reason=reason) 
                    await interaction.response.send_message(embed = modEmbed(
                        interaction.user, 
                        f"{member.name} expulsado", 
                        reason, 
                        member.avatar)
                        )
                    
            else:
                await interaction.response.send_message(mention) 

        except discord.Forbidden:
           await interaction.response.send_message("No tengo permisos suficientes para llevar a cabo esta acción")



    @app_commands.command(name = "ban", description = "Banea a un miembro",)
    @app_commands.describe(member="Miembro a banear", reason= "Razon del baneo" )
    @app_commands.checks.has_permissions(administrator=True)
    async def ban(self, interaction: discord.Interaction, member: discord.Member, *, reason: str = "Sin espcificar"):
        try:
            mention = checkMention(member, interaction.user, self.bot.user)

            if mention is True:
                await member.ban(reason = reason) 

                await interaction.response.send_message(embed = modEmbed(
                    interaction.user, 
                    f"{member.name} baneado!!!", 
                    reason, 
                    member.avatar)
                    )
                
            else:
                await interaction.response.send_message(mention)

        except discord.Forbidden:
           await interaction.response.send_message("No tengo permisos suficientes para llevar a cabo esta acción")



    @app_commands.command(name = "unban", description = "Desbanea a un miembro")
    @app_commands.describe(member="Miembro a desbanear")
    @app_commands.checks.has_permissions(administrator=True)
    async def unban(self, interaction: discord.Interaction, member: discord.Member):
        try:
            await member.unban()
            await interaction.response.send_message(f"Se ha desbaneado a {member.name}")
    
        except discord.NotFound:
            await interaction.response.send_message("No se encontró una entrada de ban para ese usuario")
        
        except discord.Forbidden:
            await interaction.response.send_message("No tengo permisos suficientes para llevar a cabo esta acción")

        except discord.HTTPException:
            await interaction.response.send_message("Error desconocido al intentar desbanear a {member.name}")



async def setup(bot):
    await bot.add_cog(slashMod(bot))