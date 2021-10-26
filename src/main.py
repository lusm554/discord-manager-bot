import discord
from discord.ext import commands
from env import BOT_TOKEN

bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    await bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.listening,
                name=">help")
            )
    print('Running as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command(brief='Run server', description='Run minecraft server')
async def run(ctx):
    await ctx.send('run')

@bot.command(brief='Stop server', description='Stop minecraft server')
async def stop(ctx):
    await ctx.send('stop')

@bot.command(brief='Restart server', description='Restart minecraft server')
async def restart(ctx):
    await ctx.send('restart')

bot.run(BOT_TOKEN)

