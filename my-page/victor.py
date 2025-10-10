import discord
import random
from discord.ext import commands

TOKEN = "MTQyMDg2NjYxMDg2Nzk5NDcwNA.G6-Kru.KasJ9Tn-1cJkhxkoFgyzK_YEuG3dRf642_2HbQ"

bot = commands.Bot(command_prefix="-", intents=discord.Intents.all())

personagens = [
    "Twilight Sparkle",
    "Rainbow Dash",
    "Fluttershy",
    "Pinkie Pie",
    "Applejack",
    "Rarity",
    "Spike",
    "Starlight Glimmer",
    "Princess Celestia",
    "Princess Luna",
    "Princess Cadance",
    "Shining Armor",
    "Discord",
    "Trixie",
    "Sunset Shimmer",
    "Big Macintosh",
    "Zecora",
    "Chrysalis",
    "King Sombra",
    "Tirek"
]

@bot.event
async def on_ready():
    print(f"Bot {bot.user} está online!")

@bot.command()
async def aparecer(ctx):
    personagem = random.choice(personagens)
    resultado = random.choice([
        "ganhou 50 pontos! 🎉",
        "perdeu 25 pontos... 😢",
        "não aconteceu nada. 🤔",
        "ganhou 100 pontos!! 🔥",
        "perdeu 50 pontos... 💔",
        "ganhou 200 pontos!!! 💎",
        "perdeu 100 pontos... ⚡"
    ])
    await ctx.send(f"{personagem} apareceu e você {resultado}")

bot.run(TOKEN)