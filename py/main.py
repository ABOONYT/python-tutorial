

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!' , intents=discord.Intents.all())


@bot.event
async def on_ready():
    print('the bot is online!!')



bot.run("your token")
