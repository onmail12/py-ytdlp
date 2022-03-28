from functions import *
import discord
import random

TOKEN = "OTU3MTQxNzMzNTc2MTc5NzUy.Yj6dtA.pobFo_Oi69lHNfBP9eYnCUxrX9M"
client = discord.Client()


@client.event
async def on_ready():
    print("BOT READY: {0.user}".format(client))


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    authorId = "<@{}>".format(message.author.id)

    if message.content.startswith("dl 1080 "):
        message.content = message.content.split()[2]
        print(message.content)
        await message.channel.send(mainGetBest(message.content))

    elif message.content.startswith("dl 720 "):
        message.content = message.content.split()[2]
        print(message.content)
        await message.channel.send(mainGet720(message.content))

    elif message.content.startswith("dl 480 "):
        message.content = message.content.split()[2]
        print(message.content)
        await message.channel.send(mainGet480(message.content))

    elif message.content.startswith("dl 360 "):
        message.content = message.content.split()[2]
        print(message.content)
        await message.channel.send(mainGet360(message.content))

    elif message.content.startswith("dl 240 "):
        message.content = message.content.split()[2]
        print(message.content)
        await message.channel.send(mainGet240(message.content))

    elif message.content.startswith("dl 144 "):
        message.content = message.content.split()[2]
        print(message.content)
        await message.channel.send(mainGet144(message.content))

    # ---------------------------------------- SPOT-DL --------------------------------------------------

    elif message.content.startswith("dl spot "):
        message.content = message.content.split()[2]
        if "playlist" in message.content:
            await message.channel.send(authorId + "\n" + playlistSpot(message.content))

        elif "album" in message.content:
            await message.channel.send(authorId + "\n" + playlistSpot(message.content))

        else:
            await message.channel.send(authorId + "\n" + mainSpot(message.content))

    # ---------------------------------------- MISC -----------------------------------------------------

    elif message.content == "dl speedtest":
        await message.channel.send(speedtest())

    elif message.content == "dl help":
        await message.channel.send(
            "**Download Youtube Video**\n`dl [RESOLUTION] [URL]` all args required\n\n**Download Spotify Track/Playlist/Album**\n`dl spot [TRACK/ALBUM/PLAYLIST URL]`"
        )

    elif message.content == "dl about":
        await message.channel.send(
            "Simple yt-dlp bot\nBot uploads all output files produced by yt-dlp to google drive using rclone\nHosted on heroku\n\nmade by Gouhund#3329 :thumbsup:"
        )
    elif message.content == "dl pingme":
        await message.channel.send(authorId)


client.run(TOKEN)
