import discord, os, asyncio

from discord.ext import commands
from dotenv import load_dotenv



load_dotenv('keys/.env.key')
YOUR_TOKEN: str = os.getenv('TOKEN_BOT_KEY')


bot=commands.Bot(command_prefix= '+', intents = discord.Intents.all(), help_command=None)


@bot.event
async def on_ready():

    await bot.change_presence(status=discord.Status.online, activity=discord.Game(">help'"))

    print("")
    print(f"{bot.user} ahora esta en en linea")
    print("")
    sync = await bot.tree.sync()
    print("")
    print(f"{len(sync)} comandos slash disponibles")
    print("")

    
async def load():
    for filename in os.listdir('./commands'):
        if filename.endswith(".py"):
            await bot.load_extension(f'commands.{filename[:-3]}')


async def main():
    async with bot:
        await load()
        await bot.start(YOUR_TOKEN)


asyncio.run(main())
