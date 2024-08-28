#UI for music player
from tkinter import *
import pygame 
import os
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk

f=open('emotion','r')

root=Tk()
# fav icon
root.iconbitmap(r'D:\UWin_ML_Project\Music_App\images\music_icon.ico')
global paused
paused=False 

root.title("Music app")
root.geometry("440x510")

global status
status = StringVar()
status.set("-Hello!!")
global track
track= StringVar()
# Initiating Pygame & mixer
pygame.init()
pygame.mixer.init()

def play_time():
    #this will fix looping and fasting song/ double speed
    if stopped:
        return
    current_time=pygame.mixer.music.get_pos()/1000

    # slider_label.config(text=f'Slider: {int(slider.get())} of Song : {int(current_time)}')
    convert_current_time=time.strftime('%M:%S',time.gmtime(current_time))
    
    # current_song=playlist.curselection()
    song=playlist.get(ACTIVE)
    song_mut=MP3(song)
    
    global song_length
    song_length= song_mut.info.length
    convert_song_length=time.strftime('%M:%S',time.gmtime(song_length))
    #increase to make same like slider value
    current_time+=1

    if int(slider.get())==int(song_length):
         status_bar.config(text=f'Time Elapsed : {convert_song_length} of {convert_song_length}')


    #checking pause
    elif paused:
        pass
    elif int(slider.get())==int(current_time):
        #slider hasnt moved
        slider_position=int(song_length)
        slider.config(to=int(song_length), value=int(current_time))
        # slider_label.config(text=f'{int(slider.get())} of {int(current_time)}')


    else:
        #slider hasnt moved
        slider_position=int(song_length)
        slider.config(to=int(song_length), value=int(slider.get()))

        #covert to time format
        convert_current_time=time.strftime('%M:%S',time.gmtime(int(slider.get())))
        # output time to status bar
        status_bar.config(text=f'Time Elapsed : {convert_current_time} of {convert_song_length}')

        #Move this thing along by one second
        next_time=int(slider.get())+1
        slider.config(value=next_time)

    
    
    status_bar.after(1000,play_time)



def playsong():
    #to make false to play song
    # global stopped
    # stopped=False
    #if u click play again
    slider.config(value=0)
    display=playlist.get(ACTIVE)
    track.set(display)
    status.set("-Playing")
    pygame.mixer.music.load(display)
    pygame.mixer.music.play(loops=0)
    play_time()

    #update slider position & value makes slider to zero everytime
    # slider.config(to=int(song_length), value=int(current_time))
global stopped
stopped = False
def stopsong():
    #stop formating & reset slider
    status_bar.config(text='')
    slider.config(value=0)
    status.set("-Stopped")
        # Stopped Song
    pygame.mixer.music.stop()
    # status_bar.config(text='')
    
    global stopped
    stopped=True
    

def pausesong(is_paused):
    global paused
    paused=is_paused

    if paused:
             # Playing back Song
        status.set("-Playing")
        pygame.mixer.music.unpause()
        paused=False
    else:
        status.set("-Paused")
            # Paused Song
        pygame.mixer.music.pause()
        paused=True

def backward():

    status_bar.config(text='')
    slider.config(value=0)
  
    next_one=playlist.curselection()
    next_one=next_one[0]-1
    display=playlist.get(ACTIVE)
    track.set(display)
    pygame.mixer.music.load(playlist.get(next_one))
    pygame.mixer.music.play()

        #move active bar in playlist
    playlist.selection_clear(0,END)
        #change active bar
    playlist.activate(next_one)
    playlist.selection_set(next_one)

def forward():
    status_bar.config(text='')
    slider.config(value=0)

    #get current tuple number
    next_one=playlist.curselection()
    
    next_one=next_one[0]+1
    
    pygame.mixer.music.load(playlist.get(next_one))
    pygame.mixer.music.play()

        #move active bar in playlist
    playlist.selection_clear(0,END)
        #change active bar
    playlist.activate(next_one)
    playlist.selection_set(next_one)
    display=playlist.get(ACTIVE)
    track.set(display)


def slide(x):
    display=playlist.get(ACTIVE)
    track.set(display)
    status.set("-Playing")
    pygame.mixer.music.load(display)
    pygame.mixer.music.play(loops=0,start=int(slider.get()))
    
def change_volume(x):
    pygame.mixer.music.set_volume(volume_slider.get())
    

songsframe = LabelFrame(root,text="Song Playlist",font=("Arial",15,"bold"),bg="#E01E1E",fg="white",bd=5,relief=GROOVE)
songsframe.pack(ipadx=300)
        # Inserting scrollbar
scrol_y = Scrollbar(songsframe,orient=VERTICAL)
        # Inserting Playlist listbox
playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="#F8BE00",selectmode=SINGLE,font=("Arial",12,"bold"),bg="#EFEFEF",fg="black",bd=5,relief=GROOVE)
        # Applying Scrollbar to listbox
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=playlist.yview)
playlist.pack(fill=BOTH)
        
os.chdir(f'D:/UWin_ML_Project/Music_App/songs/{f.read()}_songs')
songtracks = os.listdir()
f.close()
        
for id in songtracks:
    playlist.insert(END,id)
# scrol_y = Scrollbar(root,orient=VERTICAL)
#         # Inserting Playlist listbox
# playlist = Listbox(root,yscrollcommand=scrol_y.set,selectbackground="red",selectmode=SINGLE,font=("times new roman",12,"bold"),bg="silver",fg="navyblue",width=70)
#         # Applying Scrollbar to listbox
# scrol_y.pack(side=RIGHT,fill=BOTH)
# scrol_y.config(command=playlist.yview)
# playlist.pack()
        
# os.chdir(f'F:/songs/{f.read()}_songs')
# songtracks = os.listdir()
# f.close()
# for id in songtracks:
#     playlist.insert(END,id)       



trackframe = LabelFrame(root,text="Song Track",font=("Arial",15,"bold"),bg="#18A0C8",fg="white",relief="ridge")
trackframe.pack()
songtrack = Label(trackframe,textvariable=track,width=20,font=("Arial",19,"bold"),bg="#E5F1D4",fg="#1E8449",bd=1,relief="sunken").grid(row=0,column=0,padx=8,pady=5)
trackstatus = Label(trackframe,textvariable=status,font=("Arial",19,"bold"),relief="sunken",bg="#E5F1D4",fg="#1E8449").grid(row=0,column=1,padx=10,pady=5)


back_button_img=PhotoImage(file=r'D:\UWin_ML_Project\Music_App\images\buttons\backward.png')
foward_button_img=PhotoImage(file=r'D:\UWin_ML_Project\Music_App\images\buttons\forward.png') 
play_button_img=PhotoImage(file=r'D:\UWin_ML_Project\Music_App\images\buttons\play.png')
pause_button_img=PhotoImage(file=r'D:\UWin_ML_Project\Music_App\images\buttons\pause.png')
stop_button_img=PhotoImage(file=r'D:\UWin_ML_Project\Music_App\images\buttons\stop.png')

slider=ttk.Scale(root,from_=0 , to=100, orient=HORIZONTAL,value=0,command=slide,length=360)
slider.pack(pady=15)


buttonframe =Frame(root)
buttonframe.pack(padx=5)
back_button=Button(buttonframe,image=back_button_img,borderwidth=0,command=backward)
foward_button=Button(buttonframe,image=foward_button_img,borderwidth=0,command=forward)
play_button=Button(buttonframe,image=play_button_img,borderwidth=0,command=playsong)
pause_button=Button(buttonframe,image=pause_button_img,borderwidth=0,command=lambda:pausesong(paused))
stop_button=Button(buttonframe,image=stop_button_img,borderwidth=0,command=stopsong)


back_button.grid(row=0,column=0,padx=10,pady=5)
pause_button.grid(row=0,column=3,padx=10,pady=5)
play_button.grid(row=0,column=1,padx=10,pady=5)
stop_button.grid(row=0,column=4,padx=10,pady=5)
foward_button.grid(row=0,column=2,padx=10,pady=5)



main_frame=LabelFrame(root,text="Volume")
main_frame.place(x=133,y=433,width=150)
# main_frame.place(x=410,y=360,width=30)
# main_frame.place(x=8,y=320,width=25)
volume_slider=ttk.Scale(main_frame,from_=0 , to=1, orient=HORIZONTAL,value=1,command=change_volume,length=140)
volume_slider.pack()

# slider_label=Label(root,text='0')
# slider_label.pack(pady=3)

status_bar=Label(root,text='',relief="groove",anchor="e")
status_bar.pack(fill=X,side=BOTTOM)
   
root.mainloop()

#Reference: Graphical User Interfaces with Tk, https://docs.python.org/3/library/tk.html