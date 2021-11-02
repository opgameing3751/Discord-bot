import bot
from PIL import Image, ImageTk
from bot import bot_alive_time
from bot import bot_version
from tkinter import *
GUI_version = 0.1

root = Tk()
root.configure(bg='gray')
root.geometry("550x305")
root.maxsize(550, 305)
root.minsize(550, 305)
root.title(f'Stream Manager v{version}')
ico = Image.open('ico.png')
icon = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, icon)
root.attributes('-topmost', True)

def Bot_uptime():
    print('hello')    

root.mainloop()