import discord, os, asyncio

from discord.ext import commands
from dotenv import load_dotenv

from functions.functions import prefixes


load_dotenv('keys/.env')
YOUR_TOKEN: str = os.getenv('TOKEN_BOT_KEY')


bot=commands.Bot(command_prefix= prefixes, intents = discord.Intents.all())
#bot=commands.Bot(command_prefix= prefixes, intents = discord.Intents.all(), help_command=None)


@bot.event
async def on_ready():
    global guild_configs
    await bot.change_presence(status=discord.Status.online, activity=discord.CustomActivity("Listening: Love Live Songs"))
    print("")
    print(f"{bot.user} ahora esta en en linea")
    print("")
    print("")
    print(f"{len(await bot.tree.sync())} slash commands")
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
