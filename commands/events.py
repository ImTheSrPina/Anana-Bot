import discord
from discord.ext import commands


from functions.functions import loadGuildConfig, loadGuildConfig, autoRol, readJson, memberEmbed


class EventListener(commands.Cog):






    def __init__(self, bot):
        self.bot = bot





    @commands.Cog.listener()
    async def on_ready(self):
        print("Events Listener ready!")



    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        loadGuildConfig(guild.id)



    @commands.Cog.listener()
    async def on_message(self, message):
        if message.mentions[0] == self.bot.user:
            jsonConfig = loadGuildConfig(str(message.guild.id))
            #print(jsonConfig)
            prefix = jsonConfig["guilds"][str(message.guild.id)]["prefix"]
            await message.channel.send(f"Prefijo del servidor: {prefix}")

        await self.process_commands(message)  # Procesa los comandos si los hay



    @commands.Cog.listener()
    async def on_member_join(self, new_member: discord.Member):

        guildData = loadGuildConfig(str(new_member.guild.id))
        data = guildData["guilds"][str(new_member.guild.id)]

        try:
            #Definicion de variables: 
            autoRole = data["autoRol"]
            rolMember = int(data["rolMember"])
            rolBot = int(data["rolBot"])

            path = "json/welcome.json"

            jsonData = readJson(path)
            guildWelcome = jsonData["guilds"].get(str(new_member.guild.id), None)

            if new_member.bot:
                await autoRol(new_member, autoRole, rolBot)

                if guildWelcome:
                    if all(value is None for value in [guildWelcome["channel"], guildWelcome["tittle"], guildWelcome["description"], guildWelcome["url"], guildWelcome["enable"]]):
                        return
                        
                    else:
                        channelID = int(guildWelcome["channel"])
                        channel = new_member.guild.get_channel(channelID)
                        
                        if channel:
                            await channel.send(embed = memberEmbed(path, new_member.guild.id, new_member, new_member.guild.name))
                        
                        else:
                            return

            else:
                await autoRol(new_member, autoRole, rolMember)

                if guildWelcome:
                    if all(value is None for value in [guildWelcome["channel"], guildWelcome["tittle"], guildWelcome["description"], guildWelcome["url"], guildWelcome["enable"]]):
                        return
                    
                    else:
                        channelID = int(guildWelcome["channel"])
                        channel = new_member.guild.get_channel(channelID)
                        
                        if channel:
                            await channel.send(embed = memberEmbed(path, new_member.guild.id, new_member, new_member.guild.name))
                        
                        else:
                            return

        except ValueError:
            return



    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):

        path = "json/goodbye.json"

        jsonData = readJson(path)
        guildBye = jsonData["guilds"].get(str(member.guild.id), None)
        
        if guildBye:
            if all(value is None for value in [guildBye["channel"], guildBye["tittle"], guildBye["description"], guildBye["url"], guildBye["enable"]]):
                return

            else:
                channelID = int(guildBye["channel"])
                channel = member.guild.get_channel(channelID)
                
                if channel:
                    await channel.send(embed = memberEmbed(path, member.guild.id, member, member.guild.name))
                
                else:
                    return


        


async def setup(bot):
    await bot.add_cog(EventListener(bot))