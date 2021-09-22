import numpy as np
import pytesseract
import pyttsx3
import urllib
import numpy as np
import time
from gtts import gTTS
import os
from PIL import Image
import cv2
#from playsound import playsound
from pygame import mixer
mixer.init()

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
Lang='b'
engine_option=False

engine = pyttsx3.init() # object creation
engine.setProperty('rate', 125)     # setting up new voice rate
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female



webcam=False

if webcam:
    url='http://192.168.0.229:8080/shot.jpg'
    imgResp = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img = cv2.imdecode(imgNp,-1)
    img = cv2.resize(img, None, fx=1, fy=1)
else:
    img=cv2.imread('bangla.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)


    #img=Image.open('bangla.png')


#adaptive_threshold = img
config = "--psm 3"

if Lang=='b':
    text = pytesseract.image_to_string(adaptive_threshold, config=config, lang="Bengali")
    language = 'bn' 
else:    
    text = pytesseract.image_to_string(adaptive_threshold, config=config, lang="eng")
    language = 'en' 


#print(text)
text_split=text.split("।")


def make_sound(text,i):
    try:
        myobj = gTTS(text,lang=language,slow=False)
        myobj.save('welcome'+str(i%2)+'.mp3')
        #os.system("mpg321 /home/pi/tesseract/audiodata/welcome'+str(i)+'.mp3 &")
        mixer.music.load('welcome'+str(i%2)+'.mp3')
        mixer.music.play(0)
        while(mixer.music.get_busy()==True):
            #print('busy')
            time.sleep(0.05)
    except:
        None


for i in range(len(text_split)):
    print(i,text_split[i])
    make_sound(text_split[i],i)
    