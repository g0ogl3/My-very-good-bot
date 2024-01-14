from random import choice
import time
from discord import Intents
import discord
from discord.ext import commands
from credits import TOKEN
import os
print(os.listdir('facts'))
bot = commands.Bot(command_prefix="/", intents=Intents.all())
@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
print(os.listdir('facts'))
@bot.command()
async def know(ctx):
    files_list = os.listdir('facts')
    await ctx.send(file=discord.File(f'facts/{choice(files_list)}'))
bot.run(TOKEN)
