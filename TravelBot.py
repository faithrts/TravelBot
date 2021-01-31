#!/usr/bin/env python3

import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
	print("Online")

choice = ""

@client.event
async def on_reaction_add(reaction, user):
	if user.bot:
		return
	'''
	if reaction.emoji == "\U0001f30e":
		choice =  "americas"	
	elif reaction.emoji == "\U0001f30d":
		choice = "africa_europe"
	elif reaction.emoji == "\U0001f30f":
		choice = "asia_australia"

	elif



	return choice
	'''
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
	# displays list of continent groups
	question = await ctx.send("Where do you want to go?\n\
	\U0001f30e - The Americas\n\
	\U0001f30d - Africa or Europe\n\
	\U0001f30f - Asia or Australia")
	
	emojis = ["\U0001f30e", "\U0001f30d", "\U0001f30f"]
	for emoji in emojis:
		await question.add_reaction(emoji)

	def check(reaction, user):
		return not(user.bot)
	
	continent_react = await client.wait_for('reaction_add', check=check, timeout=60.0)
	continent = str(continent_react[0])

	# the Americas
	if continent == "\U0001f30e":		
		await ctx.send("_ _")		
		await ctx.send("The Americas it is!")
		await ctx.send("_ _")
	
		question2_a = await ctx.send("Which city would you like to visit?\n\
	\U0001f1e8\U0001f1e6 - Montréal, Canada\n\
	\U0001f1f2\U0001f1fd - Mexico City, Mexico\n\
	\U0001f1e8\U0001f1fa - Havana, Cuba")

		emoji2_a = ["\U0001f1e8\U0001f1e6","\U0001f1f2\U0001f1fd","\U0001f1e8\U0001f1fa"]
		for emoji in emoji2_a:
			await question2_a.add_reaction(emoji)

	# Africa or Europe
	elif continent == "\U0001f30d":
		await ctx.send("_ _")
		await ctx.send("Spiriting you to Africa or Europe!")
		await ctx.send("_ _")
	
		question2_b = await ctx.send("Which city would you like to visit?\n\
	\U0001f1ff\U0001f1e6 - Cape Town, South Africa\n\
	\U0001f1ea\U0001f1f8 - Barcelona, Spain\n\
	\U0001f1ee\U0001f1f9 - Rome, Italy")

		emoji2_b = ["\U0001f1ff\U0001f1e6","\U0001f1ea\U0001f1f8","\U0001f1ee\U0001f1f9"]
		for emoji in emoji2_b:
			await question2_b.add_reaction(emoji)		
	
	# Asia and Australia
	elif continent == "\U0001f30f":
		await ctx.send("_ _")
		await ctx.send("I hear Asia and Australia are lovely this time of year!")
		await ctx.send("_ _")

		question2_c = await ctx.send("Which city would you like to visit?\n\
	\U0001f1e8\U0001f1f3 - Beijing, China\n\
	\U0001f1f5\U0001f1ed - Manila, Philippines\n\
	\U0001f1fb\U0001f1f3 - Hanoi, Vietnam")		

		emoji2_c = ["\U0001f1e8\U0001f1f3","\U0001f1f5\U0001f1ed","\U0001f1fb\U0001f1f3"]
		for emoji in emoji2_c:
			await question2_c.add_reaction(emoji)

	city_react = await client.wait_for('reaction_add', check=check, timeout=60.0)
	city = str(city_react[0])

	# Montréal, Canada
	if city == "\U0001f1e8\U0001f1e6":
		Place =
		Recipe =
		Music =
	# Mexico City, Mexico
	elif city == "\U0001f1f2\U0001f1fd":
		Place =
		Recipe =
		Music =
	# Havana, Cuba
	elif city == "\U0001f1e8\U0001f1fa":
		Place = 
		Recipe = 
		Music =
	# Cape Town, South Africa
	elif city == "\U0001f1ff\U0001f1e6":
		Place =
		Recipe =
		Music =
	# Barcelona, Spain
	elif city == "\U0001f1ea\U0001f1f8":
		Place =
		Recipe =
		Music =
	# Rome, Italy
	elif city == "\U0001f1ee\U0001f1f9":
		Place =
		Recipe =
		Music =
	# Beijing, China
	elif city == "\U0001f1ea\U0001f1f8":
		Place =
		Recipe =
		Music =
	# Manila, Philippines
	elif city == "\U0001f1f5\U0001f1ed":
		Place =
		Recipe =
		Music =
	# Hanoi, Vietnam
	elif city == "\U0001f1fb\U0001f1f3":
		Place =
		Recipe =
		Music =

	'''
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
client.run("token")


