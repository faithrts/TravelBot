import discord
from discord.ext import commands

# client = discord.Client() establishing connection with discord
TOKEN = ''

client = commands.Bot(command_prefix='.') # establishing command prefix

@client.event
async def on_ready():
	print("Online")

""" call to the bot; bot prints "Where do you want to go?"

code

"""

print("hello")

# insert token below
bot.run(TOKEN)
