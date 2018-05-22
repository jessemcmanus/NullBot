# BangNull Bot
# Client ID: 448257175056547851
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

# Define variables that will remain constant
TOKEN = 'FAKETOKEN'

Client = discord.Client()
client = commands.Bot(command_prefix = "!")

# This will display a message when Null Bot has connected to the BangNull server.
@client.event
async def on_ready():
    print('Connected as: ' + client.user.name)
    print(client.user.id)
    print('---------------')

# When a user sends a message
@client.event
async def on_message(message):
    # If the message is from the Bot, ignore it
    if message.author == client.user:
        return
    # If the message starts with "!hello"
    if message.content.upper().startswith('!HELLO'):
        # Save the user ID
        userID = message.author.id
        # Print a message that mentions the user that called the "!hello" command
        await client.send_message(message.channel, "Hello  <@%s>"  % userID)
    elif message.content.upper().startswith("!TOPIC"):
        userID = message.author.id
        if message.channel.topic == None:
            await client.send_message(message.channel, "There is no topic set.")
        else:
            await client.send_message(message.channel, "The topic is: " + message.channel.topic)

# For Channel specific events, such as channel deletion, creation or other similar events,
# Null bot will DM Jese.
@client.event
async def on_channel_create(channel):
    user = await client.get_user_info('309232054556426240')
    await client.send_message(user, "Channel Created " + channel.name)
@client.event
async def on_channel_delete(channel):
    user = await client.get_user_info('309232054556426240')
    await client.send_message(user, "Channel Deleted: " + channel.name)


client.run(TOKEN)
