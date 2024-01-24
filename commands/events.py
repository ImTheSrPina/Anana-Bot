import discord, json

from discord.ext import commands


class EventListener(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Events Listener ready!")

    @commands.Cog.listener()
    async def on_member_join(self, new_member: discord.Member):

        with open('json/WelcomeChannel_IDs.json', 'r') as json_file:
            data = json.load(json_file)
        
        servidor_id = str (new_member.guild.id)

        if servidor_id in data:
            channel_id = data[servidor_id]
            welcome_channel = new_member.guild.get_channel(channel_id)

            if welcome_channel is not None:

                if servidor_id in data:
                    pfp = new_member.avatar.url
                    emb = discord.Embed(title="Un evento acaba de ocurrir!!", color= 0x33f361)                                                      

                    emb.add_field(
                        name= f"{new_member.name} esta aqui!!",
                        value= f"{new_member.mention} caba de unirsenos!! No se como llegaste hasta aqui, pero soy la encargada de darte la bienvenida 🫣", 
                        inline=False)
                    emb.set_thumbnail(url=pfp)

                    await welcome_channel.send("@everyone alguien a llegado al servidor!!")
                    await welcome_channel.send(embed=emb)

                    with open('json/Rol_IDs.json', 'r') as json_file:   ## LEER JSON PARA VERIFICAR SI HAY ROLES POR ASIGNAR
                        data = json.load(json_file)

                    server_id = str(new_member.guild.id)
                    role_id = data.get(server_id)

                    if role_id is not None:
                        rol = discord.utils.get(new_member.guild.roles, id=int(role_id))

                        if rol is not None:
                            await new_member.add_roles(rol)
                        else:
                            await welcome_channel.send(
                                f"No se encontró el rol configurado para autorol, verifica que el rol aun exista")
                else:
                    pass
                    #No es encuntra un rol... por ende no hace nada


    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):

        with open('json/ByeChannel_IDs.json', 'r') as json_file:
            data = json.load(json_file)
        
        servidor_id = str (member.guild.id)

        if servidor_id in data:
            channel_id = data[servidor_id]
            welcome_channel = member.guild.get_channel(channel_id)

            pfp = member.avatar.url
            emb = discord.Embed(title=f"{member.name} nos ha abandonado", color= 0x33f361)

            emb.add_field(
                name= f"{member.name} no nos puedes hacer esto...",
                value=f"{member.mention} ha decidido irse, no puedo hacer nada mas que desearte suerte en tu viaje...", 
                inline=False)
            emb.set_thumbnail(url=pfp)

            await welcome_channel.send(f"@everyone alguien se ha ido...")
            await welcome_channel.send(embed=emb)



    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return  # Evita que el bot responda a sus propios mensajes

        if "https://" in message.content.lower() or "http://" in message.content.lower():
            await message.reply("No se pueden enviar enlaces, de todas formas no puedo hacer nada .-. ")

        await self.process_commands(message)  # Procesa los comandos si los hay


        


async def setup(bot):
    await bot.add_cog(EventListener(bot))