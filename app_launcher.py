#UI for asking Input from the User

#importing libraries
from tkinter import *
from subprocess import call
from tkinter import messagebox
import os

def testing():
    root.destroy()
    call("py D:/UWin_ML_Project/Music_App/expression.py")   #calling the file which will take input and process on them

root = Tk()
root.title("Music app")
# fav icon
root.iconbitmap(r'D:\UWin_ML_Project\Music_App\images\music_icon.ico')  #set icon
root.geometry("320x500")
#title
my_title = Label(root, text="Welcome to our\n Music Application",
                 font=("Arial bold", 25), fg="red")
my_title.pack()

# description of application
my_frame = LabelFrame(root, text="About Us:", fg="white",
                      bg="#228E9F", padx=5, pady=5)
my_frame.pack(pady=40)
my_title = Label(my_frame, text="This is an application which focuses on \nsuggesting songs for user based on their\n mood by capturing facial expressions. Once\n the emotion is recognized, the application\n suggests a list of songs for that emotion.\n So sitback and enjoy :)", font=("Arial", 11), bg="#92ECFA")
my_title.pack()

# permission
allow_label = Label(
    root, text="Allow access to web-cam to continue.", font=("Arial bold", 13))
allow_label.pack(pady=20)

my_frame2 = LabelFrame(root, text="Select", padx=5, pady=5)
my_frame2.pack()
space = Label(my_frame2, text="                       ")
yes_button = Button(my_frame2, text="YES", padx=28, pady=5, command=testing,bg="#48C41E",fg="white")
# yes_button = Button(my_frame2, text="YES", padx=28, pady=5, command=lambda :spawn_program_and_die(['python.exe',r'C:\Users\patel\SDP_project\expression.py']),bg="#48C41E",fg="white")
no_button = Button(my_frame2, text="NO", padx=28, pady=5,
                   command=root.quit, bg="#E32522", fg="white")
yes_button.grid(row=0, column=0)
space.grid(row=0, column=1)
no_button.grid(row=0, column=2)

allow_label = Label(root, text="Have a good day!!", font=("MS Sans Serif", 13))
allow_label.pack(pady=20)

# button = Button(root, text="EXIT", padx=20, pady=6, command=root.quit,bg="#E32522",fg="white")
# button.pack()
root.mainloop()
