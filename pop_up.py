from tkinter import *
from subprocess import call
from tkinter import messagebox
import time
import subprocess
import sys


f=open('emotion','r')
# dirgh=f.read()


root=Tk()
root.title("Music app")
# fav icon
root.iconbitmap(r'D:\UWin_ML_Project\Music_App\images\music_icon.ico')
root.config(bg='#5D95A9')
root.geometry("300x100")

def onclick():
    response=messagebox.askquestion("Conformation pop_up", f"Are you {f.read()}")
    f.close()
    if response == 'no':
        root.destroy()
        call("py D:/UWin_ML_Project/Music_App/expression.py",shell=True)
    else:
        root.destroy()
        call("py D:/UWin_ML_Project/Music_App//music_player.py",shell=True)



my_label=Button(root,text="CONFIRM MOOD",command=onclick,fg="white",bg='red',padx=20,pady=5, font=("arial bold",10))
my_label.grid(pady=35,padx=75)
root.mainloop()

