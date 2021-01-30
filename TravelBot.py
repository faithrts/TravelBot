import discord
from discord.ext import commands

# client = discord.Client() establishing connection with discord

client = commands.Bot(command_prefix='.') # establishing command prefix

@client.event
async def on_ready():
	print("Online")


# choose city
@client.command()
async def city_choice(ctx):
	# 2nd question
	travel = 2

	# have to update [choice ==] because of wait_for method
	# americas
	if choice == "americas":
		question2_a = await ctx.send("Which city would you like to visit?\n\
		\U0001f1e8\U0001f1e6 - Montreal, Canada\n\
		\U0001f1f2\U0001f1fd - Mexico City, Mexico\n\
		\U0001f1e8\U0001f1fa - Havana, Cuba")
		# add emojis
		emoji2_a = ["\U0001f1e8\U0001f1e6","\U0001f1f2\U0001f1fd","\U0001f1e8\U0001f1fa"]
		for emoji in emoji2_a:
			await question3.add_reactions(emoji)


	# africa_europe
	if choice == "africa_europe":
		question2_b = await ctx.send("Which city would you like to visit?\n\
		\U0001f1ff\U0001f1e6 - Cape Town, South Africa\n\
		\U0001f1ea\U0001f1f8 - Barcelona, Spain\n\
		\U0001f1ee\U0001f1f9 - Rome, Italy")
		# add emojis
		emoji2_b = ["\U0001f1ff\U0001f1e6","\U0001f1ea\U0001f1f8","\U0001f1ee\U0001f1f9"]
		for emoji in emoji2_b:
			await question3.add_reactions(emoji)	


	# asia_australia	
	if choice == "asia_australia":
		question2_c = await ctx.send("Which city would you like to visit?\n\
		\U0001f1f5\U0001f1ed - Manila, Philippines\n\
		\U0001f1e8\U0001f1ed - Beijing, China\n\
		\U0001f1fb\U0001f1f3 - Hanoi, Vietnam")		
		# add emojis
		emoji2_c = ["\U0001f1f5\U0001f1ed","\U0001f1e8\U0001f1ed","\U0001f1fb\U0001f1f3"]
		for emoji in emoji2_c:
			await question3.add_reactions(emoji)


# choose place, recipe, music, travel to another place, or go home
@client.command()
async def prm_choice(ctx):
	# 3rd question
	travel = 3
	question3 = await ctx.send("What would you like from this city?\n\
	\U0001f9ed - Place\n\
	\U0001f37d - Recipe\n\
	\U0001f3b5 - Music\n\
	\U0002708 - Travel\n\
	\U0001f3d8 - Go Home")
	# add emojis for 3rd question
	emoji3 = ["\U0001f9ed","\U0001f37d","\U0001f3b5","\U0002708","\U0001f3d8"]
	for emoji in emoji3:
		await question3.add_reactions(emoji)
	

# insert token below
bot.run("token")


