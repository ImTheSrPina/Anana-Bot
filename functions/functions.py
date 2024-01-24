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
    

def modEmbed(ctx, action, reason):
    embed = discord.Embed(
        color = 0xFF0000,
        title = action,
        description = f"Motivo: {reason}",)
    embed.set_footer(text=f"Acción realizada por {ctx.author.display_name}")
    embed.set_image(url = "https://media.discordapp.net/attachments/1199562966480195644/1199566641806196736/star-rail-pom-pom.gif?ex=65c3027e&is=65b08d7e&hm=23e50ca3da4ffdbade7ee8404cbcf55464eb6bc21f1fadf74f813dbe2198d4b5&=")
    return embed