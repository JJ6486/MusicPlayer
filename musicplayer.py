from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os

root=Tk()
root.title("Music Player")
root.geometry("920x670+290+85")
root.configure(bg="#0f1a2b")
root.resizable(False, False)

mixer.init()
#icon
image_icon = PhotoImage(file="music icon.png")
root.iconphoto(False, image_icon)

Top=PhotoImage(file="Music player top.png")
Label(root, image=Top, bg="#0f1a2b").pack()

#logo
Logo=PhotoImage(file="music icon.png")
Label(root, image=Logo, bg="#0f1a2b", bd=0).place(x=115, y=115)

#buttons
play_button=PhotoImage(file="play button.png")
Button(root, image=play_button, bg="#0f1a2b", bd=0).place(x=100, y=400)

stop_button=PhotoImage(file="stopbutton.png")
Button(root, image=stop_button, bg="#0f1a2b", bd=0).place(x=30, y=500)







root.mainloop()