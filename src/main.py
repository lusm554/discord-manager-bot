import discord
from env import BOT_TOKEN

client = discord.Client()

@client.event
async def on_ready():
    print("We have looged in as {0.user}".format(client))

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return

    if msg.content.startswith("/hello"):
        await msg.channel.send("Hello!")

client.run(BOT_TOKEN)

