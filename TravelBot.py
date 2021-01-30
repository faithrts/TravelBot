#!/usr/bin/env python3

import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

travel = 0
choice = ""

@client.event
async def on_ready():
	print("Online")

@client.event
async def on_reaction_add(reaction, user):
	if user.bot:
		return

	if travel == 1:
		print("inside the travel == 1 loop")
		if reaction.emoji == "\U0001f30e":
			# send something
			choice =  "americas"
		elif reaction.emoji == "\U0001f30d":
			# await client.send("Alright, let's go to Africa or Europe!")
			choice = "africa_europe"
		elif reaction.emoji == "\U0001f30f":
			# await client.send("Spiriting you to Asia or Australia!")
			choice = "asia_australia"
	'''	
	if travel == 1:
		choice = "temp"		

	if reaction.emoji == "\U0001f30e":
		return "americas"
	elif reaction.emoji == "\U0001f30d":
		# await client.send("Alright, let's go to Africa or Europe!")
		return "africa_europe"
	elif reaction.emoji == "\U0001f30f": 
		return "asia_australia"
	'''
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
	travel = 1

	# displays list of continent groups
	question = await ctx.send("Where do you want to go?\n\
	\U0001f30e - The Americas\n\
	\U0001f30d - Africa or Europe\n\
	\U0001f30f - Asia or Australia")
	
	emojis = ["\U0001f30e", "\U0001f30d", "\U0001f30f"]
	for emoji in emojis:
		await question.add_reaction(emoji)

	# await ctx.send("outside the loop")

	if choice == "americas":
		await ctx.send("You chose the Americas!")
	elif choice == "africa_europe":
		await ctx.send("You chose Africa or Europe!")
	elif choice == "asia_australia":
		await ctx.send("Let's go to Asia or Australia!")

	'''
	question.add_reaction("\U0001f30e")
	question.add_reaction("\U0001f30d")
	question.add_reaction("\U0001f30f")
	'''
	'''
	await client.wait_for(emoji=["\U0001f30e", "\U0001f30d", "\U0001f30f"], message=question)
	
	if reaction.emoji == "\U0001f30e":
		await ctx.send("You chose the Americas!")
	elif reaction.emoji == "\U0001f30d":
		await ctx.send("Alright, let's go to Africa or Europe!")
	elif reaction.emoji == "\U0001f30f":
		await ctx.send("Spiriting you to Asia or Australia!")
		
	# adding emoji reactions to the message (currently working on this)
	'''
# X is working on this rn
''' some code'''

# X is working on this rn
''' some code'''

# insert token below
client.run("")


