import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

PREFIX = os.getenv('PREFIX')
TOKEN = os.getenv('TOKEN')

client = commands.Bot(command_prefix=PREFIX)

@client.event
async def on_ready():
    print(f'Connected to Discord as {client.user}')

client.run(TOKEN)