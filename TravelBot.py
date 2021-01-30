#!/usr/bin/env python3

import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

travel = 1
choice = ""

@client.event
async def on_ready():
	print("Online")

@client.event
async def on_reaction_add(reaction, user):
	if user.bot:
		return

	if travel == 1:
		# print("inside the travel == 1 loop")
		if reaction.emoji == "\U0001f30e":
			choice =  "americas"	
			# copy = choice
			# return (choice, choice)
		elif reaction.emoji == "\U0001f30d":
			# await client.send("Alright, let's go to Africa or Europe!")
			choice = "africa_europe"
			# return "africa_europe"
			# return (choice, choice)
		elif reaction.emoji == "\U0001f30f":
			# await client.send("Spiriting you to Asia or Australia!")
			choice = "asia_australia"
			# return (choice, choice)
			# return "asia_australia"

	def check(reaction, user):
		return user == message.author
	# print(choice)
	return (choice, choice)
	
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

	continent_react, discard = await client.wait_for('reaction_add', check=check, timeout=60.0)

	print(continent_react)	

	# print(continent_react)
	await ctx.send(continent_react)
	
	'''
	if continent_react == "americas":
		await ctx.send("You chose the Americas!")
	elif continent_react == "africa_europe":
		await ctx.send("You chose Africa or Europe!")
	elif continent_react == "asia_australia":
		await ctx.send("Let's go to Asia or Australia!")
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
client.run("ODA0OTEzMjQyNjM4OTA5NDUw.YBTP3w.gHD33wHbRqGK1MGLd2_Xbmdzs0A")


