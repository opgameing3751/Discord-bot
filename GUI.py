#import bot
import os
import subprocess
import time
import asyncio
import dotenv
from tkinter.ttk import *


#from PIL import Image, ImageTk
#from bot import bot_alive_time
#from bot import bot_version
from tkinter import *
from dotenv import load_dotenv

from discord.ext.commands.core import command
GUI_version = 0.1
bot_alive_time = 0



print('starting GUI')
root = Tk()
root.configure(bg='gray')
root.geometry("550x305")
root.maxsize(550, 305)
root.minsize(550, 305)
root.title(f'Stream Manager')
bot_status = 1
dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

bot_alive_time = os.getenv('uptime')
GUI_uptime = 1


def start_bot():
    #os.startfile('bot.py')
    subprocess.call('start bot.py', shell=True)


    

def updatetime():
    
    global GUI_uptime
    GUI_uptime += 1
    os.environ["GUI_uptim"] = f'{GUI_uptime}'
    print(os.environ['GUI_uptim'])  # outputs 'newvalue'
    dotenv.set_key(dotenv_file, "GUI_uptim", os.environ["GUI_uptim"])
    button1.after(200, updatetime)

def update_button():
    from bot import uptime
    
    #global bot_alive_time
    #uptime = (os.environ['uptime'])
    button1.config(text=f'{uptime}')
    print(f'{uptime}')
    button1.after(200, update_button)


button1 = Button(root, text=f'start bot \n Uptime - {bot_alive_time} seconds' ,bg='gray', fg='black',command=start_bot)
button1.pack()

updatetime()
update_button()
root.mainloop()


#async def GUI_update():
 #   global bot_alive_time
  #  print('starting GUI_Update sys')
   # bot_status = 1
    #while bot_status == 1:
     #   print('started')
      #  await asyncio.sleep(1)
       # bot_alive_time = os.getenv('uptime')
        #print(f'{bot_alive_time}')
    #print('error')
        




#async def main():
 #   f1 = loop.create_task(GUI_update())
  #  f2 = loop.create_task(GUI())
   # await asyncio.wait([f1, f2])

#loop = asyncio.get_event_loop()
#loop.run_until_complete(main())
#print('program has endded')