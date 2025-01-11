from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os

root=Tk()
root.title("Music Player")
root.geometry("920x670+290+85")
root.configure(bg="#f2e7d5")
root.resizable(False, False)

mixer.init()

def open_folder():
    path= filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)
        # print(songs)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END, song)

def play_song():
    music_name=playlist.get(ACTIVE)
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music.config(text=music_name[0:-4])

#icon
image_icon = PhotoImage(file="music icon.png")
root.iconphoto(False, image_icon)

Top=PhotoImage(file="Music player top.png")
Label(root, image=Top, bg="#f2e7d5", bd=0).pack()

#logo
Logo=PhotoImage(file="music icon.png")
Label(root, image=Logo, bg="#f2e7d5", bd=0).place(x=115, y=115)

#buttons
play_button=PhotoImage(file="play button.png")
Button(root, image=play_button, bg="#f2e7d5", bd=0, command=play_song).place(x=115, y=400)

stop_button=PhotoImage(file="stopbutton.png")
Button(root, image=stop_button, bg="#f2e7d5", bd=0, command=mixer.music.stop).place(x=30, y=500)

resume_button=PhotoImage(file="resumebutton.png")
Button(root, image=resume_button, bg="#f2e7d5", bd=0, command=mixer.music.unpause).place(x=115, y=500)

pause_button=PhotoImage(file="pausebutton.png")
Button(root, image=pause_button, bg="#f2e7d5", bd=0, command=mixer.music.pause).place(x=200, y=500)

# label
music=Label(root, text="", font=("Montserrat", 12), fg="black", bg="#f2e7d5")
music.place(x=150, y=340, anchor=CENTER)

#music

music_frame=Frame(root, bd=2, relief=RIDGE)
music_frame.place(x=330, y=350, width=560,height=250)

Button(root, text="Open folder", width=15, height=2,
       font=("Montserrat", 10, "bold"), fg="white", 
       bg="#21b3de", command=open_folder).place(x=330, y=300)

scroll=Scrollbar(music_frame)
playlist=Listbox(music_frame,width=100, font=("Montserrat", 
                 10), fg="grey", bg="#393e46", selectbackground="lightblue",
                 cursor="hand2", bd=0, yscrollcommand=scroll.set)

scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT, fill=BOTH)


root.mainloop()