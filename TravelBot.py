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
        title = 'Crema Catalana', url = "https://spanishsabores.com/homemade-spanish-crema-catalana-recipe/"
        description = 'Crema Catalana (for those unfamiliar) is Spain’s version of creme brûlée. Or, as many Catalans would argue, creme brûlée is France’s version of Crema Catalana!',
        colour = discord.Colour.blue()
    )
    barc_f_embed.set_thumbnail(url='https://spanishsabores.com/wp-content/uploads/2016/01/Crema-Catalana-Recipe.jpg')


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

	
	# AREAS

	# Americas
	# Montreal area embed
    mtl_a_embed = discord.Embed(
        title = 'McGill University', url = "https://goo.gl/maps/7M5Qrc4YBpZnHzCGA"
        description = 'Best place on earth!',
        colour = discord.Colour.blue()
    )
    mtl_a_embed.set_thumbnail(url='https://www.ctvnews.ca/polopoly_fs/1.3872464.1522939278!/httpImage/image.jpg_gen/derivatives/landscape_1020/image.jpg')

	# Mexico area Embed
    mex_a_embed = discord.Embed(
        title = 'Metropolitan Cathedral of Mexico City', url = "https://goo.gl/maps/ykqEm86xtAczJxbP7"
        description = 'The Metropolitan Cathedral of the Assumption of the Most Blessed Virgin Mary into Heaven is the seat of the Catholic Archdiocese of Mexico. It is situated atop the former Aztec sacred precinct near the Templo Mayor on the northern side of the Plaza de la Constitución in Downtown Mexico City.',
        colour = discord.Colour.blue()
    )
    mex_a_embed.set_thumbnail(url='https://www.tripsavvy.com/thmb/W_aFid36f3KdzI_Xkl_w40XeK44=/3936x2214/smart/filters:no_upscale()/TAM_5392-5c79a296c9e77c0001e98e59.jpg')

	# Cuba area Embed
    cuba_a_embed = discord.Embed(
        title = 'Hotel Nacional de Cuba', url = "https://goo.gl/maps/YXCuudKwAtYhUnY98"
        description = 'The Hotel Nacional de Cuba is a historic Spanish eclectic style hotel in Havana, Cuba, opened in 1930. Located on the sea front of the Vedado district, it stands on Taganana Hill, offering commanding views of the sea and the city.',
        colour = discord.Colour.blue()
    )
    cuba_a_embed.set_thumbnail(url='https://www.beyondtheordinary.co.uk/wp-content/uploads/2019/06/Hotel-Nacional-Havana-Aerial-1600x1021.jpeg')



	# africa_europe
	# Barcelona area Embed
    barc_a_embed = discord.Embed(
        title = 'La Sagrada Familia', url = "https://goo.gl/maps/kUXNASg7vuts4DX99"
        description = 'The Basílica de la Sagrada Família, also known as the Sagrada Família, is a large unfinished Roman Catholic minor basilica in the Eixample district of Barcelona, Catalonia, Spain. Designed by Spanish/Catalan architect Antoni Gaudí, his work on the building is part of a UNESCO World Heritage Site.',
        colour = discord.Colour.blue()
    )
    barc_a_embed.set_thumbnail(url='https://images.adsttc.com/media/images/5cff/5ec5/284d/d16d/6a00/1111/large_jpg/1.jpg?1560239805')


	# Cape Town area Embed
    cape_a_embed = discord.Embed(
        title = 'New Cape Point Lighthouse', url = "https://goo.gl/maps/d9CUjwTwrZdvAA8a8"
        description = 'Check out one of the oldest lighthouses in South Africa! Explore the trails and enjoy oceanside views that run alongside this Cabo Tormentosa (Cape of Storms) as named by Bartolomeu Dias in the 15th century.',
        colour = discord.Colour.blue()
    )
    cape_a_embed.set_thumbnail(url='https://www.lightphotos.net/photos/albums/userpics/10001/normal_170.jpg')


	# Rome area Embed
    rome_a_embed = discord.Embed(
        title = 'Colosseum', url = "https://goo.gl/maps/Ce8B9F7kZsb4TkZB7"
        description = 'The Colosseum, is an oval amphitheatre in the centre of the city of Rome, Italy, just east of the Roman Forum and is the largest ancient amphitheatre ever built, and is still the largest standing amphitheater in the world today, despite its age.',
        colour = discord.Colour.blue()
    )
    rome_a_embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Colosseo_2020.jpg/1200px-Colosseo_2020.jpg')



	# asia_australia
	# Philippines area Embed
    phil_a_embed = discord.Embed(
        title = 'Metro Manila', url = "https://goo.gl/maps/MsNe3y7wCS6jwQ8TA"
        description = 'Metropolitan Manila, officially the National Capital Region, is the seat of government and one of three defined metropolitan areas in the Philippines.',
        colour = discord.Colour.blue()
    )
    phil_a_embed.set_thumbnail(url='https://assets2.rappler.com/7EAAA4EC1FCC4212B62D7308E3FDBD59/img/55244883681A47EFB4856BFA207D7758/metro-manila-skyline-august-30-2017-002.jpg')


	# Vietnam area Embed
    viet_a_embed = discord.Embed(
        title = 'Temple of Literature', url = "https://goo.gl/maps/pMhjRaE3CmrFzGQXA"
        description = 'Văn Miếu is a temple dedicated to Confucius in Hanoi, northern Vietnam. The temple also hosts the Imperial Academy, Vietnam\'s first national university. The temple was built in 1070 at the time of Emperor Lý Thánh Tông. It is one of several temples in Vietnam which is dedicated to Confucius, sages and scholars.',
        colour = discord.Colour.blue()
    )
    viet_a_embed.set_thumbnail(url='https://static.toiimg.com/photo/58747476.cms')

	# China area Embed
    china_a_embed = discord.Embed(
        title = 'The Palace Museum', url = "https://goo.gl/maps/BojWyPDzis3YGTzm8"
        description = 'The Palace Museum is a national museum housed in the Forbidden City at the core of Beijing. It was established in 1925 after the last Emperor of China was evicted from his palace, and opened its doors to the public. Constructed from 1406 to 1420, the museum consists of 980 buildings and covers 72 hectares.',
        colour = discord.Colour.blue()
    )
    china_a_embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/1/17/Flickr_-_Shinrya_-_The_Forbidden_City.jpg')
	
	# MUSIC

	# Americas
	# Montreal music embed
    mtl_m_embed = discord.Embed(
        title = 'Montreal Chill', url = "https://www.youtube.com/watch?v=qAmTrTY4VLU&list=PLykeTwOyMORwxOC2JD4Bq3v5M94K5vW62"
        description = 'Some chill montreal vibes.',
        colour = discord.Colour.blue()
    )
    mtl_m_embed.set_thumbnail(url='https://www.outfrontmedia.ca/-/media/images/ofmcanada/markets/montreal/montreal-hero.jpg')

	# Mexico music Embed
    mex_m_embed = discord.Embed(
        title = 'Mexican Mariachi Music', url = "https://www.youtube.com/watch?v=AZRbcVG6WEQ"
        description = 'This is a selection of greatest hits from traditional and popular Mexican music. Waltzes, corridos and popular rancheras in a list without pauses to enjoy in any party or event.',
        colour = discord.Colour.blue()
    )
    mex_m_embed.set_thumbnail(url='https://www.tripsavvy.com/thmb/-V4Uk1AFzhBey2DzN26GIwIj5xk=/1115x836/smart/filters:no_upscale()/mariachi_getty-5681abcf3df78ccc15b4e325.jpg')

	# Cuba music Embed
    cuba_m_embed = discord.Embed(
        title = 'Cuban Classics', url = "https://goo.gl/maps/YXCuudKwAtYhUnY98"
        description = 'Listen to some classic Cuban music, from salsa to rumba!',
        colour = discord.Colour.blue()
    )
    cuba_m_embed.set_thumbnail(url='https://mentalitch.com/wp-content/uploads/2019/12/salsa-music-band-in-cuba.jpg')



	# africa_europe
	# Barcelona music Embed
    barc_m_embed = discord.Embed(
        title = 'Rumba Catalana', url = "https://www.youtube.com/watch?v=HiFFdCBSJr4&list=PL2l5qPra0uFFt0bsuIvgbJ2tG1F7STYKy"
        description = 'The Catalan rumba is a genre of music that developed in Barcelona\'s Romani community beginning in the 1950s and 160s. Its rhythms are derived from the Andalusian flamenco rumba, with influences from Cuban music and rock and roll.',
        colour = discord.Colour.blue()
    )
    barc_m_embed.set_thumbnail(url='https://www.eventosbarcelona.com/wp-content/uploads/flamencorumba.jpg')


	# Cape Town area Embed
    cape_m_embed = discord.Embed(
        title = 'South African Traditional Music', url = "https://www.youtube.com/watch?v=A1PsDkKzi8M&list=PLhTIvz9wTTu5HQGI4myeSFW2lHwrJHkK4"
        description = 'South Africa has a very broad range of styles ranging from marabi (which is the root of south African Jazz) to local highlife, reggae and Zulu choral music known as mbube.',
        colour = discord.Colour.blue()
    )
    cape_m_embed.set_thumbnail(url='https://www.greyhound.co.za/wp-content/uploads/2018/09/120416041832-zulu-ceremony-horizontal-large-gallery.jpg')

	# Rome area Embed
    rome_m_embed = discord.Embed(
        title = 'Best Italian Songs', url = "https://www.youtube.com/watch?v=2S7BvkDN0hw"
        description = 'The music of Italy has traditionally been one of the cultural markers of Italian national and ethnic identity and holds an important position in society and in politics.',
        colour = discord.Colour.blue()
    )
    rome_m_embed.set_thumbnail(url='https://i.ytimg.com/vi/aiENvviVSO4/maxresdefault.jpg')
	

# insert token below
bot.run("token")


