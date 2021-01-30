#!/usr/bin/python3

import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')


@client.event
async def on_ready():
	print("Online")


@client.event
async def displayembed():
    embed = discord.Embed(
        title = 'Title',
        description = 'This is a description.',
        colour = discord.Colour.blue()
    )

    embed.set_footer(text='This is a footer.')
    embed.set_thumbnail(url='https://media.cntraveler.com/photos/5f5fad3f7557491753644e3b/3:2/w_4050,h_2700,c_limit/50States50Cuisines-2020-AmberDay-Lede%20Option.jpg')
    emebed.set_author(name='Author Name', icon_url='https://media.cntraveler.com/photos/5f5fad3f7557491753644e3b/3:2/w_4050,h_2700,c_limit/50States50Cuisines-2020-AmberDay-Lede%20Option.jpg')
    embed.add_field(name='Field Name', value='Field Value', inline=False)
    embed.add_field(name='Field Name', value='Field Value', inline=True)

    await client.say(embed=embed)

# insert token below
client.run('ODA0OTEzMjQyNjM4OTA5NDUw.YBTP3w.oT75087RYMK3UdFh7EY57WAnA4g')
