#import bot
import subprocess
import time
#from PIL import Image, ImageTk
#from bot import bot_alive_time
#from bot import bot_version
from tkinter import *

from discord.ext.commands.core import command
GUI_version = 0.1

root = Tk()
root.configure(bg='gray')
root.geometry("550x305")
root.maxsize(550, 305)
root.minsize(550, 305)
root.title(f'Stream Manager')



def start_bot():
    subprocess.call('start bot.py', shell=True)    

button1 = Button(root, text='start bot', bg='gray', fg='black',command=start_bot)
button1.pack()

root.mainloop()

time.sleep(10)