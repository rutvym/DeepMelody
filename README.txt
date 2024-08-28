We've crafted two distinct user interfaces: a web-based interface utilizing Streamlit and a local application-type interface built with Tkinter. To experience both unique outputs, simply run two separate files.

To run this program, follow these steps:
First and formost, Extract this zipped folder in you D drive. 
(Make sure that you are unzipping it in D drive only, do not make any other folder there)

Now,
i) For tkinter Application
	1) Open the command prompt and run "app_launcher.py" file by this command.
		python app_launcher.py
	2) Click on YES button to allow the permission to use the camera
	3) System will start to capture the emotion.
	4) Press C button to confirm your emotion.
	5) System will suggest songs according to your mood.

ii) For Web Based streamlit Application

	1) Open the command prompt and run "app.py" file by this command.
		streamlit run  D:/UWIN_ML_Project/Music_App/app.py
	2) You will reach to localhost website from your browser. 
	3) Steps are mentioned there on website. Just follow it and Enjoy the music player.
	

#Reference: 
1.Graphical User Interfaces with Tk, https://docs.python.org/3/library/tk.html
2.Beginner’s Guide to VGG16 Implementation in Keras, https://builtin.com/machine-learning/vgg16
3.Streamlit documentation, https://docs.streamlit.io/library/get-started/create-an-app
4.UI Music Player Application using Tkinter, https://www.studytonight.com/tkinter/music-player-application-using-tkinter


Following is a short description what all program file does:

Used packages and libraries : Keras, OpenCV, Tkinter, numpy, pandas, CNN, MP3, pygame, os, subprocess, Streamlit

1.Classification.py
	In this file, we are training our Machine learning model to detect the mood from facial expressions using 	CNN network by giving thousands of pictures of different types(emotions) as input. 
	
2.app_launcher.py
	This will be the starting program file of our system. It will show a UI of our home page and will
	also include camera controls.
 
3.expression.py
	In this program file we have used openCV & Haar Casacade file to identify human face and detect his/her
	emotions.

4.pop_up.py
	A pop window just to confirm the detected mood.

5.music_player.py
	This tkinter program file provides a music player UI with which a user can interact with and play songs 	from the playlist. We have implemented many funtionalities like play, pause, stop, skip forward/backward, 	volume and jump to specific time while song is playing.

6.app.py
	This file has code for web based music player. Stremlit tool is used for making web version of emotion 	based music player.

7.index.html
	This file has UI for web based music player. This UI has been made using html and css.

