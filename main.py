version = 0.5
# Created 9/15/21
# made by Adam
# special thxs to Patrick for the spam code
from tkinter import *
from PIL import Image, ImageTk
import os
import keyboard
import webbrowser
import time


Muted = False
Desktop = False
color = 1

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

# def and apps
v = StringVar()
v.set("L")


def Topmost_on():
    root.attributes('-topmost', True)


def Topmost_off():
    root.attributes('-topmost', False)


def spamexe():
    os.startfile("C:\Program Files (x86)\Adams programs\spam.exe")


def streaming():
    os.startfile('C:\Program Files\Streamlabs OBS\Streamlabs OBS.exe')
    os.startfile("C:\Program Files (x86)\Adams programs\Discord - Shortcut.lnk")
    url = 'https://www.speechchat.com'
    webbrowser.open(url)


def colorgray():
    root.configure(bg='gray')
    global color
    color = 1


def colorred():
    root.configure(bg='red')
    global color
    color = 2


def colorblue():
    root.configure(bg='blue')
    global color
    color = 3


def colorpurple():
    root.configure(bg='#280137')
    global color
    color = 4


def openxander():
    top = Toplevel()
    top.geometry('124x124')
    top.title('Xander')
    load = Image.open('xander.png')
    resize = load.resize((124, 124), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(resize)
    img = Label(top, image=render)
    img.image = render
    img.pack()


def projectlocat():
    os.startfile("C:\\Users\\jeepm\\PycharmProjects\\Programmaningerv2")


def exelocat():
    os.startfile("C:\Program Files (x86)\Adams programs")


def CRASH():
    top = Toplevel()
    top.attributes('-fullscreen', True)
    top.title('CRASH.png')
    load = Image.open('CRASH.png')
    resize = load.resize((1920, 1080), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(resize)
    img = Label(top, image=render)
    img.image = render
    img.pack()


def C418():
    os.startfile("C:\Program Files (x86)\Adams programs\C418 - Sweden.mp3")


def spamexe():
    os.startfile("C:\Program Files (x86)\Adams programs\spam.exe")
    root.wm_state('iconic')


def Togglemute():
    global Muted
    keyboard.press('Ctrl+Home')
    if not Muted:
        keyboard.press('Ctrl+Delete')
        time.sleep(.5)
        keyboard.release('Ctrl+Delete')
        Muted = True
        Button3.configure(image=unmute)
    elif Muted:
        keyboard.press('Ctrl+insert')
        time.sleep(.5)
        keyboard.release('Ctrl+insert')
        Muted = False
        Button3.configure(image=mutepng)
    else:
        print('Error 1')


def DesktopAudio():
    global Desktop
    if not Desktop:
        keyboard.press('Alt+Ctrl+Insert')
        time.sleep(.5)
        keyboard.release('Alt+Ctrl+Insert')
        Desktop = True
        Button4.configure(image=muteDesktop)
    elif Desktop:
        keyboard.press('Alt+Ctrl+Home')
        time.sleep(.5)
        keyboard.release('Alt+Ctrl+Home')
        Desktop = False
        Button4.configure(image=desktop)
    else:
        print('Error 2')


def Starting_soon():
    keyboard.press('Alt+Ctrl+shift+Equal')
    time.sleep(.1)
    keyboard.release('Alt+Ctrl+shift+Equal')


def Main_scene():
    keyboard.press('alt+Ctrl+0')
    time.sleep(.1)
    keyboard.release('alt+Ctrl+0')


def Ending_soon():
    keyboard.press('alt+Ctrl+9')
    time.sleep(.1)
    keyboard.release('alt+Ctrl+9')


def be_right_back():
    keyboard.press('alt+Ctrl+8')
    time.sleep(.1)
    keyboard.release('alt+Ctrl+8')


def Credits():
    top = Toplevel()
    top.title('Credits')
    top.geometry('219x50')
    top.maxsize(219, 50)
    top.minsize(219, 50)
    lable1 = Label(top, text=f"made by Adam\nspecial thxs to Patrick for the spam code\nversion {version}")
    lable1.grid(column=1, row=1)
    top.wm_iconphoto(False, icon)
    if color == 1:
        lable1.configure(bg='gray')
    elif color == 2:
        lable1.configure(bg='red')
    elif color == 3:
        lable1.configure(bg='blue', fg='yellow')
    elif color == 4:
        lable1.configure(bg='#280137', fg='white')
    else:
        lable1.configure(bg='gray')
        top.destroy()
    top.mainloop()


# images
background = Image.open('xander.png')
discord = Image.open('discordlogo.png')
Streamlabs = Image.open('Streamlabs-icon.png')
mute1 = Image.open('mute.png')
mutepng = ImageTk.PhotoImage(mute1)
unmute1 = Image.open('unmute.png')
unmute = ImageTk.PhotoImage(unmute1)
desktop1 = Image.open('desktop.png')
desktop2 = desktop1.resize((85, 75), Image.ANTIALIAS)
desktop = ImageTk.PhotoImage(desktop2)
muteDesktop1 = Image.open('muted desktop.png')
muteDesktop2 = muteDesktop1.resize((85, 75), Image.ANTIALIAS)
muteDesktop = ImageTk.PhotoImage(muteDesktop2)

# top bar settings
options = Menu(root, tearoff=0)
menu = Menu(root)
submenu = Menu(root, tearoff=0)
submenu.add_radiobutton(label='Toplevel on', command=Topmost_on)
submenu.add_radiobutton(label='Toplevel off', command=Topmost_off)
options.add_command(label='open project folder', command=projectlocat)
options.add_command(label='open exe location folder', command=exelocat)
options.add_command(label='CRASH', command=CRASH)

menu.add_cascade(label='file', menu=options)
options.add_cascade(label="topmost", menu=submenu)

file = Menu(menu, tearoff=1)
file.add_command(label='change background color to red', command=colorred)
file.add_command(label='change background color to blue', command=colorblue)
file.add_command(label='change background color to purple', command=colorpurple)
file.add_command(label='change background color to gray', command=colorgray)
file.add_command(label='open xander.png', command=openxander)

menu.add_cascade(label='background', menu=file)

music = Menu(menu, tearoff=0)
music.add_command(label='C418 - Sweden', command=C418)
menu.add_cascade(label='Music', menu=music)
root.config(menu=menu)
# buttons
Button1 = Button(text="start Streaming tools", bg='#567', fg='yellow', height=2, width=20, command=streaming)
Button2 = Button(text='start spam exe', bg='#567', fg='yellow', height=2, width=20, command=spamexe)
Button3 = Button(image=mutepng, bg='#567', command=Togglemute)
Button4 = Button(image=desktop, bg='#567', command=DesktopAudio)
Button5 = Button(text='Starting Soon', bg='#567', fg='yellow', height=2, width=10, command=Starting_soon)
Button6 = Button(text='Main scene', bg='#567', fg='yellow', height=2, width=10, command=Main_scene)
Button7 = Button(text='ending soon', bg='#567', fg='yellow', height=2, width=10, command=Ending_soon)
Button8 = Button(text='be right back', bg='#567', fg='yellow', height=2, width=10, command=be_right_back)
Button9 = Button(text='Credit', bg='#567', fg='yellow', height=2, width=10, command=Credits)

# labels

# button/lable config
Button1.grid(column=1, row=1)
Button2.grid(column=1, row=2)
Button3.place(x=150, y=0)
Button4.place(x=210, y=0)
Button5.place(x=470, y=0)
Button6.place(x=470, y=41)
Button7.place(x=470, y=82)
Button8.place(x=470, y=123)
Button9.place(x=230, y=260)


root.mainloop()
