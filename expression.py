from keras.models import load_model
from time import sleep
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
from cv2 import cv2
import numpy as np
from subprocess import call
import os


#loading of cascade
face_classifier = cv2.CascadeClassifier(r'D:\UWin_ML_Project\Music_App\haarcascade_frontalface_default.xml')
classifier =load_model(r'D:\UWin_ML_Project\Music_App\Emotion_little_vgg.h5')

class_labels = ['Angry','Happy','Neutral','Sad','Surprise']

#use primary web cam- infinity
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.set(3,640)
cap.set(4,1080)
while True:
    # Grab a single frame of video
    ret, frame = cap.read()
    labels = []
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #detectfaces
    faces = face_classifier.detectMultiScale(gray,1.3,5)

    #draw a rectangle around face
    for (x,y,w,h) in faces:
        #starting point.ending point,color,width of border
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        #detect eye within the face frame/region 
        roi_gray = gray[y:y+h,x:x+w]
        roi_gray = cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)
    
        if np.sum([roi_gray])!=0:
            roi = roi_gray.astype('float')/255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi,axis=0)

        # make a prediction on the ROI, then lookup the class
            preds = classifier.predict(roi)[0]
            # print(type(preds)) numpy array
            label=class_labels[preds.argmax()]
            #give label to frame
            label_position = (x,y)
            cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
            break
        else:
            cv2.putText(frame,'No Face Found',(20,60),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
    
    #display frame and hit 'q' to exit.
    cv2.imshow('Emotion Detector',frame)
    if cv2.waitKey(1) & 0xFF == ord('c'):
        break
# print(label)

f=open('emotion','w')
f.write(label)
f.close()

cap.release()
cv2.destroyAllWindows()

call("py D:/UWin_ML_Project/Music_App/pop_up.py")
#using this for further process




























