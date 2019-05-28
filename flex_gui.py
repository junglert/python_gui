#!/usr/bin/python3.5
import tkinter as ttk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk

window = Tk()
window.title("flexible GUI")
window.geometry('1920x1080')

icon = PhotoImage(file="python3.ico")
window.tk.call('wm', 'iconphoto', window._w, icon)

def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo #avoid garbage collection

image = Image.open('python3.jpeg')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(window, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)


window.mainloop()
