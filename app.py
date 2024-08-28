#File for web based UI using streamlit

from cProfile import label
from click import confirm
import numpy as np
import cv2
import streamlit as st
import webbrowser
#from tensorflow import keras
from keras.models import model_from_json
from keras.preprocessing.image import img_to_array
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase, RTCConfiguration, VideoProcessorBase, WebRtcMode
from subprocess import call
from PIL import Image

# load model

emotion_dict = {0:'angry', 1 :'happy', 2: 'neutral', 3:'sad', 4: 'surprise'}
# load json and create model
json_file = open('emotion_model1.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
classifier = model_from_json(loaded_model_json)

# load weights into new model
classifier.load_weights("emotion_model1.h5")

#load face
try:
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
except Exception:
    st.write("Error loading cascade classifiers")

RTC_CONFIGURATION = RTCConfiguration({"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]})

class Faceemotion(VideoTransformerBase):
    def transfer(out):
        return out
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")

        #image gray
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            image=img_gray, scaleFactor=1.3, minNeighbors=5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img=img, pt1=(x, y), pt2=(
                x + w, y + h), color=(255, 0, 0), thickness=2)
            roi_gray = img_gray[y:y + h, x:x + w]
            roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)
            if np.sum([roi_gray]) != 0:
                roi = roi_gray.astype('float') / 255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi, axis=0)
                prediction = classifier.predict(roi)[0]
                maxindex = int(np.argmax(prediction))
                finalout = emotion_dict[maxindex]
                output = str(finalout)
                f=open('emotion.txt','w')
                f.write(output)
                f.close()
            label_position = (x,y)
            cv2.putText(img, output, label_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        return img
#give descriotion about the appication
st.set_page_config(page_title="EmoMusic",page_icon="logo50.jpeg")
def main():
    flag=0
    f=open('emotion.txt','r')
    img=Image.open("header75.png")
    st.image(img)
    activiteis = ["Home", "Webcam Face Detection", "About"]#
    choice = st.sidebar.selectbox("Select Activity", activiteis)
    st.sidebar.markdown(
        """ Developed by The Team 18""")
    st.sidebar.markdown("""
            Tirth Patel,
            Pruthvik Das,
            Rutvy Makwana""")
    st.sidebar.markdown("""
            Have You faced any problem?           
            Contact the developers...
            Email:tirth3454@gmail.com
                  daspruthvik@gmail.com
                  rutvi3004@gmail.com
            """)
    #Shows the steps how to use the application
    if choice == "Home":
        st.header("Emotions Based Music App")
        string="These are steps for this app.\n 1. Go to Webcam Face Detection in slidebar.\n2. Click on the Start button which starts the camera.\n 3. Then, Click on capture button.\n 4. Lastly, Confirm the mood.\n Done, music player suggest music according to your mood."
        st.write(string)
    elif choice == "Webcam Face Detection":
        st.subheader("Webcam Live Feed")
        st.write("Click on start to use webcam and detect your face emotion")
        webrtc_streamer(key="example", mode=WebRtcMode.SENDRECV, rtc_configuration=RTC_CONFIGURATION,video_processor_factory=Faceemotion)
        if st.button("Capture"):
            st.write("Your mood is " + f.read())
        if st.button("Confirm"):
            webbrowser.open("index.html")
    #shows about details for application
    elif choice == "About":
        st.subheader("About this app")
        html_temp_about1= """<div style="background-color:#6D7B8D;padding:10px">
                                    <h4 style="color:white;text-align:center;">
                                    EMO Music is a music player that tunes into your emotions. It suggests songs that match your mood for a customized music experience. Simply choose a track from the playlist and dive into a high-quality musical journey.
                                    </h4>
                                    </div>
                                    </br>"""
        st.markdown(html_temp_about1, unsafe_allow_html=True)

        html_temp4 = """
                             		<div style="background-color:#98AFC7;padding:10px">
                             		<h4 style="color:white;text-align:center;">This application has been created as part of a Machine Learning project undertaken at the University of Windsor. </h4>
                             		<h4 style="color:white;text-align:center;">Thanks for Visiting.</h4>
                             		</div>
                             		<br></br>
                             		<br></br>"""

        st.markdown(html_temp4, unsafe_allow_html=True)

    else:
        pass


if __name__ == "__main__":
    main()

#Refernce : Streamlit documentation, https://docs.streamlit.io/library/get-started/create-an-app