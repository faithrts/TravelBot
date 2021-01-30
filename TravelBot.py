import discord
from discord.ext import commands

# client = discord.Client() establishing connection with discord

client = commands.Bot(command_prefix='.') # establishing command prefix

@client.event
async def on_ready():
	print("Online")

""" call to the bot; bot prints "Where do you want to go?"

# choose place, recipe, music
@client.command()
async def prm_choice(ctx):
	await ctx.send("What would you like from this city?\n\U0001F9ED Place\n\U0001F37D Recipe\n\U0001F3B5 Music")
	await message.add_reaction("\U0001F9ED")
	await message.add_reaction("\U0001F37D")
	await message.add_reaction("\U0001F3B5")

"""

# insert token below
bot.run("token")


