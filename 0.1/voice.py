import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS


def speak(text):
    tts = gTTS(text=text,lang='en')
    fn = str(hash(text)) + ".mp3"
    tts.save(fn)
    playsound.playsound(fn)
    os.remove(fn)


def getaudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
        except Exception as e:
            return str(e)
    
    return said