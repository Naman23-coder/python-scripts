import gtts # pip install gtts
import time
import os
import playsound
import random


def speak(text: str) -> None:
    file = f"{random.randint(1, 10000)}.mp3"
    tts = gtts.gTTS(text=text)
    tts.save(file)
    playsound.playsound(file)
    time.sleep(5)
    os.remove(file)
     
