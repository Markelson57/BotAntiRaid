import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

prefix = "!"

bot = commands.Bot(command_prefix=prefix, intents=intents)


created_channels = []

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')
    print('------')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return


    if message.content.startswith('@everyone'):
        async for previous_message in message.channel.history(limit=10):
            if previous_message.author == bot.user and previous_message.content == message.content:
                await message.delete()
                break

    await bot.process_commands(message)

@bot.event
async def on_guild_channel_create(channel):

    if isinstance(channel, discord.TextChannel) and channel.name in created_channels:
        await channel.delete()
        print(f'Canal repetido detectado y eliminado: {channel.name}')
    else:
        created_channels.append(channel.name)

@bot.event
async def on_guild_channel_delete(channel):

    if channel.name in created_channels:
        created_channels.remove(channel.name)

@bot.event
async def on_member_join(member):

    if any(channel.name in created_channels for channel in member.guild.channels):
        await member.guild.kick(member)
        print(f'Miembro expulsado por crear canales repetidos: {member}')

bot.run('TOKEN')
