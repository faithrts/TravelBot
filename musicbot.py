import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.command()
async def play(ctx):
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    
    await voiceChannel.connect()
    
    
    voiceChannel.play(discord.FFmpegPCMAudio("song.mps3"))


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing")

@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    
@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel")

client.run('ODA1MjgyMDg2MzIyNzAwMzA4.YBYnYg.o7vV5KqESTV7RWkE3W89Uttx3mM')
