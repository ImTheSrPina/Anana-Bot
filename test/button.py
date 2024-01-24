import discord

from discord.ext import commands
from discord.ui import Button, View



class button(Button):
        
    def __init__(self, label, emoji):
        super().__init__(label=label, style=discord.ButtonStyle.secondary, emoji=emoji)
        print("lee")

    
    async def callback(self, interaction):
        #print (self.button.custom_id)

        print("lee")
        view = View() 
        view.add_item(self)
        await interaction.response.edit_message(content="Bueno, solamente modifica el mensaje, no pudo hacer más, perdonenlo por favor", view = view)

class oneButton(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Un boton se puede usar...")


    @commands.command()
    async def beta(self, ctx):
        button1 = button("Preciona aqui...", "👉")
        view = View()
        view.add_item(button1)
        await ctx.send("Este es un mensaje con un boton debajo, no hace nada, al programador le dio flojera arreglar el comando", view=view)
        

async def setup(bot):
    await bot.add_cog(oneButton(bot))
