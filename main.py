from tokens import TOKEN_Orchestry as TOKEN
import discord

bot = discord.Bot(intents=discord.Intents.all(),)

@bot.event
async def on_ready():
    print('Bot está online e pronto para uso!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='suas musicas!'))

extensions = [# load cogs
    'cogs.commands',
]

if __name__ == '__main__': # import cogs from cogs folder
    for extension in extensions:
        bot.load_extension(extension)

bot.run(TOKEN)