import discord
import asyncio
from config import channel_id, token
from discord.ext.commands import Bot

client = Bot(command_prefix='!')
#Start Bot...
@client.event
async def on_ready():
    print('StallBot initiated.')
    print(client.user.name)
    print(client.user.id)
    print('------')

#Wait for messages and reply to them...
@client.event
async def on_message(message):
    if message.content.startswith('!register-stall'):
        str = message.content
        token_list = str.split(' ')
        flag = 0
        #Check length of command, send stall information to designated channel...
        if len(token_list) == 4:

            msg = token_list[1] + "\'s " + token_list[2] + " stall on " + token_list[3] + " island."
            flag = 1
            await client.send_message(client.get_channel(channel_id), msg)
        else:
            msg = 'Format should be !register-stall <owner> <type-of-stall> <island>'
            await client.send_message(message.channel,msg)

        #Check if stall was registered and let user know...
        if flag == 1:
            msg = '{0.author.mention}'.format(message) + ' the stall has been registered.'
            await client.send_message(message.channel, msg)
        else:
            msg = "Your stall has not been registered."
            await client.send_message(message.channel, msg)

client.run(token)
