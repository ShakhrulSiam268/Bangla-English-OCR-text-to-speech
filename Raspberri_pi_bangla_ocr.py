import numpy as np
import pytesseract
import pyttsx3
import urllib
import numpy as np
import time
from gtts import gTTS
import os
from PIL import Image


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
    #img = cv2.imdecode(imgNp,-1)
    #img = cv2.resize(img, None, fx=1, fy=1)
else:
    #img=Image.open('Capture.jpeg')
    img=Image.open('bangla.png')


adaptive_threshold = img
config = "--psm 3"

if Lang=='b':
    text = pytesseract.image_to_string(adaptive_threshold, config=config, lang="Bengali")
    language = 'bn' 
else:    
    text = pytesseract.image_to_string(adaptive_threshold, config=config, lang="eng")
    language = 'en' 


print(text)

if engine_option:
    engine.say(text)
    engine.runAndWait()
    engine.stop()
else:
     
    myobj = gTTS(text,lang=language,slow=False)
    myobj.save("welcome.mp3")
    os.system("mpg321 /home/pi/tesseract/welcome.mp3 &")

