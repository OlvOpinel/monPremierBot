import discord
import os
import random
from discord.ext import commands 
from dotenv import load_dotenv
load_dotenv()

print("Lancement du bot…")

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot allumé !")
    try:
        synced = await bot.tree.sync()
        print(f"Commandes synchronisées : {len(synced)}")
    except Exception as e:
        print(e)


@bot.event
async def on_message(message: discord.Message):

    if message.author.bot:
        return

    if "ice spice" in message.content.lower():
        channel = message.channel

        gifs = [
            "https://tenor.com/view/ice-spice-ice-spice-ass-ice-spice-twerk-ice-spice-body-twerk-gif-12664761973288080220",
            "https://klipy.com/gifs/ice-spice-twerk",
            "https://klipy.com/gifs/ice-spice-ass-ice-spice-twerking",
            "https://klipy.com/gifs/baddie-ice-spice-2",
            "https://klipy.com/gifs/ice-spice-gyatt-2",
            "https://tenor.com/view/ice-spice-munch-music-artist-music-artist-gif-26867362",
            "https://tenor.com/view/ice-spice-ice-spice-munchies-spice-cabinets-gif-27008897"
        ]

        await channel.send(random.choice(gifs))

    if "krkrkr" in message.content.lower():
        test_channel = bot.get_channel(1560259835319296010)

        gifs = [
            "https://tenor.com/view/ishowspeed-try-not-to-laugh-gif-7682731162751353849",
            "https://klipy.com/gifs/ishowspeed-1711",
            "https://klipy.com/gifs/ishowspeed-ksi-4",
            "https://klipy.com/gifs/ishowspeed-fortnite-6",
            "https://tenor.com/view/pffttt-cantholdlaugh-father-laugh-dad-laugh-gif-13166789396741539132",
            "https://tenor.com/view/maddy-perez-alexa-demie-euphoria-pajama-laughing-gif-15418340",
            "https://tenor.com/view/bh187-family-guy-peter-griffin-laugh-laughing-gif-21485227",
            "https://klipy.com/gifs/lebron-laugh",
            "https://klipy.com/gifs/lebron-lakers-10",
            "https://klipy.com/gifs/amp-laugh",
            "https://klipy.com/gifs/zepeck-mendoso"
        ]

        await test_channel.send(random.choice(gifs))



@bot.tree.command(name="warnguy", description="Alerter quelqu'un")
async def warnguy(interaction: discord.Interaction, member: discord.Member):
    await interaction.response.send_message("Alerte envoyé !")
    await member.send("T'as reçu une alerte")

@bot.tree.command(name="banguy", description="Bannir un membre")
async def banguy(interaction: discord.Interaction, member: discord.Member):
    await interaction.response.send_message("Ban envoyé !")
    await member.ban()
    await member.send("Tu as été banni !")

@bot.tree.command(name="letterboxd", description="Affiche mon Letterboxd")
async def letterboxd(interaction: discord.Interaction):
    await interaction.response.send_message("Mon letterboxd : https://letterboxd.com/OlvSosaa/")
    

bot.run(os.getenv('DISCORD_TOKEN'))

