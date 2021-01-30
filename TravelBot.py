#!/usr/bin/env python3

import discord
from discord.ext import commands

# client = discord.Client() establishing connection with discord

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
	print("Online")

'''
@client.event
async def on_message(message):
	# check if the message says "Take me away" or "take me away"
	if message.content == "Take me away":
		# call launch_travel
		await ctx.invoke(self.bot.get_command("launch_travel")	
	
	await client.process_commands(message)
'''		

# faith is working on this rn
@client.command(aliases=['travelbot', 'TravelBot'])
async def launch_travel(ctx):
	await ctx.send("Where do you want to go?\n\u1514 North America")
	await message.add_reaction("\u1514")

# X is working on this rn
''' some code'''

# X is working on this rn
''' some code'''

# insert token below
client.run("")


