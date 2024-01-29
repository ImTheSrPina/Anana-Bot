import discord, time
from discord.ext import commands


from functions.functions import loadGuildConfig, saveConfig, welcomeOptions, goodbyeOptions, createWelcomeGoodbyeJSON, memberEmbed, readJson, configAutorol


class configs(commands.Cog):



    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print("Configs commands loaded")



    @commands.command()
    @commands.has_permissions(administrator = True)
    async def prefix(self, ctx, prefix = None):
        try:
            if prefix is None:
                await ctx.send("Este comando permite que cambies el prefix de tu servidor, ingresa el comando mas el nuevo prefix que deseas usar")
            
            else:
                jsonConfig = loadGuildConfig(ctx.guild.id)
                guildID = str (ctx.guild.id)

                if guildID not in jsonConfig["guilds"]:
                    await ctx.send("Un error ha ocurrido, contacta al servicio de soporte del bot o intentalo de nuevo mas tarde")

                else:

                    jsonConfig["guilds"][guildID]["prefix"] = prefix
                    saveConfig("json/guildConfig.json", jsonConfig)

                    await ctx.send("Configuración guardada, menciona al bot para verificar tu nueva configuracion")

        except Exception as e:
            await ctx.send(f"Ha ocurrido un error: {e}")


    
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def welcome(self, ctx, option = None, *, configData = None):
        path = "json/welcome.json"

        if option in ["channel", "tittle", "description", "url", None] and configData is None and not ctx.message.attachments:
            await ctx.send(welcomeOptions(option))

        if option == "enable":
            response = createWelcomeGoodbyeJSON(path, ctx.guild.id, "enable")
            await ctx.send(f"{response} Los eventos de bienvenida estan activados")

        if option == "disable":
            response = createWelcomeGoodbyeJSON(path, ctx.guild.id, "disable")
            await ctx.send(f"{response} Los eventos de bienvenida estan desactivados")

        if option == "tittle" and configData != None:
            response = createWelcomeGoodbyeJSON(path, ctx.guild.id, "tittle", configData)
            await ctx.send(response)

        if option == "description" and configData != None:
            response = createWelcomeGoodbyeJSON(path, ctx.guild.id, "description", configData)
            await ctx.send(response)

        if ctx.message.attachments and option == "url":
            attachment = ctx.message.attachments[0]
            response = createWelcomeGoodbyeJSON(path, ctx.guild.id, "url", attachment.url)
            await ctx.send(response)

    

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def wchannel(self, ctx, channel: discord.TextChannel = None):
        try:
            if channel == None:
                await ctx.send("Es necesario que menciones un canal")
            else:
                path = "json/welcome.json"
                channelID = str(channel.id)
                response = createWelcomeGoodbyeJSON(path, ctx.guild.id, "channel", channelID)
                await ctx.send(response)

        except Exception as error:
            await ctx.send(f"Error: {error}")



    @commands.command()
    @commands.has_permissions(administrator = True)
    async def goodbye(self, ctx, option = None, *, configData = None):
        path = "json/goodbye.json"

        if option in ["channel", "tittle", "description", "url", None] and configData is None and not ctx.message.attachments:
            await ctx.send(goodbyeOptions(option))

        if option == "enable":
            response = createWelcomeGoodbyeJSON(path, ctx.guild.id, "enable")
            await ctx.send(f"{response} Los eventos de despedida estan activados")

        if option == "disable":
            response = createWelcomeGoodbyeJSON(path, ctx.guild.id, "disable")
            await ctx.send(f"{response} Los eventos de bienvenida estan desactivados")

        if option == "tittle" and configData != None:
            response = createWelcomeGoodbyeJSON(path, ctx.guild.id, "tittle", configData)
            await ctx.send(response)

        if option == "description" and configData != None:
            response = createWelcomeGoodbyeJSON(path, ctx.guild.id, "description", configData)
            await ctx.send(response)

        if ctx.message.attachments and option == "url":
            attachment = ctx.message.attachments[0]
            response = createWelcomeGoodbyeJSON(path, ctx.guild.id, "url", attachment.url)
            await ctx.send(response)
    


    @commands.command()
    @commands.has_permissions(administrator = True)
    async def bchannel(self, ctx, channel: discord.TextChannel = None):
        try:
            if channel == None:
                await ctx.send("Es necesario que menciones un canal")
            else:
                path = "json/goodbye.json"
                channelID = str(channel.id)
                response = createWelcomeGoodbyeJSON(path, ctx.guild.id, "channel", channelID)
                await ctx.send(response)

        except Exception as error:
            await ctx.send(f"Error: {error}")



    @commands.command()
    @commands.has_permissions(administrator = True)
    async def test(self, ctx, option: str = None):

        if option == "welcome":
            path = "json/welcome.json"
            jsonData = readJson(path)

            guild_data = jsonData["guilds"].get(str(ctx.guild.id), None)

            if guild_data:
                if all(value is None for value in [guild_data["channel"], guild_data["tittle"], guild_data["description"], guild_data["url"], guild_data["enable"]]):
                    await ctx.send(f"\nAun no has terminado la configuracion de tu embed de bienvenida"
                                   f"\nO tal vez no has activado los eventos de bienvenida, utiliza el comando **welcome enable** para activarlo." 
                                   f"\nTermina tu configuracion y vuelve mas tarde :)")

                else:
                    await ctx.send(embed = memberEmbed(path, ctx.guild.id, ctx.author, ctx.guild.name))

            if not guild_data:
                await ctx.send(
                    "No existe ninguna configuracion de bienvenida, prueba a usar el comando **welcome** para mas informacion :)")
                
        if option == "goodbye":
            path = "json/goodbye.json"
            jsonData = readJson(path)

            guild_data = jsonData["guilds"].get(str(ctx.guild.id), None)

            if guild_data:
                if all(value is None for value in [guild_data["channel"], guild_data["tittle"], guild_data["description"], guild_data["url"], guild_data["enable"]]):
                    await ctx.send(f"\nAun no has terminado la configuracion de tu embed de despedida." 
                                   f"\nO tal vez no has activado los eventos de despedida, utiliza el comando **goodbye enable** para activarlo." 
                                   f"\nTermina tu configuracion y vuelve mas tarde :)")

                else:
                    await ctx.send(embed = memberEmbed(path, ctx.guild.id, ctx.author, ctx.guild.name))

            if not guild_data:
                await ctx.send(
                    "No existe ninguna configuracion de bienvenida, prueba a usar el comando **goodbye** para mas informacion :)")



    @commands.command()
    @commands.has_permissions(administrator = True)
    async def autorol(self, ctx, option: str = None, rol : discord.Role = None):
        response = configAutorol(str(ctx.guild.id), option, rol, self.bot.user.name)
        await ctx.send(response)





    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        async with ctx.typing():
            async with ctx.typing():
                if isinstance(error, commands.MissingPermissions):
                    await ctx.send("No tienes suficientes permisos para usar este comando.")



async def setup(bot):
    await bot.add_cog(configs(bot))