# bot.py
import os
import discord
import asyncio
import time
import GUI
from tkinter import *
from discord import message
from discord.ext import commands
from dotenv import load_dotenv
bot_version = 0.2
os.startfile('GUI.py')

load_dotenv()
TOKEN = 'OTAyOTE4NzEyNjQwNzk4Nzkw.YXlalA.NdhJBu5KNpC3ygZBYwg3akYmgnk'
bot = discord.Client()
times = 0
bot = commands.Bot(command_prefix='!')
prefix = ('!')
bot_alive_time = 0


@bot.event
async def on_ready():
    global bot_alive_time
    bot_status = 1
    print(f'{bot.user} has connected to Discord!')
    channel = bot.get_channel(902902470328594452)
    await channel.send(f'**Bot is now online**')
    bot_alive_time = 1
    while bot_status == 1:
        await asyncio.sleep(1)
        bot_alive_time += 1

@bot.command(name = 'uptime', help = 'hows how long the bot has been online')
async def uptime(ctx):
    await ctx.send(f'I have been online for {bot_alive_time} seconds')


@bot.command(name = "ping", help='sends a ping mosly for testing')
async def  ping(ctx):
    await ctx.send("pong")

@bot.command(name = 'quit', help = 'kills the bot')
async def quit(ctx):
    global bot_alive_time
    await ctx.send('ok im shuting down')
    channel = bot.get_channel(902902470328594452)
    await channel.send(f'**{ctx.author.name}** used the "quit" command')
    await ctx.send(f'the bot was online for {bot_alive_time} seconds')
    await exit()

@bot.command(name = 'spamtimes', help = 'number of time you want the spam command to spam')
async def spamtimes(ctx):
    global times
    spamedtimes = f'{ctx.message.content}'
    spamtime = spamedtimes.replace('!spamtimes', '')
    times = int(spamtime)
    await ctx.send(f'{prefix}spam will now spam {times} times')
    

@bot.command(name = 'spam', help = 'spams a message')
async def spam(ctx):
    global times
    spamed = f'{ctx.message.content}'
    spam = spamed.replace('!spam', '')
    channel = bot.get_channel(902902470328594452)
    await channel.send(f'**{ctx.author.name}** is spaming**{spam}** in **{ctx.channel}**')
    
    if times == 0:
        await ctx.send(f'spemed nothing plz use {prefix}spamtimes to set how many times to spam')
    else:
        while times > 0:
            await ctx.send(f'{spam}')
            print(f'{spam}')
            time.sleep(.1)
            times -= 1


@bot.command(name='set_activity', help='sets the activity of the bot')
async def bot_activity(ctx):
    yes = f'{ctx.message.content}'
    final_yes = yes.replace('!set_activity', '')
    activit = discord.Game(name=f'{final_yes}', type=3)
    await bot.change_presence(activity=activit)
    channel = bot.get_channel(902902470328594452)
    await channel.send(f'**{ctx.author.name}** used the "set_activity" command')
#@bot.event
#async def on_message(ctx):
#    print(f"{ctx.channel}-{ctx.author.name}: {ctx.content}")

bot.run(TOKEN)
root = mainloop()