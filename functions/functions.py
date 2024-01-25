import discord, requests


def imageEmbedCreate(color, url):
    embed = discord.Embed(color= color)
    embed.set_image(url=url)
    return embed


async def apiRequest(url):
    response = requests.get(url)

    if response.status_code == 200:
        jsonData = response.json()
        return jsonData
    else:
        return False
    

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


def ckeckMention(memberMention, authorMention, botMention):
    if memberMention == None:
        return "Debes mencionar a alguen"
    if memberMention == authorMention:
        return "No puedes aplicar esta accion a ti mismo"
    if memberMention == botMention:
        return "Mi programacion no me permite dañarme myself"
    if memberMention != None:
        return True
