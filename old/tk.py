from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sys
import os
import funct
import functions

player = {
    "fname": '',
    "lname": '',
    "age": '',
    "gender": '',
    "personality": '',
    "term1grades": {
        "acit1420": '',
        "acit1515": '',
        "acit1620": '',
        "acit1630": '',
        "comm1116": '',
        "math1310": '',
        "orgb1100": '',
    }
}

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    # creation of init_window
    def init_window(self):

        # changing title of master widget
        self.master.title('ACITventure')

        # fill space of root window
        self.pack(fill=BOTH, expand=1)

        # creating menu instance
        menu = Menu(self.master)
        self.master.config(menu = menu)

        # create file object
        file = Menu(menu)

        # exit command in file menu
        file.add_command(label = 'Exit', command = self.client_exit)

        # add 'file' to menu
        menu.add_cascade(label= 'File', menu = file)

        # create edit object
        edit = Menu(menu)

        # show image and text commands in edit menu
        # edit.add_command(label = 'Show Image', command = self.showImg)
        # edit.add_command(label = 'Show Text', command = self.showText)

        # add 'edit' to menu
        menu.add_cascade(label = 'Edit', menu = edit)

        # creating a button
        quitButton = Button(self, text='Quit', command = self.client_exit)

        # placing button
        quitButton.place(x = 0, y = 0)
    
    # exit function
    def client_exit(self):
        exit()

    """
    # show image and text functions
    def showImg(self):
        load = Image.open('images/owo.png')
        render = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = Label(self, image = render)
        img.image = render
        img.place(x = 0, y = 0)

    # background image
    def backgroundImg(self):
        load = Image.open('images/main.png')
        render = ImageTk.PhotoImage(load)
        background_label = Label(root, image = render)
        background_label.render = render
        background_label.place(x = 0, y = 0, height = 720, width = 720)


    def showText(self):
        text = Label(self, text='OwO')
        text.pack()
    """

# create root window - can add windows within windows
root = Tk()

def helpbox():
    def goback():
        h.destroy()
    h = Canvas(maincanvas, width=720, height=720)
    h.configure(background="#E1C699")
    h.pack()
    h.place(relx=0.5, rely=0.5, anchor=CENTER)    
    back_button = Button(h, text = 'Go Back', command = goback, width = 10, activebackground = '#33B5E5')
    back_button_window = h.create_window(1, 1, anchor = 'nw', window = back_button)
    helpfile = open('helpbox.txt', 'r')
    x = helpfile.read()
    h.create_text(100, 100, fill="darkblue", font="Times 20 italic bold", text = x)

def week0():
    def goback():
        w.destroy()

    w = Canvas(maincanvas, width=720, height=720)
    w.configure(background="#E1C699")
    w.pack()
    w.place(relx=0.5, rely=0.5, anchor=CENTER)    
    continue_button = Button(w, text = 'Continue', command = goback, width = 10, activebackground = '#33B5E5')
    continue_button_window = w.create_window(1, 1, anchor = 'nw', window = continue_button)
    if player['fname'] == '':
        messagebox.showinfo("Hold up", "You should create your profile first!")
        goback()


# background image for root window
loadbackground = Image.open('images/main.png')
maincanvas = Canvas(root, width = 720, height = 720)
maincanvas.pack()
tk_img = ImageTk.PhotoImage(loadbackground)
maincanvas.create_image(125, 125, image = tk_img)
quit_button = Button(root, text = 'Quit', command = root.quit, width = 10, activebackground = '#33B5E5')
quit_button_window = maincanvas.create_window(10, 690, anchor = 'nw', window = quit_button)

help_button = Button(root, text = 'Help', command = helpbox, width = 10, activebackground = '#33B5E5')
help_button_window = maincanvas.create_window(100, 690, anchor = 'nw', window = help_button)

profile_button = Button(root, text = 'Profile', command = functions.createprofile, width = 10, activebackground = '#33B5E5')
profile_button_window = maincanvas.create_window(190, 690, anchor = 'nw', window = profile_button)

start_button = Button(root, text = 'Start', command = week0, width = 10, activebackground = '#33B5E5')
start_button_window = maincanvas.create_window(280, 690, anchor = 'nw', window = start_button)


# size of the window
root.geometry("720x720")

# create instance
app = Window(root)

# mainloop
root.mainloop()

