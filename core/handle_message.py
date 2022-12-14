from core import commands
import discord
from dotenv import dotenv_values
import os

dotenv_values()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


def handle_message(msg):
    command_found = [
        command for command in commands.value if command['key'] == msg][0]
    command_found['callback'](msg)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    command_found = [command for command in commands.value if command['key'] == message.content][0]

    if command_found:
        await message.channel.send(command_found['callback'](message))



token = os.environ.get("DISCORD_SECRET")
client.run(token)


