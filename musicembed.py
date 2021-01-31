import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print("Online")


@client.command()
async def displayembed(ctx):
    
    # MUSIC

    # asia_australia
    # Philippines food Embed
    phil_m_embed = discord.Embed(
        title = 'Philippines Kundiman Classical Songs', url = "https://www.youtube.com/watch?v=7zUd96I4JN8"
        description = 'Kundiman is a genre of traditional Filipino love songs. The lyrics of the kundiman are written in Tagalog. The melody is characterized by a smooth, flowing and gentle rhythm with dramatic intervals. Kundiman was the traditional means of serenade in the Philippines.',
        colour = discord.Colour.blue()
    )
    phil_m_embed.set_thumbnail(url='https://judebgallery.files.wordpress.com/2015/08/thai-musical-instruments.jpg')


	# Vietnam food Embed
    viet_m_embed = discord.Embed(
        title = 'Vietnamese Dan Bau Music', url = "https://www.youtube.com/watch?v=lhS0B-8j02g"
        description = 'The đàn bầu (Vietnamese: [ɗàːn.ɓə̀w]; "gourd zither"; chữ Nôm: 彈匏), also called độc huyền cầm (獨絃琴, "one-string zither") is a Vietnamese stringed instrument, in the form of a monochord (one-string) zither.',
        colour = discord.Colour.()
    )
    viet_m_embed.set_thumbnail(url='https://4.bp.blogspot.com/-x-xw0A2ZdWU/WHRQ-FpLpVI/AAAAAAAAEHY/298Z4Fzusxcm5umbYM_I_Gx5DxsiMCUvACLcB/s1600/Dan%2BBau6.jpeg')

	# China food Embed
    china_m_embed = discord.Embed(
        title = 'Traditional Chinese Music', url = "https://www.youtube.com/watch?v=7D-Nj64uMW8"
        description = 'The flute, especially the bone flute, is one of the oldest musical instruments known. Examples of Paleolithic bone flutes have survived for more than 40,000 years, to be discovered by archaeologists. While the oldest flutes currently known were found in Europe, Asia too has a long history with the instrument that has continued into the present day. In China, a playable bone flute was discovered, about 9000 years old.',
        colour = discord.Colour.red()
    )
    china_m_embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/0/02/Bansuri_bamboo_flute_23inch.jpg')
