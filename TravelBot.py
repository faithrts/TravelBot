#!/usr/bin/env python3

import asyncio
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
@client.event
async def on_message(message):
	# check if the message says "Take me away" or "take me away"
	if message.content == "Take me away":
		# call launch_travel
		await ctx.invoke(self.bot.get_command("launch_travel")	
	
	await client.process_commands(message)	
'''

@client.command(aliases=['travelbot', 'TravelBot'])
async def launch_travel(ctx):	
	await ctx.send("Hi there! You're right on time for our next flight \U00002708")
	await asyncio.sleep(2)

	await ctx.send("_ _")	
	question = await ctx.send("Where do you want to go?\n\
	\U0001f30e - The Americas\n\
	\U0001f30d - Africa or Europe\n\
	\U0001f30f - Asia or Australia")
	
	
	await asyncio.sleep(2)
	emojis = ["\U0001f30e", "\U0001f30d", "\U0001f30f"]
	for emoji in emojis:
		await question.add_reaction(emoji)

	def check(reaction, user):
		return not(user.bot)
	
	continent_react = await client.wait_for('reaction_add', check=check, timeout=60.0)
	continent = str(continent_react[0])
	await asyncio.sleep(2)

	# the Americas
	if continent == "\U0001f30e":		
		await ctx.send("_ _")		
		await ctx.send("The Americas it is!")
		await ctx.send("_ _")

		question2_a = await ctx.send("Which city would you like to visit?\n\
	\U0001f1e8\U0001f1e6 - Montréal, Canada\n\
	\U0001f1f2\U0001f1fd - Mexico City, Mexico\n\
	\U0001f1e8\U0001f1fa - Havana, Cuba")
		
		await asyncio.sleep(2)
		emoji2_a = ["\U0001f1e8\U0001f1e6","\U0001f1f2\U0001f1fd","\U0001f1e8\U0001f1fa"]
		for emoji in emoji2_a:
			await question2_a.add_reaction(emoji)

	# Africa or Europe
	elif continent == "\U0001f30d":
		await ctx.send("_ _")
		await ctx.send("Spiriting you to Africa or Europe!")
		await ctx.send("_ _")
		
		await asyncio.sleep(2)
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

		await asyncio.sleep(2)
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

	# the unicodes of each city
	vietnam = "\U0001f1fb\U0001f1f3"
	montreal = "\U0001f1e8\U0001f1e6"
	mexico_city = "\U0001f1f2\U0001f1fd"		
	havana = "\U0001f1e8\U0001f1fa"
	cape_town = "\U0001f1ff\U0001f1e6"
	barcelona = "\U0001f1ea\U0001f1f8"	
	rome = "\U0001f1ee\U0001f1f9"	
	beijing = "\U0001f1e8\U0001f1f3"
	manila = "\U0001f1f5\U0001f1ed"
	
	if city == montreal:
		# area
		area = "https://goo.gl/maps/7M5Qrc4YBpZnHzCGA"
		area_title = "McGill University"
		area_desc = "The best place on Earth!"
		area_thumb = "https://www.ctvnews.ca/polopoly_fs/1.3872464.1522939278!/httpImage/image\
.jpg_gen/derivatives/landscape_1020/image.jpg"
		# recipe
		recipe = "https://www.seasonsandsuppers.ca/authentic-canadian-poutine-recipe/"
		rep_title = "Poutine"	
		rep_desc = "Poutine is a dish of french fries and cheese curds topped with a brown gravy. Enjoy!" 		
		rep_thumb = "https://v1.nitrocdn.com/eSLhakvQipAhEWtksvxrnpAZbKWwysTe/assets/static/source\
/rev-744f298/wp-content/uploads/2014/01/new-poutine-1-1170x.jpg"		
		# music
		music = "https://www.youtube.com/watch?v=qAmTrTY4VLU&list=PLykeTwOyMORwxOC2JD4Bq3v5M94K5vW62"
		music_title = "Montréal Chill"
		music_desc = "Some chill Montréal vibes"
		music_thumb = "https://www.outfrontmedia.ca/-/media/images/ofmcanada/markets/montreal/montreal\
-hero.jpg"

	elif city == mexico_city: 
		# area
		area = "https://goo.gl/maps/ykqEm86xtAczJxbP7"
		area_title = "Metropolitan Cathedral of Mexico City"
		area_desc = "The Metropolitan Cathedral of the Assumption of the Most Blessed Virgin Mary\
 into Heaven is the seat of the Catholic Archdiocese of Mexico. It is situated atop the former Aztec sacred\
 precinct near the Templo Mayor on the northern side of the Plaza de la Constitución in Downtown Mexico City."
		area_thumb = "https://www.tripsavvy.com/thmb/W_aFid36f3KdzI_Xkl_w40XeK44=/3936x2214/smart\
/filters:no_upscale()/TAM_5392-5c79a296c9e77c0001e98e59.jpg"	
		# recipe
		recipe = "https://www.isabeleats.com/chile-relleno-recipe/"
		rep_title = "Chiles Rellenos"
		rep_desc = "Chile rellenos (or ‘stuffed peppers‘ in English) are a traditional Mexican dish\
 made from roasted poblano peppers stuffed with cheese, then coated in a fluffy egg batter and fried until\
 golden brown. Enjoy!"
		rep_thumb = "https://www.isabeleats.com/wp-content/uploads/2020/03/chile-rellenos-small-13-650x975.jpg"
		#music
		music = "https://www.youtube.com/watch?v=AZRbcVG6WEQ"
		music_title = "Mexican Mariachi Music"
		music_desc = "A selection of greatest hits from traditional and popular Mexican music. Waltzes,\
 corridos and popular rancheras in a list without pauses to enjoy in any party or event"
		music_thumb = "https://www.tripsavvy.com/thmb/-V4Uk1AFzhBey2DzN26GIwIj5xk=/1115x836/smart/filters\
:no_upscale()/mariachi_getty-5681abcf3df78ccc15b4e325.jpg"

	elif city == havana:
		# area
		area = "https://goo.gl/maps/YXCuudKwAtYhUnY98"
		area_title = "Hotel Nacional de Cuba"
		area_desc = "The Hotel Nacional de Cuba is a historic Spanish eclectic style hotel in Havana,\
 Cuba, opened in 1930. Located on the sea front of the Vedado district, it stands on Taganana Hill, offering\
 commanding views of the sea and the city."
		area_thumb = "https://www.beyondtheordinary.co.uk/wp-content/uploads/2019/06/Hotel-Nacional\
-Havana-Aerial-1600x1021.jpeg"
		# recipe
		recipe = "https://www.bonappetit.com/recipe/ropa-vieja"
		rep_title = "Ropa Vieja"
		rep_desc = "Ropa vieja is one of the national dishes of Cuba, but is also popular in other\
 areas of the region such as Puerto Rico and Panama, in Spain, and in the Philippines. It consists of shredded\
 or pulled stewed beef with vegetables. Enjoy!"
		rep_thumb = "https://assets.bonappetit.com/photos/59c924d03b3bf713cb638086/1:1/w_2560%2Cc_limit\
/1017%252520WEB%252520WEEK0869.jpg"
		# music
		music = "https://www.youtube.com/watch?v=uEKHY3M2e7Q&list=PLC7F35B68F959C351"
		music_title = "Cuban Classics"
		music_desc = "Listen to some classic Cuban music, from salsa to rumba!"
		music_thumb = "https://mentalitch.com/wp-content/uploads/2019/12/salsa-music-band-in-cuba.jpg"
	
	elif city == cape_town:
		# area
		area = "https://goo.gl/maps/d9CUjwTwrZdvAA8a8"
		area_title = "New Cape Point Lighthouse"
		area_desc = "Check out one of the oldest lighthouses in South Africa! Explore the trails and\
 enjoy oceanside views that run alongside this Cabo Tormentosa (Cape of Storms) as named by Bartolomeu Dias\
 in the 15th century"
		area_thumb = "https://www.lightphotos.net/photos/albums/userpics/10001/normal_170.jpg"
		# recipe
		recipe = "https://www.bbcgoodfood.com/recipes/cape-malay-chicken-curry-yellow-rice"
		rep_title = "Cape Malay Chicken Curry"
		rep_desc = "Spice up chicken thighs in a South African curry, packed with flavourful spices\
 and served with a side of sweet, fragrant rice. Enjoy!"
		rep_thumb = "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/cape-malay\
-chicken-curry-with-yellow-rice-ab30139.jpg?quality=90&webp=true&resize=300,272"
		#music
		music = "https://www.youtube.com/watch?v=A1PsDkKzi8M&list=PLhTIvz9wTTu5HQGI4myeSFW2lHwrJHkK4"
		music_title = "South African Traditional Music"
		music_desc = "South Africa has a very broad range of styles ranging from marabi (which is the\
 root of south African Jazz) to local highlife, reggae and Zulu choral music known as mbube"
		music_thumb = "https://www.greyhound.co.za/wp-content/uploads/2018/09/120416041832-zulu-\
ceremony-horizontal-large-gallery.jpg"		

	elif city == barcelona:
		# area
		area = "https://goo.gl/maps/kUXNASg7vuts4DX99"
		area_title = "La Sagrada Familia"
		area_desc = "The Basílica de la Sagrada Família, also known as the Sagrada Família, is a\
 large unfinished Roman Catholic minor basilica in the Eixample district of Barcelona, Catalonia, Spain.\
 Designed by Spanish/Catalan architect Antoni Gaudí, his work on the building is part of a UNESCO World\
 Heritage Site"
		area_thumb = "https://images.adsttc.com/media/images/5cff/5ec5/284d/d16d/6a00/1111/\
large_jpg/1.jpg?1560239805"
		# recipe
		recipe = "https://spanishsabores.com/homemade-spanish-crema-catalana-recipe/"
		rep_title = "Crema Catalana"
		rep_desc = "Crema Catalana is Spain’s version of creme brûlée. Or, as many Catalans\
 would argue, creme brûlée is France’s version of Crema Catalana!" 
		rep_thumb = "https://spanishsabores.com/wp-content/uploads/2016/01/Crema-Catalana-Recipe.jpg" 
		# music
		music = "https://www.youtube.com/watch?v=HiFFdCBSJr4&list=PL2l5qPra0uFFt0bsuIvgbJ2tG1F7STYKy"
		music_title = "Rumba Catalana"
		music_desc = "The Catalan rumba is a genre of music that developed in Barcelona's Romani\
 community beginning in the 1950s and 160s. Its rhythms are derived from the Andalusian flamenco rumba, with\
 influences from Cuban music and rock and roll"
		music_thumb = "https://www.eventosbarcelona.com/wp-content/uploads/flamencorumba.jpg"

	elif city == rome:
		# area
		area = "https://goo.gl/maps/Ce8B9F7kZsb4TkZB7"
		area_title = "Colosseum"
		area_desc = "The Colosseum, is an oval amphitheatre in the centre of the city of Rome,\
 Italy, just east of the Roman Forum and is the largest ancient amphitheatre ever built, and is still\
 the largest standing amphitheater in the world today, despite its age"
		area_thumb = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Colosseo_2020\
.jpg/1200px-Colosseo_2020.jpg"
		# recipe
		recipe = "https://www.greatitalianchefs.com/recipes/pasta-alla-gricia-recipe"
		rep_title = "Pasta alla Gricia"
		rep_desc = "This pasta alla gricia recipe packs a real flavour punch thanks to the rich\
 guanciale and Pecorino Romano. This dish makes use of the pasta cooking water, emulsifying with the\
 gorgeous guanciale fat to create a rich and decidedly porky sauce. Enjoy!"
		rep_thumb = "https://gbc-cdn-public-media.azureedge.net/img72636.768x512.jpg"
		# music
		music = "https://www.youtube.com/watch?v=2S7BvkDN0hw"
		music_title = "Best Italian Songs"
		music_desc = "The music of Italy has traditionally been one of the cultural markers of\
 Italian national and ethnic identity and holds an important position in society and in politics."
		music_thumb = "https://i.ytimg.com/vi/aiENvviVSO4/maxresdefault.jpg"

	elif city == beijing:
		#area
		area = "https://goo.gl/maps/BojWyPDzis3YGTzm8"
		area_title = "The Palace Museum"
		area_desc = "The Palace Museum is a national museum housed in the Forbidden City at the\
 core of Beijing. It was established in 1925 after the last Emperor of China was evicted from his palace,\
 and opened its doors to the public. Constructed from 1406 to 1420, the museum consists of 980 buildings\
 and covers 72 hectares."
		area_thumb = "https://upload.wikimedia.org/wikipedia/commons/1/17/Flickr_-_Shinrya_-_The\
_Forbidden_City.jpg"
		# recipe
		recipe = "https://cooking.nytimes.com/recipes/1019963-peking-duck-with-honey-and-five-spice-glaze"
		rep_title = "Peking Duck"
		rep_desc = "Peking duck is a dish from Beijing that has been prepared since the Imperial\
 era. The meat is characterized by its thin, crisp skin. Enjoy!"
		rep_thumb = ("https://static01.nyt.com/images/2019/01/28/dining/kc-peking-duck/kc-peking\
-duck-articleLarge-v2.jpg")	
		# music
		music = "https://www.youtube.com/watch?v=7D-Nj64uMW8"
		music_title = "Traditional Chinese Music"
		music_desc = "The flute, especially the bone flute, is one of the oldest musical instruments\
 known. Examples of Paleolithic bone flutes have survived for more than 40,000 years, to be discovered by\
 archaeologists in China."	
		music_thumb = "https://upload.wikimedia.org/wikipedia/commons/0/02/Bansuri_bamboo_flute_23inch.jpg"

	elif city == manila: 
		# area
		area = "https://goo.gl/maps/MsNe3y7wCS6jwQ8TA"
		area_title = "Metro Manila"
		area_desc = "Metropolitan Manila, officially the National Capital Region, is the seat of\
 government and one of three defined metropolitan areas in the Philippines"
		area_thumb = "https://assets2.rappler.com/7EAAA4EC1FCC4212B62D7308E3FDBD59/img/552448836\
81A47EFB4856BFA207D7758/metro-manila-skyline-august-30-2017-002.jpg"
		# recipe
		recipe = "https://www.foxyfolksy.com/pandesal-recipe/"
		rep_title = "Pandesal"
		rep_desc = "Pandesal is a classic Filipino bread roll that is particularly eaten for\
 breakfast. It is soft and airy and slightly sweet. Normally eaten as a sandwich with filling. Enjoy!"
		rep_thumb = "https://www.foxyfolksy.com/wp-content/uploads/2015/09/pandesal.jpg"
		# music
		music = "https://www.youtube.com/watch?v=7zUd96I4JN8"
		music_title = "Philippines Kundiman Classical Songs"
		music_desc = "Kundiman is a genre of traditional Filipino love songs. The lyrics of the\
 kundiman are written in Tagalog. The melody is characterized by a smooth, flowing and gentle rhythm with\
 dramatic intervals. Kundiman was the traditional means of serenade in the Philippines."
		music_thumb = "https://judebgallery.files.wordpress.com/2015/08/thai-musical-instruments.jpg"

	elif city == vietnam:
		# area
		area = "https://goo.gl/maps/pMhjRaE3CmrFzGQXA"
		area_title = "Temple of Literature"
		area_desc = "Văn Miếu is a temple dedicated to Confucius in Hanoi, northern Vietnam.\
 The temple also hosts the Imperial Academy, Vietnam\'s first national university. The temple was built\
 in 1070 at the time of Emperor Lý Thánh Tông. It is one of several temples in Vietnam which is dedicated\
 to Confucius, sages and scholars"
		area_thumb = "https://static.toiimg.com/photo/58747476.cms"
		# recipe
		recipe = "https://www.allrecipes.com/recipe/228443/authentic-pho/"
		rep_title = "Pho"
		rep_desc = "Phở or pho is a Vietnamese soup consisting of broth, rice noodles, herbs,\
 and meat. Enjoy!"
		rep_thumb = "https://www.recipetineats.com/wp-content/uploads/2019/04/Beef-Pho_6.jpg"
		# music
		music = "https://www.youtube.com/watch?v=lhS0B-8j02g"
		music_title = "Vietnamese Dan Bau Music"
		music_desc = "The đàn bầu is a Vietnamese stringed instrument, taking the form of a\
 monochord (one-string) zither"
		music_thumb = "https://4.bp.blogspot.com/-x-xw0A2ZdWU/WHRQ-FpLpVI/AAAAAAAAEHY/298Z4F\
zusxcm5umbYM_I_Gx5DxsiMCUvACLcB/s1600/Dan%2BBau6.jpeg"		

	await asyncio.sleep(2)
	await ctx.send("_ _")
	question3 = await ctx.send("What would you like from this city?\n\
	\U0001f9ed - Area\n\
	\U0001f37d - Food\n\
	\U0001f3b5 - Music")

	await asyncio.sleep(2)
	emoji3 = ["\U0001f9ed","\U0001f37d","\U0001f3b5"]
	for emoji in emoji3:
		await question3.add_reaction(emoji)

	activity_react = await client.wait_for('reaction_add', check=check, timeout=60.0)
	activity = str(activity_react[0])
	
	title = ""
	desc = ""
	thumb = ""
	link = ""
	
	# area
	if activity == "\U0001f9ed":
		link = area
		title = area_title
		desc = area_desc
		thumb = area_thumb
		name = "Location"	
	
	# food
	elif activity == "\U0001f37d":
		link = recipe
		title = rep_title
		desc = rep_desc
		thumb = rep_thumb
		name = "Recipe"
	
	# music
	elif activity == "\U0001f3b5":
		link = music
		title = music_title
		desc = music_desc
		thumb = music_thumb
		name = "Playlist"
		
	await ctx.send("_ _")
	await ctx.send("This should be of interest:")

	embed = discord.Embed(
		title = title,
		description = desc,
		colour = discord.Colour.blue()
	)

	embed.set_thumbnail(url=thumb)
	embed.add_field(name=name, value=link, inline=True)

	await ctx.send(embed=embed)
	
	await asyncio.sleep(5)
	await ctx.send("_ _")
	await ctx.send("Oh! Your return flight is here! See you next time. \U00002708")

# insert token below
client.run("token")
