import discord, requests, json, random



async def prefixes(bot, message):
    jsonConfig = loadGuildConfig(str(message.guild.id))
    return jsonConfig["guilds"][str(message.guild.id)]["prefix"]



async def apiRequest(url):
    response = requests.get(url)

    if response.status_code == 200:
        jsonData = response.json()
        return jsonData
    else:
        return False



def embedCreate(color, url: str = None, title: str = None, description: str = None, tumbail: str = None, objetItems = None):
    embed = discord.Embed(color = color,
                          title = title,
                          description = description)
    embed.set_thumbnail(url = tumbail)
    embed.set_image(url=url)

    if objetItems != None:
        for [name, value] in objetItems.items():
            embed.add_field(name=name+":",value=value, inline=False)

    return embed



def modEmbed(author, action, reason, avatarUrl):
    embed = discord.Embed(
        color = 0xFF0000,
        title = action,
        description = "")
    embed.set_thumbnail(url = avatarUrl)
    embed.add_field(
                name = "", 
                value = f"Motivo: {reason}",
                inline = True)
    embed.set_footer(text = f"Acción realizada por {author}")
    embed.set_image(url = "https://media.discordapp.net/attachments/1199562966480195644/1199566641806196736/star-rail-pom-pom.gif?ex=65c3027e&is=65b08d7e&hm=23e50ca3da4ffdbade7ee8404cbcf55464eb6bc21f1fadf74f813dbe2198d4b5&=")
    return embed



def checkMention(memberMention, authorMention, botMention):
    if memberMention == None:
        return "Debes mencionar a alguen"
    if memberMention == authorMention:
        return "No puedes aplicar esta accion a ti mismo"
    if memberMention == botMention:
        return "Mi programacion no me permite dañarme por mi propia cuenta"
    return True



def readJson(path):
    jsonData = None
    try:
        with open(path, "r") as file:
            jsonData = json.load(file)

    except FileNotFoundError:
        jsonData = {"guilds": {}}
        with open(path, "w") as file:
            json.dump(jsonData, file)
    
    return jsonData



def loadGuildConfig(guild_id):
    path = "json/guildConfig.json"
    guild_id_str = str(guild_id)

    try:
        with open(path, "r") as file:
            jsonData = json.load(file)

    except FileNotFoundError:
        jsonData = {"guilds": {}}
        with open(path, "w") as file:
            json.dump(jsonData, file)

    if guild_id_str not in jsonData["guilds"]:
        jsonData["guilds"][guild_id_str] = {
            "prefix" : "+", 
            "antiSpam" : False,
            "spamChannel" : None,
            "autoRol" : False,
            "rolMember" : None,
            "rolBot" : None,}
        
        saveConfig(path, jsonData)

    return jsonData



def welcomeOptions(option):
    if option == "channel":
        return(
        "Esta opcion permite establecer el canal en el que se envia el mensaje de bienvenida, para ello usa el comando **wchannel (mencion a un canal)**")
        
    if option == "tittle":
        return(
        f"\nEsta opcion permite establecer un titulo en el embed de bienvenida."
        f"\nUsa el comando de la siguente forma: **+welcome tittle (mencion del canal)**." 
        f"\nSi planeas que tu titulo incluya la mencion de un miembro en una parte del mensaje, escribe **@mention** en donde desees que vaya la mencion." 
        f"\nSi deseas que tu bienvenida escriba la mencion del servidor, escribe **@guild**.")
    
    if option == "description":
        return(
        f"\nEsta opcion permite establecer una descripcion en el embed de bienvenida, usa el comando de la siguente forma: **+welcome description (aqui va tu descripcion)**."
        f"\nSi planeas que tu descripcion incluya la mencion de un miembro, escribe **@mention** en donde desees que vaya la mencion"
        f"\nSi deseas que tu comando escriba la mencion del servidor, escribe **@guild**." 
        f"\nPor ultimo, si planeas que se mencione un canal en especifico, solo basta con mencionarlo al momento de establecer la descripción")

    if option == "url":
        return(
        "Esta opcion permite establecer una imagen o gif en el embed para decorarlo, solo basta con que escribas **welcome url** y al mismo tiempo envies la imagen o gif que deseas adjuntar al embed.")
    
    if option == None:
        return(
        f"\n**welcome** permite establecer un mensaje de bienvenida como embed, pueder usar el comado más una de las siguientes opciones para conocer mas configuraciones:"
        f"\n "
        f"\n**channel**" 
        f"\n**tittle**" 
        f"\n**description**" 
        f"\n**url**" 
        f"\n "
        f"\nEjemplo: **welcome channel**." 
        f"\n "
        f"\n**Recuerda**, para activar el uso de los mensajes de bienvenida, es necesario que uses el comando **welcome enable** para activarlos, si deseas desactivar esta configuracion, usa el comando **welcome disable** para desactivar estos eventos")



def goodbyeOptions(option):
    if option == "channel":
        return(
        "Esta opcion permite establecer el canal en el que se envia el mensaje de despedida, para ello usa el comando **bchannel (mencion a un canal)**")
        
    if option == "tittle":
        return(
        f"\nEsta opcion permite establecer un titulo en el embed de despedida."
        f"\nUsa el comando de la siguente forma: **+goodbye tittle (mencion del canal)**." 
        f"\nSi planeas que tu titulo incluya la mencion de un miembro en una parte del mensaje, escribe **@mention** en donde desees que vaya la mencion."
        f"\nDe igual forma, si quieres que tu titulo escriba la mencion del servidor, escribe **@guild**.")
    
    if option == "description":
        return(
        f"\nEsta opcion permite establecer una descripcion en el embed de despedida, usa el comando de la siguente forma: **+goodbye description (aqui va tu descripcion)**." 
        f"\nSi planeas que tu descripcion incluya la mencion de un miembro, escribe **@mention** en donde desees que vaya la mencion."
        f"\nSi quieres que tu comando escriba la mencion del servidor, escribe **@guild**"
        f"\nPor ultimo, para que la despedida mencione un canal en especifico, solo basta con mencionarlo al momento de establecer la descripción")

    if option == "url":
        return(
        "Esta opcion permite establecer una imagen o gif en el embed para decorarlo, solo basta con que escribas **goodbye url** y al mismo tiempo envies la imagen o gif que deseas adjuntar al embed.")
    
    if option == None:
        return(
        f"\n**goodbye** permite establecer un mensaje de despedida como embed."
        f"\nPuedes usar el comando más una de las siguientes opciones para conocer mas configuraciones: "
        f"\n "
        f"\n**channel**" 
        f"\n**tittle**" 
        f"\n**description**" 
        f"\n**url**"
        f"\n "
        f"\nEjemplo: **goodbye channel**." 
        f"\n "
        f"\n**Recuerda**, para activar el uso de los mensajes de despedida, es necesario que uses el comando **goodbye enable** para activarlos, si deseas desactivar esta configuracion, usa el comando **goodbye disable** para desactivar estos eventos")



def createWelcomeGoodbyeJSON(path, guild_id, value, data : str = None):
    
    guild_id_str = str(guild_id)

    jsonData = readJson(path)

    try:
        if guild_id_str not in jsonData["guilds"]:
            jsonData["guilds"][guild_id_str] = {
                "enable" : None,
                "channel": None,
                "tittle": None,
                "description" : None,
                "url" : None
                }
            saveConfig(path, jsonData)
            return("Parece que no existe ninguna configuracion establecida, hemos creado una por defecto, trata de enviar tu configuracion de nuevo")

        if value == "enable":
            jsonData["guilds"][guild_id_str]["enable"] = 1
        
        if value == "disable":
            jsonData["guilds"][guild_id_str]["enable"] = None

        if value == "channel":
            jsonData["guilds"][guild_id_str]["channel"] = str(data)

        if value == "tittle":
            jsonData["guilds"][guild_id_str]["tittle"] = data

        if value == "description":
            jsonData["guilds"][guild_id_str]["description"] = data

        if value == "url":
            jsonData["guilds"][guild_id_str]["url"] = data
    

    except json.JSONDecodeError as error:
       return(f"Error al decodificar el JSON: {error}")

    except Exception as error:
        import traceback
        traceback.print_exc()
        return(f"Ocurrió un error inesperado: {error}")

    saveConfig(path, jsonData)
    return("Configuracion almacenada correctamente.")



def memberEmbed(path, guild_id, member = None, guild = None):
    guild_id_str = str(guild_id)

    try:
        with open(path, "r") as file:
            jsonData = json.load(file)

    except FileNotFoundError:
        jsonData = {"guilds": {}}
        return

    if guild_id_str not in jsonData["guilds"]:
        return

    else:
        data = jsonData["guilds"][guild_id_str]

        titleData = fetchMentions(data["tittle"], member.name, guild)
        descriptionData = fetchMentions(data["description"], member.mention, guild)

        color = 0xFF00D5
        embed = embedCreate(color, data["url"], titleData, descriptionData, member.avatar)

        return embed
    


def fetchMentions(string, mention, guild):
    string = string.replace("@guild", guild)
    string = string.replace("@mention", mention)

    return string



def saveConfig(path, data):
    with open(path, "w") as file:
        json.dump(data, file, indent=4)



async def autoRol(member, confirm, rol):
    if confirm == True:

        if rol:
            role = member.guild.get_role(rol)

            if role:
                await member.add_roles(role)
            else:
                return



def configAutorol(guildID, option, rol, botName):

    path = "json/guildConfig.json"
    jsonData = readJson(path)

    if str(guildID) in jsonData["guilds"]:
        try:
            if option == "member":
                if rol:
                    role = rol.guild.get_role(rol.id)
                    if role:
                        jsonData["guilds"][str(guildID)]["rolMember"] = str(rol.id)
                        saveConfig(path, jsonData)
                        return(f"Configuracion almacenada, el rol {role.name} se asignara automaticamente a los usuarios")

            elif option == "bot":
                print("lee bot")
                if rol:
                    role = rol.guild.get_role(rol.id)
                    print(role)
                    if role:
                        jsonData["guilds"][str(guildID)]["rolBot"] = str(rol.id)
                        saveConfig(path, jsonData)
                        return(f"Configuracion almacenada, el rol {role.name} se asignara automaticamente a los bots")

            elif option == "enable":
                jsonData["guilds"][str(guildID)]["autoRol"] = True
                saveConfig(path, jsonData)
                return("Autorol activado")

            elif option == "disable":
                jsonData["guilds"][str(guildID)]["autoRol"] = False
                saveConfig(path, jsonData)
                return("Autrol desactivado")

            else:
                return(
                    f"\nEste comando te permite activar la funcion de auto rol en tu servidor."
                    f"\nConsiste en que, al momento de que un nuevo miembro se una a tu servidor, **{botName}** le asignara un rol que hayas establecido."
                    f"\nPuedes establecer un rol para miembros y otro para bots."
                    f"\nSi deseas agregar un rol a asiganar para un miembro, usa el comando **autorol member (mención del rol a asignar)**."
                    f"\nDe igual forma, si deseas asignar un rol para bots, usa el comando **autorol bot (mencion del rol a asignar**)."
                    f"\nSi ya has hecho una configuracion de autorol, debes activar este evento para que se ejecute en tu servidor, activalo usando **autorol enable** para activarlo, y **autorol disable** para desactivarlo")

        except Exception as error:
            return(f"Un error ha ocurrido, codigo de error: {error}")
        
    else:
        return("Ha ocurrido un error con la consulta de tus configuraciones, intentalo mas tarde.")



def actionsFunction(action, author, member, bot, url):
    jsonData = readJson("json/actions.json")

    if url != False:

        if jsonData:
            if member == None:
                data = jsonData["action"][action]["noMention"]

            elif member == author:
                data = jsonData["action"][action]["author"]

            else:
                data = jsonData["action"][action]["mention"]
                
            if data != None:
                if member == None:
                    strDescription = fetchActionMentions(data, author.mention, None, bot)
                else:
                    strDescription = fetchActionMentions(data, author.mention, member.mention, bot)
                
                return embedCreate(0xF37ED2, url, description = strDescription)

            else:
                return False

        else:
            return("Fallo al recuperar los datos de acciones, por favor intentalo mas tarde.")

    else:
        return("Fallo en la solicitud a la api.")



def fetchActionMentions(string, author, member, bot):

    if member is not None:
        string = string.replace("@member", member)
    string = string.replace("@author", author)
    string = string.replace("@bot", bot)

    return string



def botResponse():
    jsonData = readJson("json/responses.json")
    index = random.randint(1, 57)
    if jsonData:
        return jsonData["responses"][str(index)]["text"]
    else:
        return
    