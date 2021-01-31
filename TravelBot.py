#!/usr/bin/python3

import discord
from discord.ext import commands
import ffmpeg
import youtube_dl

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
	print("Online")


@client.command()
async def displayembed(ctx):
    embed = discord.Embed(
        title = 'Title',
        description = 'This is a description.',
        colour = discord.Colour.blue()
    )

    embed.set_footer(text='This is a footer.')
    embed.set_thumbnail(url='https://media.cntraveler.com/photos/5f5fad3f7557491753644e3b/3:2/w_4050,h_2700,c_limit/50States50Cuisines-2020-AmberDay-Lede%20Option.jpg')
    embed.set_author(name='Author Name', icon_url='https://media.cntraveler.com/photos/5f5fad3f7557491753644e3b/3:2/w_4050,h_2700,c_limit/50States50Cuisines-2020-AmberDay-Lede%20Option.jpg')
    embed.add_field(name='Field Name', value='Field Value', inline=False)
    embed.add_field(name='Field Name', value='Field Value', inline=True)

    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.guild.voice_client
    await server.disconnect()
'''
@client.command()
async def channels(ctx):
    voice_channel_list = ctx.guild.voice_channels
    print(voice_channel_list)

@client.command(pass_context=True)
async def join(ctx):
    global voice
    channel = ctx.author.voice.channel
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        print("move")
        await voice.move_to(channel)
    else:
        print("play1")
        chan = ctx.author.voice.channel
        await discord.change_voice_state(chan)
        print("hi")
        await channel.connect()
        print("play2")
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        print("play3")
        voice.play(discord.FFmpegPCMAudio("song.mp3"))
 
    #await voice.disconnect
    
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f"The bot has connected to {channel}\n")
    await ctx.send(f"Joined {channel}")

@client.command(pass_context=True)
async def leave(ctx):
    #channel = ctx.message.author.voice.channel
    channel = discord.utils.get(ctx.guild.voice_channels, name='General')
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    
    chan = ctx.author.voice.channel
    await discord.change_voice_state(None)
    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"The bot has left {channel}")
        await ctx.send(f"Left {channel}")
    else:
        print("Bot was told to leave voice channel, but was not in one")
        await ctx.send("Don't think I am in a voice channel")

@client.command(pass_context=True)
async def play(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("song.mp3"))

#@client.command(pass_context=True)

'
players = {}

@client.command(pass_context=True)
async def join(ctx):
    
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')

    #if not voice.is_connected():
    await voiceChannel.connect()


@client.command(pass_context=True)
async def leave(ctx):
    
    server = ctx.message.guild
    voice_client = ctx.guild.voice_client(server)
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    
    await voiceChannel.disconnect()


@client.command(pass_context=True)
async def play(ctx):
    server = ctx.message.guild
    voice_client = ctx.guild.voice_client(server)
    player = await voiceChannel.connect_ytdl_player('https://www.youtube.com/watch?v=2L02HAEBHE4')
    players[server.id] = player
    print(player)
    player.start()'

@client.command()
async def play(ctx):
    print("play")
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    
    #if not voice.is_connected():
    await voiceChannel.connect()
    print(voiceChannel)
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild) 
    print("hello")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    print("bye")


@client.command()
async def leave(ctx):
    print("leave")
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel")

@client.command()
async def pause(ctx):
    print("pause")
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing")

@client.command()
async def resume(ctx):
    print("resume")
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused")

@client.command()
async def stop(ctx):
    print("stop")
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()
'''

# insert token below
client.run('ODA1MDc3MjcxNzM5MjM2MzUy.YBVoow.9etQO8FSSpYLUMxdHnsmoqUkID0')
