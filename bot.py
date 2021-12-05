# bot.py
import subprocess
import os
import discord
import asyncio
import time
import dotenv
from datetime import datetime
from tkinter import *
from discord import message
from discord.ext import commands
from dotenv import load_dotenv

bot_version = 0.2


root =Tk()
now = datetime.now()
dotenv_file = dotenv.find_dotenv()
load_dotenv()

TOKEN = 'OTAyOTE4NzEyNjQwNzk4Nzkw.YXlalA.NdhJBu5KNpC3ygZBYwg3akYmgnk'
bot = discord.Client()
times = 0
bot = commands.Bot(command_prefix='!')
prefix = ('!')
bot_alive_time = 0
final_yes = os.getenv('last_act')

uptime = 0
uptime = os.getenv('uptime')
print(f'last online time was {uptime}')
life = os.getenv('lifetime')
print(f'life time is {life}')
#lifetime = int(uptime)
lifetime = int(life) + int(uptime) 
os.environ["lifetime"] = f"{lifetime}"
dotenv.set_key(dotenv_file, 'lifetime', os.environ['lifetime'])
print(f'after math {lifetime}')         
time.sleep(1)
restart()


def updatetime():
    global lifetime
    os.environ["uptime"] = f"{bot_alive_time}"
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
    print(os.environ['uptime'])  # outputs 'newvalue'
    dotenv.set_key(dotenv_file, "uptime", os.environ["uptime"])
    os.environ['last_act'] = f'{final_yes}'
    dotenv.set_key(dotenv_file, 'last_act', os.environ['last_act'])
    dotenv.set_key(dotenv_file, 'lifetime', os.environ['lifetime'])
    
    
    

@bot.event
async def on_ready():
    global final_yes
    global bot_alive_time
    bot_status = 1
    print(f'{bot.user} has connected to Discord!')
    channel = bot.get_channel(902902470328594452)
    await channel.send(f'**Bot is now online**')
    await channel.send(f'last online time {os.getenv("uptime")}')
    await channel.send(f'lifetime {os.getenv("lifetime")}')
    await channel.send(f'current activity is {final_yes}')
    bot_alive_time = 1
    while bot_status == 1:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if current_time == "00:00:00":
            print('restarting server')
            channel = bot.get_channel(829002985048113154)
            await channel.send(f'server restart in 10s')
            await asyncio.sleep(1)
            await channel.send(f'server restart in 9s')
            await asyncio.sleep(1)
            await channel.send(f'server restart in 8s')
            await asyncio.sleep(1)
            await channel.send(f'server restart in 7s')
            await asyncio.sleep(1)
            await channel.send(f'server restart in 6s')
            await asyncio.sleep(1)
            await channel.send(f'server restart in 5s')
            await asyncio.sleep(1)
            await channel.send(f'server restart in 4s')
            await asyncio.sleep(1)
            await channel.send(f'server restart in 3s')
            await asyncio.sleep(1)
            await channel.send(f'server restart in 2s')
            await asyncio.sleep(1)
            await channel.send(f'server restart in 1s')
            await asyncio.sleep(1)
            await channel.send(f'server restarting')
            await asyncio.sleep(1)
            channel = bot.get_channel(916176075539750963)
            await channel.send('stop')
        else:
            await asyncio.sleep(1)
            bot_alive_time += 1
            activit = discord.Game(name=f'uptime - {bot_alive_time} | {final_yes}', type=3)
            await bot.change_presence(activity=activit)
            updatetime()
        
        
        
@bot.command(name = 'uptime', help = 'hows how long the bot has been online')
async def uptime(ctx):
    await ctx.send(f'I have been online for {bot_alive_time} seconds')
    await ctx.send(f'and my life time is {lifetime}')

@bot.command(name = "ping", help='sends a ping mosly for testing')
async def  ping(ctx):
    await ctx.send("pong")


@bot.command(name = 'quit', help = 'kills the bot')
async def quit(ctx):
    if ctx.author.name == "opgameing3751":
        global bot_alive_time
        await ctx.send('ok im shuting down')
        channel = bot.get_channel(902902470328594452)
        await channel.send(f'**{ctx.author.name}** used the "quit" command')
        await ctx.send(f'the bot was online for {bot_alive_time} seconds')
        await exit()
    else:
        await ctx.send(f"sorry {ctx.author.name} you cant do that.")


@bot.command(name = 'spamtimes', help = 'number of time you want the spam command to spam')
async def spamtimes(ctx):
    global times
    spamedtimes = f'{ctx.message.content}'
    spamtime = spamedtimes.replace(f'{prefix}spamtimes', '')
    times = int(spamtime)
    await ctx.send(f'{prefix}spam will now spam {times} times')
    

@bot.command(name = 'spam', help = 'spams a message')
async def spam(ctx):
    global times
    spamed = f'{ctx.message.content}'
    spam = spamed.replace(f'{prefix}spam','')
    spam2 = spam.replace('@everyone', '')
    spam3 = spam2.replace('@', ':}')
    if spam2 == '@everyone':
        await ctx.send('ya no sorry you can just @ everyone')
    else:
        channel = bot.get_channel(902902470328594452)
        await channel.send(f'**{ctx.author.name}** is spaming**{spam}** in **{ctx.channel}**')
        if times == 0:
            await ctx.send(f'spammed nothing plz use {prefix}spamtimes to set how many times to spam')
        else:
            while times > 0:
                await ctx.send(f'{spam3}')
                print(f'{spam}')
                time.sleep(.1)
                times -= 1


@bot.command(name='set_activity', help='sets the activity of the bot')
async def bot_activity(ctx):
    global final_yes
    if ctx.author.name == "opgameing3751":
        yes = f'{ctx.message.content}'
        final_yes = yes.replace(f'{prefix}set_activity', '')
        activitity = (f'{final_yes}')
        channel = bot.get_channel(902902470328594452)
        await channel.send(f'**{ctx.author.name}** used the "set_activity" command')
    else:
        await ctx.send(f"sorry {ctx.author.name} you can't do that")
        channel = bot.get_channel(902902470328594452)
        await channel.send(f'**{ctx.author.name}** tried to use "set_activity" but did not have the perms to')

@bot.command(name='xander', help='xander')
async def xander(ctx):
    await ctx.send(file=discord.File("xander.png"))
    await ctx.send('Xander')


@bot.command(name='restart_server', help='restarts the minecraft server')
async def restart(ctx):
    if ctx.author.name == "opgameing3751":
        channel = bot.get_channel(829002985048113154)
        await channel.send(f'server restart in 10s')
        time.sleep(1)
        await channel.send(f'server restart in 9s')
        time.sleep(1)
        await channel.send(f'server restart in 8s')
        time.sleep(1)
        await channel.send(f'server restart in 7s')
        time.sleep(1)
        await channel.send(f'server restart in 6s')
        time.sleep(1)
        await channel.send(f'server restart in 5s')
        time.sleep(1)
        await channel.send(f'server restart in 4s')
        time.sleep(1)
        await channel.send(f'server restart in 3s')
        time.sleep(1)
        await channel.send(f'server restart in 2s')
        time.sleep(1)
        await channel.send(f'server restart in 1s')
        time.sleep(1)
        channel = bot.get_channel(916176075539750963)
        await channel.send('stop')
    else:
        await ctx.send('you dont have the perms to do that')
        
@bot.command(name='time', help='tells the time i hope')
async def time(ctx):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    await ctx.send(f'Current Time= {current_time}')



#@bot.event
#async def on_message(ctx):
#    print(f"{ctx.channel}-{ctx.author.name}: {ctx.content}")

bot.run(TOKEN)
root.mainloop()