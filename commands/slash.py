import discord

from discord.ext import commands
from discord import app_commands

from functions.functions import apiRequest, embedCreate



class slash(commands.Cog):



    def __init__(self, bot):
        self.bot = bot



    @commands.Cog.listener()
    async def on_ready(self):
        print("Slash commands loaded")




    @app_commands.command(name = "ping", description = "El hola mundo de los bots")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message("pong")
    


    @app_commands.command(name = "kill", description = "/kill")
    async def kill(self, interaction: discord.Interaction):
        await interaction.response.send_message("/kill")




async def setup(bot):
    await bot.add_cog(slash(bot))