import cv2
import numpy as np
import pytesseract
import pyttsx3
import urllib
import numpy as np
import time
from gtts import gTTS
import os


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#url='http://192.168.10.82:8080/shot.jpg'    # For IP camera Image

#imgResp = urllib.request.urlopen(url)
#imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
#img = cv2.imdecode(imgNp,-1)

img=cv2.imread('Capture.png')

img = cv2.resize(img, None, fx=1, fy=1)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)

config = "--psm 3"
#text = pytesseract.image_to_string(adaptive_threshold, config=config, lang="eng")
text = pytesseract.image_to_string(adaptive_threshold, config=config, lang="bengali")

print(text)

language = 'bn'  
myobj = gTTS(text,lang=language,slow=False)
  
myobj.save("welcome.mp3")
os.system("welcome.mp3")
