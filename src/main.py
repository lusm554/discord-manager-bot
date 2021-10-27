import discord
from python_aternos import Client as AternosClient
from discord.ext import commands
from env import BOT_TOKEN, USER, PWD

bot = commands.Bot(command_prefix='>')
# log in
aternos = AternosClient(USER, password=PWD)

# get servers list
atservers = aternos.servers
mineserver = atservers[0]
addr = mineserver.address

permissions = [257541382627917825]

@bot.event
async def on_ready():
    await bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.listening,
                name=">help")
            )
    await bot.user.edit(username='minecraft manager')
    print(f'Running as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.before_invoke
async def checkpermission(msg):
    author = msg.author.id
    cmd = msg.command
    if not author in permissions:
        await msg.send("Пшел нахуй, это на новый год")
        raise discord.ext.commands.CommandError(f'User {author} try to run command \'{cmd}\'.')

@bot.command(brief='Run server', description='Run minecraft server')
async def run(ctx):
    mineserver.start()
    await ctx.send('Starting server (server starts up for about 2 minutes). Connect:```{}```'.format(addr))

@bot.command(brief='Stop server', description='Stop minecraft server')
async def stop(ctx):
    mineserver.stop()
    await ctx.send('Shutdown server...')

@bot.command(brief='Restart server', description='Restart minecraft server')
async def restart(ctx):
    mineserver.restart()
    await ctx.send('Rebooting server. Connect:```{}```'.format(addr))

@bot.command(brief='Get server address', description='Get server address')
async def address(ctx):
    await ctx.send('Address:```{}```'.format(addr))

bot.run(BOT_TOKEN)

