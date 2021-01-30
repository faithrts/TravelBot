#!/usr/bin/python3

import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('TravelBot says hi and is ready.')

client.run('ODA1MDc3MjcxNzM5MjM2MzUy.YBVoow.ySgNX18V2sQYesrVzMWwZB3puhg')

