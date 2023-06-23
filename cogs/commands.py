import discord
from discord.ext import commands
from discord import app_commands
from main import *
import youtube_dl
from youtube_dl import YoutubeDL

client = commands.Bot(command_prefix='?', intents= discord.Intents.all())

@client.tree.command(guild_ids= 1035387699227541605, name = "play", description = "Comece a tocar")
async def play(ctx, url):
    voice_channel = ctx.author.voice.channel
    await voice_channel.connect()
    ydl_opts = {'format': 'bestaudio'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False, process=True, force_generic_extractor=False, verbose=True)
        audio_url = info_dict.get("url", None)

    vc = ctx.voice_client
    vc.play(discord.FFmpegPCMAudio(audio_url, executable="ffmpeg.exe", options="-vn"))

'''@bot.command()
async def play(ctx, *, query):
    voice_channel = ctx.author.voice.channel

    await voice_channel.connect()

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'song.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    'nocheckcertificate': True,
    'noplaylist': True,
    'quiet': True,
    'verbose': True,
    'no-call-home': True,
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['ytsearch:' + query])

    for file in os.listdir('./'):
        if file.endswith('.mp3'):
            os.rename(file, 'song.mp3')

    voice_client = ctx.guild.voice_client
    source = discord.FFmpegPCMAudio('song.mp3')
    player = voice_client.play(source)'''

@client.command()
async def stop(ctx):
    voice_client = ctx.guild.voice_client
    await voice_client.disconnect()