import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands

client = Bot(description="MyFirstBot", command_prefix="Prefix", pm_help=True)


@client.event
async def on_ready():
    print('Logged in as ' + client.user.name + ' (ID:' + client.user.id + ') | Connected to ' + str(
        len(client.servers)) + ' servers | Connected to ' + str(len(set(client.get_all_members()))) + ' users')
    print('--------')


@client.command()
async def ping(*args):
    await client.say(":ping_pong: Pong!")
    await asyncio.sleep(3)

client.run('Token')
