import discord
from discord.ext import commands

client = discord.Client() # establishing connection with discord

bot = commands.Bot(command_prefix='.') # establishing command prefix
