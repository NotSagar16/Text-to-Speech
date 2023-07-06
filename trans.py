
from PIL import Image
from pytesseract import *
from googletrans import Translator
import pyttsx3
import gtts
import playsound
import os
def con(lang):
    pytesseract.tesseract_cmd = r'C:\Users\Hp\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    img = Image.open("texttoconvert.png")

    output = pytesseract.image_to_string(img)
    print(output)
    translater = Translator()
    out = translater.translate(output, src='en', dest=lang)
    text = out.text
    print(text)
    speak = gtts.gTTS(text=text, lang=lang, slow=False)
    speak.save("captured_voice.mp3")

    playsound.playsound('captured_voice.mp3')
    os.remove('captured_voice.mp3')




