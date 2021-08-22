import cv2
import numpy as np
import pytesseract
import pyttsx3
import urllib
import cv2
import numpy as np
import time
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"



engine = pyttsx3.init() # object creation
engine.setProperty('rate', 125)     # setting up new voice rate
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female



url='http://192.168.0.229:8080/shot.jpg'

imgResp = urllib.request.urlopen(url)
imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
img = cv2.imdecode(imgNp,-1)
img = cv2.resize(img, None, fx=1, fy=1)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)

config = "--psm 3"
text = pytesseract.image_to_string(adaptive_threshold, config=config, lang="eng")
#text = pytesseract.image_to_string(adaptive_threshold, config=config, lang="bengali")

print(text)

engine.say(text)
engine.runAndWait()
engine.stop()
