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
	
	
# embed
@client.command()
async def displayembed(ctx):

	# FOOD

	# Americas
	# Montreal food embed
    mtl_f_embed = discord.Embed(
        title = 'Poutine', url = "https://www.seasonsandsuppers.ca/authentic-canadian-poutine-recipe/"
        description = 'Poutine is a dish of french fries and cheese curds topped with a brown gravy. Enjoy!',
        colour = discord.Colour.blue()
    )
    mtl_f_embed.set_thumbnail(url='https://v1.nitrocdn.com/eSLhakvQipAhEWtksvxrnpAZbKWwysTe/assets/static/source/rev-744f298/wp-content/uploads/2014/01/new-poutine-1-1170x.jpg')

	# Mexico food Embed
    mex_f_embed = discord.Embed(
        title = 'Chiles Rellenos', url = "https://www.isabeleats.com/chile-relleno-recipe/"
        description = 'Chile rellenos (or ‘stuffed peppers‘ in English) are a traditional Mexican dish made from roasted poblano peppers stuffed with cheese, then coated in a fluffy egg batter and fried until golden brown. Enjoy!',
        colour = discord.Colour.blue()
    )
    mex_f_embed.set_thumbnail(url='https://www.isabeleats.com/wp-content/uploads/2020/03/chile-rellenos-small-13-650x975.jpg')

	# Cuba food Embed
    cuba_f_embed = discord.Embed(
        title = 'Ropa Vieja', url = "https://www.bonappetit.com/recipe/ropa-vieja"
        description = 'Ropa vieja is one of the national dishes of Cuba, but is also popular in other areas of the region such as Puerto Rico and Panama, in Spain, and in the Philippines. It consists of shredded or pulled stewed beef with vegetables. Enjoy!',
        colour = discord.Colour.blue()
    )
    cuba_f_embed.set_thumbnail(url='https://assets.bonappetit.com/photos/59c924d03b3bf713cb638086/1:1/w_2560%2Cc_limit/1017%252520WEB%252520WEEK0869.jpg')



	# africa_europe
	# Barcelona food Embed
    barc_f_embed = discord.Embed(
        title = 'Paella', url = "https://tastesbetterfromscratch.com/paella/"
        description = 'You can make a delicious, authentic Paella–the most popular dish of Spain–in your own kitchen with simple ingredients like rice, saffron, vegetables, chicken, and seafood. Enjoy!',
        colour = discord.Colour.blue()
    )
    barc_f_embed.set_thumbnail(url='https://tastesbetterfromscratch.com/wp-content/uploads/2020/04/Paella-7.jpg')


	# Cape Town food Embed
    cape_f_embed = discord.Embed(
        title = 'Cape Malay Chicken Curry', url = "https://www.bbcgoodfood.com/recipes/cape-malay-chicken-curry-yellow-rice"
        description = 'Spice up chicken thighs in a South African curry, packed with flavourful spices and served with a side of sweet, fragrant rice. Enjoy!',
        colour = discord.Colour.blue()
    )
    cape_f_embed.set_thumbnail(url='https://images.immediate.co.uk/production/volatile/sites/30/2020/08/cape-malay-chicken-curry-with-yellow-rice-ab30139.jpg?quality=90&webp=true&resize=300,272')


	# Rome food Embed
    rome_f_embed = discord.Embed(
        title = 'Pasta alla Gricia', url = "https://www.greatitalianchefs.com/recipes/pasta-alla-gricia-recipe"
        description = 'This pasta alla gricia recipe packs a real flavour punch thanks to the rich guanciale and Pecorino Romano. This dish makes use of the pasta cooking water, emulsifying with the gorgeous guanciale fat to create a rich and decidedly porky sauce. Enjoy!',
        colour = discord.Colour.blue()
    )
    rome_f_embed.set_thumbnail(url='https://gbc-cdn-public-media.azureedge.net/img72636.768x512.jpg')



	# asia_australia
	# Philippines food Embed
    phil_f_embed = discord.Embed(
        title = 'Pandesal', url = "https://www.foxyfolksy.com/pandesal-recipe/"
        description = 'Pandesal is a classic Filipino bread roll that is particularly eaten for breakfast. It is soft and airy and slightly sweet. Normally eaten as a sandwich with filling. Enjoy!',
        colour = discord.Colour.blue()
    )
    phil_f_embed.set_thumbnail(url='https://www.foxyfolksy.com/wp-content/uploads/2015/09/pandesal.jpg')


	# Vietnam food Embed
    viet_f_embed = discord.Embed(
        title = 'Pho', url = "https://www.allrecipes.com/recipe/228443/authentic-pho/"
        description = 'Phở or pho is a Vietnamese soup consisting of broth, rice noodles, herbs, and meat, sometimes chicken. Enjoy!',
        colour = discord.Colour.blue()
    )
    viet_f_embed.set_thumbnail(url='https://www.recipetineats.com/wp-content/uploads/2019/04/Beef-Pho_6.jpg')

	# China food Embed
    china_f_embed = discord.Embed(
        title = 'Peking Duck', url = "https://cooking.nytimes.com/recipes/1019963-peking-duck-with-honey-and-five-spice-glaze"
        description = 'Peking duck is a dish from Beijing that has been prepared since the Imperial era. The meat is characterized by its thin, crisp skin. Enjoy!',
        colour = discord.Colour.blue()
    )
    china_f_embed.set_thumbnail(url='https://static01.nyt.com/images/2019/01/28/dining/kc-peking-duck/kc-peking-duck-articleLarge-v2.jpg')


# insert token below
bot.run("token")


