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

	recipe = ""
	rep_title = ""
	rep_thumb = ""
	rep_desc = ""
	
	# Montréal, Canada
	if city == "\\U0001f1e8\\U0001f1e6":
		# area
		area = 0
		
		# recipe
		recipe = "https://www.seasonsandsuppers.ca/authentic-canadian-poutine-recipe/"
		rep_title = "Poutine"	
		rep_desc = "Poutine is a dish of french fries and cheese curds topped with a brown gravy. Enjoy!" 		
		rep_thumb = "https://v1.nitrocdn.com/eSLhakvQipAhEWtksvxrnpAZbKWwysTe/assets/static/source/rev-744f298/wp-content/uploads/2014/01/new-poutine-1-1170x.jpg"		

		# music
		music = 0

	# Mexico City, Mexico
	elif city == "\\U0001f1f2\\U0001f1fd":
		# area
		area = 0
		
		# recipe
		recipe = "https://www.isabeleats.com/chile-relleno-recipe/"
		rep_title = "Chiles Rellenos"
		rep_desc = "Chile rellenos (or ‘stuffed peppers‘ in English) are a traditional Mexican dish made from roasted poblano peppers stuffed with cheese, then coated in a fluffy egg batter and fried until golden brown. Enjoy!"
		rep_thumb = "https://www.isabeleats.com/wp-content/uploads/2020/03/chile-rellenos-small-13-650x975.jpg"
		
		#music
		music = 0

	# Havana, Cuba
	elif city == "\\U0001f1e8\\U0001f1fa":
		# area
		area = 0
		
		# recipe
		recipe = "https://www.bonappetit.com/recipe/ropa-vieja"
		rep_title = "Ropa Vieja"
		rep_desc = "Ropa vieja is one of the national dishes of Cuba, but is also popular in other areas of the region such as Puerto Rico and Panama, in Spain, and in the Philippines. It consists of shredded or pulled stewed beef with vegetables. Enjoy!"
		rep_thumb = "https://assets.bonappetit.com/photos/59c924d03b3bf713cb638086/1:1/w_2560%2Cc_limit/1017%252520WEB%252520WEEK0869.jpg"
		
		# music
		music = 0
	
	# Cape Town, South Africa
	elif city == "\\U0001f1ff\\U0001f1e6":
		# area
		area = 0
		
		# recipe
		recipe = "https://www.bbcgoodfood.com/recipes/cape-malay-chicken-curry-yellow-rice"
		rep_title = "Cape Malay Chicken Curry"
		rep_desc = "Spice up chicken thighs in a South African curry, packed with flavourful spices and served with a side of sweet, fragrant rice. Enjoy!"
		rep_thumb = "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/cape-malay-chicken-curry-with-yellow-rice-ab30139.jpg?quality=90&webp=true&resize=300,272"
		
		#music
		music = 0

	# Barcelona, Spain
	elif city == "\\U0001f1ea\\U0001f1f8":
		# area
		area = 0
		
		# recipe
		recipe = "https://tastesbetterfromscratch.com/paella/"
		rep_title = "Paella"
		rep_desc = "You can make a delicious, authentic Paella–the most popular dish of Spain–in your own kitchen with simple ingredients like rice, saffron, vegetables, chicken, and seafood. Enjoy!" 
		rep_thumb = "https://tastesbetterfromscratch.com/wp-content/uploads/2020/04/Paella-7.jpg" 
		
		# music
		music = 0
	
	# Rome, Italy
	elif city == "\\U0001f1ee\\U0001f1f9":
		# area
		area = 0
		
		# recipe
		recipe = "https://www.greatitalianchefs.com/recipes/pasta-alla-gricia-recipe"
		rep_title = "Pasta alla Gricia"
		rep_desc = "This pasta alla gricia recipe packs a real flavour punch thanks to the rich guanciale and Pecorino Romano. This dish makes use of the pasta cooking water, emulsifying with the gorgeous guanciale fat to create a rich and decidedly porky sauce. Enjoy!"
		rep_thumb = "https://gbc-cdn-public-media.azureedge.net/img72636.768x512.jpg"


	# Beijing, China
	elif city == "\\U0001f1ea\\U0001f1f8":
		#area
		area = 0
		
		# recipe
		recipe = "https://cooking.nytimes.com/recipes/1019963-peking-duck-with-honey-and-five-spice-glaze"
		rep_title = "Peking Duck"
		rep_desc = "Peking duck is a dish from Beijing that has been prepared since the Imperial era. The meat is characterized by its thin, crisp skin. Enjoy!"
		rep_thumb = ("https://static01.nyt.com/images/2019/01/28/dining/kc-peking-duck/kc-peking-duck-articleLarge-v2.jpg")	
	
		# music
		music = 0
	
	# Manila, Philippines
	elif city == "\\U0001f1f5\\U0001f1ed":
		# area
		area = 0

		# recipe
		recipe = "https://www.foxyfolksy.com/pandesal-recipe/"
		rep_title = "Pandesal"
		rep_desc = "Pandesal is a classic Filipino bread roll that is particularly eaten for breakfast. It is soft and airy and slightly sweet. Normally eaten as a sandwich with filling. Enjoy!"
		rep_thumb = "https://www.foxyfolksy.com/wp-content/uploads/2015/09/pandesal.jpg"
		
		# music
		music = 0

	# Hanoi, Vietnam
	elif city == "\\U0001f1fb\\U0001f1f3":
		print("Vietnam chosen")
		# area
		area = 0

		# recipe
		recipe = "https://www.allrecipes.com/recipe/228443/authentic-pho/"
		rep_title = "Pho"
		rep_desc = "Phở or pho is a Vietnamese soup consisting of broth, rice noodles, herbs, and meat. Enjoy!"
		rep_thumb = "https://www.recipetineats.com/wp-content/uploads/2019/04/Beef-Pho_6.jpg"
	
	await ctx.send("_ _")
	question3 = await ctx.send("What would you like from this city?\n\
	\U0001f9ed - Area\n\
	\U0001f37d - Food\n\
	\U0001f3b5 - Music\n\
	\U00002708 - Return flight")

	emoji3 = ["\U0001f9ed","\U0001f37d","\U0001f3b5","\U00002708"]
	for emoji in emoji3:
		await question3.add_reaction(emoji)

	activity_react = await client.wait_for('reaction_add', check=check, timeout=60.0)
	activity = str(activity_react[0])

	# area
	if activity == "\U0001f9ed":
		title = ""
	
	# food
	elif activity == "\U0001f37d":
		title = rep_title
		desc = rep_desc
		thumb = rep_thumb
		link = recipe
	
	# music
	elif activity == "\U0001f3b5":
		title = ""
	
	# return flight
	elif activity == "\U00002708":
		title = ""

	embed = discord.Embed(
		title = title,
		description = desc,
		colour = discord.Colour.blue()
	)

	embed.set_thumbnail(url=thumb)
	embed.add_field(name="Recipe", value=link, inline=True)

	await ctx.send(embed=embed)

# X is working on this rn
''' some code'''

# X is working on this rn
''' some code'''

# insert token below
client.run("token")


